import os
import os.path
import shutil

# Get the paths of the GoldStandard and the Output.
pwd = os.getcwd()
o = [os.path.join(pwd,o) for o in os.listdir(pwd) if os.path.isdir(os.path.join(pwd,o))]
for item in o:
    if os.path.exists(item + '/demo_goldstandard.txt'):
        goldstandard_path = item + '/demo_goldstandard.txt'
    if os.path.exists(item + '/demo_output.txt'):
        output_path = item + '/demo_output.txt'

with open(goldstandard_path, 'r', encoding="utf-8") as f:
    tgoldstandard = f.readlines()
with open(output_path, 'r', encoding="utf-8") as f:
    toutput = f.readlines()

goldstandard = []
output = []

for i in range(0, len(tgoldstandard)):
    goldstandard.append(tgoldstandard[i].rstrip())
for i in range(0, len(toutput)):
    output.append(toutput[i].rstrip())

def rogue_1():

    total_words_output = 0
    total_words_goldstandard = 0
    output_words = []
    goldstandard_words = []

    for tsentence in output:
        sentence = list(tsentence.split(" "))
        for word in sentence:
            output_words.append(word)
            total_words_output += 1
    for tsentence in goldstandard:
        sentence = list(tsentence.split(" "))
        for word in sentence:
            total_words_goldstandard += 1
            goldstandard_words.append(word)
    
    matchedwords = 0
    bool_goldstandard = [False for x in range(0, total_words_goldstandard)]

    for i in range(0, total_words_goldstandard):
        if(bool_goldstandard[i] == True):
            continue
        for j in range(0, total_words_output):
            if (bool_goldstandard[i] == False and goldstandard_words[i] == output_words[j]):
                matchedwords += 1
                bool_goldstandard[i] + True
                break
            
    print("The accuracy for ROUGE-1 is " + str(matchedwords/total_words_output))

rogue_1()