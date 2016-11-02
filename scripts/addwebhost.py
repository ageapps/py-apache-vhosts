#!/usr/bin/env python
# Virtual Host configuration script
import sys
import subprocess
import optparse

# function that actually adds the virtual hosts' configuration
def cofigHost(domainName,ip):

    sitesConfigPath = "/etc/apache2/sites-available/"
    defaultConfigFile = "000-default.conf"
    defaultConfigPath = sitesConfigPath+defaultConfigFile

    hostName = domainName.split(".")[1]

    print("Domain: " + domainName)
    print("Host Name: " + hostName)
    myFile = hostName + ".conf"
    myFilePath =  sitesConfigPath + myFile
    print("Domain configuration file: " + myFile)

    print("Checking permissions")
    execCommand("touch " + defaultConfigPath, "Checking")

    s = " " # separator

    documentRoot = "/var/www/" + hostName
    serverName = hostName + ".com"
    serverAlias = domainName

    print("Writing configuration files...")
    # open files
    fr = open(defaultConfigPath,"rt")
    fw = open(myFilePath,"wb") # create if doesnt exist
    for line in fr:
        fields = line.split()

        if len(fields) >= 2 and (fields[0] == "DocumentRoot") :
            print("Changing configuration file...")
            print(fields[1] + " --> " + documentRoot)
            fields[1] = documentRoot
            print("New host DocumentRoot: " + documentRoot)
            fw.write("  DocumentRoot " + documentRoot)
            fw.write("\n")
            fw.write("  ServerName " + serverName)
            print("New host ServerName: " + serverName)
            fw.write("\n")
            fw.write("  ServerAlias " + serverAlias)
            print("New host ServerAlias: " + serverAlias)
            fw.write("\n")

        else:
            fw.write(line)

    fr.close()
    fw.close()
    print("Writing...OK")

    print("Setting Up web page...")
    execCommand("mkdir " + documentRoot,"Creating")
    execCommand("cp /var/www/html/index.html " + documentRoot + "/", "Set Up")

    print("Disabling default domain configuration file...")
    execCommand("a2dissite " + defaultConfigFile, "Disabling")

    print("Enabling domain configuration file...")
    execCommand("a2ensite " + myFile, "Enabling")

    print("Adding domain to hosts file...")
    with open("/etc/hosts", "a") as hostsFile:
        hostsFile.write( ip + " " + hostName + " " + domainName + "\n")
    print("Adding...OK")

def restartApache():
    print("Restarting Apache2 to save changes...")
    execCommand("sudo service apache2 restart", "Restarting")

    print("/******************************************************************/")
    print("/* WARNING: if the virtual hoststs' domain does not exist         */")
    print("/* (wich is in most cases), you have to add the domain to your    */")
    print("/* known hosts file by typing in your host terminal as root user: */")
    print("/* $ sudo -i # to enter root user                                 */")
    print("/* $ echo \"192.168.122.241      www.mydomain.com\" >> /etc/hosts   */")
    print("/* $ exit # to exit root user                                     */")
    print("/******************************************************************/")

def execCommand(command,msg):
    p = subprocess.call(command, shell=True)
    if p == 0:
        print(msg + "...OK")
    else:
        print(msg + "...ERROR")
        print(">>>>>>>>>> Try using sudo <<<<<<<<<<<")
        sys.exit(1)


parser = optparse.OptionParser()
defaultIPAddress = "192.168.122.241"
defaultDomain = "www.mydomain.com"


parser.add_option('-d', '--domain', dest='domain', help='Domain Name')
# parser.add_option('-p', '--password', dest='password', help='Your host password')
parser.add_option('-i', '--ip', dest='guestIp', help='Your guest IP address')

(options, args) = parser.parse_args()

if options.domain is None:
    options.domain = raw_input('Enter a domain name ('+ defaultDomain +'): ')

if options.domain == "":
    options.domain = defaultDomain

# if options.password is None:
#    options.password = "cdps"


if options.guestIp is None:
    options.guestIp = raw_input('Enter your guest IP address ('+ defaultIPAddress +'): ')

if options.guestIp == "":
    options.guestIp = defaultIPAddress

cofigHost(options.domain,options.guestIp)
restartApache()
