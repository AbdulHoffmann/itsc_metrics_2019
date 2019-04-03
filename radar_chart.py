# Libraries
import matplotlib
import matplotlib.pyplot as plt
import pandas as pd
from math import pi
import collections

def radar_chart(df):
    # ------- PART 1: Create background
    # font = {
    #     'family' : 'normal',
    #     'size'   : 14
    #     }

    # plt.rc('font', **font)

    # number of variable
    groups = list(df.iloc[:,0])
    categories=list(df)[1:]
    N = len(categories)
    
    # What will be the angle of each axis in the plot? (we divide the plot / number of variable)
    angles = [n / float(N) * 2 * pi for n in range(N)]
    angles += angles[:1]
    
    # Initialise the spider plot
    ax = plt.subplot(111, polar=True)
    
    # If you want the first axis to be on top:
    ax.set_theta_offset(pi / 2)
    ax.set_theta_direction(-1)
    
    # Draw one axe per variable + add labels labels yet
    plt.xticks(angles[:-1], categories, size=16)

    # Custom for positioning tick labels
    for idx, item in enumerate(ax.get_xticklabels()):
        if idx == 0:
            item.set_position((0,-.0525))
        elif idx == 1:
            item.set_position((0,-.08))
        elif idx == 2:
            item.set_position((0,-.08))
        elif idx == 3:
            item.set_position((0,-.025))
        elif idx == 4:
            item.set_position((0,-.06))


    # Draw ylabels
    ax.set_rlabel_position(0)
    ax.grid(color='#444444')
    plt.yticks([0, .25,.5,.75, 1], ["0","0.25","0.50","0.75", "1"], color="#323231", size=13)
    plt.ylim(0,1)

    
    # ------- PART 2: Add plots
    
    # Plot each individual = each line of the data
    # I don't do a loop, because plotting more than 3 groups makes the chart unreadable

    for idx, individual in enumerate(groups):
        values=df.loc[idx].drop('group').values.flatten().tolist()
        values += values[:1]
        ax.plot(angles, values, linewidth=1, linestyle='solid', label=individual)
        ax.fill(angles, values, 'b', alpha=0.1)

    # Add legend
    # plt.legend(loc='best', bbox_to_anchor=(0.1, 0.1))