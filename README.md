# Text Summarizer for Hindi Wikipedia Articles

This is a project made by:
* Prajneya Kumar
* Shivansh S.
* Tejasvi Chebrolu

## How to Use

* Clone the repository
* Install all dependencies mentioned in ```requirements.txt```
* Choose which method you would like to use, and depending on that go to appropriate section

### Extractive

This model generates a summary using a Document Term Matrix and frequency count. To use this

* Go to the ```Extractive``` folder
* Place your article in ```valid``` folder named as ```article.txt```.
* Run the ```extractive.py``` file using python3.

* You will end up getting a summary named as ```summary.txt``` inside the ```valid``` folder.

### Rule Based

This model generates a summary using modified TF-IDF of the document dataset, with weights attached. To use this

* Place your article in ```valid``` folder
* Run the code in jupyter notebook
* Input the name of your file which is within that directory

* You will end up getting a summary + wordcloud as a text file :)

### Calculating Accuracy

* Add the Gold standard for the summary as ```n.txt``` in the Gold folder in the Summaries directory. Here `n` is the next number in the sequence in the Gold folder.
* For example, if there are 7 files in the Gold Folder, they must be labelled as ```1.txt``` ```2.txt``` ... ```7.txt``` etc.
* Repeat this process for the summaries generated by the rule-based method and the extractive method and store them in the `Extractive` and `RuleBased` directories.
* You can do this on the terminal via simple redirection. 
* Now, in the `accuracy.py` file on line number 53, change the code to ```for i in range(1, n+1):``` where n is the same variable as above.
* For example, if your file was saved as `9.txt` you would change the code to ```for i in range(1, 10):```
* Run the code as `python accuracy.py`
* If you want individual accuracies for any article, you can uncomment line number 63 in the same file.
* It is advised then to redirect to a new file as `python accuracy.py > output.txt` to enable better formatting.

## How to Contribute

* Fork this repository 
* Clone the forked repository to your local system
* ```git remote add upstream https://github.com/AurumnPegasus/Text-Summariser.git```
* Install all required dependencies (mentioned in ```requirements.txt```)
* Commit and Send PRs :)
