import requests
from ..config import CLIENT_ID, CLIENT_SECRET, DOMAIN
from ..helpers.error import AuthError
from ..constants import ERROR_MESSAGE_400, ERROR_MESSAGE_401


def login_user_logic(content):
    # Check 400 error
    required_attributes = ["username", "password"]
    if not content or not all(attr in content for attr in required_attributes):
        raise AuthError(ERROR_MESSAGE_400, 400)

    username = content["username"]
    password = content["password"]

    body = {
        "grant_type": "password",
        "username": username,
        "password": password,
        "client_id": CLIENT_ID,
        "client_secret": CLIENT_SECRET,
    }
    headers = {"content-type": "application/json"}
    url = f"https://{DOMAIN}/oauth/token"

    response = requests.post(url, json=body, headers=headers)

    # Check 401 error
    if (
        response.status_code == 403
        and response.json().get("error_description") == "Wrong email or password."
    ):
        raise AuthError(ERROR_MESSAGE_401, 401)

    try:
        id_token = response.json()["id_token"]
    except KeyError:
        raise AuthError({"Error": response.json().get("error")}, response.status_code)

    return id_token
