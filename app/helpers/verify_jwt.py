from .error import AuthError
from ..constants import ERROR_MESSAGE_401, ALGORITHMS
from ..config import DOMAIN, CLIENT_ID
from six.moves.urllib.request import urlopen
import json
from jose import jwt


# Verify the JWT in the request's Authorization header
def verify_jwt(request):
    if "Authorization" in request.headers:
        auth_header = request.headers["Authorization"].split()
        if len(auth_header) == 1:
            token = auth_header[0]
        else:
            token = auth_header[1]
    else:
        raise AuthError(
            {
                "code": "no auth header",
                "description": "Authorization header is missing",
            },
            401,
        )

    jsonurl = urlopen("https://" + DOMAIN + "/.well-known/jwks.json")
    jwks = json.loads(jsonurl.read())

    try:
        unverified_header = jwt.get_unverified_header(token)
    except jwt.JWTError:
        raise AuthError(
            {
                "code": "invalid_header",
                "description": "Invalid header. Use an RS256 signed JWT Access Token",
            },
            401,
        )

    if unverified_header["alg"] == "HS256":
        raise AuthError(
            {
                "code": "invalid_header",
                "description": "Invalid header. Use an RS256 signed JWT Access Token",
            },
            401,
        )

    rsa_key = {}
    for key in jwks["keys"]:
        if key["kid"] == unverified_header["kid"]:
            rsa_key = {
                "kty": key["kty"],
                "kid": key["kid"],
                "use": key["use"],
                "n": key["n"],
                "e": key["e"],
            }
    if rsa_key:
        try:
            payload = jwt.decode(
                token,
                rsa_key,
                algorithms=ALGORITHMS,
                audience=CLIENT_ID,
                issuer="https://" + DOMAIN + "/",
            )
        except jwt.ExpiredSignatureError:
            raise AuthError(
                {"code": "token_expired", "description": "token is expired"}, 401
            )
        except jwt.JWTClaimsError:
            raise AuthError(
                {
                    "code": "invalid_claims",
                    "description": "incorrect claims, please check the audience and issuer",
                },
                401,
            )
        except Exception:
            raise AuthError(
                {
                    "code": "invalid_header",
                    "description": "Unable to parse authentication token.",
                },
                401,
            )

        return payload
    else:
        raise AuthError(
            {"code": "no_rsa_key", "description": "No RSA key in JWKS"}, 401
        )
