#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for `github_commit_status` package."""

import unittest
from click.testing import CliRunner

#from github_commit_status import github_commit_status
from github_commit_status import cli


class TestGithub_commit_status(unittest.TestCase):
    """Tests for `github_commit_status` package."""

    def setUp(self):
        """Call CLI with --help"""
        self.runner = CliRunner()
        self.help_result = self.runner.invoke(cli.main, ['--help'])

    def test_cli_help(self):
        """It responds properly to --help"""
        self.assertEqual(self.help_result.exit_code, 0)
        self.assertTrue('Show this message and exit.' in
                        self.help_result.output)

    def test_cli_github_token(self):
        """It responds to --github-token argument"""

        self.assertTrue('--github-token TEXT' in self.help_result.output)

    def test_cli_github_repo(self):
        """It responds to --repo argument"""

        self.assertTrue('--repo TEXT' in  self.help_result.output)

    def test_cli_github_commit(self):
        """It responds to --commit argument"""

        self.assertTrue('--commit TEXT' in  self.help_result.output)

    def test_cli_github_status(self):
        """It responds to --status argument"""

        self.assertTrue('--status [error|failure|pending|success]' in
                        self.help_result.output)


    def test_cli_github_description(self):
        """It responds to --description argument"""

        self.assertTrue('--description TEXT' in  self.help_result.output)

