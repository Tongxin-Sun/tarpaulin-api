from google.cloud import secretmanager
import os


def get_secret(secret_id: str) -> str:
    """Fetch a secret from Google Secret Manager."""
    client = secretmanager.SecretManagerServiceClient()
    project_id = os.getenv("GOOGLE_CLOUD_PROJECT")
    if not project_id:
        raise RuntimeError("GOOGLE_CLOUD_PROJECT not set.")
    name = f"projects/{project_id}/secrets/{secret_id}/versions/latest"
    response = client.access_secret_version(request={"name": name})
    return response.payload.data.decode("UTF-8")


def get_config_value(name: str) -> str:
    """Check environment variable first, fallback to Secret Manager."""
    return os.getenv(name) or get_secret(name)


CLIENT_ID = get_config_value("CLIENT_ID")
CLIENT_SECRET = get_config_value("CLIENT_SECRET")
DOMAIN = get_config_value("DOMAIN")
