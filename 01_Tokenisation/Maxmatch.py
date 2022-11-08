import pyconll

path = "C:\\Users\\Jerem\\Desktop\\maxmatch\\ja_gsd-ud-train.conllu"

corpus = pyconll.iter_from_file(path)

for sentence in corpus:
    print(sentence)




# dictionary = []
# for sentence in corpus:
#     for token in sentence:
#         dictionary.append(token.form)

# sorted_dict = sorted(dictionary, key=len, reverse=True)

# training_dict = open('training_dict.txt', 'w', encoding='utf-8')

# for sent in sorted_dict:
#     training_dict.write(sent)
#     training_dict.write('\n')
# training_dict.close()


# def maxmatch(sentence, dictionary):
#     if len(sentence) == 0:
#         return []
#     for i in range(len(sentence), 1, -1):
#         first_word = sentence[:i]
#         remainder = sentence[i:]
#         if first_word in sorted_dict:
#             return (list(first_word, maxmatch(remainder, dictionary)))
#     first_word = sentence[:1]
#     remainder = sentence[1:]
#     return list(first_word, maxmatch(remainder, dictionary))
