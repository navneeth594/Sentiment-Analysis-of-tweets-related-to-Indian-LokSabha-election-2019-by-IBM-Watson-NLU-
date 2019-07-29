import pandas as pd
import csv

data = pd.read_csv('congress.csv', header=0)
data1=pd.read_csv('bjp.csv', header=0)
cc1=list(data1.text)
cc2=list(data1.sentiment)
col_a = list(data.text)
col_b=list(data.sentiment)
pos=0
neu=0
neg=0
for i in col_b:
	if i=='positive':
		pos=pos+1
	if i== 'negative':
		neg=neg+1
	if i=='neutral':
		neu=neu+1
print("CONGRESS\n")
print("positive :", pos)
print("negative :", neg)
print("neutral :", neu)

pos1=0
neu1=0
neg1=0

for i in cc2:
	if i=='positive':
		pos1=pos1+1
	if i== 'negative':
		neg1=neg1+1
	if i=='neutral':
		neu1=neu1+1
print('\n\n\n')
print("BJP\n")
print("positive :", pos1)
print("negative :", neg1)
print("neutral :", neu1)


import matplotlib
import matplotlib.pyplot as plt
import numpy as np


labels = ['CONGRESS','BJP']
men_means = [pos,pos1]
women_means = [neg,neg1]


x = np.arange(len(labels))  # the label locations
width = 0.25  # the width of the bars

fig, ax = plt.subplots()
rects1 = ax.bar(x - width/2, men_means, width, label='positivve')
rects2 = ax.bar(x + width/2, women_means, width, label='negative')


# Add some text for labels, title and custom x-axis tick labels, etc.
ax.set_ylabel('NUMBER OF TWEETS')
ax.set_title('TWEET ANALYSIS')
ax.set_xticks(x)
ax.set_xticklabels(labels)
ax.legend()


def autolabel(rects):
    """Attach a text label above each bar in *rects*, displaying its height."""
    for rect in rects:
        height = rect.get_height()
        ax.annotate('{}'.format(height),
                    xy=(rect.get_x() + rect.get_width() / 2, height),
                    xytext=(0, 3),  # 3 points vertical offset
                    textcoords="offset points",
                    ha='center', va='bottom')


autolabel(rects1)
autolabel(rects2)

fig.tight_layout()

plt.show()
