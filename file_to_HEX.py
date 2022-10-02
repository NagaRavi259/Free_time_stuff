import os

location=input("Files directory: ")
os.chdir(location)
directory = os.getcwd()
k=os.listdir(directory)
g=[]
for i in k:
    print(i)
    path = i
    with open(path, 'rb') as fin:
        while True:
            data = fin.read(16)
            if len(data) == 0:
                break
            # iterate over each byte in byte sequence
            for b in data:
                g.append(' {:02x}'.format(b))
            #print()
    f=open(i+".txt",'w')
    for ele in g:
        f.write(ele+'\n')
    f.close()