import re
with open("yh.txt",'r',encoding='utf-8') as file:
    for line in file:
        result = re.sub(r'[0-9]','',line).lstrip()
        with open('rossetta_non.txt','a') as new:
            new.write(result)