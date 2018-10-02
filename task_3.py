def access_list(file_name):
    file = open(file_name)
    l1 = []
    for line in file:
        line = line.strip()
        for i in line.split():
            if i == 'global_access' or i == 'fw-management_access_in':
               l1.append(line)
    return l1

print(access_list('running-config.cfg'))
