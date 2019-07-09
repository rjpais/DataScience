"""
Function to generate annotated heatmap like images with
Example of the probabilities of a given detected blood abnormalitie
"""
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import scipy


# Examples of blood abnormalities

X = ["Haemoglobinopathy", "alpha-Thalasemia", "beta-Thalasemia", "Pre-diabetes", "Diabetes"]
Y = ["Estimated", "Determined"]
DATA1 = np.array([[0, 0, 0.2, 0.1, 0],[0.1, 0.2, 0.0, 0.4, 0.8]] )
DATA2 = np.array([[0.5, 0, 1.0, 0.8, 0.6],[0.6, 0.2, 0.9, 0.8, 0.4]] )
DATA3 = np.array([[1, 0.7, 0.1, 0.4, 0.1],[0.2, 0.8, 0.5, 0.4, 0.3]] )


#--------------------------------------------------------------------
# Function that generates an annotated heatmap and saves it
#--------------------------------------------------------------------

def HeatmapPrint(X,Y, DATA, Path, Title ):
    # variables names
    # X -> the colums names, Y -> the rows names, DATA a list of lists with the data to plot
    # path -> the location path to save figure with name of figure
    # Title -> a string that describes what it stands for
    plt.close()
    fig, ax = plt.subplots()
    im = ax.imshow(DATA, cmap = "RdYlGn_r", vmin=0, vmax=1 )
    # Create colorbar
    cbar = ax.figure.colorbar(im, ax=ax, cmap = "RdYlGn_r")
    # We want to show all ticks...
    ax.set_xticks(np.arange(DATA.shape[1]))
    ax.set_yticks(np.arange(DATA.shape[0]))
    ax.set_xticklabels(X)
    ax.set_yticklabels(Y)
    # Turn spines off and create white grid.
    for edge, spine in ax.spines.items():
        spine.set_visible(False)
    ax.set_xticks(np.arange(DATA.shape[1]+1)-.5, minor=True)
    ax.set_yticks(np.arange(DATA.shape[0]+1)-.5, minor=True)
    ax.grid(which="minor", color="w", linestyle='-', linewidth=3)
    ax.tick_params(which="minor", bottom=False, left=False)
    # Let the horizontal axes labeling appear on top if we want do do this.
    #    ax.tick_params(top=True, bottom=False,
    #                   labeltop=True, labelbottom=False)
    # Rotate the tick labels and set their alignment.
    plt.setp(ax.get_xticklabels(), rotation = 45, ha="right",  rotation_mode="anchor")
    # Loop over data dimensions and create text annotations.
    for i in range(len(Y)):
        for j in range(len(X)):
            Valueij = str(round(DATA[i, j]*100, 0)) + " %"
            text = ax.text(j, i, Valueij, ha="center", va="center", color="k")
    ax.set_title(Title)
    fig.tight_layout()
    return fig.savefig(Path)
#--------------------------------------------------------------------


# Calling function to Print the 3 examples

EXAMPLES = [DATA1, DATA2, DATA3 ]

for n, data in enumerate(EXAMPLES):
    path = "example" + str(n+1)
    Title = "Probability of blood abnormalities" + path
    HeatmapPrint(X,Y, data, path, Title )
