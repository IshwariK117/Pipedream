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

# List first page of apps
response = client.apps.list(
    limit=5,              # number of apps to fetch
    sort_key="name",
    sort_direction="asc"
)

# Iterate over apps in the first page
for app in response:
    print("App listed:", app)

# Optional: paginate through all pages
# for page in response.iter_pages():
#     print("Page of apps:", page)
