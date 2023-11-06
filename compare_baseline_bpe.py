from nltk import

with open("assignments/03/baseline/translations.p.txt") as baseline, \
    open("assignments/03/bpe/translations.p.txt") as bpe, \
        open("data/en-fr/raw/test.en") as ref:
    for baseline_line, bpe_line, ref_line in zip(baseline, bpe, ref):
        baseline_line = baseline_line.replace("\n", "").split(" ")
        bpe_line = bpe_line.replace("\n", "").split(" ")
        ref_line = ref_line.replace("\n", "").split(" ")
        for word in bpe_line:
            if word in ref_line and word not in baseline_line:
                print(word)
                print(baseline_line)
                print(bpe_line)
                print(ref_line)
                print()