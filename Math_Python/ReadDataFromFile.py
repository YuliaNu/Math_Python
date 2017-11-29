
file_obj=open('Robert_Frost.txt','r')

#Print type of file_obj
print(type(file_obj))

#Print all data from Robert_Frost.txt
print(file_obj.read())

#Close file
file_obj.close()

#Read by line
file_obj=open('Robert_Frost.txt','r')
for line in file_obj:
    print(line.strip())

#Create data list
file_object=open('Robert_Frost.txt','r')
data_list=list(file_obj)

#Close file
file_obj.close()


for line in data_list:
    print(line)

#Close file
file_obj.close()

#Codecs
import codecs
file_obj=codecs.open('Robert_Frost.txt','r',encoding='utf-8')
print(file_obj.read())


