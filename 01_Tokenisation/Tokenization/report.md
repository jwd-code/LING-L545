Jeremy Dickinson - Maxmatch Report

1. Implementation of Maxmatch
My implementation of maxmatch was created following the pseudocode description of the algorithm shown in Section 3.9.1 of Jurafsky and Martin (2nd Edition). The Maxmatch.py file in the repo takes in the training file and the testing file. As I was struggling with grep, I decided to use a Python library called pyconll to extract a dictionary of Japanese words/characters (stored as a list of strings), and I sorted it in reverse order by the length of the strings so that the maxmatch algorithm would search through the list faster. I then defined the maxmatch function, which takes in a sentence as well as the dictionary, and recursively takes in a chunk of each sentence and searches for it in the dictionary until it returns the maximum length item found in the dictionary. I also defined a function that creates the hypothesis.txt file, which is used in the evaluation. This function iterates over each sentence in the test file, runs maxmatch on it, and then stores the tokenized sentence in another file. 


2. Instructions on how to use it
To run the maxmatch.py file, you need to open the python file and put in the path for the train conllu file, the path for the test conllu file, and the output path for the hypothesis.txt file. You also need to install pyconll in order to create the dictionary used in the maxmatch function. After all of that has been done, if you run the python file, it should run maxmatch on every sentence in the test file and create a hypothesis.txt file. 

To evaluate the hypothesis.txt file, all you have to do is run 'python3 wer.py reference.txt hypothesis.txt' and it should print out the WER for each line of hypothesis.txt file. I changed the WER.py to print out the WER line for line rather than evaluating both files as two huge chunks. 




3. Performance and Examples to Support Findings

The performance for my implementation of the maxmatch algorithm was found by looking at the first ten lines that were evaluated by the WER.py file. The lowest error rate of the ten sentences examined was 2.00% and the highest was 14.04%. The most common errors appear to be insertions and deletions, however, after reviewing these erros marked by WER.py, I personally do not see where things were inserted or deleted. It is possible that these insertions or deletions are actually spaces, but I tried counting them as well and could not find any additional or missing spaces. Overall, it seems that the performance is pretty good, with most of the error rates being under 10% for each sentence.  



REF: こ れ   に   不 快   感   を   示 す   住 民   は   い   ま し   た   が   ,   現 在   ,   表   立 っ   て   反 対   や   抗 議   の   声   を   挙 げ   て   い る   住 民   は   い   な い   よ う   で す   。

HYP: こ れ   に   不 快   感   を   示 す   住 民   は   い   ま し   た   が   ,   現 在   ,   表   立 っ   て   反 対   や   抗 議   の   声   を   挙 げ   て   い る   住 民   は   い   な い   よ う   で す   。

EVA:                                       D                                   I                                                               D                         I
WER: 4.88%
-----------------------------------------------
REF: 幸 福   の   科 学   側   か ら   は   ,   特 に   ど う   し   て   ほ し い   と   い   う   要 望   は   い   た だ   い   て   い   ま   せ   ん   。

HYP: 幸 福   の   科 学   側   か ら   は   ,   特 に   ど う   し   て   ほ し い   と   い   う   要 望   は   い   た だ   い   て   い   ま   せ   ん   。

EVA:                                                                 D   I             D   I     I           D   I           I
WER: 14.04%
-----------------------------------------------
REF: 星   取 り   参 加   は   当 然   と   さ   れ   ,   不   参 加   は   白   眼   視   さ   れ る   。

HYP: 星   取 り   参 加   は   当 然   と   さ   れ   ,   不   参 加   は   白   眼   視   さ   れ る   。

EVA:   I                                                       I                     I
WER: 7.69%
-----------------------------------------------
REF: 室 長   の   対 応   に   は   終 始   誠 実   さ   が   感 じ   ら れ   た   。

HYP: 室 長   の   対 応   に   は   終 始   誠 実   さ   が   感 じ   ら れ   た   。

EVA:                                                               I
WER: 3.12%
-----------------------------------------------
REF: 多 く   の   女 性   が   生   理   の   こ と   で   悩 ん   で   い   ま   す   。

HYP: 多 く   の   女 性   が   生   理   の   こ と   で   悩 ん   で   い   ま   す   。

EVA:                       I                               D   I       I
WER: 12.50%
-----------------------------------------------
REF: 先 生   の   理 想   は   限 り   な く   高 い   。

HYP: 先 生   の   理 想   は   限 り   な く   高 い   。

EVA:                         I               I
WER: 10.00%
-----------------------------------------------
REF: そ れ   は   兎   も   角   ,   私   も   明 日   の   社   説   を   楽 し み   に   し   て   お り   ま す   。

HYP: そ れ   は   兎   も   角   ,   私   も   明 日   の   社   説   を   楽 し み   に   し   て   お り   ま す   。

EVA:             I   I                             I                                           I
WER: 9.30%
-----------------------------------------------
REF: そ う   だ っ   た ら   い い   な あ   と   は   思 い   ま す   が   ,   日 本   学 術   会 議   の   会 長   談   話   に   つ い   て   “   当 会   で   は   ,   標 記   の   件   に   つ い   て   ,   以 下   の   よ う   に   考 え   ま す   。   ”

HYP: そ う   だ っ   た ら   い い   な あ   と   は   思 い   ま す   が   ,   日 本   学 術   会 議   の   会 長   談   話   に   つ い   て   “   当 会   で   は   ,   標 記   の   件   に   つ い   て   ,   以 下   の   よ う   に   考 え   ま す   。   ”

EVA:                                                                                         I
                                       I
WER: 2.00%
-----------------------------------------------
REF: 教 団   に   と っ   て   は   存 続   が   厳 し く   な る   と   思 う   。

HYP: 教 団   に   と っ   て   は   存 続   が   厳 し く   な る   と   思 う   。

EVA:                                                             I
WER: 3.23%
-----------------------------------------------
REF: し か し   強 制   し   て   い   な く   て   も   問 題   で す

HYP: し か し   強 制   し   て   い   な く   て   も   問 題   で す

EVA:                                                   I
WER: 3.85%  







The sentence with the highest error rate is below:

REF: 幸 福   の   科 学   側   か ら   は   ,   特 に   ど う   し   て   ほ し い   と   い   う   要 望   は   い   た だ   い   て   い   ま   せ   ん   。

HYP: 幸 福   の   科 学   側   か ら   は   ,   特 に   ど う   し   て   ほ し い   と   い   う   要 望   は   い   た だ   い   て   い   ま   せ   ん   。

EVA:                                                                 D   I             D   I     I           D   I           I
WER: 14.04%
---------------------------------------



The sentence with the lowest error rate is below:

REF: そ う   だ っ   た ら   い い   な あ   と   は   思 い   ま す   が   ,   日 本   学 術   会 議   の   会 長   談   話   に   つ い   て   “   当 会   で   は   ,   標 記   の   件   に   つ い   て   ,   以 下   の   よ う   に   考 え   ま す   。   ”

HYP: そ う   だ っ   た ら   い い   な あ   と   は   思 い   ま す   が   ,   日 本   学 術   会 議   の   会 長   談   話   に   つ い   て   “   当 会   で   は   ,   標 記   の   件   に   つ い   て   ,   以 下   の   よ う   に   考 え   ま す   。   ”

EVA:                                                                                         I
                                       I
WER: 2.00%
---------------------------------------------




