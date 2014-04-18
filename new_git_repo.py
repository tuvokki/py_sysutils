#!/usr/bin/env python

import argparse, os, subprocess

parser = argparse.ArgumentParser(description='Create a new git repo.')

parser.add_argument('-repo_name', help='The name of the repo', required=True)

args = parser.parse_args()

git_dir = "/Users/wouter/test/development/git/"
#git_dir = "/home/development/git/"
repo_dir = git_dir + args.repo_name + ".git"
git_user = "root"
git_group = "wheel"
##
# This is what we have to do
##
# cd /home/development/git
# sudo mkdir test.git
# cd test.git
# sudo git --bare init
# cd ..
# sudo chown -R git:git test.git
##
print "Nothing implemented yet. This is what we want to do, eventually:"

# create git_dir
if not os.path.isdir(repo_dir):
  try:
    # print "cd %s" %(args.repo_name)
    # print "sudo mkdir %s.git" %(args.repo_name)
    os.makedirs(repo_dir)
    # print "cd %s.git" %(args.repo_name)
    # print "sudo git --bare init"
    proc = subprocess.Popen(['sudo','/usr/bin/env','git','--bare','init'], cwd=repo_dir)
    # print "cd .."
    # print "sudo chown -R git:git %s.git" %(args.repo_name)
    proc = subprocess.Popen(['sudo','/usr/bin/env','chown','-R',git_user+':'+git_group,repo_dir])
  except OSError, e:
    raise e



