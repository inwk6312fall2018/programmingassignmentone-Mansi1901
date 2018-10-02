def replace_ip(file_name):
    file = open(file_name)
    l1 = []
    l2 = [] #all ip address
    l3 = [] #elements in ip
    l4 = [] #updated ip
    for line in file:
        line = line.strip()
        for word in line.split():
            l1.append(word)

    for i in range(len(l1)):
        if l1[1-i] != 'no' and l1[i] == 'ip' and l1[i+1] == 'address':
               l2.append(l1[i+2]) #add all ip address in l2

    for i in l2:
        l3.append(i.split('.'))
    for i in l3: #loop to remove 192 and 172 and update it with 10
        del i[0]
        i.insert(0,'10') #insert 10 at place of 192 or 172
        l4.append('.'.join(i)) #adding updated ip in l4
    return l4

print(replace_ip('running-config.cfg'))
