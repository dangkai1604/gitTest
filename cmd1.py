import os
os.chdir('f:\\')
os.getcwd()
for i in range(1000):
    name = 'test'+str(i)
    os.mkdir(name)
    os.chdir(name)
    print(i)
