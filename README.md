# Create a new local repo

####This simple script adds a new bare initialized git repo on a local filesystem.

It accepts the folowing arguments:

usage: new_git_repo.py [-h] -r REPO_NAME [-d GIT_DIR] [-u GIT_USER]
                       [-g GIT_GROUP]

Create a new git repo.

optional arguments:

  -h, --help            show this help message and exit
  
  -r REPO_NAME, --repo_name REPO_NAME
                        The name of the repo
                        
  -d GIT_DIR, --git_dir GIT_DIR
                        The base dir of git
                        
  -u GIT_USER, --git_user GIT_USER
                        The name git user
                        
  -g GIT_GROUP, --git_group GIT_GROUP
                        The groups of the git user

Run this program as regular user with sudo or with sufficient rights to chown.

##### After running this program do the following on the client's computer
* cd myproject
* git init
* git add .
* git commit -m 'initial commit'
* git remote add origin git@gitserver:GIT_DIR/REPO_NAME.git
* git push origin master

#####and to get the repo's updates
* git pull origin master

Inprired by [Git on the Server - Setting Up the Server](http://git-scm.com/book/en/Git-on-the-Server-Setting-Up-the-Server)