#!/usr/bin/python2

import commands as sp

print("content-type:  text/html")
print("")


print("<h1 align='center'><u>Welcome to Docker Server</u></h1>")




cmd="sudo rpm -q docker-ce"
output = sp.getstatusoutput(cmd)
if output[0] == 0:
	docker_status_check="installed"
else:
	docker_status_check="uninstalled"


docker_service_status_cmd = "sudo systemctl  is-active   docker"

ds_output = sp.getstatusoutput(docker_service_status_cmd)

if ds_output[1] == "active":
	docker_service_status = "running"
else:
	docker_service_status = "stopped"



print("<form action='docker_launch.py' align='center'>")
print("<div align='center'>")
print("""
<table border='5'>
<tr>
<td>Check docker software status</td>
<td>{}</td>
</tr>

<tr>
<td>Install docker</td>
<td><a href='docker_install.py'>Click to install docker</a></td>
</tr>

<tr>
<td>Docker service status</td>
<td>{}</td>
</tr>

<tr>
<td>Docker Service Manage</td>
<td><a href='docker_start.py'>Click to start docker</a></td>
</tr>

<tr>
<td>Click here to clean all container</td>
<td>  <a href='docker_clean_os.py'>Click to Clean</a>  </td>
</tr>


<tr>
<td>Docker Images</td>
<td>

<select name='imagename'>""".format(docker_status_check, docker_service_status))



cmd="sudo docker images"
output = sp.getoutput(cmd)
imagelist = output.split("\n")
for i in imagelist[1:]:
        print("<option>" + i.split()[0] + ":" +  i.split()[1] +      "</option>")


print("""
</select>

</td>
</tr>

<tr>
<td>Launch Docker Container Name</td>
<td> 
<input name='dockername' />  
</td>

<tr>
<td>Do u require GUI</td>
<td>
yes <input type='radio' name='gui' value='gui_yes' />
no <input type='radio' name='gui' value='gui_no' />
</td>
</tr>

<tr>
<td>Do u require remote GUI Console</td>
<td>
yes <input type='radio' name='gui_c' value='gui_c_yes' />
no <input type='radio' name='gui_c' value='gui_c_no' />
</td>
</tr>

<tr>
<td>submit</td>
<td>
<input type='submit' />

</td>
</tr>

<tr>
<td>click here to manage container</td>
<td><a href='docker_manage.py'>click here</a></td>
</tr>



</tr>

</table>
""")

print("</div>")
print("</form>")
