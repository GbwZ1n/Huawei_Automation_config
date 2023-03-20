###############################################
##											 ##
## Extraction information on Switches Huawei ##
##											 ##
###############################################

import netmiko
import sys

#Conexion via SSH
connection = netmiko.ConnectHandler(
	ip = "10.248.0.194", 
	device_type = "huawei",
	username = "admin",
	password = "adminp1234"
	)

#Inicio de la configs
A = connection.send_command("display current configuration\n")
f = open('SEDE-IP10.txt','w')
f.write('###display current configuration###\n' + A)
f.close()
B = connection.send_command("display interface\n")
f = open('SEDE-IP10.txt','a')
f.write('\n' + '###display interface###\n' + B)
f.close()
C = connection.send_command("display interface brief\n")
f = open('SEDE-IP10.txt','a')
f.write('\n' + '###display interface brief###\n' + C)
f.close()
D = connection.send_command("display vlan\n")
f = open('SEDE-IP10.txt','a')
f.write('\n' + '###display vlan###\n' + D)
f.close()
E = connection.send_command("display version\n")
f = open('SEDE-IP10.txt','a')
f.write('\n' + '###display version###\n'+ E)
f.close()
F = connection.send_command("display lldp neighbor brief\n")
f = open('SEDE-IP10.txt','a')
f.write('\n' + '###display lldp neighbor brief###\n'+ F)
f.close()
G = connection.send_command("display lldp neighbor\n")
f = open('SEDE-IP10.txt','a')
f.write('\n' + '###display lldp neighbor###\n'+ G)
f.close()
H = connection.send_command("display arp all\n")
f = open('SEDE-IP10.txt','a')
f.write('\n' + '###display arp all###\n'+ H)
f.close()
I = connection.send_command("display interface description\n")
f = open('SEDE-IP10.txt','a')
f.write('\n' + '###display interface description###\n'+ I)
f.close()

######STACKING######

J = connection.send_command("display stack\n")
f = open('SEDE-IP10.txt','a')
f.write('\n' + '###display stack###\n'+ J)
f.close()
K = connection.send_command("display stack port\n")
f = open('SEDE-IP10.txt','a')
f.write('\n' + '###display stack port###\n'+ K)
f.close()
L = connection.send_command("display stack channel\n")
f = open('SEDE-IP10.txt','a')
f.write('\n' + '###display stack channel###\n'+ L)
f.close()
M = connection.send_command("dispLay stack configuration\n")
f = open('SEDE-IP10.txt','a')
f.write('\n' + '###dispLay stack configuration###\n'+ M)
f.close()

connection.disconnect()
