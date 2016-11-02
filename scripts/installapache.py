#!/usr/bin/env python
# Apache Configuration script
import sys
import subprocess
import optparse

def configIp(path,ip):

    filePath = path
    print("path: " + filePath)

    pathSplited = filePath.split("/")
    fileName = pathSplited[len(pathSplited)-1]
    print("File name: <" + fileName + ">")

    s = " " # separator

    ipSplit = ip.split(".")
    ipSplit[3] = "1"
    gateway = (".").join(ipSplit)

    oldFilePath = filePath + ".old"
    # create backup file
    print("Saving BackUp File <.old> ...")
    execCommand("mv " + filePath + " " + oldFilePath, "Saving")

    print("Writing configuration files...")
    # open files
    fr = open(oldFilePath,"r")
    fw = open(filePath ,"wb") # create if doesnt exist
    for line in fr:
        fields = line.strip().split()

        if (len(fields) >= 4 and (fields[0] == "iface")) and (fields[3] == "dhcp") :
            print("Changing ip configuration...")
            value = "static"
            print(fields[3] + " --> " + value)
            fields[3] = value
            fw.write(s.join(fields))
            fw.write("\n")
            fw.write("address " + ip)
            fw.write("\n")
            fw.write("netmask 255.255.255.0")
            fw.write("\n")
            fw.write("gateway " + gateway)
            fw.write("\n")
            fw.write("dns-nameservers " + gateway)
            fw.write("\n")
        else:
            fw.write(line)

    fr.close()
    fw.close()
    print("Writing...OK")


    print("Restoring permissions...")
    execCommand("chmod 644 " + filePath, "Restoring")

def restartApache():
    print("Applying changes...")
    execCommand("/etc/init.d/apache2 restart", "Applying")

def setUpApache():
    print("Updating current packages...")
    execCommand("apt-get -y update", "Updating")

    print("Installing new packages...")
    execCommand("apt-get install -y apache2 curl lynx wget", "Installing")


def execCommand(command,msg):
    p = subprocess.call(command, shell=True)
    if p == 0:
        print(msg + "...OK")
    else:
        print(msg + "...ERROR")
        print(">>>>>>>>>> Try using sudo <<<<<<<<<<<")
        sys.exit(1)


defaultRoute= "/etc/network/interfaces"
defaultIPAddress = "192.168.122.241"
parser = optparse.OptionParser()

parser.add_option('-r', '--route', dest='route', help='Interfaces Path')
parser.add_option('-i', '--ip', dest='serverIp', help='Your guest static IP address')

(options, args) = parser.parse_args()

if options.route is None:
    options.route = defaultRoute

if options.serverIp is None:
    options.serverIp = raw_input('Enter your server static address ('+ defaultIPAddress +'): ')

if options.serverIp == "":
    options.serverIp = defaultIPAddress


configIp(options.route,options.serverIp)
setUpApache()
restartApache()
