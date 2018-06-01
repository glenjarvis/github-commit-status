#!python
# -*- coding: utf-8 -*-

"""Update Status of GitHub to simulate a CI Server response

This tool will update GitHub status for a given commit SHA1. The
following information needs to be given to GitHub so that the update can
happen:

    - GitHub Token. Personal Access Token (from Developer Settings) to
      give command access to update GitHub repo. See documentation for
      help creating. Environment variable GITHUB_COMMIT_STATUS_TOKEN is
      taken as the default if set.

    - The name of the GitHub repository. Environment variable
      GITHUB_COMMIT_STATUS_REPO is taken as the default if set.

    - The 40 character SHA commit string where the status will be
      updated. Environment variable GITHUB_COMMIT_STATUS_COMMIT is taken
      as the default if set.

    - The status of the test to be reported. There are four possible
      choices:
        o error
        o failure
        o pending
        o success

    - A short description
"""

import os

import click
from github import Github

VERSION = "1.0.3"


def update_github(repo_name, github_token, commit, status, description):
    """Update GitHub with values given"""

    github_client = Github(github_token)
    repo = github_client.get_user().get_repo(repo_name)
    sha = repo.get_commit(sha=commit)
    sha.create_status(
        state=status,
        target_url="",
        description=description,
        context='ci/fake'
    )
    click.echo("GitHub has been updated.")


def print_version(ctx, param, value):
    """Find version from file VERSION and print"""

    # param is passed by click but not needed here
    # pylint: disable=unused-argument
    if not value or ctx.resilient_parsing:
        return
    click.echo('Version {}'.format(VERSION))
    ctx.exit()


# pylint: disable=no-value-for-parameter
@click.command()
@click.option('--github-token', prompt='GitHub Token',
              default=lambda: os.environ.get('GITHUB_COMMIT_STATUS_TOKEN', ''))
@click.option('--repo', prompt='Name of the GitHub repository',
              default=lambda: os.environ.get('GITHUB_COMMIT_STATUS_REPO', ''),
              help='Name of the GitHub repository')
@click.option('--commit', prompt='Commit SHA',
              default=lambda: os.environ.get('GITHUB_COMMIT_STATUS_COMMIT'),
              help='The 40 character SHA1 string for the commit.')
@click.option('--status',
              type=click.Choice(['error', 'failure', 'pending', 'success']),
              help='The status of the commit', prompt=True)
@click.option('--description', prompt='Description',
              help='Description for the test')
@click.option('--version', is_flag=True, callback=print_version,
              expose_value=False, is_eager=True)
def main(repo, github_token, commit, status, description):
    """Update GitHub with the arguments given"""
    update_github(repo, github_token, commit, status, description)


if __name__ == '__main__':
    main()  # pragma: no cover

# TOOD: Validate SHA is 40 characters
# Make github token hidden
