FROM python:3.11-slim

RUN apt-get update && apt-get install -y --no-install-recommends \
    curl \
    build-essential \
    git \
    libffi-dev \
    && rm -rf /var/lib/apt/lists/*

# Create a non-root user
ARG USERNAME=vscode
ARG USER_UID=1000
ARG USER_GID=1000

RUN groupadd --gid $USER_GID $USERNAME && \
    useradd --uid $USER_UID --gid $USER_GID -m $USERNAME && \
    chown -R $USERNAME:$USERNAME /home/$USERNAME

USER $USERNAME
WORKDIR /workspace

# Install Poetry as vscode user
ENV POETRY_VERSION=1.8.2
RUN curl -sSL https://install.python-poetry.org | python3 - && \
    echo 'export PATH="$HOME/.local/bin:$PATH"' >> ~/.bashrc

ENV PATH="/home/${USERNAME}/.local/bin:${PATH}"

