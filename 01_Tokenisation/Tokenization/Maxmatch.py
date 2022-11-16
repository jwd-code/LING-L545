import pyconll


train_path = 'C:\\Users\\Jerem\\Downloads\\UD_Japanese-GSD-master\\UD_Japanese-GSD-master\\ja_gsd-ud-train.conllu'
test_path = 'C:\\Users\\Jerem\\Documents\\Fall 2022\\L-545\\Practicals\\maxmatch\\testfile.txt'
output_path = 'C:\\Users\\Jerem\\Documents\\Fall 2022\\L-545\\Practicals\\maxmatch\\hypothesis.txt'

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


def create_hyp(test_file, output_path):
    hyp_file = open(output_path, 'a', encoding='utf-8')
    for num, line in enumerate(test_file):
        sent = (maxmatch(line, sorted_dict))
        # new_sent = [x for x in sent if x != '\n']
        new_sent = ' '.join(sent)
        print(num+1, new_sent)
        hyp_file.write(new_sent)

    hyp_file.close()
    print("DONE")


create_hyp(test_file=test_file, output_path=output_path)

