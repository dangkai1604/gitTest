import re
import os
number = 0


def dealFile(fileName ,writeFile):
    global number
    writeFile.write(fileName)
    writeFile.write('\n')
    number = number + 1
    return


def dealDir(dirName,writeFile):       
    try:
        file = os.listdir(dirName)
    except :
        print('except :',dirName)
    else:
        for f in file:
            fileName = os.path.join(dirName,f)
            if os.path.isfile(fileName):                               
                dealFile(fileName,writeFile)
            elif os.path.isdir(fileName):                                
                dealDir(fileName,writeFile)
    return


def main():
    try:        
        file = os.listdir()
        writeFile = open('writeFile.txt','w')
    except:
        print('except : os.listdir()')
    else:        
        for f in file:
            if os.path.isfile(f):
                dealFile(f,writeFile)
            elif os.path.isdir(f):
                dealDir(f,writeFile )
        writeFile.write('total scan : '+ str(number)+' files'+'\n')
        writeFile.close()
    return
        
if __name__ =='__main__':
    main()

        
        
    


    
