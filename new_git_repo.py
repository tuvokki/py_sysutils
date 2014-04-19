#!/usr/bin/env python

import argparse, os, subprocess, sys

if os.geteuid() != 0:
    exit("You need to have root privileges to run this script.\nPlease try again, this time using 'sudo'. Exiting.")

parser = argparse.ArgumentParser(description='Create a new git repo.',epilog='Run this program as regular user with sudo.')

parser.add_argument('-r','--repo_name', help='The name of the repo', required=True)
parser.add_argument('-d','--git_dir', help='The base dir of git', dest='git_dir', default='/home/development/git/', required=False)
parser.add_argument('-u','--git_user', help='The name git user', dest='git_user', default='git', required=False)
parser.add_argument('-g','--git_group', help='The groups of the git user', dest='git_group', default='git', required=False)

def show_next(rd):
  print """
# Now on the client's computer
$ cd myproject
$ git init
$ git add .
$ git commit -m 'initial commit'
$ git remote add origin git@gitserver:%s
$ git push origin master
# to get the repo's updates
$ git pull origin master
  """ % (rd)

args = parser.parse_args()

repo_dir = args.git_dir + args.repo_name + ".git"
repo_rights = args.git_user+':'+args.git_group

# create git_dir
if not os.path.isdir(repo_dir):
  try:

    # Create the repository directory
    os.makedirs(repo_dir)

    # Initialize the repor with: git --bare init
    git_init_prog = ['/usr/bin/env','git','--bare','init']
    subprocess.call(git_init_prog, cwd=repo_dir)

    print "Adding rights [%s] to repo"%(repo_rights)
    # chown -R git:git repo_name
    chown_proc = ['/usr/bin/env','chown','-R',repo_rights,repo_dir]
    try:
      subprocess.check_call(chown_proc)
    except subprocess.CalledProcessError, e:
      print "Process error(%s)\nUser %s or group %s does not exist on this system. Exiting."%(e.returncode, args.git_user, args.git_group)
      sys.exit(1)

    show_next(repo_dir)
  except OSError, e:
    print "I/O error(%s): %s\nMaybe try a different git-base directory with the --git_dir option. Exiting."%(e.errno, e.strerror)
    sys.exit(1)
else:
  print "%s already exists! Aborting!"%(repo_dir)

