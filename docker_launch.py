#!/usr/bin/python2

import commands as sp
import cgi

print("content-type: text/html")


form  = cgi.FieldStorage()

imgname = form.getvalue("imagename")
dname = form.getvalue("dockername")
gui = form.getvalue("gui")

if gui == "gui_no":
	cmd="sudo ansible-playbook docker_launch_nogui.yml --extra-vars 'dname={} imagename={}'".format(dname, imgname)
else:
	cmd="sudo ansible-playbook docker_launch_gui.yml --extra-vars 'dname={} imagename={}'".format(dname, imgname)


output = sp.getstatusoutput(cmd)

if output[0] == 0:
	print("location: docker.py")
	print("")
else:
	print("")
	print("error")
