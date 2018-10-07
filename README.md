# Environments

## dev sandbox

- virtualbox: 5.2.18
    - https://download.virtualbox.org/virtualbox/5.2.18/VirtualBox-5.2.18-124319-Win.exe
- vagrant: 2.1.5
    - https://releases.hashicorp.com/vagrant/2.1.5/vagrant_2.1.5_x86_64.msi
- vagrant box: win-2012r2-standard-amd64-nocm
    - https://app.vagrantup.com/opentable/boxes/win-2012r2-standard-amd64-nocm

# Step By Step

## download and install Microsoft packages

- https://visualstudio.microsoft.com/thank-you-downloading-visual-studio/?sku=BuildTools&rel=15 (for 'dtaidistance')
- https://www.microsoft.com/en-us/download/details.aspx?id=49984 (install for Apache 2.4 services)
- https://www.microsoft.com/en-us/download/confirmation.aspx?id=48159

## download packages

- https://www.python.org/ftp/python/3.6.6/python-3.6.6-amd64.exe
- https://files.pythonhosted.org/packages/19/9f/5b0780662486b1775ed8f70b63b73a2ec386f875a878c46efb6e2bc355ba/dtaidistance-1.1.3.tar.gz (dtaidistance==1.1.3)
- https://www.apachehaus.com/cgi-bin/download.plx?dli=gYy0keSNVW04EVj9yYzQWcJVlUGRVYRlXZWpkW
- https://download.lfd.uci.edu/pythonlibs/h2ufg7oq/mod_wsgi-4.6.4+ap24vc14-cp36-cp36m-win_amd64.whl

## install apache

1. unzip 'httpd-2.4.35-o102p-x64-vc14.zip'
1. move 'Apache24' folder to 'C:\Apache24'.
1. In 'C:\Apache24\bin\', run `httpd.exe -k install`.

## install mod_wsgi

1. `pip3 install mod_wsgi-4.6.4+ap24vc14-cp36-cp36m-win_amd64.whl`
1. `mod_wsgi-express module-config`
1. put the result of above command into 'C:\Apache24\conf\httpd.conf'.

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

### 'dtaidistance'

1. unzip 'dtaidistance-1.1.3.tar.gz'
1. move 'dtaidistance-1.1.3' to 'C:\dtaidistance-1.1.3'
1. In 'C:\dtaidistance-1.1.3\setup.py' replace lines from 140 to 141 with `long_description = 'pass'`.
    1. https://github.com/wannesm/dtaidistance/blob/f0b60b6c8c770b915e07815fe2932bd24aaa064d/setup.py#L140-L141
1. In 'C:\dtaidistance-1.1.3\' run `python setup.py install`.

## run django for dev or test

In 'C:\ss\Hyundai_Chart_Manager\' run `python manage.py runserver 0.0.0.0:8080`.
