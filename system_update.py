#!/usr/bin/python
#################################################
#This script keeps my mac osx uptodate with the #    
#latest patches and updates                     #
#written by cyclonis                            #
#Feb 8, 2018                                    #
#################################################

from subprocess import call, PIPE, Popen
import pexpect 
import getpass
import sys

################################
#This function applies updates #
#to your Operating System      #
#################################


def software_update():
            p = getpass.getpass()
            child = pexpect.spawn('sudo softwareupdate -d -i -r')
            child.expect('Password:')
            child.sendline(p)
            child.expect('$')
            child.interact()






software_update()






