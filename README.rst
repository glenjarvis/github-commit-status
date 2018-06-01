====================
github_commit_status
====================

A simple command line for updating a commit's status in GitHub

Project and Build Status
------------------------

.. image:: https://travis-ci.org/glenjarvis/github_commit_status.svg?branch=master
     :target: https://travis-ci.org/glenjarvis/github_commit_status
     :alt: Travis tests

.. image:: https://pyup.io/repos/github/glenjarvis/github_commit_status/shield.svg
     :target: https://pyup.io/repos/github/glenjarvis/github_commit_status/
     :alt: Updates

.. image:: https://pyup.io/repos/github/glenjarvis/github_commit_status/python-3-shield.svg
     :target: https://pyup.io/repos/github/glenjarvis/github_commit_status/
     :alt: Python 3

.. image:: https://readthedocs.org/projects/github_commit_status/badge/?version=latest
     :target: http://github_commit_status.readthedocs.io/en/latest/?badge=latest
     :alt: Documentation Status

.. image:: https://ci.appveyor.com/api/projects/status/github/glenjarvis/github_commit_status?branch=master&svg=true
     :target: https://ci.appveyor.com/project/glenjarvis/github_commit_status/branch/master
     :alt: Windows build status on Appveyor

* GitHub repo: https://github.com/glenjarvis/github_commit_status/
* Documentation: `Read The Docs <https://github_commit_status.readthedocs.io/>`_
* Free software: `LICENSE <https://github.com/glenjarvis/github_commit_status/blob/master/LICENSE>`_


How to Use
----------

Background and Purpose
^^^^^^^^^^^^^^^^^^^^^^

In GitHub, Pull Requests can have some checks against the code in question.
This is a great way to check for things such as white space, coding standards,
etc. Continuous Integration tools, like Travis, use this to update the status
of the commit that you see in Pull Requests in GitHub.

.. image:: https://github.com/glenjarvis/github_commit_status/blob/master/docs/imgs/figure_1_background.png

This is a fairly simple integration and you can also place your own checks here.
In the following example, I made the status pending with a yellow circle with
the phrase "You know you can change this, right?"

.. image:: https://github.com/glenjarvis/github_commit_status/blob/master/docs/imgs/figure_2_custom_status.png

This command line tool will allow you to update the status of any commit that
you have access to in GitHub. It was built to be a teaching tool for a course
on Source Control Management (Git) and GitHub integrations. However, it is
stable and can be used in production seamlessly -- especially environments
where it makes sense to use a command line instead of your own library.


Gather the info that you need
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

To update the status of a commit in a Pull Request, you will need to provide
some basic information:

1. The name of the GitHub repository which has your Pull Request

2. The commit SHA that is to be updated (e.g., the last commit  in a pull
   request)

3. The desired status of the commit:
    - "success" (GitHub displays a green checkmark)
    - "pending" (GitHub displays a yellow circle)
    - "error" or "failure" (GitHub displays a red 'X')

4. Description (e.g., "You know you can change this, right?" was the description
   used in the example above)

5. Authorization token. This will allow the command to act like you.
   Instructions on how to create this token follow.


Personal Access Token
^^^^^^^^^^^^^^^^^^^^^

This tool is intended to change the status of a GitHub Pull Request. That is
something that should only be allowed by someone who is authorized. You
wouldn't want someone that you hadn't authorized updating your Pull Request
statuses.

You will need to generate a Personal Access Token so that this command line can
act like you. Keep this token safe -- it is like a password.

This is done in your account settings configuration. Don't confuse the
project's settings with your settings for your account.


Profile Settings
""""""""""""""""

In the upper right hand corner, you will see your avatar photo (or a default
avatar image). When you click the avatar, there will be a drop down menu with
menu options. Choose the **Settings** option.

.. image:: https://github.com/glenjarvis/github_commit_status/blob/master/docs/imgs/figure_3_account_settings.png



Developer Settings
""""""""""""""""""

On the next page that is loaded, the Profile settings page, you will see another
menu to the left. It is a longer menu where the bottom looks similar to the
following. Choose **Developer settings**:

.. image:: https://github.com/glenjarvis/github_commit_status/blob/master/docs/imgs/figure_4_developer_settings.png


Create a Personal Access Token
""""""""""""""""""""""""""""""
On the next page, the Developer Settings page, you will see one final menu.
Choose **Personal access tokens**:

.. image:: https://github.com/glenjarvis/github_commit_status/blob/master/docs/imgs/figure_5_personal_accesstokens.png



1. Press the button to **Generate new token**.

2. In the **Token description** enter "github_commit_status". This way we
   remember the purpose of this token.

3. Select the **repo:status** scope checkbox. Anyone who has this token could
   update your GitHub account. So, keep the scope of this token so that it can
   **only** update or access the commit status.

   .. image:: https://github.com/glenjarvis/github_commit_status/blob/master/docs/imgs/figure_6_generate_personal_access_tokens.png

4. Scroll to the bottom of click the green **Generate token** button.

5. Your token should now be displayed. This token will only display this time.
   You won't be able to see it again and it cannot be recovered.

6. Keep your token safe so that you can use it with this program. Remember, if
   someone else can access this token, they can update your GitHub statuses -
   even if you don't want them to.


Example: When needed rarely
---------------------------

If you only need to use this comand line rarely, there's no need to worry about
getting the command line arguments correct - you will be prompted for any
required arguments that are missing. This is ideal for students in my class who
only need to update a Pull Requests a few times for a homework assignment. See
the next section for a more scriptable and professional example.


1. Install::

     pip install github_commit_status

2. Run::

     github_commit_status

3. Enter the data that you have collected (e.g., Personal Access Token, commit
   SHA, etc.)

   Here is an example that I used for one of my projects. Remember, don't let
   your Personal Access Token get published like I intentionally did here. I
   ensured this token was deleted before I published this::

     $ github_commit_status
     Github token []: 26fee6a5d440111a2648312d458b6b4e44c20c1d
     Name of the GitHub repository []: experiment_20180525
     Commit SHA []: 2dd5f9ce1108d69e863444ee6486e64e0299868f
     Status: pending
     Description: Tests are running
     GitHub has been updated.


Example: For scripting
----------------------

This command can also be used for shell scripts that need to update GitHub. In
this example, we include the Personal Access Token as a command line option.
That's not as secure, since the shell keeps a history of your commands. See the
next example for a better option.


1. Install::

     pip install github_commit_status

2. To see command line options that can be provided::

    $ github_commit_status --help
    Usage: github_commit_status [OPTIONS]

      Update GitHub with the arguments given

    Options:
      --github-token TEXT
      --repo TEXT                     Name of the GitHub repository
      --commit TEXT                   The 40 character SHA1 string for the commit.
      --status [error|failure|pending|success]
                                      The status of the commit
      --description TEXT              Description for the test
      --version
      --help                          Show this message and exit.

3. Here is an example usage. Remember, using your Personal Access Token
   on the command line isn't as secure::

      $ github_commit_status --status=failure --description="There are failed tests." --commit=2dd5f9ce1108d69e863444ee6486e64e0299868f --repo=experiment_20180525 --github-token=26fee6a5d440111a2648312d458b6b4e44c20c1d


Example: Scripting with better security
---------------------------------------

This command can be used for shell scripts to update GitHub without including
the Personal Access Token as an option. If GitHub token (e.g., your Personal
Access Token) isn't provided, this command will look for the token in the
**GITHUB_COMMIT_STATUS_TOKEN** environment variable.


1. Install::

     pip install github_commit_status

2. Export the GITHUB_COMMIT_STATUS_TOKEN. For example, in the Bash shell::

     export GITHUB_COMMIT_STATUS_TOKEN=26fee6a5d440111a2648312d458b6b4e44c20c1d

3. To see command line options that can be provided::

    $ github_commit_status --help
    Usage: github_commit_status [OPTIONS]

      Update GitHub with the arguments given

    Options:
      --github-token TEXT
      --repo TEXT                     Name of the GitHub repository
      --commit TEXT                   The 40 character SHA1 string for the commit.
      --status [error|failure|pending|success]
                                      The status of the commit
      --description TEXT              Description for the test
      --version
      --help                          Show this message and exit.


4. Here is an example usage. However, we simply neglect to include the::

     --github-token

   argument as we have already set the **GITHUB_COMMIT_STATUS_TOKEN**
   environment variable::

      $ github_commit_status --repo=experiment_20180525 --commit=2dd5f9ce1108d69e863444ee6486e64e0299868f --status=success --description="All tests passed."
      GitHub Token [26fee6a5d440111a2648312d458b6b4e44c20c1d]:
      GitHub has been updated.

   This currently still displays the GitHub Access Token on the screen, but it
   is not recorded into your shell's history. In future versions of this command
   line, we will prevent the Personal Access Token from displaying on the screen
   as well. `Lucky Issue #13
   <https://github.com/glenjarvis/github_commit_status/issues/13>`_ is used to
   track the status of this change


Make this better by Contributing
--------------------------------

This is an Open Source project and contributions are always welcome, and they
are greatly appreciated! Every little bit helps, and credit will always be
given.

You can contribute in many ways:

* `Report bugs <https://github.com/glenjarvis/github_commit_status/issues>`__
* `Write Documentation <https://github_commit_status.readthedocs.io/>`__
* `Fix bugs <https://github.com/glenjarvis/github_commit_status/issues>`__

To maximize the chance that your hard work gets merged, we have these guidelines
to guide you along the way to a successfully merged Pull Request:

* :ref:`contribution_link`
* https://github.com/glenjarvis/github_commit_status/blob/master/CONTRIBUTING.rst
