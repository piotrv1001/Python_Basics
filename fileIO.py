import os

with open("text.txt", 'w', encoding = 'utf-8') as f:
    f.write("Hello\n")
    f.write("world\n")
    f.writelines(["Python\n","is\n","awesome\n"])

with open("text.txt", 'r', encoding = 'utf-8') as f:
    for line in f:
        print(line, end ='')

    f.seek(0)
    l = f.readlines()
    for i in range(len(l)):
        l[i] = l[i].rstrip('\n')
    print(l)
    print(f.tell())


print(os.getcwd())
print(os.listdir())
# os.mkdir('test')