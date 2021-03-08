# docker_download_parallel_test

Test on docker download simulation of 30 parallel threads from a ubuntu machine. 

azureuser@gopiUbuntu18:~$ sudo apt-add-repository ppa:projectatomic/ppa

azureuser@gopiUbuntu18:~$ sudo apt-get update

azureuser@gopiUbuntu18:~$ sudo apt-get install -y skopeo

azureuser@gopiUbuntu18:~$ python3 ./docker_acr_download.py 
