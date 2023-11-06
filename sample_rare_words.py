from string import punctuation

in_dict = set()
not_in_dict = 0
accuracy = 0

with open("data/en-fr/prepared/dict.en", "r", encoding="utf-8") as dict_file:
    for line in dict_file:
        word, freq = line.replace("\n", "").lower().split(" ")
        freq = int(freq)
        if freq < 50:
            break
        in_dict.add(word)

with open("data/en-fr/raw/test.en", "r", encoding="utf-8") as test, \
        open("assignments/03/bpe/translations.p.txt", "r", encoding="utf-8") as hyp:
    for line_test, line_hyp in zip(test, hyp):
        words_test = line_test.replace("\n", "").lower().translate(str.maketrans('', '', punctuation)).split(" ")
        words_hyp = line_hyp.replace("\n", "").lower().translate(str.maketrans('', '', punctuation)).split(" ")
        for word in words_test:
            if word not in in_dict:
                not_in_dict += 1
                if word in words_hyp:
                    print(word)
                    print(words_hyp)
                    accuracy += 1

print(accuracy/not_in_dict)
