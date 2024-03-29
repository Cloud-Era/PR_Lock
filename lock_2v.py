import os
import requests

def lock_pull_request(repo_owner, repo_name, pr_number, github_token):
    headers = {
        "Authorization": f"token {github_token}",
        "Accept": "application/vnd.github.v3+json"
    }
    url = f"https://api.github.com/repos/{repo_owner}/{repo_name}/pulls/{pr_number}/lock"
    response = requests.put(url, headers=headers)

    if response.status_code == 204:
        print(f"Pull request #{pr_number} locked successfully.")
    else:
        print(f"Failed to lock pull request #{pr_number}. Status code: {response.status_code}")

if __name__ == "__main__":
    # GitHub repository information
    repo_owner = "your_org_or_username"
    repo_name = "your_repository_name"
    
    # Pull request number obtained from the environment variable
    pr_number = os.getenv("PR_NUMBER")
    if not pr_number:
        print("Pull request number not found. Make sure to set the PR_NUMBER environment variable.")
    else:
        # GitHub personal access token
        github_token = os.getenv("GITHUB_TOKEN")
        if not github_token:
            print("GitHub token not found. Make sure to set the GITHUB_TOKEN environment variable.")
        else:
            lock_pull_request(repo_owner, repo_name, pr_number, github_token)




----------------------------------------------------------------------------------------------------------------------------------------------------
----------------------------------------------------------------------------------------------------------------------------------------------------
----------------------------------------------------------------------------------------------------------------------------------------------------
----------------------------------------------------------------------------------------------------------------------------------------------------
 YML


name: Lock Pull Request

on:
  pull_request:
    types: [opened]

jobs:
  lock_pull_request:
    runs-on: ubuntu-latest
    steps:
      - name: Set PR_NUMBER environment variable
        run: echo "PR_NUMBER=${{ github.event.pull_request.number }}" >> $GITHUB_ENV
      
      - name: Execute Python script
        run: python lock_pull_request.py
        env:
          GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
          PR_NUMBER: ${{ env.PR_NUMBER }}

