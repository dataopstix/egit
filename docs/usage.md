# Usage

## Generate access token

Create a GitHub access token to use when submitting pull requests

## Modify Configuration

1. Modify the configuration file

    > egit/config/app_config.yml

    - **github_account:** _Github account name or organization name._
    - **base_branch:** _For building feature branches, start with the base branch._
    - **feature_branch:** _Give the name of the feature branch._
    - **replace_text:** _In the key value pair, enter the text you want to replace(left: old value, right: new value)._
    - **file_pattern:** _If there is a file extension, specify it; otherwise, leave it blank._
    - **github_access_token:** _Copy the access token that was generated in Step [1]._

2. Add the Github repositories to the list.

    > egit/config/git_repos_config.json

## Run the application

```
$ cd egit
$ poetry run egit
```

[1]: #generate-access-token
