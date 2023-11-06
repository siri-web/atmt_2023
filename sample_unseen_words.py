from string import punctuation

seen = set()
unseen = 0
accuracy = 0

with open("data/en-fr/raw/train.en", "r", encoding="utf-8") as training:
    for line in training:
        words = line.replace("\n", "").lower().translate(str.maketrans('', '', punctuation)).split(" ")
        for word in words:
            seen.add(word)

with open("data/en-fr/raw/test.en", "r", encoding="utf-8") as test, \
        open("assignments/03/bpe/translations_decoded.txt", "r", encoding="utf-8") as hyp:
    for line_test, line_hyp in zip(test, hyp):
        words_test = line_test.replace("\n", "").lower().translate(str.maketrans('', '', punctuation)).split(" ")
        words_hyp = line_hyp.replace("\n", "").lower().translate(str.maketrans('', '', punctuation)).split(" ")
        for word in words_test:
            if word not in seen:
                unseen += 1
                print(word)
                print(words_hyp)
                if word in words_hyp:
                    accuracy += 1

print(accuracy/unseen)
