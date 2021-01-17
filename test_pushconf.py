from jnpr.junos import Device
from jnpr.junos.utils.config import Config

dev = Device(host='172.30.110.25', user='test', passwd='Juniper123').open()
cu = Config(dev)
cu.load('set system hostname test', format='set')
cu.pdiff()
cu.commit()

dev.close()
