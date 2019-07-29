import pandas as pd
import csv
data = pd.read_csv('namo.csv', header=0)
namo=len(list(data.sadness))
l1=(sum(list(data.sadness)))/namo
l2=(sum(list(data.joy)))/namo
l3=(sum(list(data.fear)))/namo
l4=(sum(list(data.disgust)))/namo
l5=(sum(list(data.anger)))/namo
print(l1)

data1=pd.read_csv('rahul.csv',header=0)
pappu=len(list(data1.sadness))
n1=(sum(list(data1.sadness)))/pappu
n2=(sum(list(data1.joy)))/pappu
n3=(sum(list(data1.fear)))/pappu
n4=(sum(list(data1.disgust)))/pappu
n5=(sum(list(data1.anger)))/pappu
print(n1)

import numpy as np
import matplotlib.pyplot as plt
 
# width of the bars
barWidth = 0.3
 
# Choose the height of the blue bars
bars1 = [l1, l2, l3,l4,l5]
 
# Choose the height of the cyan bars
bars2 = [n1,n2,n3,n4,n5]
 
# Choose the height of the error bars (bars1)
#yer1 = [0.5, 0.4, 0.5]
 
# Choose the height of the error bars (bars2)
#yer2 = [1, 0.7, 1]
 
# The x position of bars
r1 = np.arange(len(bars1))
r2 = [x + barWidth for x in r1]
 
# Create blue bars
plt.bar(r1, bars1, width = barWidth, color = 'blue', edgecolor = 'black', capsize=7, label='modi')
 
# Create cyan bars
plt.bar(r2, bars2, width = barWidth, color = 'yellow', edgecolor = 'black',  capsize=7, label='rahul')
 
# general layout
plt.xticks([r + barWidth for r in range(len(bars1))], ['sadness','joy','fear','disgust','anger'])
plt.ylabel('scores')
plt.legend()
 
# Show graphic
plt.show()
