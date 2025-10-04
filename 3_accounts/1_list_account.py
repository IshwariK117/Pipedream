from pipedream import Pipedream
import os
from dotenv import load_dotenv

load_dotenv()

client = Pipedream(
    project_id=os.getenv("project_id"),
    project_environment=os.getenv("project_environment"),
    client_id=os.getenv("client_id"),
    client_secret=os.getenv("client_secret"),
)

external_user_id = os.getenv("external_user_id")
# optional: set app_name or oauth_app_id if you want to filter
app_name = "hubspot"  

# Fetch connected accounts for the external user
response = client.accounts.list(
    external_user_id=external_user_id,
    include_credentials=True,
    limit=5  # number of items per page
)

# Iterate over accounts in the first page
for account in response:
    account_app_name = getattr(account.app, "name", "").lower() if account.app else ""
    if app_name.lower() == account_app_name:
        print("Connected account found:", account.id, account_app_name)


