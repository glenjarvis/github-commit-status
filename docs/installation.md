# Installation

## Stable release

To install github_commit_status, run this command in your terminal:

``` console
$ pip install github_commit_status
```

This is the preferred method to install github_commit_status, as it will
always install the most recent stable release.

If you don't have [pip](https://pip.pypa.io) installed, this [Python
installation
guide](http://docs.python-guide.org/en/latest/starting/installation/)
can guide you through the process.

## From sources

The sources for github_commit_status can be downloaded from the [Github
repo](https://github.com/glenjarvis/github_commit_status).

You can either clone the public repository:

``` console
$ git clone git://github.com/glenjarvis/github_commit_status
```

Or download the
[tarball](https://github.com/glenjarvis/github_commit_status/tarball/main):

``` console
$ curl  -OL https://github.com/glenjarvis/github_commit_status/tarball/main
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
