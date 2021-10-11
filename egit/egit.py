"""Module: Main module for all actions!"""
import logging
import os
from datetime import datetime

import yaml
from git_branch import git_create_branch
from git_clone import clone_git_repo
from git_edit import git_replace_text
from git_push import git_push_changes

# datetime object containing current date and time
now = datetime.now()

# Get the current execute file path
file_path = os.path.realpath(__file__)
# print(file_path)

# Get the current directory
cur_dir = os.path.dirname(file_path)
# print(cur_dir)

# Target local git directory
local_dir = os.path.join(cur_dir, "target")
# print(local_dir)

# Logs directory
log_dir = os.path.join(cur_dir, "logs")
# print(log_dir)

log_file = "egit-log-" + now.strftime("%Y%m%d%H%M%S" + ".txt")
log_file_name = os.path.join(log_dir, log_file)
# print(log_file_name)

# Configuration file
app_config_file = os.path.join(cur_dir, "config\\app_config.yml")
# print(config_file)

# Git repos confguration file
git_repos_config_file = os.path.join(cur_dir, "config\\git_repos_config.json")
# print(git_repos_config_file)


with open(app_config_file, "r") as open_config_file:
    cfg = yaml.safe_load(open_config_file)

# Get Github account name
github_account = cfg["main"]["github_account"]
# print(github_account)

base_branch = cfg["main"]["base_branch"]
# print(base_branch)
feature_branch = cfg["main"]["feature_branch"]
# print(feature_branch)
replace_text = cfg["main"]["replace_text"]
# print(replace_text)
file_pattern = cfg["main"]["file_pattern"]
# print(file_pattern)
github_access_token = cfg["main"]["github_access_token"]
# print(github_access_token)

logging.basicConfig(
    filename=log_file_name,
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    datefmt="%Y-%m-%d %I:%M:%S %p",
)


def main():
    """Main function executes all submodules!"""
    logging.info("START - MAIN")
    logging.info("START - CLONE TO LOCAL")
    clone_git_repo(local_dir, git_repos_config_file, github_account)
    logging.info("END - CLONE TO LOCAL")
    logging.info("START - FEATURE BRANCH CHECKOUT")
    git_create_branch(local_dir, git_repos_config_file, base_branch, feature_branch)
    logging.info("END - FEATURE BRANCH CHECKOUT")
    logging.info("START - REPLACE TEXT")
    git_replace_text(
        local_dir,
        git_repos_config_file,
        replace_text,
        file_pattern,
    )
    logging.info("END - REPLACE TEXT")
    logging.info("START - PUSH TO ORIGIN")
    git_push_changes(
        local_dir,
        git_repos_config_file,
        feature_branch,
        github_account,
        base_branch,
        github_access_token,
    )
    logging.info("END - PUSH TO ORIGIN")
    logging.info("END - MAIN")


if __name__ == "__main__":
    main()
