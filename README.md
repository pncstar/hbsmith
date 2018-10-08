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
- download `httpd-2.4.35-o102p-x64-vc14.zip`
    - https://www.apachehaus.com/cgi-bin/download.plx
- unzip `httpd-2.4.35-o102p-x64-vc14.zip`
- move 'Apache24' folder to 'C:\Apache24'.
- in 'C:\Apache24\bin\', run `httpd.exe -k install`.
- reboot Windows OS and open `http://127.0.0.1/`

## Install Python

- get Python 3.6.6
    - https://www.python.org/downloads/
- unchecking 'Install launcher for all users' (for Windowns 7).
- checking 'Add Python to environment variables' in 'Customize installation'.

## Install pip packages

- run `python -m pip install -r https://raw.githubusercontent.com/pncstar/hbsmith/master/requirements.txt`.
- install 'Build Tools for Visual Studio 2017' in 'Tools for Visual Studio 2017' (for 'dtaidistance')
    - https://visualstudio.microsoft.com/downloads/
    - choose 'Visual Studio Build Tools 2017'
- install 7zip
    - https://www.7-zip.org/
- download 'dtaidistance 1.1.3'
    - https://pypi.org/project/dtaidistance/#files
- unzip 'dtaidistance-1.1.3.tar.gz'
- move 'dtaidistance-1.1.3' to 'C:\dtaidistance-1.1.3'
- in 'C:\dtaidistance-1.1.3\setup.py' replace lines from 140 to 141 with `long_description = 'pass'`.
    - https://github.com/wannesm/dtaidistance/blob/f0b60b6c8c770b915e07815fe2932bd24aaa064d/setup.py#L140-L141
- in 'C:\dtaidistance-1.1.3\' run `python setup.py install`.

## Test django development web server

- get django server source code
    - https://github.com/pncstar/hbsmith/raw/master/ss.zip
- in 'C:\ss\Hyundai_Chart_Manager\'
    - run `python manage.py runserver 0.0.0.0:8080`.
    - open `http://127.0.0.1:8080/upload`

## Install mod_wsgi

- download `mod_wsgi‑4.6.4+ap24vc14‑cp36‑cp36m‑win_amd64.whl`
    - https://www.lfd.uci.edu/~gohlke/pythonlibs/#mod_wsgi
- run `python -m pip install mod_wsgi‑4.6.4+ap24vc14‑cp36‑cp36m‑win_amd64.whl`
- run `mod_wsgi-express module-config >> C:\Apache24\conf\httpd.conf`
- put the wsgi configure below the end of 'C:\Apache24\conf\httpd.conf':

```
WSGIScriptAlias / /ss/Hyundai_Chart_Manager/Hyundai_Chart_Manager/wsgi.py
WSGIPythonPath /ss/Hyundai_Chart_Manager

<Directory /ss/Hyundai_Chart_Manager/Hyundai_Chart_Manager>
<Files wsgi.py>
Require all granted
</Files>
</Directory>
```

- in 'C:\ss\Hyundai_Chart_Manager\'
    - run `python manage.py collectstatic`.
- restart Apache web server and open `http://127.0.0.1/upload/`
