import re

with open("111.pdf",'r',encoding='utf-8') as filek:
    for line in filek:
        line = line.strip()
        new = re.sub(',',' / ',line)
        newO = re.sub('[0-9]+.',';',new)
        new1 = re.sub(':',',',newO)
        print(new1)
    