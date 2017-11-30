# python program
import os
file = 'test.py'
f = open(file,'r+')
f.seek(0)
f.truncate(0)
f.close()
os.remove(file)

print('game over!')
