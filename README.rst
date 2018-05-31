====================
github_commit_status
====================

A simple command line for updating a GitHub status

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


How to Configure
-----------------

Background
^^^^^^^^^^

If you have every looked at a Pull Request in GitHub, you've seen that there are
"Checks" that should pass before the Pull Request is merged. If all is well, you
will see a message like "All checks have passed" and a big green button "Merge
pull request." Or, on a very bad day, you may see a large red 'X' with a message
like 'All checks have failed.'

How exactly does that get set? To help teach about GitHub integrations, this
command was made so one can see how updates to Git Hub pull requests are made.

In reality, this is an update of a "status" of a commit hash. And, GitHub
reflects those statuses in a Pull Request.

Personal Access Token
^^^^^^^^^^^^^^^^^^^^^

This code is intended to change the status of a GitHub Pull Request. That is
something that should only be allowed by someone who is authorized. You wouldn't
want someone that you hadn't authorized updating your Pull Request statuses. So,
you will need to generate a Personal Access Token so that you can authorize
yourself to update.

This is done in your account settings configuration. Don't confuse the project
settings with the settings for your account


Profile Settings
""""""""""""""""

In the upper right hand corner, you will see your avatar photo (or a default
avatar image). When you click the avatar, there will be a drop down menu with
meu options such as:

- Signed in as...
- Your profile
- Your stars
- Your gists
- Help
- **Settings**
- Sign out

Choose the **Settings** option.


Developer Settings
""""""""""""""""""

On the next page that is loaded, the Profile settings page, you will see another
menu to the left. It is a longer menu where the bottom looks similar to:

- Repositories
- Organizations
- Saved replies
- Applications

- **Developer settings**


Note that **Developer settings** is offset from the other menu. Choose
**Developer settings**.


Personal Access Tokens
""""""""""""""""""""""
Os the next page, the Developer Settings page, you will see one final menu:

- OAuth Apps
- GitHub Apps
- **Personal access tokens**

Choose **Personal access tokens**.


1. Press the button to **Generate new token**.
2. In the **Token description** enter "github_commit_status". This way we
   remember the purpose of this token.
3. Select the **repo:status** scope checkbox. Anyone who has this token could
   update your GitHub account. So, keep the scope of that the token can do to be
   **only** updating or accessing the commit status.
4. Scroll to the bottom of click the green **Generate token** button.
5. Your should now be displayed. This token will only display this time. You
   won't be able to see it again and it cannot be recovered.
6. Keep your token safe so that you can use it with this program. Remember, if
   someone else can access this token, they can update your GitHub statuses -
   even if you don't want them to.


Name of the repository
^^^^^^^^^^^^^^^^^^^^^^

The Personal Access Token that you have generated above can be used to update
any repository that you have access to. You will need to specify the repository
to update.

Remember, the GitHub URL has the repository name. The format is as follows:

https://github.com/<github_username>/<project_name>

For example, the Linux GitHub repository is at this URL:

https://github.com/torvalds/linux

The username is **torvalds** (Linus Torvalds) and the GitHub respoitory name is
**linux**.

You will need the name of your repository when using this program.


How to use
----------

Find a commit in a Pull Request that you would like to update.

1. `pip install github_commit_status`

2. run `github_commit_status`

3. Enter the data that you have collected as seen in the code snippet below.
   Don't worry, I deleted this GitHub token in this example before this was ever
   published. (You should *always* keep your Personal Access Tokens to GitHub a
   secret - its like a password):

.. code::

    $ github_commit_status
    Github token []: 26fee6a5d440111a2648312d458b6b4e44c20c1d
    Name of the GitHub repository []: experiment_20180525
    Commit SHA []: 2dd5f9ce1108d69e863444ee6486e64e0299868f
    Status: pending
    Description: Tests are running
    GitHub has been updated.



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
