from app import create_app
import os
from dotenv import load_dotenv

# Load .env only if running locally (GAE_ENV is set in App Engine)
if os.environ.get("GAE_ENV") is None:
    load_dotenv()

app = create_app()

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8080, debug=True)
