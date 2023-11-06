from sys import argv
import re
import seaborn as sns
from matplotlib import pyplot as plt

base = argv[1]
lr_5 = argv[2]
lr_7 = argv[3]
files = {'Baseline (Learning Rate 0.0003)': base, 'Learning Rate 0.0005': lr_5, 'Learning Rate 0.0007': lr_7}


valid_losses = {}
ppls = {}

for name, file in files.items():
    with open(file, "r", encoding="utf-8") as ofile:
        valid_loss = []
        ppl = []
        for line in ofile:
            if re.search(r'valid_loss \d+\.?\d+', line):
                valid_loss.append(float(re.search(r'valid_loss (\d+\.?\d+)', line).group(1)))
                ppl.append(float(re.search(r'valid_perplexity\s+(\d+\.?\d+)', line).group(1)))
        valid_losses[name] = valid_loss
        ppls[name] = ppl

ax = sns.lineplot(data=valid_losses)
ax.set(xlabel="Epochs", ylabel="Validation Loss", title="Validation Loss for different Learning Rates")
plt.savefig("assignments/03/valid_loss_plot.pdf")
plt.close()

ax = sns.lineplot(data=ppls)
ax.set(xlabel="Epochs", ylabel="Validation Perplexity", title="Validation Perplexity for different Learning Rates")
plt.savefig("assignments/03/ppl_plot.pdf")
plt.close()
