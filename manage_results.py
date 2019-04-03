import os
from radar_chart import radar_chart
from bars import bars_plot
import matplotlib.pyplot as plt

from radar_config import df_dict, save_radar, df
from bars_config import save_bars, real, carmaker, vtd, bar_dict

def assure_path_exists(path):
    if not os.path.exists(path):
        os.makedirs(path)

def run_radar():
    global df, df_dict
    if save_radar:
        path_to_dir = os.path.join(os.environ['HOME'], 'Desktop', 'radar charts')
        assure_path_exists(path_to_dir)
        for filename, df in df_dict.items():
            radar_chart(df)
            plt.savefig(os.path.join(path_to_dir,'%s.png') % filename, bbox_inches='tight', dpi=300)
            plt.close()
    else:
        radar_chart(df)
        plt.show()

def run_bars():
    if save_bars:
        path_to_dir = os.path.join(os.environ['HOME'], 'Desktop', 'bar charts')
        assure_path_exists(path_to_dir)
        for filename, content in bar_dict.items():
            bars_plot(*content)
            plt.savefig(os.path.join(path_to_dir,'%s.png') % filename, bbox_inches='tight', dpi=300)
            plt.close()
    else:
        bars_plot(real, carmaker, vtd)
        plt.show()

# Run either run_bars() or run_radar()
run_radar()