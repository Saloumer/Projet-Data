import json

#creer mon fichier 
def create(self, name):
    with open(name,'w') as file:
        print(f"cookie {name}: à été créé")

# faire une lecture
def read(self, name):
    with open(name, "r") as file:
        return json.load(file)

# faire une écriture
def write(name, dict):
    with open(name, 'w') as file:
         json.dump(dict, file)

def update(data):
    c = read("data.json")
    keys = list(c.data())

    for key in keys:
        c[key] = None
    
    write("data.json",c)


def clean():
    c = read("data.json")
    keys = list(c.keys())
    for key in keys :
        c[key] = None
    write("data.json",c)

print(f"Avant : ")
print(read("data.json"))

print("\n Modification en cours...")
update({'test': "numero2"})

print(f"\nZpres : ")
read("data.json")
