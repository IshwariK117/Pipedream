from pipedream import Pipedream
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Get credentials from environment
PROJECT_ID = os.getenv("project_id")
PROJECT_ENVIRONMENT = os.getenv("project_environment")
CLIENT_ID = os.getenv("client_id")
CLIENT_SECRET = os.getenv("client_secret")
EXTERNAL_USER_ID = os.getenv("external_user_id")  # The user you want to check
APP_NAME = "hubspot"  # Change this to the app you want to check

# Initialize Pipedream client
client = Pipedream(
    project_id=PROJECT_ID,
    project_environment=PROJECT_ENVIRONMENT,
    client_id=CLIENT_ID,
    client_secret=CLIENT_SECRET,
)

# List all connected accounts in the project
accounts = client.accounts.list()

# Search for the connected account for the given user and app
auth_provision_id = None
for account in accounts:
    account_app_name = getattr(account.app, "name", "").lower() if account.app else ""
    account_external_id = getattr(account, "external_id", "")
    
    if account_app_name == APP_NAME.lower() and account_external_id == EXTERNAL_USER_ID:
        auth_provision_id = account.id
        print(f"Found connected account for {APP_NAME}: authProvisionId = {auth_provision_id}")
        break

if not auth_provision_id:
    print(f"No connected {APP_NAME} account found for external user {EXTERNAL_USER_ID}")
