import os
f1 = open('eh.txt', 'w')
documents = os.listdir('valid')
for doc in documents:
    articleName = "valid/" + doc
    f = open(articleName).read()
    sentences = f.split('।')
    if len(sentences) > 100:
        f1.write(str(doc))
        f1.write("\n")