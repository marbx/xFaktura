# Create ~128 MiB virtual Python environment
# Outside this folder, because folder could be in a cloud.
# TODO why not /usr/local/
sudo apt install python3 python3-venv virtualenv python3-virtualenv
sudo python3 -m venv /opt/xFaktura/xFakturaPythonVenv
