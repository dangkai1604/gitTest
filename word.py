import docx

text = []
doc = docx.Document('f:\\test1.docx')
paras = doc.paragraphs
for p in paras:
    text.append(p.text)

file = open('f:\\test.txt','w')
for t in text:
    if len(t)!=0:
        file.write(t+'\n')

file.close()
#print(text)

