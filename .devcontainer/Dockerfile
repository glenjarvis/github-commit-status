FROM python:3.12-slim

RUN apt-get update && apt-get install -y --no-install-recommends \
    curl \
    build-essential \
    git \
    libffi-dev \
    bash-completion \
    vim \
    && rm -rf /var/lib/apt/lists/*

# Create a non-root user
ARG USERNAME=user
ARG USER_UID=1000
ARG USER_GID=1000

RUN groupadd --gid $USER_GID $USERNAME && \
    useradd --uid $USER_UID --gid $USER_GID -m $USERNAME && \
    chown -R $USERNAME:$USERNAME /home/$USERNAME

USER $USERNAME
WORKDIR /workspace

# Set PATH for pip packages (needed before postCreateCommand runs)
ENV PATH="/home/${USERNAME}/.local/bin:${PATH}"

# Enable bash completion
RUN echo 'if [ -f /etc/bash_completion ]; then . /etc/bash_completion; fi' >> ~/.bashrc
