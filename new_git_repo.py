#!/usr/bin/env python

import argparse, os, subprocess

parser = argparse.ArgumentParser(description='Create a new git repo.')

parser.add_argument('-repo_name', help='The name of the repo', required=True)

args = parser.parse_args()

git_dir = "/Users/wouter/test/development/git/"
#git_dir = "/home/development/git/"

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
os.makedirs(git_dir + args.repo_name + ".git")

print "cd %s" %(args.repo_name)
print "sudo mkdir %s.git" %(args.repo_name)
print "cd %s.git" %(args.repo_name)
print "sudo git --bare init"
print "cd .."
print "sudo chown -R git:git %s.git" %(args.repo_name)

