import pyconll

train_path = 'C:\\Users\\Jerem\\Downloads\\UD_Japanese-GSD-master\\UD_Japanese-GSD-master\\ja_gsd-ud-train.conllu'
test_path = 'C:\\Users\\Jerem\\Documents\\Fall 2022\\L-545\\Practicals\\maxmatch\\testfile.txt'

corpus = pyconll.iter_from_file(train_path)

dictionary = []
for sentence in corpus:
    for token in sentence:
        dictionary.append(token.form)

sorted_dict = sorted(dictionary, key=len, reverse=True)




test_file = open(test_path, 'r', encoding='utf-8')


def maxmatch(sentence, dictionary):
    if len(sentence) == 0:
        return []
    for i in range(len(sentence), 1, -1):
        first_word = sentence[:i]
        remainder = sentence[i:]
        if first_word in sorted_dict:
            first_word = [first_word]
            return list(first_word) + maxmatch(remainder, dictionary)
            # return [first_word + [maxmatch(remainder, dictionary)]]
    first_word = sentence[:1]
    remainder = sentence[1:]
    first_word = [first_word]

    return list(first_word) + maxmatch(remainder, dictionary)

for line in test_file:
    x = (maxmatch(line, sorted_dict))
    print(x)

print('DONE')