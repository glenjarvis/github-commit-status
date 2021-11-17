FROM python:3.8.7

RUN  pip install --upgrade pip &&  \
     pip install poetry && \
     mkdir /mnt/repo

COPY . /mnt/repo/

WORKDIR /mnt/repo

RUN poetry install && poetry run python tests/test_github_commit_status.py
