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

1. download and install packages

http://nginx.org/download/nginx-1.14.0.zip

https://www.python.org/ftp/python/3.6.6/python-3.6.6-amd64.exe

https://nssm.cc/release/nssm-2.24.zip

# Create 'nginx' window service

- Move nginx folder as 'C:\nginx'
- Run "nssm install nginx" from the command line.
- On the application tab: set path to 'C:\nginx\nginx.exe'
- On the I/O tab type "start nginx" on the Input.
- Click "install service". Go to services, start "nginx".


https://stackoverflow.com/questions/40846356/run-nginx-as-windows-service
