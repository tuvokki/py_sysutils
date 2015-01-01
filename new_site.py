#!/usr/bin/env python

# Load the jinja library's namespace into the current module.
import jinja2, argparse, os, subprocess

parser = argparse.ArgumentParser(description='Create a new vhost config for nginx.')

parser.add_argument('-domain', help='The domainname', required=True)
parser.add_argument('-host', help='The hostname', required=True)

args = parser.parse_args()
#print(args.accumulate(args.integers))

# Specify any input variables to the template as a dictionary.
templateVars = { "vhost" : args.host,
                 "site" : args.domain }

nginx_dir     = "/etc/nginx/"
available_dir = nginx_dir + "sites-available/"
enabled_dir   = nginx_dir + "sites-enabled/"
template_dir  = nginx_dir + "templates/"
web_dir       = "/webdir/"
log_dir       = "/var/log/nginx/"

# In this case, we will load templates off the filesystem.
# This means we must construct a FileSystemLoader object.
# 
# The search path can be used to make finding templates by
#   relative paths much easier.  In this case, we are using
#   absolute paths and thus set it to the filesystem root.
templateLoader = jinja2.FileSystemLoader( searchpath="/" )

# An environment provides the data necessary to read and
#   parse our templates.  We pass in the loader object here.
templateEnv = jinja2.Environment( loader=templateLoader )

# This constant string specifies the template file we will use.
VHOST_TEMPLATE_FILE = template_dir + "site_vhost.tmpl"

# Read the template file using the environment object.
# This also constructs our Template object.
template = templateEnv.get_template( VHOST_TEMPLATE_FILE )

# Finally, process the template to produce our final text.
outputText = template.render( templateVars )

# print outputText
with open(available_dir + args.host + '.' + args.domain +'.vhost', 'w') as myFile:
    myFile.write(outputText)

if not os.path.isdir(web_dir + args.domain):
        # domain dir is not there
        os.makedirs(web_dir + args.domain)

if not os.path.isdir(log_dir + args.domain):
  # domain dir is not there
  proc = subprocess.Popen(['sudo','/bin/mkdir',args.domain])


if os.path.isdir(web_dir + args.domain + "/" + args.host):
        print "Directory %s already exists." %(web_dir + args.domain + "/" + args.host)
else:
        print "Creating host dir %s" %(web_dir + args.domain + "/" + args.host)
        os.makedirs(web_dir + args.domain + "/" + args.host)

os.symlink(available_dir + args.host + '.' + args.domain +'.vhost', enabled_dir + "000-" + args.host + '.' + args.domain)

index_TEMPLATE_FILE = template_dir + "site_index.tmpl"
template = templateEnv.get_template( index_TEMPLATE_FILE )
outputText = template.render( templateVars )
with open(web_dir + args.domain + "/" + args.host + "/index.html", 'w') as myFile:
    myFile.write(outputText)