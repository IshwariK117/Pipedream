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
oauth_token_response = client.oauth_tokens.create(
  client_id=os.getenv('client_id'),
  client_secret=os.getenv('client_secret'),
)
print("OAuth token created successfully", oauth_token_response)


