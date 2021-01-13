from jinja2 import Environment, FileSystemLoader
import yaml

env=Environment(loader=FileSystemLoader("templates"))
MyTemplate=env.get_template("template.j2")

with open("Topology.yaml", 'r') as yamlfile:
  Devices = yaml.load(yamlfile,Loader=yaml.FullLoader)


for Router in Devices.keys(): 
  result=MyTemplate.render(Devices[Router])
  f = open("configs/"+str(Router)+".txt", "w")
  f.write(result)
  f.close()