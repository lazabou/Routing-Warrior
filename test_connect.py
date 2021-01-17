import sys
from jnpr.junos import Device
from jnpr.junos.utils.config import Config

login = "test"
passwd = "Juniper123"
IP="172.30.110.25"

while True:
  print("Do you want to connect to another router? Y/N?")
  print("Y. Yes")
  print("N. No")
  Choice = input()

  if Choice==('Y'):
    IP=input("Router IP:")
    Port=input("Type enter to leave default port or enter Netconf port:")
# Use default port to connect which is 830
    if not (Port):
        Port='830'
    dev = Device(host=IP, user=login, passwd=passwd, port=Port).open()
    try:
       dev.open()
    except ConnectError as err:
       print ("Cannot connect to device: {0}".format(err))
       sys.exit(1)
    except Exception as err:
       print (err)
       sys.exit(1)

    print (dev.facts)
    dev.close()

  elif Choice==('N'):
    break
  else:
    print("invalid choice")
