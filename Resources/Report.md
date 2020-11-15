# Hindi Article Summarizer

---

## Computational Linguistics II

Shivansh S *2019114003*

C.S. Ramakrishna Tejasvi *2019114005*

Prajneya Kumar *2019114011*

---

## Summarizer

A summarizer is any piece of software that converts a long piece of text into a shorter, more concise one. This helps users save time, and prevents them from going through long articles to find what they are looking for. A good summarizer is one that manages to capture the essence of the entire article without it being of the same length.

There are two types of summarizers based on the process/algorithm followed by the summarizer. They are:

### Extractive Summarizer

The extractive approach involves picking up the most important phrases and lines from the documents. It then combines all the important lines to create the summary. So, in this case, every line and word of the summary actually belongs to the original document, which is summarized.

**Flow Chart**

![Hindi%20Article%20Summarizer%20ce335f4117124730a2aaa8428ca2f049/Untitled.png](Hindi%20Article%20Summarizer%20ce335f4117124730a2aaa8428ca2f049/Untitled.png)

*This is the method that we are following for our summarizer.*

**Further Reading:** 

[](https://www.researchgate.net/publication/329945598_Review_of_recent_techniques_for_extractive_text_summarization)

---

### Abstractive Summarizer

The abstractive approach involves summarization based on deep learning. So, it uses new phrases and terms, different from the actual document, keeping the points the same, just like how we actually summarize. So, it is much harder than the extractive approach.

**Flow Chart**

![Hindi%20Article%20Summarizer%20ce335f4117124730a2aaa8428ca2f049/Untitled%201.png](Hindi%20Article%20Summarizer%20ce335f4117124730a2aaa8428ca2f049/Untitled%201.png)

**Further Reading:**

[](https://home.iitk.ac.in/~soumye/cs498a/report.pdf)

---

## Evaluation Methodology

### ROUGE

ROUGE stands for **Recall-Oriented Understudy for Gisting Evaluation**. It is the method that determines the quality of the summary by comparing it to other summaries made by humans as a reference. To evaluate the model, there are a number of references created by humans and the generated candidate summary by machine. The intuition behind this is if a model creates a good summary, then it must have common overlapping portions with the human references. It was proposed by Chin-Yew Lin, University of California.

The common versions of Rogue are:

- **ROUGE-n**

    It is measure on the comparison between the machine-generated output and the reference output based on n-grams. An **n-gram** is a contiguous sequence of n items from a given sample of text or speech, i.e, it is simply a sequence of words.

    $ROUGE{-n} = p/q$

    *“Where $p$ is “the number of common n-grams between candidate and reference summary”, and $q$ is “the number of n-grams extracted from the reference summary only.”*

- **ROUGE-L**

    It states that the longer the longest common subsequence in two texts, the similar they are. So, it is flexible than n-gram. It assigns scores based on how long can be a sequence, which is common to the machine-generated candidate and the human reference.

We shall be using a mixture of *ROUGE-n* and *ROUGE-L* to evaluate our summaries. The gold standard/reference summary shall be manually done.

**Further Reading:**

[Text Summarization Techniques: A Brief Survey](https://arxiv.org/abs/1707.02268v3)