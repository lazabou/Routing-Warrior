import yaml

def AddRouter(Id,HostName):
  
  #get current topology
  with open("Topology.yaml", 'r') as yamlfile:
    Devices = yaml.load(yamlfile,Loader=yaml.FullLoader)

  #create dictionnary with default values
  NewRouter = {
    Id: {
      'HostName': HostName,
      'NetconfPort': 830,
      'Interfaces':{
        'lo0':{
          'IP':"10.0.0."+str(Id),
        }
      }
    }
  }

  #if current topo file is empty
  if Devices == None:
    Devices=NewRouter
    with open("Topology.yaml", 'w') as yamlfile:
        data = yaml.dump(Devices, yamlfile, explicit_start = True)
    return("Device Created")
  
  #check if router is already in topo file
  else :
    DeviceExists = False
    for x in Devices.keys(): 
      if x == Id:
        DeviceExists = True
  
    #if yes, update hostname
    if DeviceExists == True:
      Devices[Id]["HostName"]=HostName
      with open("Topology.yaml", 'w') as yamlfile:
        data = yaml.dump(Devices, yamlfile, explicit_start = True)
      return("This device already exists, hostname updated")
    
    #if not, add new router to topo
    else:
      Devices[Id]=NewRouter[Id]
      with open("Topology.yaml", 'w') as yamlfile:
        data = yaml.dump(Devices, yamlfile, explicit_start = True)
      return("Device Created")


def AddLink(SrcId,SrcIf,DstId,DstIf,IsCore):
  #get current topology
  with open("Topology.yaml", 'r') as yamlfile:
    Devices = yaml.load(yamlfile,Loader=yaml.FullLoader)
  
  #create src-interface
  SrcIfName='ge-0/0/'+str(SrcIf)
  if IsCore == 'y':
    if int(SrcId)<int(DstId):
      IP='10.'+str(SrcId)+'.'+str(DstId)+'.'+str(SrcId)+'/24'
    else:
      IP='10.'+str(DstId)+'.'+str(SrcId)+'.'+str(SrcId)+'/24'
  
    SrcInterface= {
      SrcIfName: {
        'ConnectedTo': DstId,
        'MPLS': IsCore,
        'IP':IP
      }
    }
  else:
        SrcInterface= {
      SrcIfName: {
        'ConnectedTo': DstId,
        'MPLS': IsCore,
      }
    }

  #create dst-interface
  DstIfName='ge-0/0/'+str(DstIf)
  if IsCore == 'y':
    if int(SrcId)<int(DstId):
      IP='10.'+str(SrcId)+'.'+str(DstId)+'.'+str(DstId)+'/24'
    else:
      IP='10.'+str(DstId)+'.'+str(SrcId)+'.'+str(DstId)+'/24'

    DstInterface= {
      DstIfName: {
        'ConnectedTo': SrcId,
        'MPLS': IsCore,
        'IP':IP
      }
    }
  else:
    DstInterface= {
      DstIfName: {
        'ConnectedTo': SrcId,
        'MPLS': IsCore,
      }
    }

  #check if routers are already in topo file
  SrcDeviceExists = False
  for x in Devices.keys(): 
    if x == SrcId:
      SrcDeviceExists = True
  
  DstDeviceExists = False
  for x in Devices.keys(): 
    if x == SrcId:
      DstDeviceExists = True

  if SrcDeviceExists==False or DstDeviceExists == False:
    print("Router does not exist")
  else:
   Devices[SrcId]["Interfaces"][SrcIfName]=SrcInterface[SrcIfName]
   Devices[DstId]["Interfaces"][DstIfName]=DstInterface[DstIfName]
   with open("Topology.yaml", 'w') as yamlfile:
    data = yaml.dump(Devices, yamlfile, explicit_start = True)
   return("Link Created")