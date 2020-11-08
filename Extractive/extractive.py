from nltk.tokenize import word_tokenize

with open('sample.txt', 'r', encoding="utf8") as f:
    sentences = f.readlines()

with open('stopwords.txt', 'r', encoding="utf8") as s:
    stopwords = s.readlines()

for i in range(len(stopwords)):
    stopwords[i] = stopwords[i].strip()

stemmed_words = set()
cleaned_sentences = []
sentence_scores = []

for i in range(len(sentences)):
    sentence = sentences[i]
    sentence_tokens = word_tokenize(sentence)
    cleaned_sentence = [word for word in sentence_tokens if not word in stopwords]

    suffixes = {
    1: [u"ो",u"े",u"ू",u"ु",u"ी",u"ि",u"ा"],
    2: [u"कर",u"ाओ",u"िए",u"ाई",u"ाए",u"ने",u"नी",u"ना",u"ते",u"ीं",u"ती",u"ता",u"ाँ",u"ां",u"ों",u"ें"],
    3: [u"ाकर",u"ाइए",u"ाईं",u"ाया",u"ेगी",u"ेगा",u"ोगी",u"ोगे",u"ाने",u"ाना",u"ाते",u"ाती",u"ाता",u"तीं",u"ाओं",u"ाएं",u"ुओं",u"ुएं",u"ुआं"],
    4: [u"ाएगी",u"ाएगा",u"ाओगी",u"ाओगे",u"एंगी",u"ेंगी",u"एंगे",u"ेंगे",u"ूंगी",u"ूंगा",u"ातीं",u"नाओं",u"नाएं",u"ताओं",u"ताएं",u"ियाँ",u"ियों",u"ियां"],
    5: [u"ाएंगी",u"ाएंगे",u"ाऊंगी",u"ाऊंगा",u"ाइयाँ",u"ाइयों",u"ाइयां"],
    }

    cleaned_sentences.append(cleaned_sentence)

    for word in cleaned_sentence:
        if word == '।':
            continue
        for L in 5, 4, 3, 2, 1:
            if len(word) > L + 1:
                for suf in suffixes[L]:
    				#print type(suf),type(word),word,suf
                    if word.endswith(suf):
                        stemmed_words.add(word[:-L])
        stemmed_words.add(word)

stemmed_words_array = list(stemmed_words)
rows, cols = (len(stemmed_words), len(cleaned_sentences))
dtm = [[0 for i in range(cols)] for j in range(rows)]

for i in range(len(cleaned_sentences)):
    for word in cleaned_sentences[i]:
        if word == '।':
            continue
        for L in 5, 4, 3, 2, 1:
            if len(word) > L + 1:
                for suf in suffixes[L]:
    				#print type(suf),type(word),word,suf
                    if word.endswith(suf):
                        if word not in stemmed_words_array:
                            print(word)
                        else:
                            dtm[stemmed_words_array.index(word[:-L])][i] = dtm[stemmed_words_array.index(word[:-L])][i] + 1
        if word not in stemmed_words_array:
            print(word)
        else:
            dtm[stemmed_words_array.index(word)][i] = dtm[stemmed_words_array.index(word)][i] + 1

for j in range(len(cleaned_sentences)):
    sentence_score = 0
    for i in range(len(stemmed_words_array)):
        sentence_score = sentence_score + dtm[i][j]
    sentence_score = sentence_score/len(cleaned_sentences[j])
    sentence_scores.append(sentence_score)

sentence_index = sorted(range(len(sentence_scores)), key=lambda k: sentence_scores[k])

count = int(len(sentence_index)*0.3)
check = 0

sentence_index = sentence_index[(len(sentence_index)-count):]
sentence_index.sort()

for i in range(len(sentence_index)):
    with open("output.txt", "a", encoding="utf8") as text_file:
        print(sentences[sentence_index[i]], file=text_file)

# for i in reversed(range(len(sentence_index))):
#     check = check + 1
#     with open("output.txt", "a", encoding="utf8") as text_file:
#         print(sentences[sentence_index[i]], file=text_file)
#     if check == count:
#         break
