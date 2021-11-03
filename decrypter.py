key = open('key.txt', 'r')
    file = open('copy.txt', 'r')
    de_file = open('decrypted.txt','w')
    content = file.readlines()
    list = []
    for i in key:
        list.append(int(i))
    print(list)
    count = len(list)
    i = 1
    e = 0
    while i<len(list)+1:
        if i!= int(list[e]):
            e+=1
        elif i==int(list[e]):
            de_file.write(content[e])
            i+=1
            e=0
