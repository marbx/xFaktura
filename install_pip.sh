# TODO dont specify 3.9 
#           https://stackoverflow.com/questions/122327/how-do-i-find-the-location-of-my-python-site-packages-directory
python3 -c 'import sysconfig; print(sysconfig.get_paths()["purelib"])'
sudo pip install -r requirements.txt -t /opt/xFaktura/.venv/lib/python3.9/site-packages --upgrade
