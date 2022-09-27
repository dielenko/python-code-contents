#!/usr/bin/env bash
#-------------------------------------------------------------------------------------------------------------

# Adding custom .bashrc
sudo cp .devcontainer/source-bashrc/.bashrc ~/.bashrc

# Creating folder to store all needed autocompletion scripts
mkdir ~/.bash_completion_custom

# Setting up Docker CLI with autocompletion
sudo curl \
    -L https://raw.githubusercontent.com/docker/docker-ce/master/components/cli/contrib/completion/bash/docker \
    -o ~/.bash_completion_custom/.docker-completion.sh

# Setting up Docker-compose CLI with autocompletion
sudo curl \
    -L https://raw.githubusercontent.com/docker/compose/1.29.2/contrib/completion/bash/docker-compose \
    -o ~/.bash_completion_custom/.docker-compose-completion.sh

# Setting up Git with autocompletion
sudo curl \
    -L https://raw.githubusercontent.com/git/git/master/contrib/completion/git-completion.bash \
    -o ~/.bash_completion_custom/.git-completion.sh

source ~/.bashrc

echo "Done!"