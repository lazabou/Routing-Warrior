import sys
from jnpr.junos import Device
from jnpr.junos.utils.config import Config

login = test
passwd = Juniper123


while True:
  print("Do you want to connect to another router? Y/N?")
  print("Y. Yes")
  print("N. No")
  Choice = input()

  if Choice==('Y' or 'y'):
    IP=input("Router IP:")
    dev = Device(host=IP, login=login, passwd=passwd).open()
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

  elif Choice==('N' or 'n'):
    break
  else:
    print("invalid choice")
