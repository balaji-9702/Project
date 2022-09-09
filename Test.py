

from pathlib import Path


#newfile_name = "tst_document"
file_path = Path(r"C:\Users\YY617KW\Downloads\Test\sample.txt")
f = open(file_path)
#f = open("sample.txt","r")
lines = f.readlines()
with open(r'C:\Users\YY617KW\Downloads\Test\tst_document.txt','w') as f:
    f.write(f''' {lines}''')
value = f''' {lines}'''
#list = [lines]
print(value)
#if value.find('password'):
if ('password' in value ):
 print(value.find('password'))
else:
    print('cannot find "password"')
 
