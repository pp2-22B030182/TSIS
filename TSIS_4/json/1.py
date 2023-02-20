import json 
 
with open ("a.json", "r") as read_file: 
    a = json.load(read_file) 
 
print("Interface Status") 
print("================================================================================") 
print("DN                                                 Description           Speed    MTU") 
print("-------------------------------------------------- --------------------  ------  ------") 
 
for i in a["imdata"]: 
    if (i["l1PhysIf"]["attributes"]["dn"] == "topology/pod-1/node-201/sys/phys-[eth1/33]") \
        or (i["l1PhysIf"]["attributes"]["dn"] == "topology/pod-1/node-201/sys/phys-[eth1/34]") \
            or (i["l1PhysIf"]["attributes"]["dn"] == "topology/pod-1/node-201/sys/phys-[eth1/35]"): 
        s = "" 
        s += i["l1PhysIf"]["attributes"]["dn"]  
        s += "                              " 
        s += i["l1PhysIf"]["attributes"]["speed"]  
        s += "   " 
        s += i["l1PhysIf"]["attributes"]["mtu"] 
        print(s)    