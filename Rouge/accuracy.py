def rouge_1(gold, hypothesis):

    number_gold_words = 0
    gold_words = []
    number_hypothesis_words = 0
    hypothesis_words = []

    for temp_sentence in gold:

        sentence = temp_sentence.split(" ")        
        for word in sentence:
            if word != "।":
                number_gold_words += 1
                gold_words.append(word)

    for temp_sentence in hypothesis:

        sentence = temp_sentence.split()
        for word in sentence:
            if word != "।":
                number_hypothesis_words += 1
                hypothesis_words.append(word)

    vis_gold_words = [False for i in range(0, number_gold_words)]
    commonwords = []
    number_common_words = 0

    for i in range(0, number_gold_words):
        for j in range(0, number_hypothesis_words):
            if (hypothesis_words[j] == gold_words[i] and vis_gold_words[i] == False):
                commonwords.append(hypothesis_words[j])
                vis_gold_words[i] == True
                number_common_words += 1
                break
    
    accuracy = number_common_words/number_hypothesis_words
    # print(number_common_words)
    # print(commonwords)
    # print(hypothesis_words)
    # print(number_hypothesis_words)
    # print('The accuracy for Rouge_1 for this article is ' + str(accuracy))

    return accuracy

total_accuracy_extractive = 0
total_accuracy_rulebased = 0

g_path = "../Summaries/Gold/"
h_path = "../Summaries/Extractive/"
r_path = "../Summaries/RuleBased/"

counter = 0
for i in range(1, 8):

    gold_path = g_path + str(i) + ".txt"
    hypothesis_path = h_path + str(i) + ".txt"
    rulebased_path = r_path + str(i) + ".txt"

    with open(gold_path, 'r', encoding='utf-8') as f:
        g1 = f.readlines()
    with open(hypothesis_path, 'r', encoding='utf-8') as f:
        e1 = f.readlines()
    with open(rulebased_path, 'r', encoding='utf-8') as f:
        r1 = f.readlines()
    
    counter += 1
    total_accuracy_extractive += rouge_1(g1, e1)
    total_accuracy_rulebased += rouge_1(g1, r1)
    
final_accuracy_extractive = total_accuracy_extractive/counter
final_accuracy_rulebased = total_accuracy_rulebased/counter

print("\nThe accuracy for the extractive method is " + str(final_accuracy_extractive))
print("\nThe accuracy for the rule based method is " + str(final_accuracy_rulebased))





