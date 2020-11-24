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
# If you want to know the accuracy for the Rouge1 per article uncomment line 62.


    # print(number_common_words)
    # print(commonwords)
    # print(hypothesis_words)
    # print(number_hypothesis_words)
    # print('The accuracy for Rouge_1 for this article is ' + str(accuracy))
    
    return accuracy