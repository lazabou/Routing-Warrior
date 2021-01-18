import yaml
import sys
from jnpr.junos import Device
from jnpr.junos.utils.config import Config

login = "test"
passwd = "Juniper123"

with open("Topology.yaml", 'r') as yamlfile:
  Devices = yaml.load(yamlfile,Loader=yaml.FullLoader)

for Key, Router in Devices.items():
  print ('Je vais prendre la conf du routeur' + str(Key))
  print ("Quelle IP pour le "+(Router['HostName']) + "?")
  IP=input()
  Port=input("Type enter to leave default port or enter Netconf port:")
  if not (Port):
      Port='830'
  dev = Device(host=IP, user=login, passwd=passwd, port=Port)
  try:
    dev.open()
  except ConnectError as err:
    print ("Cannot connect to device: {0}".format(err))
    sys.exit(1)
#  except Exception as err:
#      print (err)
#      sys.exit(1)
  print (dev.facts)
  dev.close()
