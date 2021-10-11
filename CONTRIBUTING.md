# Contributing

Contributions are always welcome and much appreciated! Every little amount helps, and credit will be provided whenever possible.

You can contribute in many ways:

## Types of Contributions

### Report Bugs

Report bugs at https://github.com/nawinto99/egit/issues.

If you are reporting a bug, please include:

-   Your operating system name and version.
-   Any details about your local setup that might be helpful in troubleshooting.
-   Detailed steps to reproduce the bug.

### Fix Bugs

Look through the GitHub issues for bugs. Anything tagged with "bug" and "help
wanted" is open to whoever wants to implement it.

### Implement Features

Look through the GitHub issues for features. Anything tagged with "enhancement"
and "help wanted" is open to whoever wants to implement it.

### Write Documentation

egit could always use more documentation, whether as part of the
official egit docs, in docstrings, or even on the web in blog posts,
articles, and such.

### Submit Feedback

The best way to send feedback is to file an issue at https://github.com/nawinto99/egit/issues.

If you are proposing a feature:

-   Describe how it would work in detail.
-   Keep the scope as little as possible to make implementation easy.
-   Remember that this is a volunteer-driven effort, so any help is appreciated.

## Get Started!

Ready to contribute? Here's how to set up `egit` for local development.

1. Fork the `egit` repo on GitHub.
2. Locally clone your fork.

```
    $ git clone git@github.com:your_name_here/egit.git
```

3. Make sure your fork is set up for local development.

```
    $ cd egit
    $ python -m pip install --upgrade pip
    $ pip install poetry
    $ poetry install -E dev -E test -E doc

```

1. Create a branch for local development:

```
    $ git checkout -b name-of-your-bugfix-or-feature
```

Now you can make your changes locally.

5. Commit your changes and push your branch to GitHub:

```
    $ git add .
    $ git commit -m "Your detailed description of your changes."
    $ git push origin name-of-your-bugfix-or-feature
```

6. Use the GitHub website to submit a pull request.

## Pull Request Guidelines

Before submitting a pull request, make sure it complies with the following guidelines:

1. Tests should be included in the pull request.
2. The docs should be updated if the pull request adds any functionality. Put your new feature in a function with a docstring and add it to the README.md feature list.
3. The pull request should work for Python 3.9. Check
   https://github.com/nawinto99/egit/actions
   and Check to see if the tests pass for the Python version.
