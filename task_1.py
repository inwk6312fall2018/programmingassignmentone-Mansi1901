#open file

myfile = open("running-config.cfg")

#Variable to load values

mylist_intname=[]

#Running throughout the file and collect interface names

for line in myfile:
    #first remove whitespace and extra things
    line = line.strip()
    line = line.split()
if(line[0] == "interface"):
    mylist_intname.append(line[1])

print(mylist_intname)
