echo --------CHECKING DEPENDENCIES-----
sudo apt-get install -y systemd
echo ----------CREATING FILE-----------
cp ./misc/ada.service /etc/systemd/system/ada.service
echo ----------SOURCING---------
sudo systemctl daemon-reload
sudo systemctl enable ada.service
echo ----------STARTING SERVICE---
sudo systemctl start ada.service