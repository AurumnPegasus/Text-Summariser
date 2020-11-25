from nltk.tokenize import word_tokenize

# Iterate over each file to summarize
article_name = "valid/article.txt"
print("Summarizing article...")
with open(article_name, 'r', encoding="utf8") as f:
    sentences = f.readlines()

# store stopwords
with open('stopwords.txt', 'r', encoding="utf8") as s:
    stopwords = s.readlines()

for i in range(len(stopwords)):
    stopwords[i] = stopwords[i].strip()

stemmed_words = set()
cleaned_sentences = []
sentence_scores = []

for i in range(len(sentences)):
    sentence = sentences[i]
    sentence_tokens = word_tokenize(sentence) # Tokenize words for processing
    cleaned_sentence = [word for word in sentence_tokens if not word in stopwords] # Eliminate StopWords


    # Suffix Strip Algorithm
    suffixes = {
    1: [u"ो",u"े",u"ू",u"ु",u"ी",u"ि",u"ा"],
    2: [u"कर",u"ाओ",u"िए",u"ाई",u"ाए",u"ने",u"नी",u"ना",u"ते",u"ीं",u"ती",u"ता",u"ाँ",u"ां",u"ों",u"ें"],
    3: [u"ाकर",u"ाइए",u"ाईं",u"ाया",u"ेगी",u"ेगा",u"ोगी",u"ोगे",u"ाने",u"ाना",u"ाते",u"ाती",u"ाता",u"तीं",u"ाओं",u"ाएं",u"ुओं",u"ुएं",u"ुआं"],
    4: [u"ाएगी",u"ाएगा",u"ाओगी",u"ाओगे",u"एंगी",u"ेंगी",u"एंगे",u"ेंगे",u"ूंगी",u"ूंगा",u"ातीं",u"नाओं",u"नाएं",u"ताओं",u"ताएं",u"ियाँ",u"ियों",u"ियां"],
    5: [u"ाएंगी",u"ाएंगे",u"ाऊंगी",u"ाऊंगा",u"ाइयाँ",u"ाइयों",u"ाइयां"],
    }

    cleaned_sentences.append(cleaned_sentence) # Store cleaned sentences

    # Remove Suffixes to obtain stem words
    for word in cleaned_sentence:
        if word == '।':
            continue
        for L in 5, 4, 3, 2, 1:
            if len(word) > L + 1:
                for suf in suffixes[L]:
                    if word.endswith(suf):
                        stemmed_words.add(word[:-L])
        stemmed_words.add(word)

# Convert stemmed words set to array
stemmed_words_array = list(stemmed_words)

# Initialize DTM (Document Term Matrix)
rows, cols = (len(stemmed_words), len(cleaned_sentences))
dtm = [[0 for i in range(cols)] for j in range(rows)]

# Build the Document Term Matrix
for i in range(len(cleaned_sentences)):
    for word in cleaned_sentences[i]:
        if word == '।':
            continue
        for L in 5, 4, 3, 2, 1:
            if len(word) > L + 1:
                for suf in suffixes[L]:
                    if word.endswith(suf):
                        if word not in stemmed_words_array:
                            print(word)
                        else:
                            dtm[stemmed_words_array.index(word[:-L])][i] = dtm[stemmed_words_array.index(word[:-L])][i] + 1
        if word not in stemmed_words_array:
            print(word)
        else:
            dtm[stemmed_words_array.index(word)][i] = dtm[stemmed_words_array.index(word)][i] + 1

# Score each Sentence according to the algorithm
for j in range(len(cleaned_sentences)):
    sentence_score = 0
    for i in range(len(stemmed_words_array)):
        sentence_score = sentence_score + dtm[i][j]
    if len(cleaned_sentences[j]) == 0:
        continue
    sentence_score = sentence_score/len(cleaned_sentences[j])
    sentence_scores.append(sentence_score)

# Sort sentences based on their scores
sentence_index = sorted(range(len(sentence_scores)), key=lambda k: sentence_scores[k])

# Retrieve the top 30% of highest scored sentences
count = int(len(sentence_index)*0.3)

# Sort sentences based on the order in which they appear in the text document
sentence_index = sentence_index[(len(sentence_index)-count):]
sentence_index.sort()

# Print the obtained summary
summary_name = "valid/summary.txt"
for i in range(len(sentence_index)):
    with open(summary_name, "a", encoding="utf8") as text_file:
        print(sentences[sentence_index[i]], file=text_file)
