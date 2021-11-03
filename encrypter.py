#name = str(input("Enter a name of a text file to encrypt:\n"))
    file = open('text.txt', "r")
    copy_file = open('copy.txt', 'w')
    key = open('key.txt', 'w')
    content = file.readlines()
    list = []
    count = len(open('text.txt').readlines())
    int_random = random.randint(0,count)
    while len(list)<count:
        int_random = random.randint(1, count)
        if int_random  not in list:
            list.append(int_random)
    for i in list:
        #print(i)
        line = int(i)
        line -= 1
        copy_file.write(content[line])
        key.write(str(i)+"\n")
