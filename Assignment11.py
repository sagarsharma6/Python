#Ques 1

import re
matches=re.finditer('[a-zA-Z0-9_.]*[@](gmail.com|yahoo.com)','abc@gmail.com_def@yahoo.com')
print("Valid email id:")
for i in matches:
    print(i.group())


#Ques 2

matches=re.finditer('[+][9][1][-][6-9][0-9]{9}','+91-8146004295 abc +91-8143578340')
print("Valid phone numbers:")
for i in matches:
    print(i.group())
