# ClamAV tool

> The ClamAV command can identify and relocate files on Linux that have been infected by viruses, but not remove the viruses themselves.

ClamAV's tools are 'clamscan' to do the scanning and 'freshclam' to update the list of known virus signatures.

'''
sudo apt update && sudo apt upgrade -y
sudo apt-get install clamav clamav-daemon
clamscan --version
clamscan --infected --remove --verbose .
'''

references

- https://www.networkworld.com/article/3652690/using-clamav-to-detect-and-remove-viruses-on-linux.html
