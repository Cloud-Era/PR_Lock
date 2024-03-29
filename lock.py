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
    
    # Pull request information
    pr_number = "123"  # Replace with the pull request number
    
    # GitHub personal access token
    github_token = os.getenv("GITHUB_TOKEN")
    if not github_token:
        print("GitHub token not found. Make sure to set the GITHUB_TOKEN environment variable.")
    else:
        lock_pull_request(repo_owner, repo_name, pr_number, github_token)
