from jinja2 import Environment, FileSystemLoader
import yaml

env=Environment(loader=FileSystemLoader("templates"))
MyTemplate=env.get_template("template.j2")

with open("Topology.yaml", 'r') as yamlfile:
  Devices = yaml.load(yamlfile,Loader=yaml.FullLoader)

result=MyTemplate.render(Devices[2])
print("voici le resultat")
print(result)
