# ADA 🐛

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

0. bash install.sh

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

