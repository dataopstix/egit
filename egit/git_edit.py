"""Module: Replace the text in local repo files!"""
import fnmatch
import json
import logging
import os

from git import Repo


def find_replace(directory, find, replace, file_pattern):
    """Find files!"""
    for path, _, files in os.walk(os.path.abspath(directory)):
        for filename in fnmatch.filter(files, file_pattern):
            filepath = os.path.join(path, filename)
            with open(filepath) as file:
                source = file.read()
            source = source.replace(find, replace)
            with open(filepath, "w") as file:
                file.write(source)


def git_replace_text(
    local_dir,
    git_repos_config_file,
    replace_text,
    file_pattern,
):
    """Replace text in files!"""
    with open(git_repos_config_file) as open_git_config_file:
        data = json.load(open_git_config_file)

    for git_repo_name in data:
        repo_path = os.path.join(local_dir, git_repo_name)
        repo = Repo(repo_path)
        logging.info(f"START - [{git_repo_name}]")
        for replace_from, replace_to in replace_text.items():
            logging.info(
                f"CHECK - find and replace text from: [{replace_from}] to: [{replace_to}]"
            )

            find_replace(
                repo_path,
                replace_from,
                replace_to,
                file_pattern,
            )
            if repo.is_dirty(untracked_files=True):
                commit_message = "[Update]: Text from: {0} to: {1}".format(
                    replace_from, replace_to
                )
                repo.git.add(A=True)
                repo.git.commit(m=commit_message)
                logging.info("COMMIT - Commit changes")
            else:
                logging.info("COMMIT - No changes found")
        logging.info(f"END - [{git_repo_name}]")
