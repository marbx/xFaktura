# Install python libraries
#           https://stackoverflow.com/questions/122327/how-do-i-find-the-location-of-my-python-site-packages-directory
#
# why -t target?
# Must be that complicated, because even after activating the venv pip pollutes the the /usr/lib
pythonpurelib=`python3 -c 'import sysconfig; print(sysconfig.get_paths()["purelib"])'`
echo installing into $pythonpurelib
sudo pip install -r requirements.txt -t $pythonpurelib --upgrade
