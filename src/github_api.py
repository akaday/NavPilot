import requests
import json

def create_github_tree():
    url = "https://api.github.com/repos/owner/repo/git/trees"
    headers = {
        "Authorization": "token YOUR_ACCESS_TOKEN",
        "Accept": "application/vnd.github.v3+json"
    }
    data = {
        "tree": [
            {
                "path": "file.txt",
                "mode": "100644",
                "type": "blob",
                "sha": "YOUR_BLOB_SHA"
            }
        ]
    }

    response = requests.post(url, headers=headers, data=json.dumps(data))

    if response.status_code == 201:
        print("Tree created successfully!")
    else:
        print("Error creating tree:", response.content)
