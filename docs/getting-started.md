---
title: Getting started
---

# Getting started

e(g)it is a app for replace text in many files across multiple Github repositories. If you're familiar with Python, you
can install e(g)it with [`pip`][1], the Python package manager.

In case you're running into problems, consult the [troubleshooting][2] section.

## Prerequisites

-   Install [git](https://git-scm.com/)
-   Install [Python](https://www.python.org/)

## Installation

### with pip <small>recommended</small> { data-toc-label="with pip" }

e(g)it can be installed with `pip`:

```
pip install egit
```

### with git

e(g)it can be directly used from [GitHub][3] by cloning the
repository into a subfolder of your project root which might be useful if you
want to use the very latest version:

1. Clone repository to your local

```
    $ git clone https://github.com/datadlog/egit.git
```

1. Ensure [poetry](https://python-poetry.org/docs/) is installed, if not follow below.

```
    $ cd egit
    $ python -m pip install --upgrade pip
    $ pip install poetry
```

1. Install dependencies and start your virtualenv:

```
    $ poetry install
```

[1]: #with-pip-recommended
[2]: troubleshooting.md
[3]: https://github.com/datadlog/egit
