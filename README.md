# Environments

## DEV

- virtualbox: 5.2.18
  - https://download.virtualbox.org/virtualbox/5.2.18/VirtualBox-5.2.18-124319-Win.exe
- vagrant: 2.1.5
  - https://releases.hashicorp.com/vagrant/2.1.5/vagrant_2.1.5_x86_64.msi
- vagrant box: win-2012r2-standard-amd64-nocm
  - https://app.vagrantup.com/opentable/boxes/win-2012r2-standard-amd64-nocm

## Production

- windows
- nginx
- python
- django

# Step By Step

## download packages

- http://nginx.org/download/nginx-1.14.0.zip
- https://www.python.org/ftp/python/3.6.6/python-3.6.6-amd64.exe
- https://nssm.cc/release/nssm-2.24.zip

## Create 'nginx' window service

1. Move nginx folder as 'C:\nginx'
1. Move nssm folder as 'C:\nssm'
1. Run "nssm install nginx" from the command line in 'C:\nssm\win64\'.
1. On the application tab: set path to 'C:\nginx\nginx.exe'
1. On the I/O tab type "start nginx" on the Input.
1. Click "install service". Go to services, start "nginx".

## install python3

- check 'Add Python to environment variables' in 'Advanced Options'.
- if you get error 0x80240017, then install patch from Microsoft site
  - KB2919442 for Windows 2012R2
  - KB2919335 for Windows 2012R2


E:\dev\Hyundai_Chart_Manager\venv\Scripts\python.exe "C:\Program Files\JetBrains\PyCharm 2018.1.4\helpers\pydev\pydevd.py" --multiproc --qt-support=auto --client 127.0.0.1 --port 49990 --file E:/dev/Hyundai_Chart_Manager/Hyundai_Chart_Manager/manage.py runserver localhost:8081
