#file Operation 
'''s=input("Enter String1:\n")
f=open('test.txt','w')
f.write(s)
f.close()
s1=input("Enter String2:\n")
f1=open('test.txt','a')
f1.writelines(s1)
f1.write("\n"s)
f1.writelines(s1)
f1.write(s)
f1.writelines(s1)
f1.close()'''
e=open('test.txt','r')
dd=e.read()
e.close()
print(dd)
f=open('test2.txt','w')
f.write(dd)
f.close()