#open file

myfile = open("running-config.cfg")

#Running throughout the file and collect interfacenames

for line in myfile:
    #first remove whitespace and extra stuff
    line = line.strip()
