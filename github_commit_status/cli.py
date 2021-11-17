#!python
# -*- coding: utf-8 -*-

"""Update Status of a commit in GitHub

This tool will update the GitHub status for a given commit SHA1. The
following information needs to be given so that the update can happen:

* GitHub Token. Personal Access Token (from Developer Settings) to
  give command access to update GitHub repo. See documentation for
  help creating. Environment variable GITHUB_COMMIT_STATUS_TOKEN is
  taken as the default if set.

* The name of the GitHub repository. Environment variable
  GITHUB_COMMIT_STATUS_REPO is taken as the default if set.

* The 40 character SHA commit string where the status will be
  updated. Environment variable GITHUB_COMMIT_STATUS_COMMIT is taken
  as the default if set.

* The status of the test to be reported. There are four possible
  choices (error, failure, pending or success).

* A short description

There are two modes for this command: prompt and update

Prompt
------
This command line was originally written as a learning exercise for a
beginner course. This allows prompting for options if not provided to
make this command easier to use. To enable this mode, use the subcommand
"prompt".

Example::

    $ github_commit_status prompt

Update
------
This command can be very useful as component of a shell script. To
enable this functionality without the prompting, use the subcommand
"update".

Example::

    $ github_commit_status update --repo=my_target_repo \
          --commit="2dd5f9ce1108d69e863444ee6486e64e0299868f" \
          --status=pending \
          --description="Tests are running."
"""

import os

import click
from github import Github

VERSION = "1.1.0"
INVALID_TOKEN = "Invalid GitHub Token"


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


def validate_commit_sha1(ctx, param, value):
    """Validate value is a valid SHA1"""
    # params ctx, param passed by click but not needed here
    # pylint: disable=unused-argument

    if len(value) > 40:
        raise click.BadParameter("commit should be less than 40 characters")

    try:
        int(value, 16)
    except ValueError:
        raise click.BadParameter("commit should be hexadecimal")

    return value


def print_version(ctx, param, value):
    """Find version from file VERSION and print"""

    # param is passed by click but not needed here
    # pylint: disable=unused-argument
    if not value or ctx.resilient_parsing:
        return
    click.echo('Version {}'.format(VERSION))
    ctx.exit()


@click.group()
@click.option('--version', is_flag=True, callback=print_version,
              expose_value=False, is_eager=True)
def cli():
    """Update the status of a commit in GitHub"""
    pass


# pylint: disable=no-value-for-parameter
@click.command()
@click.option('--github-token', prompt='GitHub Token',
              default=lambda: os.environ.get('GITHUB_COMMIT_STATUS_TOKEN', ''))
@click.option('--repo', prompt='Name of the GitHub repository',
              default=lambda: os.environ.get('GITHUB_COMMIT_STATUS_REPO', ''),
              help='Name of the GitHub repository')
@click.option('--commit', callback=validate_commit_sha1, prompt='Commit SHA',
              default=lambda: os.environ.get('GITHUB_COMMIT_STATUS_COMMIT'),
              help='The 40 character SHA1 string for the commit.')
@click.option('--status',
              type=click.Choice(['error', 'failure', 'pending', 'success']),
              help='The status of the commit', prompt=True)
@click.option('--description', prompt='Description',
              help='Description for the test')
def prompt(repo, github_token, commit, status, description):
    """Prompt for missing options and update GitHub

    Example:
      $ github_commit_status prompt
      GitHub Token [26fee6a5d440111a2648312d458b6b4e44c20c1d]:
      Name of the GitHub repository []: my_target_repo
      Commit SHA []: 2dd5f9ce1108d69e863444ee6486e64e0299868f
      Status: pending
      Description: Tests have started

      GitHub has been updated.
    """
    update_github(repo, github_token, commit, status, description)


@click.command()
@click.option('--repo', required=True,
              help='Name of the GitHub repository')
@click.option('--commit', callback=validate_commit_sha1, required=True,
              help='The 40 character SHA1 string for the commit.')
@click.option('--status', required=True,
              type=click.Choice(['error', 'failure', 'pending', 'success']),
              help='The status of the commit')
@click.option('--description', required=True, help='Description for the test')
def update(repo, commit, status, description):
    """If all options are provided, update GitHub

    For security reasons, this subcommand does not provide an option for
    `--github-token` as this is preserved in most shell histories.

    Instead, the environment variable `GITHUB_COMMIT_STATUS_TOKEN`
    should already be set. For example, in a bash shell::

      export GITHUB_COMMIT_STATUS_TOKEN=26fee6a5d440111a2648312d458b6...

    Token must be provided as part of the environment, it cannot be
    given as part of a command line option for security reasons.

    Example:
     $ github_commit_status update --repo=my_target_repo \\
           --commit="2dd5f9ce1108d69e863444ee6486e64e0299868f" \\
            --status=pending
           --description="Tests are running."
    """
    github_token = os.environ.get('GITHUB_COMMIT_STATUS_TOKEN', INVALID_TOKEN)
    update_github(repo, github_token, commit, status, description)


# Subcommands
cli.add_command(prompt)
cli.add_command(update)


if __name__ == '__main__':
    cli()
