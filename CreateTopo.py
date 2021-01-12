import ModuleTopo as Topo
import yaml

while True:
  print("choose your action:")
  print("1. Add a Router")
  print("2. Add a link")
  print("3. Quit")
  Choice = input()

  if Choice=='1':
    Id=int(input("Router Id (1-253):"))
    if Id>253 or Id<1: print("wrong id")
    else :
      HostName=input("Router HostName:")
      Answer=Topo.AddRouter(Id,HostName)
      print(Answer)
  elif Choice=='2':
    SrcId=int(input("Source Router Id (1-253):"))
    DstId=int(input("Destination Router Id (1-253):"))
    SrcIf=int(input("Source Router Interface (0-6):"))
    DstIf=int(input("Destination Router Interface (0-6):"))
    while True:
      IsCore=str(input("MPLS interface? y/n:"))
      if IsCore=="y" or IsCore=="n":
        break
      else : print("invalid choice")
    if SrcId==DstId and SrcIf==DstIf:
      print("error: same source/destination router id and same source/destination router interface")
    else:
      Answer=Topo.AddLink(SrcId,SrcIf,DstId,DstIf,IsCore)
      print(Answer)
  elif Choice=='3':
    break
  else: 
    print("invalid choice")