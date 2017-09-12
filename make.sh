#!/bin/bash

#Check if git is install or not in the system

echo 'Check if git is installed in the System'
git --version 2>&1 >/dev/null
GIT_IS_AVAILABLE=$?

if [ $GIT_IS_AVAILABLE -eq 0 ]; then
echo 'Git is installed'
else
    echo 'Git is not installed '
    echo 'Running brew command to install git'
    brew install git
fi

echo 'Removing the codebase if it is already present in the working Directory'
rm -rf PasswordProtect

echo 'Pulling the CodeBase from git'
git clone https://github.com/arpithpathange/PasswordProtect.git

echo 'Need root permission to create the log folder and file \in /var/lib direcrtory. Please provide the root access'
sudo mkdir /var/log/password
sudo touch /var/log/password/password.log
echo 'changing the owner of the log file to' $USER
sudo chown $USER /var/log/password/password.log





