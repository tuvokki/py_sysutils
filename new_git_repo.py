#!/usr/bin/env python

import argparse, os, subprocess

parser = argparse.ArgumentParser(description='Create a new git repo.',epilog='Run this program as regular user with sudo.')

parser.add_argument('-r','--repo_name', help='The name of the repo', required=True)

args = parser.parse_args()

git_dir = "/Users/wouter/test/development/git/"
git_user = "root"
git_group = "wheel"
# git_dir = "/home/development/git/"
# git_user = "git"
# git_group = "git"
repo_dir = git_dir + args.repo_name + ".git"

# create git_dir
if not os.path.isdir(repo_dir):
  try:
    # print "cd %s" %(args.repo_name)
    # print "sudo mkdir %s.git" %(args.repo_name)
    os.makedirs(repo_dir)
    # print "cd %s.git" %(args.repo_name)
    # print "sudo git --bare init"
    proc = subprocess.Popen(['/usr/bin/env','git','--bare','init'], cwd=repo_dir)
    # print "cd .."
    # print "sudo chown -R git:git %s.git" %(args.repo_name)
    proc = subprocess.Popen(['/usr/bin/env','chown','-R',git_user+':'+git_group,repo_dir])
    print """
  # Now on the client's computer
  $ cd myproject
  $ git init
  $ git add .
  $ git commit -m 'initial commit'
  $ git remote add origin git@gitserver:/opt/git/project.git
  $ git push origin master
  # to get the repo's updates
  $ git pull origin master
    """
  except OSError, e:
    raise e



