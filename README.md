# ADA 🐛


> [!WARNING]
> This is a mirror of https://gitlab.com/Louciole/ada, please use the original repo


❓️The favourite URL shortener of nobody but me. <br>  
🟢 Status : https://louciole.github.io/carbon-status/ <br>
🌍 Production : https://kip.yt

## 🏎️ getting started

### prerequisite :
- Python > 3.8
- PostgreSQL

### download :
      git clone git@gitlab.com:Louciole/ada.git  
or download it manually

https://gitlab.com/Louciole/ada/-/releases/v1

### install :

0. install postgresql

       apt install postgresql postgresql-contrib -y
1. edit `ada.ini` with your parameters

2. Install the dependencies

       bash install.sh  

3. (optional) create a service to bundle it  
   edit `/misc/ada.service` with your path then :

       bash misc/createService.sh  

### one time run :

	sudo venv/bin/python ada.py  

### starting the service :
	systemctl start ada  


## 🖥️ Work
If you plan to commit something don't forget to IGNORE the *.ini file
run

	git update-index --assume-unchanged ada.ini

## 🧶 Miscellaneous

### show logs :
	journalctl -u ada  

### show status :
	systemctl status ada  

### restart :
	systemctl restart ada  

