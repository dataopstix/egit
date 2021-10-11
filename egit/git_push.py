"""Module: Checks any changes in local repo, if it finds any push it to remote!"""
import json
import logging
import os

import requests
from git import Repo


def create_pull_request(
    github_account,
    git_repo_name,
    title,
    description,
    base_branch,
    feature_branch,
    github_access_token,
):
    """Creates the pull request for the head_branch against the base_branch!"""
    github_pull_api = "https://api.github.com/repos/{0}/{1}/pulls".format(
        github_account, git_repo_name
    )
    headers = {
        "Authorization": "token {0}".format(github_access_token),
        "Content-Type": "application/json",
    }

    payload = {
        "title": title,
        "body": description,
        "head": feature_branch,
        "base": base_branch,
    }

    request = requests.post(github_pull_api, headers=headers, data=json.dumps(payload))

    if not request.ok:
        print(f"Error Message: {request.text}.")


def git_push_changes(
    local_dir,
    git_repos_config_file,
    feature_branch,
    github_account,
    base_branch,
    github_access_token,
):
    """Push changes to source repo!"""
    with open(git_repos_config_file) as open_git_config_file:
        data = json.load(open_git_config_file)

    for git_repo_name in data:
        local_repo_path = os.path.join(local_dir, git_repo_name)
        repo = Repo(local_repo_path)
        try:
            if repo.git.diff("HEAD~1..HEAD"):
                logging.info(f"START - [{git_repo_name}]")
                logging.info("PUSH - push changes to origin")
                repo.git.push("--set-upstream", "origin", feature_branch)
                logging.info("PULL - create pull request")
                create_pull_request(
                    github_account,
                    git_repo_name,
                    feature_branch,
                    "Replace text",
                    base_branch,
                    feature_branch,
                    github_access_token,
                )
                logging.info(f"END - [{git_repo_name}]")
        except OSError as error:
            logging.error(f"Error: {error.filename} - {error.strerror}")
