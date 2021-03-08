# docker_download_parallel_test

Test on docker download simulation of 30 parallel threads from a ubuntu machine. 

azureuser@gopiUbuntu18:~$ sudo apt-add-repository ppa:projectatomic/ppa

azureuser@gopiUbuntu18:~$ sudo apt-get update

azureuser@gopiUbuntu18:~$ sudo apt-get install -y skopeo

 ### use this path in code for command exceution
azureuser@gopiUbuntu18:~$ which skopeo
/usr/bin/skopeo


azureuser@gopiUbuntu18:~$ pwd
/home/azureuser
azureuser@gopiUbuntu18:~$ mkdir skopeo


azureuser@gopiUbuntu18:~$ cd  skopeo

**###use this path in code as destination for copying. 
**azureuser@gopiUbuntu18:~/skopeo$  pwd
/home/azureuser/skopeo 


azureuser@gopiUbuntu18:~/skopeo$ 
azureuser@gopiUbuntu18:~$ python3 ./docker_acr_download.py 

