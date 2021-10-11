"""Module: Clone remote repos to local!"""
import json
import logging
import os
import shutil
import stat

from git import Repo


def remove_readonly_file(_, name, __):
    """Change the mode of the file from read-only to write!"""
    logging.info(f"REMOVE - remove read only file: {name}")
    os.chmod(name, stat.S_IWRITE)
    os.remove(name)


def clone_git_repo(local_dir, git_repos_config_file, github_account):
    """Clone the repos from remote directory!"""
    with open(git_repos_config_file) as open_git_config_file:
        data = json.load(open_git_config_file)

    for git_repo_name in data:
        remote_git_repo_url = (
            "https://github.com/" + github_account + "/" + git_repo_name + ".git"
        )
        local_repo_dir = os.path.join(local_dir, git_repo_name)
        try:
            logging.info(f"START - [{git_repo_name}]")
            if os.path.isdir(local_repo_dir):
                logging.info("CLEAN - cleaning local folder")
                shutil.rmtree(local_repo_dir, onerror=remove_readonly_file)
                Repo.clone_from(remote_git_repo_url, local_repo_dir)
            else:
                Repo.clone_from(remote_git_repo_url, local_repo_dir)
            logging.info(f"END - [{git_repo_name}]")

        except OSError as error:
            logging.error(f"Error: {error.filename} - {error.strerror}")
