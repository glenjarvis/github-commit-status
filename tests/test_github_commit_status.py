#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for `github_commit_status` package."""

import unittest
from click.testing import CliRunner

from github_commit_status import cli

# These names are from unittest conventions. Ignore
# pylint: disable=invalid-name


class TestGithub_commit_status(unittest.TestCase):
    """Tests for `github_commit_status` package."""

    SAMPLE_SETTINGS = [
        "--repo=sample_repo",
        "--status=pending",
        '--description="Tests started"',
    ]

    def setUp(self):
        """Call CLI with --help"""
        self.runner = CliRunner()
        self.help_result = self.runner.invoke(cli.cli, ["--help"])
        self.version_result = self.runner.invoke(cli.cli, ["--version"])
        self.prompt_result = self.runner.invoke(cli.cli, ["prompt", "--help"])
        self.update_result = self.runner.invoke(cli.cli, ["update", "--help"])

    def test_cli_help(self):
        """It responds properly to --help"""
        self.assertEqual(self.help_result.exit_code, 0)
        self.assertTrue(
            "Show this message and exit." in self.help_result.output
        )

    def test_cli_version(self):
        """It responds properly to --version"""
        self.assertEqual(self.version_result.exit_code, 0)
        self.assertTrue("Version" in self.version_result.output)

    def test_cli_subcommands(self):
        """It has subcommands prompt and update"""
        self.assertEqual(self.help_result.exit_code, 0)
        self.assertTrue(
            "prompt  Prompt for missing options" in self.help_result.output
        )
        self.assertTrue(
            "update  If all options are provided" in self.help_result.output
        )

    def test_cli_prompt_github_token(self):
        """It responds to --github-token argument"""

        self.assertTrue("--github-token TEXT" in self.prompt_result.output)

    def test_cli_prompt_github_repo(self):
        """It responds to --repo argument"""

        self.assertTrue("--repo TEXT" in self.prompt_result.output)

    def test_cli_prompt_github_commit(self):
        """It responds to --commit argument"""

        self.assertTrue("--commit TEXT" in self.prompt_result.output)

    def test_cli_prompt_github_status(self):
        """It responds to --status argument"""

        self.assertTrue(
            "--status [error|failure|pending|success]"
            in self.prompt_result.output
        )

    def test_cli_prompt_github_description(self):
        """It responds to --description argument"""

        self.assertTrue("--description TEXT" in self.prompt_result.output)

    def test_cli_update_github_token(self):
        """It does not respond to --github-token argument"""

        self.assertFalse("--github-token TEXT" in self.update_result.output)

    def test_cli_update_github_repo(self):
        """It responds to --repo argument"""

        self.assertTrue("--repo TEXT" in self.update_result.output)

    def test_cli_update_github_commit(self):
        """It responds to --commit argument"""

        self.assertTrue("--commit TEXT" in self.update_result.output)

    def test_cli_update_github_status(self):
        """It responds to --status argument"""

        self.assertTrue(
            "--status [error|failure|pending|success]"
            in self.update_result.output
        )

    def test_cli_update_github_description(self):
        """It responds to --description argument"""

        self.assertTrue("--description TEXT" in self.update_result.output)

    def test_cli_update_github_commit_length(self):
        """It ensures --commit argument is less than 40 characters"""

        commit_chars = "123456789abcdef0" * 3
        args_opts = ["update", f"--commit={commit_chars}"]
        args_opts.extend(self.SAMPLE_SETTINGS)
        result = self.runner.invoke(cli.cli, args_opts)
        self.assertTrue(
            "commit should be less than 40 characters" in result.output
        )

    def test_cli_update_github_commit_hex(self):
        """It ensures --commit argument only accepts hexadecimal"""

        args_opts = ["update", "--commit=1g"]
        args_opts.extend(self.SAMPLE_SETTINGS)
        result = self.runner.invoke(cli.cli, args_opts)
        self.assertTrue("commit should be hexadecimal" in result.output)


if __name__ == "__main__":
    unittest.main()
