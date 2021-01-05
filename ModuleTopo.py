import yaml

def AddRouter(Id,HostName):
  
  #get current topology
  with open("Topology.yaml", 'r') as yamlfile:
    Devices = yaml.load(yamlfile,Loader=yaml.FullLoader)

  NewRouter = {
    Id: {
      'HostName': HostName,
      'MgmtIP': '127.0.0.1',
      'NetconfPort': 830,
      'Interfaces': {
        'Name': 'ge-0/0/0',
        'ConnectedTo': 'None',
        'Core': False
       }
    }
  }
  
  
  if Devices == None:
    Devices=NewRouter
    with open("Topology.yaml", 'w') as yamlfile:
        data = yaml.dump(Devices, yamlfile, explicit_start = True)
    return("Device Created")
  else :
    DeviceExists = False
    for x in Devices.keys(): 
      if x == Id:
        DeviceExists = True
  
    if DeviceExists == True:
      return("This device already exists")
    else:
      Devices[Id]=NewRouter[Id]
      with open("Topology.yaml", 'w') as yamlfile:
        data = yaml.dump(Devices, yamlfile, explicit_start = True)
      return("Device Created")


 
    