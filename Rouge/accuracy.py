from rouge import Rouge
from pprint import pprint
with open('./Gold_Standards/demo_goldstandard.txt', 'r', encoding="utf-8") as f:
    tgoldstandard = f.readlines()
with open('./Outputs/demo_output.txt', 'r', encoding="utf-8") as f:
    toutput = f.readlines()

goldstandard = []
output = []

for i in range(0, len(tgoldstandard)):
    goldstandard.append(tgoldstandard[i].rstrip())
for i in range(0, len(toutput)):
    output.append(toutput[i].rstrip())

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

def rouge_1():
    
    bool_goldstandard = [False for x in range(0, total_words_goldstandard)]
    matchingwords = []
    matchedwords = 0

    for i in range(0, total_words_goldstandard):
        if(bool_goldstandard[i] == True):
            continue
        for j in range(0, total_words_output):
            if (bool_goldstandard[i] == False and goldstandard_words[i] == output_words[j]):
                matchedwords += 1
                matchingwords.append(goldstandard_words[i])
                bool_goldstandard[i] + True
                break
            
    print("The accuracy for ROUGE-1 is " + str(matchedwords/total_words_output))
    # print(matchingwords)

def rouge_L ():

    longest_common_string = ""
    matched_string = ""

    for i in range(0, total_words_goldstandard):
        for j in range(0, total_words_output):
            flag = False
            if (goldstandard_words[i] == output_words[j]):
                matched_string += goldstandard_words[i]
                if len(matched_string) >= len(longest_common_string):
                    longest_common_string = matched_string


rouge_1()    

hypothesis = ""
reference = ""

for i in range(0, len(goldstandard)):
    reference += goldstandard[i]
# print(reference)
for i in range(0, len(output)):
    hypothesis += output[i]
# print(hypothesis)

rouge = Rouge()
scores = rouge.get_scores(hypothesis, reference)
pprint(scores)
