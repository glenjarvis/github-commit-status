====================
github_commit_status
====================

A simple command line for updating a commit's status in GitHub

Project and Build Status
------------------------

.. image:: https://circleci.com/gh/glenjarvis/github-commit-status.svg?style=shield
     :target: https://circle-ci.com/gh/glenjarvis/github_commit_status.svg
     :alt: CircleCI build status

.. image:: https://readthedocs.org/projects/github_commit_status/badge/?version=latest
     :target: http://github_commit_status.readthedocs.io/en/latest/?badge=latest
     :alt: Documentation Status


* `GitHub repo <https://github.com/glenjarvis/github_commit_status/>`_
* `Online Documentation <https://github-commit-status.readthedocs.io/en/latest/readme.html>`_
* `Free Software <https://github.com/glenjarvis/github_commit_status/blob/main/LICENSE>`_


How to Use
----------

Background and Purpose
^^^^^^^^^^^^^^^^^^^^^^

In GitHub, Pull Requests can have some checks against the code in question.
This is a great way to check for things such as white space, coding standards,
etc. Continuous Integration tools, like Travis, use this to update the status
of the commit that you see in Pull Requests in GitHub.

.. image:: https://github.com/glenjarvis/github_commit_status/blob/main/docs/imgs/figure_1_background.png?raw=true
     :alt: Figure 1 Pull Request Example

This is a fairly simple integration and you can also place your own checks here.
In the following example, I made the status pending with a yellow circle with
the phrase "You know you can change this, right?"

.. image:: https://github.com/glenjarvis/github_commit_status/blob/main/docs/imgs/figure_2_custom_status.png?raw=true
     :alt: Custom Status Example

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

.. image:: https://github.com/glenjarvis/github_commit_status/blob/main/docs/imgs/figure_3_account_settings.png?raw=true
     :alt: Upper Right Hand Corner Menu 


Developer Settings
""""""""""""""""""

On the next page that is loaded, the Profile settings page, you will see another
menu to the left. It is a longer menu where the bottom looks similar to the
following. Choose **Developer settings**:

.. image:: https://github.com/glenjarvis/github_commit_status/blob/main/docs/imgs/figure_4_developer_settings.png?raw=true
     :alt: Developer Settings Menu


Create a Personal Access Token
""""""""""""""""""""""""""""""
On the next page, the Developer Settings page, you will see one final menu.
Choose **Personal access tokens**:

.. image:: https://github.com/glenjarvis/github_commit_status/blob/main/docs/imgs/figure_5_personal_accesstokens.png?raw=true
     :alt: Personal Access Token Menu


1. Press the button to **Generate new token**.

2. In the **Token description** enter "github_commit_status". This way we
   remember the purpose of this token.

3. Select the **repo:status** scope checkbox. Anyone who has this token could
   update your GitHub account. So, keep the scope of this token so that it can
   **only** update or access the commit status.

   .. image:: https://github.com/glenjarvis/github_commit_status/blob/main/docs/imgs/figure_6_generate_personal_access_tokens.png?raw=true
       :alt: New Token Screenshot

4. Scroll to the bottom of click the green **Generate token** button.

5. Your token should now be displayed. This token will only display this time.
   You won't be able to see it again and it cannot be recovered.

6. Keep your token safe so that you can use it with this program. Remember, if
   someone else can access this token, they can update your GitHub statuses -
   even if you don't want them to.


Example: Prompt mode
--------------------

If you only need to use this command line rarely, there's no need to worry about
getting the command line arguments correct - you will be prompted for any
required arguments that are missing. This is ideal for students in my class who
only need to update a Pull Requests a few times for a homework assignment. See
the next section for a more scriptable mode and example.


1. Install::

     pip install github_commit_status

2. Run::

     github_commit_status prompt

3. Enter the data that you have collected (e.g., Personal Access Token, commit
   SHA, etc.)

   Here is an example that I used for one of my projects. Remember, don't let
   your Personal Access Token get published like I intentionally did here. I
   ensured this token was deleted before I published this::

     $ github_commit_status prompt

     GitHub Token [26fee6a5d440111a2648312d458b6b4e44c20c1d]:
     Name of the GitHub repository []: my_target_repo
     Commit SHA []: 2dd5f9ce1108d69e863444ee6486e64e0299868f
     Status: pending
     Description: Tests have started

     GitHub has been updated.


Example: For scripting
----------------------

This command can also be used for shell scripts that need to update GitHub.

For security reasons, this mode/subcommand does not provide an option for::

    --github-token

as this is preserved in most shell histories. Instead, the
environment variable *GITHUB_COMMIT_STATUS_TOKEN* should already be set. For
example, in a bash shell::

  export GITHUB_COMMIT_STATUS_TOKEN=26fee6a5d440111a2648312d458b6...


1. Install::

     pip install github_commit_status

2. To see command line options that can be provided::

    $ github_commit_status update --help
    Usage: github_commit_status update [OPTIONS]

      If all options are provided, update GitHub

    Options:
      --repo TEXT                     Name of the GitHub repository  [required]
      --commit TEXT                   The 40 character SHA1 string for the commit.
                                      [required]
      --status [error|failure|pending|success]
                                      The status of the commit  [required]
      --description TEXT              Description for the test  [required]
      --help                          Show this message and exit.

3. Here is an example usage. Remember, your Personal Access Token
   needs to be pre-set in environment variable **GITHUB_COMMIT_STATUS_TOKEN**::

      $ github_commit_status update --repo=my_target_repo \
          --commit="2dd5f9ce1108d69e863444ee6486e64e0299868f" \
          --status=pending \
          --description="Tests are running."


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

* `Contributing <https://github.com/glenjarvis/github_commit_status/blob/main/CONTRIBUTING.rst>`__
