#file.py
import os
 
def getName(num):
    if num <10:
        strRes = '0000' + str(num)
    elif num <100:
        strRes = '000' + str(num)
    elif num <1000:
        strRes = '00' + str(num)
    elif num < 10000:
        strRes = '0' + str(num)
    return strRes

#Give the name of your timestamp file 
file_object = open('rgb.txt','w')
Ostr = ''
    #Change the name of the image doc
num = len(os.listdir('rgb'))
for i in range(1,num+1):
    name = getName(i)
    #Change here too
    Ostr = Ostr + name + ' rgb/' + name + '.png\n'
file_object.writelines(Ostr)
file_object.close()
