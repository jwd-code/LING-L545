I tested the NLTK tokenizer and the Pragmatic Segmenter on 10 lines from the Occitan Wiki dump, and both segmenters had 100% accuracy. To test this again, I tested the next 10 lines from the text file. After manually segmenting the 10 lines, there were 15 lines in total. 

The information about the Pragmatic Segmenter that I could find is taken from the Github page: https://github.com/diasks2/pragmatic_segmenter. This segmenter is a rule-based sentence boundary detector that does not use any machine learning, meaning it does not have to be trained. The objective of the segmenter is to be a tool that can "work out of the box" on many languages. The creators advertise the segmenter as being "opinionated" in that it has been specifically designed for the creation of translation memories. 

The information that I found regarding NLTK sentence segmenter comes from the documentation on https://www.nltk.org/api/nltk.tokenize.punkt.html. According to this page, the segmenter uses an unsupervised machine learning algorithm, meaning that it requires training on a large dataset prior to being used. The unsupervised algorithm learns parameters, like a list of abbreviation, collocations and words that frequently occur at the beginning of sentences from this dataset. 

Quantitative Evaluation:
NLTK Accuracy accuracy: 73% (four errors out of 15 lines)
Pragmatic Segmenter accuracy: 100% (0 errors)

Qualitative Evaluation:
The NLTK segmenter segmented sentences that should not have been segmented, and failed to segment sentences that should have been. For example, after the abbreviation "var." the segmenter split the sentence onto a new line, meaning that it interpreted this abbrevation as marking the end of the sentence. There were cases in the text in which the end of the sentence had a space before the period, for example:

"L'esquiròl es una bèstia solitari .Passa principalament lo temps..."

The NLTK segmenter did not separate these sentences into two sentences, leaving the line as shown above. This means that it failed to recognize the end of the sentence. The Pragmatic Segmenter, on the other hand, did not make either of the mistakes mentioned.

