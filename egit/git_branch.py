"""Module: Create feature branch from the base branch!"""
import json
import logging
import os

from git import Repo


def git_create_branch(local_dir, git_repos_config_file, base_branch, feature_branch):
    """Create feature branch from the base branch!"""
    with open(git_repos_config_file) as open_git_config_file:
        data = json.load(open_git_config_file)

    for git_repo_name in data:

        logging.info(f"START - [{git_repo_name}]")
        try:
            local_repo_path = os.path.join(local_dir, git_repo_name)
            repo = Repo.init(local_repo_path)
            logging.info(f"CREATE - Checkout branch [{base_branch}]")
            repo.git.checkout(base_branch)
            repo.git.branch(feature_branch)
            logging.info(f"CREATE - Checkout branch [{feature_branch}]")
            repo.git.checkout(feature_branch)

        except OSError as error:
            logging.error(f"Error: {error.filename} - {error.strerror}")
        logging.info(f"END - [{git_repo_name}]")
