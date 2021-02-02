import yaml
import sys
from jnpr.junos import Device
from jnpr.junos.utils.config import Config
from jnpr.junos.utils.config import Config
from jnpr.junos.exception import ConnectError
from jnpr.junos.exception import LockError
from jnpr.junos.exception import UnlockError
from jnpr.junos.exception import ConfigLoadError
from jnpr.junos.exception import CommitError

# When calling the script type:
# - as first argument: device login
# - as second argument: device password

if len(sys.argv)==3:
  login = sys.argv[1]
  passwd = sys.argv[2]
else:
  login="jcluser"
  passwd="Juniper!1"


# Parse Topology file to connect to each device
with open("Topology.yaml", 'r') as yamlfile:
  Devices = yaml.load(yamlfile,Loader=yaml.FullLoader)

# Parse device dictionnary ie Topology file to map each device with JCL IP and Netconf port
get_ip = input("Quelle IP JCL? ")
for Key, Router in Devices.items():
  IP=get_ip
  Port = Router['NetconfPort']
  print ('Device '+ str(Router['HostName'] + ' port '+str(Port)))
  dev = Device(host=IP, user=login, passwd=passwd, port=int(Port))

# Then connect to each IP mapped to the device to load relevant config file which is in /Config folder
  try:
    dev.open()
  except ConnectError as err:
    print ("Cannot connect to device: {0}".format(err))
    sys.exit(1)
  else:
    cu = Config(dev)
    print ("Loading configuration changes for %s" %str(Key))
    try:
        cu.load(path="configs/"+str(Key)+".txt", merge=True)
        cu.pdiff()
        cu.commit()
    except:
        print ("Unable to load configuration changes: {0}".format(err))
    finally:
        dev.close()



#
#
#
#
#
#
#
#
#
#
#
