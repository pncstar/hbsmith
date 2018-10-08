# Environments

## dev sandbox

- virtualbox: 5.2.18
    - https://www.virtualbox.org/wiki/Downloads
- vagrant: 2.1.5
    - https://www.vagrantup.com/downloads.html
- vagrant box: windows 7 enterprise 64bit
    - https://app.vagrantup.com/senglin/boxes/win-7-enterprise

# Step By Step

## Install Apache

- Visual C++ Redistributable for Visual Studio 2015 Update 1 (for Apache 2.4 services)
    - https://www.microsoft.com/en-us/download/details.aspx?id=49984
- Download 'httpd-2.4.35-o102p-x64-vc14.zip'
    - https://www.apachehaus.com/cgi-bin/download.plx
- Unzip 'httpd-2.4.35-o102p-x64-vc14.zip'
- Move 'Apache24' folder to 'C:\Apache24'.
- In 'C:\Apache24\bin\', run `httpd.exe -k install`.
- Reboot Windows OS and open `http://127.0.0.1/`

## Install Python

- Get Python 3.6.6
    - https://www.python.org/downloads/
- Unchecking 'Install launcher for all users' (for Windowns 7).
- Checking 'Add Python to environment variables' in 'Advanced Options'.











- https://visualstudio.microsoft.com/thank-you-downloading-visual-studio/?sku=BuildTools&rel=15 (for 'dtaidistance')
    - choose 'Visual Studio Build Tools 2017'


## download packages


- https://files.pythonhosted.org/packages/19/9f/5b0780662486b1775ed8f70b63b73a2ec386f875a878c46efb6e2bc355ba/dtaidistance-1.1.3.tar.gz (dtaidistance==1.1.3)

- https://github.com/pncstar/hbsmith/raw/master/ss.zip
- https://www.lfd.uci.edu/~gohlke/pythonlibs/#mod_wsgi (download 'mod_wsgi‑4.6.4+ap24vc15‑cp37‑cp37m‑win_amd64.whl')

## install pip packages

1. download 'requirements.txt' from github repository (here).
    1. https://raw.githubusercontent.com/pncstar/hbsmith/master/requirements.txt
1. run `python -m pip install -r requirements.txt`.

## install 7zip

1. https://www.7-zip.org/a/7z1805-x64.exe

## install 'dtaidistance'

1. unzip 'dtaidistance-1.1.3.tar.gz'
1. move 'dtaidistance-1.1.3' to 'C:\dtaidistance-1.1.3'
1. In 'C:\dtaidistance-1.1.3\setup.py' replace lines from 140 to 141 with `long_description = 'pass'`.
    1. https://github.com/wannesm/dtaidistance/blob/f0b60b6c8c770b915e07815fe2932bd24aaa064d/setup.py#L140-L141
1. In 'C:\dtaidistance-1.1.3\' run `python setup.py install`.

## run django for dev or test

In 'C:\ss\Hyundai_Chart_Manager\' run `python manage.py runserver 0.0.0.0:8080`.

## install mod_wsgi

1. `python -m pip install mod_wsgi‑4.6.4+ap24vc15‑cp37‑cp37m‑win_amd64.whl`
1. `mod_wsgi-express module-config >> C:\Apache24\conf\httpd.conf`
1. put the wsgi configure below into 'C:\Apache24\conf\httpd.conf':

```
WSGIScriptAlias / /ss/Hyundai_Chart_Manager/Hyundai_Chart_Manager/wsgi.py
WSGIPythonPath /ss/Hyundai_Chart_Manager

<Directory /ss/Hyundai_Chart_Manager/Hyundai_Chart_Manager>
<Files wsgi.py>
Require all granted
</Files>
</Directory>
```
