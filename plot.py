import seaborn as sns
from matplotlib import pyplot as plt

beam = [1, 5, 10, 15, 20, 25]
bleu = [17.1, 20, 22.2, 22.1, 21.8, 21.4]
time = [15, 41, 94, 175, 291, 472]
brevity_penalty = [1, 1, 1, 0.949, 0.864, 0.790]

# Create figure and axis #1
fig, ax1 = plt.subplots(figsize=(9, 9))
ax1.set_title("BLEU Score and Brevity Penalty with different Beam Sizes", pad=30)
ax1.title.set_size(20)

# plot line chart on axis #1
p1, = ax1.plot(beam, bleu)
ax1.set_ylabel("BLEU Score")
ax1.set_xlabel("Beam Size")
ax1.set_ylim(17, 23)
ax1.set_xlim(1, 25)
ax1.legend(["BLEU Score"], loc="upper left")
ax1.yaxis.label.set_color(p1.get_color())
ax1.yaxis.label.set_fontsize(14)
ax1.xaxis.label.set_fontsize(14)
ax1.tick_params(axis='y', colors=p1.get_color(), labelsize=14)

# set up the 2nd axis
ax2 = ax1.twinx()
# plot bar chart on axis #2
p2, = ax2.plot(beam, brevity_penalty, color="red")
ax2.grid(False) # turn off grid #2
ax2.set_ylabel("Brevity Penalty")
ax2.set_ylim(0.79, 1)
ax2.legend(["Brevity Penalty"], loc="upper right")
ax2.yaxis.label.set_color(p2.get_color())
ax2.yaxis.label.set_fontsize(14)
ax2.tick_params(axis='y', colors=p2.get_color(), labelsize=14)
plt.savefig("assignments/05/bleu_plot.pdf")
plt.close()

fig3, ax3 = plt.subplots(figsize=(9, 9))
ax3.set_title("Decoding Time for different Beam Sizes", pad=30)
ax3.title.set_size(20)

# plot line chart on axis #1
p1, = ax3.plot(beam, time)
ax3.set_ylabel("Time in Seconds")
ax3.set_xlabel("Beam Size")
ax3.set_ylim(15, 500)
ax3.set_xlim(1, 25)
ax3.yaxis.label.set_color(p1.get_color())
ax3.yaxis.label.set_fontsize(14)
ax3.xaxis.label.set_fontsize(14)
ax3.tick_params(axis='y', colors=p1.get_color(), labelsize=14)
plt.savefig("assignments/05/time_plot.pdf")
plt.close()
