# e(g)it

_e(g)it is an app for replacing text in files across multiple GitHub repositories._

[![CodeQL](https://github.com/datadlog/egit/actions/workflows/codeql-analysis.yml/badge.svg?branch=main)](https://github.com/datadlog/egit/actions/workflows/codeql-analysis.yml) [![PyPI version](https://badge.fury.io/py/egit.svg)](https://badge.fury.io/py/egit) [![Total alerts](https://img.shields.io/lgtm/alerts/g/datadlog/egit.svg?logo=lgtm&logoWidth=18)](https://lgtm.com/projects/g/datadlog/egit/alerts/) [![Language grade: Python](https://img.shields.io/lgtm/grade/python/g/datadlog/egit.svg?logo=lgtm&logoWidth=18)](https://lgtm.com/projects/g/datadlog/egit/context:python)
## Features

-   Clones the configured Github repositories to your local.
-   From a specified base branch, creates a feature branch.
-   Replaces the content in files if it finds the matching text exists in the local repositories, if there is a file pattern specified in the configuration file, the app replaces only in those files.
-   Commits the changes and creates a pull request for code review.

## Tech

e(g)it uses a number of open source projects to work properly:

-   [Python] - Python for the backend.
-   [GitPython] - Python library used to interact with git repositories.
-   [PyYAML] - PyYAML features a complete YAML 1.1 parser.
-   [MkDocs] - MkDocs is a fast, simple and downright gorgeous static site generator that's geared towards building project documentation.
-   [Flake8] - Flake8 is a great toolkit for checking your code base against coding style (PEP8), programming errors and to check cyclomatic complexity.
-   [Tox] - Tox is a generic virtualenv management and test command line tool.
-   [Twine] - Twine is a utility for publishing Python packages on PyPI.
-   [CodeQL] - CodeQL is the analysis engine used by developers to automate security checks, and by security researchers to perform variant analysis.
-   [VSCode] - Visual Studio Code is a source-code editor.

## Documentation

Check out the following website for further information **[egit]**

## License

MIT

[egit]: https://datadlog.github.io/egit/
[python]: https://www.python.org/
[gitpython]: https://gitpython.readthedocs.io/en/stable/tutorial.html
[pyyaml]: https://pyyaml.org/wiki/PyYAML
[mkdocs]: https://www.mkdocs.org/
[flake8]: https://flake8.pycqa.org/en/latest/
[tox]: https://tox.readthedocs.io/en/latest/
[twine]: https://twine.readthedocs.io/en/latest/
[codeql]: https://securitylab.github.com/tools/codeql/
[vscode]: https://code.visualstudio.com/
