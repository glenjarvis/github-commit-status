.. _contribution_link:

============
Contributing
============

Ready to contribute? Your contributions are very much welcomed and credit will
be given. These Guidelines will help you effectively contribute to this project
and guide you to successfully merged Pull Requests.

If you haven't contributed to an Open Source project before, these Guidelines
may feel intimidating. Consider taking my online course `How to contribute to
an Open Source Project <https://GlenJarvis.com/v/how-to-open-source>`_.

Here's how to set up **github_commit_status** for local development.


Getting Started!
----------------

Docker Setup
^^^^^^^^^^^^

For a quick set-up, without having to install much:

 .. code-block:: bash

      cd <to the repo directory>
      docker image fetch glenjarvis/github_commit_status:latest
      docker run --rm -it -v $(pwd):/mnt/repo glenjarvis/github_commit_status bash
      poetry shell

In another window, you can use any text editor that you want while running
python commands in the running docker container.

I am just starting to convert to a Docker setup, so feel free to report any
problems and/or sugestions regarding the above.


Local Setup
^^^^^^^^^^^

For a more traditional stup:

This repository is in standard wheel format so it can be used like a normal
Python Package. However, if you follow these instructions, you can avoid having
your python environment look like this:

.. image:: https://imgs.xkcd.com/comics/python_environment.png

If you need help with background knowledge, see online training video:
https://GlenJarvis.com/v/virtual-environments.

1. Find a place to work:

    .. code-block:: bash

      $ cd path_where_you_want_this_repo

2. Clone the project:

    .. code-block:: bash

      $ git clone https://github.com/glenjarvis/github_commit_status.git
      $ cd github_commit_status

3. Make a virtualenv named **venv** for your Python environment of choice:

    .. code-block:: bash

      $ python3 -m venv venv

4. Activate the Virtual Enviroment. Every time you come back to work on this
   project, you will need to activate your virtual environment:

    .. code-block:: bash

      $ cd path_of_this_repo
      $ source venv/bin/activate

   When the Virtual Environment is activated, you should see ``venv`` in the
   prompt. It may look something  to this:

    .. code-block:: bash

       (venv) $

   I often like to be able to jump to this folder quickly from
   anywhere and have it automatically setup my virtual environment.
   So, I put something like this in my ``$HOME/.bashrc`` (or equivalent)
   file:

     .. code-block:: bash

         function cd_github_commit_status {
             deactivate 2> /dev/null
             cd /FULL_PATH_TO_THIS_DIRECTORY
             source venv/bin/activate
         }

5. Upgrade Pip. The Pip that comes with a new Virtual Environment is often too
   old. Upgrade it to be sure it is current:

       .. code-block:: bash

         (venv)$ pip install --upgrade pip


6. Decide if you wish to use Poetry (I recommend it).

   It will do a pretty good job of keeping the dependencies for this project
   organized. If you use Poetry, do the following and skip to step 9.

       .. code-block:: bash

         (venv)$ pip install poetry
         (venv)$ poetry install


7. If you didn't do Poetry above, go ahead and install the project as normal:

   This project is in wheel format. So, simply install a reference in your
   virtual environment so that you can edit files in this folder and see an
   immediate affect in the virtual environment::

       (venv)$ pip install .

8. Install extra packages for development::

       (venv)$  pip install -r requirements_dev.txt

9. (optional) Install the Git Hooks. Git Hooks are a way of running code
   locally against your commits before you make them. Often this can catch
   errors before they are pushed to GitHub.

   To install the GitHook:

       .. code-block:: bash

         $ make git-hook

   If you are having a difficult time making the commit and want to over-ride
   the behavior in the hook ("Just do it anyway"), you can do this:

       .. code-block:: bash

         $ git commit --no-verify

   If it is getting in your way and you want to remove it (you can always put
   it back), do this:

       .. code-block:: bash

         $ make hooks-go-away


10. Check out a topic branch and begin working.



Extra Code Style
^^^^^^^^^^^^^^^^

* Functions and methods should be as short as possible, breaking concepts into
  smaller functions/methods whenever possible.

* The pull request should work for Python 3.5, 3.6, 3.7, 3.8, and for PyPy.
  When you push to GitHub, we will check this for you. If you want to test it
  yourself, either run `tox` locally, or check
  https://travis-ci.org/glenjarvis/github_commit_status/pull_requests and make
  sure that the tests pass for all supported Python versions::

      $ tox

* Follow the Zen

  .. code-block:: text

    The Zen of Python, by Tim Peters

    Beautiful is better than ugly.
    Explicit is better than implicit.
    Simple is better than complex.
    Complex is better than complicated.
    Flat is better than nested.
    Sparse is better than dense.
    Readability counts.
    Special cases aren't special enough to break the rules.
    Although practicality beats purity.
    Errors should never pass silently.
    Unless explicitly silenced.
    In the face of ambiguity, refuse the temptation to guess.
    There should be one-- and preferably only one --obvious way to do it.
    Although that way may not be obvious at first unless you're Dutch.
    Now is better than never.
    Although never is often better than *right* now.
    If the implementation is hard to explain, it's a bad idea.
    If the implementation is easy to explain, it may be a good idea.
    Namespaces are one honking great idea -- let's do more of those!


Tips and Tricks
^^^^^^^^^^^^^^^

* TravisCI will run tests against your pull requests and catch test errors:
  https://travis-ci.org/glenjarvis/github_commit_status/pull_requests

* The pull request should work for Python 3.5, 3.6, 3.7, 3.8 and for PyPy.
  Running ``tox`` locally will help catch errors across versions of Python
  and make sure that the tests pass for all supported Python versions::

      $ tox

* Commits should follow `the seven rules of a great Git commit <https://chris.beams.io/posts/git-commit/>`_


Pull Request Guidelines
-----------------------

Please keep a good Git hygiene in your contribution. Not everyone knows how to
use a Source Control Management system like Git properly. We're here to help.

Guidelines
^^^^^^^^^^

* Use a different topic branch for each topic
* Keep commits small
* Rebase topic branches (i.e., Don't merge main back into topic)
* `Use proper commit message <https://chris.beams.io/posts/git-commit/>`_


Code of Conduct
---------------

We value the participation of each member of the Open Source community and want
all contributors and consumers of this project to have an enjoyable and
fulfilling experience. Accordingly, all contributors are expected to show
respect and courtesy to other contributors and community members working within
this project.

To make clear what is expected, all communication around this project by all
contributing members (including Glen Jarvis) are required to conform to the
`Python Packaging Authority Code of Conduct
<https://www.pypa.io/en/latest/code-of-conduct/>`__.

