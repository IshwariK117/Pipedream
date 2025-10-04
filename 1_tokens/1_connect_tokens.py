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
token_response = client.tokens.create(
  external_user_id=os.getenv('external_user_id'),
)
print("Token created successfully", token_response)

