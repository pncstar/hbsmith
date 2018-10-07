# Environments

## DEV

virtualbox: 5.2.18
vagrant: 2.1.5
vagrant box: win-2012r2-standard-amd64-nocm
  https://app.vagrantup.com/opentable/boxes/win-2012r2-standard-amd64-nocm

## Production

windows
nginx
python
django

# Step By Step

## download packages

http://nginx.org/download/nginx-1.14.0.zip

https://www.python.org/ftp/python/3.6.6/python-3.6.6-amd64.exe

https://nssm.cc/release/nssm-2.24.zip

## Create 'nginx' window service

- Move nginx folder as 'C:\nginx'
- Move nssm folder as 'C:\nssm'
- Run "nssm install nginx" from the command line in 'C:\nssm\win64\'.
- On the application tab: set path to 'C:\nginx\nginx.exe'
- On the I/O tab type "start nginx" on the Input.
- Click "install service". Go to services, start "nginx".

## install python3 (require Windows Administrator privilege

- check 'Add Python to environment variables' in 'Advanced Options'.

- if you get error 0x80240017, then install patch from Microsoft site below:
https://www.microsoft.com/en-us/download/details.aspx?id=48234 
