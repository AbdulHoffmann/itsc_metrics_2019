import numpy as np
import matplotlib.pyplot as plt

def bars_plot(real, carmaker, vtd):
    plt.style.use('seaborn')
    n_groups = 4
    fig, ax = plt.subplots()
    index = np.arange(n_groups)
    bar_width = .225
    offset = .025
    opacity = 0.85

    rects1 = ax.bar(index, real, bar_width,
                    alpha=opacity, color='#30A2DA',
                    label='Test Hall')

    rects2 = ax.bar(index + bar_width + offset, carmaker, bar_width,
                    alpha=opacity, color='#FC4F30',
                    label='CarMaker')

    rects3 = ax.bar(index + 2*bar_width + 2*offset, vtd, bar_width,
                    alpha=opacity, color='#E5AE38',
                    label='VTD')

    # ax.set_xlabel('Group')
    ax.set_ylabel('F1 Score')
    ax.set_title('Score by Class')
    ax.set_xticks(index + bar_width)
    ax.set_xticklabels(('Bicycle', 'Car', 'Pedestrian', 'TLight'))
    ax.legend()

    fig.tight_layout()
