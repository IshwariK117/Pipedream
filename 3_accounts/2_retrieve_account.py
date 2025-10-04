from pipedream import Pipedream
import os
from dotenv import load_dotenv
load_dotenv()
client = Pipedream(
  project_id=os.getenv('project_id'),
  project_environment=os.getenv('project_environment'),
  client_id=os.getenv('client_id'),
  client_secret=os.getenv('client_secret'),
)
response = client.accounts.retrieve(
  account_id="apn_x7h3zak",
  include_credentials=True,
)
print("Account retrieved successfully", response)



