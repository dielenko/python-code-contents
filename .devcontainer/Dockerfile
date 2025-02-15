ARG IMAGE_NAME="noble"
FROM mcr.microsoft.com/devcontainers/base:${IMAGE_NAME}

# Install Bash Completion
RUN sudo apt update && \
    sudo apt install bash-completion

# Setting Git with autocompletion
RUN sudo curl \
    -L https://raw.githubusercontent.com/git/git/master/contrib/completion/git-completion.bash \
    -o /usr/share/bash-completion/completions/git

# Enable autocompletion for Git
RUN { \
    echo 'source /usr/share/bash-completion/completions/git'; \
    echo 'source <(helm completion bash)'; \
} >> ~/.bashrc
