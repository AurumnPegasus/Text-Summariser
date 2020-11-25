# Importing the Rouge files.
from Rouge_1 import rouge_1

# Variables to store the accuracies for the extractive and rulebased methods
total_accuracy_extractive = 0
total_accuracy_rulebased = 0

# Storing the relative paths to read the text files.
g_path = "../Summaries/Gold/"
h_path = "../Summaries/method_1/"
r_path = "../Summaries/method_2/"

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

print("\nThe accuracy for the method I is " + str(final_accuracy_rulebased))
print("\nThe accuracy for the method II is " + str(final_accuracy_extractive))

