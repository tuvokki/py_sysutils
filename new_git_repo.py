#!/usr/bin/env python

import argparse, os, subprocess

parser = argparse.ArgumentParser(description='Create a new git repo.',epilog='Run this program as regular user with sudo.')

parser.add_argument('-r','--repo_name', help='The name of the repo', required=True)
parser.add_argument('-d','--git_dir', help='The base dir of git', dest='git_dir', default='/home/development/git/', required=False)
parser.add_argument('-u','--git_user', help='The name git user', dest='git_user', default='git', required=False)
parser.add_argument('-g','--git_group', help='The groups of the git user', dest='git_group', default='git', required=False)

args = parser.parse_args()

repo_dir = args.git_dir + args.repo_name + ".git"
repo_rights = args.git_user+':'+args.git_group

# create git_dir
if not os.path.isdir(repo_dir):
  try:

    # Create the repository directory
    os.makedirs(repo_dir)

    # Initialize the repor with: git --bare init
    proc = subprocess.Popen(['/usr/bin/env','git','--bare','init'], cwd=repo_dir)

    print "Adding rights [%s] to repo"%(repo_rights)
    # chown -R git:git repo_name
    proc = subprocess.Popen(['/usr/bin/env','chown','-R',repo_rights,repo_dir])

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
    """ % (repo_dir)
  except OSError, e:
    raise e
  except IOError as e:
      if (e[0] == errno.EPERM):
         print >> sys.stderr, "You need root permissions to do this, laterz!"
         sys.exit(1)
else:
  print "%s already exists! Aborting!"%(repo_dir)

