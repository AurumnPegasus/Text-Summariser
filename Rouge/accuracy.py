
# Function to calculate the accuracy using Rouge-1 as a base.

def rouge_1(gold, hypothesis):

# Initialising the variables which will store words and the number of the words.

    number_gold_words = 0
    gold_words = []
    number_hypothesis_words = 0
    hypothesis_words = []


# Converting sentences into a list of words.
    for temp_sentence in gold:

        sentence = temp_sentence.split(" ")        
        for word in sentence:
# Removing fullstops.
            if word != "।":
                number_gold_words += 1
                gold_words.append(word)

# Converting sentences into a list of words.
    for temp_sentence in hypothesis:

        sentence = temp_sentence.split()
        for word in sentence:
# Removing fullstops.
            if word != "।":
                number_hypothesis_words += 1
                hypothesis_words.append(word)

# Creating an array of bools to check whether a word exists or not.
# Also initialising the variables which will store the length of the common words and the common words as well.
    vis_gold_words = [False for i in range(0, number_gold_words)]
    commonwords = []
    number_common_words = 0

# Algorithm to find the common words and the number. 
    for i in range(0, number_gold_words):
        for j in range(0, number_hypothesis_words):
            if (hypothesis_words[j] == gold_words[i] and vis_gold_words[i] == False):
                commonwords.append(hypothesis_words[j])
                vis_gold_words[i] == True
                number_common_words += 1
                break
    
# Storing the final accuracy of Rouge-1
    accuracy = number_common_words/number_hypothesis_words

# Uncomment any of the code below if you want to print either the common words, how many common words there are.
# Do the same if you want to know about the hypothesis words.
# If you want to know the accuracy for the Rouge1 per article uncomment line 63.


    # print(number_common_words)
    # print(commonwords)
    # print(hypothesis_words)
    # print(number_hypothesis_words)
    # print('The accuracy for Rouge_1 for this article is ' + str(accuracy))
    
    return accuracy


# Variables to store the accuracies for the extractive and rulebased methods
total_accuracy_extractive = 0
total_accuracy_rulebased = 0

# Storing the relative paths to read the text files.
g_path = "../Summaries/Gold/"
h_path = "../Summaries/Extractive/"
r_path = "../Summaries/RuleBased/"

# Calculating the accuracies for all the files.
counter = 0 # Variable to store number of articles.
for i in range(1, 8):

# Making a new path for every article.
    gold_path = g_path + str(i) + ".txt"
    hypothesis_path = h_path + str(i) + ".txt"
    rulebased_path = r_path + str(i) + ".txt"

# Reading the files.
    with open(gold_path, 'r', encoding='utf-8') as f:
        g1 = f.readlines()
    with open(hypothesis_path, 'r', encoding='utf-8') as f:
        e1 = f.readlines()
    with open(rulebased_path, 'r', encoding='utf-8') as f:
        r1 = f.readlines()

# Calculating the total accuracies. 
    counter += 1
    total_accuracy_extractive += rouge_1(g1, e1)
    total_accuracy_rulebased += rouge_1(g1, r1)

# Calculate the final accuracies for each method.

final_accuracy_extractive = total_accuracy_extractive/counter
final_accuracy_rulebased = total_accuracy_rulebased/counter

print("\nThe accuracy for the extractive method is " + str(final_accuracy_extractive))
print("\nThe accuracy for the rule based method is " + str(final_accuracy_rulebased))

