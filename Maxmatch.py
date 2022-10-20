import pyconll

path = 'C:\\Users\\Jerem\\Downloads\\UD_Japanese-GSD-master\\UD_Japanese-GSD-master\\ja_gsd-ud-train.conllu'

corpus = pyconll.iter_from_file(path)


dictionary = []
for sentence in corpus:
    for token in sentence:
        dictionary.append(token.form)


sorted_dict = sorted(dictionary, key=len, reverse=True)

print(sorted_dict[:10])

def maxmatch(sentence, dictionary):
    if len(sentence) == 0:
        return []
    for i in range(len(sentence), 1, -1):
        first_word = sentence[:i]
        remainder = sentence[i:]
        if first_word in sorted_dict:
            return (list(first_word, maxmatch(remainder, dictionary)))

    first_word = sentence[:1]
    remainder = sentence[1:]

    return list(first_word, maxmatch(remainder, dictionary))
