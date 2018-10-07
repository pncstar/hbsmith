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
- https://visualstudio.microsoft.com/thank-you-downloading-visual-studio/?sku=BuildTools&rel=15

## Create 'nginx' window service

1. Move nginx folder as 'C:\nginx'
1. Move nssm folder as 'C:\nssm'
1. Move ss fodler as 'C:\ss'
1. Run "nssm install nginx" from the command line in 'C:\nssm\win64\'.
1. On the application tab: set path to 'C:\nginx\nginx.exe'
1. On the I/O tab type "start nginx" on the Input.
1. Click "install service". Go to services, start "nginx".

## install prerequirements

- vs_buildtools__544792918.1538907809 (for 'dtaidistance')

## install python3

- check 'Add Python to environment variables' in 'Advanced Options'.
- if you get error 0x80240017, then install patch from Microsoft site
  - KB2919442 for Windows 2012R2
    - https://www.microsoft.com/en-us/download/details.aspx?id=42153
  - KB2919335 for Windows 2012R2
    - https://www.microsoft.com/en-us/download/details.aspx?id=42334
    - (install 'clearcompressionflag.exe' first, then 'Windows8.1-KB2919355-x64.msu')

## install pip packages

In 'C:\ss\' run `python -m pip install -r requirements.txt`.

## run django

In 'C:\ss\Hyundai_Chart_Manager\' run `python manage.py runserver 0.0.0.0:8080`.
