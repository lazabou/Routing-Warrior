import ModuleTopo as Topo
import yaml

print("choose your action:")
print("1. Add a Router")
print("2. Add an Interface to a router")
Choice = input()

print("Your Choice is :")
print(Choice)

if Choice=='1':
  Id=int(input("Router Id (1-253):"))
  if Id>253 or Id<1: print("wrong id")
  else :
    HostName=input("Router HostName:")
    Answer=Topo.AddRouter(Id,HostName)
    print(Answer)

else: 
  print("invalid choice")