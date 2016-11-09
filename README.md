# py-apache-vhosts

Python scripts that help you to easily set up an [apache server] and add virtual hosts to it.


## Usage in a fresh machine
Downloading the scripts

```groovy
// check if you have curl installed, if not, run
$ apt-get -y update
$ apt-get -y curl
// download configuration scripts
$ curl https://raw.githubusercontent.com/ageapps/py-apache-vhosts/master/scripts/installapache.py -o installapache.py
$ curl https://raw.githubusercontent.com/ageapps/py-apache-vhosts/master/scripts/addwebhost.py -o addwebhost.py
// run installapache file to install apache and configure a static IP
$ sudo python installapache.py
$ Enter your server static address (192.168.122.241):
// now you can check if apache is up by putting in you browser the IP
// run addwebhost file to add any webhost with any domain name
$ sudo python addwebhost.py
Enter a domain name (www.mydomain.com):
Enter your guest IP address (192.168.122.241):
...
/******************************************************************/
/* WARNING: if the virtual hoststs' domain does not exist         */
/* (wich is in most cases), you have to add the domain to your    */
/* known hosts file by typing in your host terminal as root user: */
/* $ sudo -i # to enter root user                                 */
/* $ echo "192.168.122.241      www.mydomain.com" >> /etc/hosts   */
/* $ exit # to exit root user                                     */
/******************************************************************/
// now go to your browser, enter your domain and check if it works
//
```

## Usage in Vagrant Playground
Suposing you have [vagrant] installed
```groovy
// download repo with all files
$ git clone https://github.com/ageapps/py-apache-vhosts.git
$ cd py-apache-vhosts
// start Playground VM
$ vagrant up
// ssh into the VM
$ vagrant ssh
// scripts are allready inside the VM
$ cd /scripts
// run installapache file to install apache, leave 192.168.122.241 as IP
$ sudo python installapache.py
$ Enter your server static address (192.168.122.241):
// now you can check if apache is up by putting 192.168.122.241 in you browser
// run addwebhost file to add any webhost with any domain name
$ sudo python addwebhost.py
Enter a domain name (www.mydomain.com):
Enter your guest IP address (192.168.122.241):
...
/******************************************************************/
/* WARNING: if the virtual hoststs' domain does not exist         */
/* (wich is in most cases), you have to add the domain to your    */
/* known hosts file by typing in your host terminal as root user: */
/* $ sudo -i # to enter root user                                 */
/* $ echo "192.168.122.241      www.mydomain.com" >> /etc/hosts   */
/* $ exit # to exit root user                                     */
/******************************************************************/
// now go to your browser, enter your domain and check if it works
//
```

[apache server]: https://httpd.apache.org/
[vagrant]: https://www.vagrantup.com/
