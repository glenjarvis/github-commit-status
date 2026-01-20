# Installation

## Stable release

To install github-commit-status, run this command in your terminal:

``` console
$ pip install github-commit-status
```

This is the preferred method to install github-commit-status, as it will
always install the most recent stable release.

If you don't have [pip](https://pip.pypa.io) installed, this [Python
installation
guide](http://docs.python-guide.org/en/latest/starting/installation/)
can guide you through the process.

## From sources

The sources for github-commit-status can be downloaded from the [Github
repo](https://github.com/glenjarvis/github-commit-status).

You can either clone the public repository:

``` console
$ git clone git://github.com/glenjarvis/github-commit-status
```

Or download the
[tarball](https://github.com/glenjarvis/github-commit-status/tarball/main):

``` console
$ curl  -OL https://github.com/glenjarvis/github-commit-status/tarball/main
```

Once you have a copy of the source, you can install it with:

``` console
$ pip install -e ".[dev]"
```

This command installs the project in editable mode with development dependencies.

Alternatively, for locked dependency versions:

``` console
$ pip install -r requirements/development.txt
```
