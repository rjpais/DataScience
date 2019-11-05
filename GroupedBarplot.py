# Example of a grouped bar chart 

import matplotlib
import matplotlib.pyplot as plt
import numpy as np


    
# use a predifined style of plots ( this case ggplots from R)
plt.style.use('ggplot')

labels = ['Central', 'Lat Esq', 'Lat Dr', 'Pivot', 'Ponta Esq','Ponta Dr' ]
Team1 = [5, 6, 9, 3, 4, 1]
Team2 = [3, 7, 3, 5, 2, 2]

x = np.arange(len(labels))  # the label locations
width = 0.35  # the width of the bars

fig, ax = plt.subplots()
rects1 = ax.bar(x - width/2, Team1, width, label='Team 1')
rects2 = ax.bar(x + width/2, Team2, width, label='Team 2')

# Add some text for labels, title and custom x-axis tick labels, etc.
ax.set_ylabel('Goals')
ax.set_title('Players scores of team 1 and 2')
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
