# -*- coding: utf-8 -*-

"""Top-level package for github_commit_status"""

from importlib.metadata import version, PackageNotFoundError

__author__ = "Glen Jarvis"
__email__ = "glen@glenjarvis.com"

try:
    __version__ = version("github_commit_status")
except PackageNotFoundError:
    # Package is not installed (e.g., running from source)
    __version__ = "unknown"
