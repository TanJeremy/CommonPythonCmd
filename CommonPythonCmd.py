import os

print os.environ["PATH"]

path = '/systeme/apero/work/jtan/wf_scripts_circus_module.4/scripts/wfTools'
newPath = os.path.normpath(path)

print newPath

from sys import platform
if platform == "linux" or platform == "linux2":
    # linux
    print 'prout'


print os.getuid()


print os.getcwd()
