echo --------------------------INSTALLING PYTHON DEPENDENCIES------------------------
sudo apt-get -y install build-essential
apt-get install -y python3-dev
apt-get install -y libpq-dev
apt-get install -y python3-venv
python3 -m venv ./venv/
source venv/bin/activate
#installing psycopg here to get the C implem in place of the pure python one
pip install "psycopg[c]"
pip install -r requirements.txt
echo --------------------------------CREATING A DATABASE-----------------------------
sudo -u postgres createdb ada
echo -----------------------------------CREATING A USER------------------------------
echo Please enter a username :
read username
sudo -u postgres createuser $username --pwprompt
echo ----------------------------CREATING TABLES AND TESTING-------------------------
python3 ./db/initDB.py