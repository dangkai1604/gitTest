import re
import os
number = 0;

def DeleteComment(fileName):
    try:
        f = open(fileName,'r+')
    except:
        pass
    else:
        list1 = f.readlines()
        list2 = []
        list3 = []

        for line in list1:
            num = line.find('//')
            if(num == -1):
                if( len(line)!=0):
                    list2.append(line)
            else:
                if( len(line[0:num])!=0 ):
                    list2.append(line[0:num]+'\n')

        mutilines = 0
        strTemp = ''
        for line in list2:
            if mutilines == 0:
                num = line.find('/*')
                if(num == -1):
                    list3.append(line)
                else:
                    strTemp = line[0:num]
                    num1 = line.find('*/',num+2)
                    if(num1 == -1):
                        if(len(strTemp )!=0):
                            list3.append(strTemp + '\n')
                        mutilines = 1
                    else:
                        list3.append(strTemp + line[num1+2:len(line)]) 
            else:
                num = line.find('*/')
                if(num != -1):
                    if(num>0 ):
                        list3.append(line[num+2:len(line)])
                    mutilines = 0
            
            
            
        f.seek(0)
        f.truncate(0)

        for line in list3:
            data = line.rstrip()
            if( len(data)!=0):
                data = data + '\n'
                f.write(data)            
        f.close()
    return


def dealFile(fileName):
    global number    
    if (len(fileName)>2 and (fileName[-2:]=='.c'or fileName[-2:]=='.h'or \
                             fileName[-2:]=='.C'or fileName[-2:]=='.H'   \
                             )):
        DeleteComment(fileName)
        print(fileName)
        number = number+1;
    return


def dealDir(dirName):       
    try:
        file = os.listdir(dirName)
    except :
        print('except :',dirName)
    else:
        for f in file:
            fileName = os.path.join(dirName,f)
            if os.path.isfile(fileName):                               
                dealFile(fileName)
            elif os.path.isdir(fileName):                                
                dealDir(fileName)
    return


def main():
    try:        
        file = os.listdir()
    except:
        print('except :',dirName)
    else:
        for f in file:
            if os.path.isfile(f):
                dealFile(f)
            elif os.path.isdir(f):
                dealDir(f)      
    print ('precoss:',number,'files')
    return
        
if __name__ =='__main__':
    main()

        
        
    


    
