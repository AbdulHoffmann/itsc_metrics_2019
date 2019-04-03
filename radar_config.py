import pandas as pd
import collections
import json

def set_config ():
    selected_df = df_fog_long  # choose selected scenario
    save = True  # save all images or display $selected_df
    return (selected_df, save)


'''Day'''

'''Longitudinal'''
df_day_long = pd.DataFrame(collections.OrderedDict([
('group', ['Test Hall','CarMaker','VTD']),
('$Precision$', [0.9397, 0.8766, 0.89635]),
('$Recall$', [0.8962, 0.8942, 0.88595]),
(r'$1-FFPI_N$', [0.9378, 0.8190, 0.8590]),
('$MOTA_N$', [0.9782, 0.9586, 0.96405]),
('$MOTP$', [0.8340, 0.811, 0.8058]),
]))

'''Lateral'''
df_day_lat = pd.DataFrame(collections.OrderedDict([
('group', ['Test Hall','CarMaker','VTD']),
('$Precision$', [0.5066, 0.5369, 0.57505]),
('$Recall$', [0.73795, 0.5975, 0.54845]),
(r'$1-FFPI_N$', [0.6293, 0.8048, 0.8299]),
('$MOTA_N$', [0.75255, 0.79165, 0.77145]),
('$MOTP$', [0.80415, 0.8301, 0.7411]),
]))


'''Night'''

'''Longitudinal'''
df_night_long = pd.DataFrame(collections.OrderedDict([
('group', ['Test Hall','CarMaker','VTD']),
('$Precision$', [0.67635, 0.83755, 0.84165]),
('$Recall$', [0.56475, 0.7163, 0.60775]),
(r'$1-FFPI_N$', [0.6240, 0.7795, 0.8492]),
('$MOTA_N$', [0.83015, 0.90525, 0.88365]),
('$MOTP$', [0.7896, 0.7937, 0.73935]),
]))

'''Lateral'''
df_night_lat = pd.DataFrame(collections.OrderedDict([
('group', ['Test Hall','CarMaker','VTD']),
('$Precision$', [0.3779, 0.6881, 0.75545]),
('$Recall$', [0.4347, 0.4442, 0.6097]),
(r'$1-FFPI_N$', [0.6932, 0.9089, 0.9341]),
('$MOTA_N$', [0.7116, 0.81955, 0.86125]),
('$MOTP$', [0.69635, 0.8635, 0.83535]),
]))


'''Fog'''

'''Longitudinal'''
df_fog_long = pd.DataFrame(collections.OrderedDict([
('group', ['Test Hall','CarMaker','VTD']),
('$Precision$', [0.7883, 0.89275, 0.8453]),
('$Recall$', [0.48355, 0.42975, 0.67145]),
(r'$1-FFPI_N$', [0.8049, 0.9575, 0.8904]),
('$MOTA_N$', [0.84475, 0.8511, 0.8981]),
('$MOTP$', [0.84325, 0.8569, 0.8341]),
]))

'''Lateral'''
df_fog_lat = pd.DataFrame(collections.OrderedDict([
('group', ['Test Hall','CarMaker','VTD']),
('$Precision$', [0.6557, 0.6598, 0.40805]),
('$Recall$', [0.54965, 0.57075, 0.4502]),
(r'$1-FFPI_N$', [0.9037, 0.8929, 0.8744]),
('$MOTA_N$', [0.83515, 0.83375, 0.78985]),
('$MOTP$', [0.7167, 0.8072, 0.786]),
]))


'''Rain'''

'''Longitudinal'''
df_rain_long = pd.DataFrame(collections.OrderedDict([
('group', ['Test Hall','CarMaker','VTD']),
('$Precision$', [0.7174, 0.49885, 0.8307]),
('$Recall$', [0.46905, 0.52275, 0.68535]),
(r'$1-FFPI_N$', [0.6982, 0.2235, 0.8011]),
('$MOTA_N$', [0.8247, 0.7391, 0.89765]),
('$MOTP$', [0.77345, 0.76205, 0.78775]),
]))

'''Lateral'''
df_rain_lat = pd.DataFrame(collections.OrderedDict([
('group', ['Test Hall','CarMaker','VTD']),
('$Precision$', [0.55935, 0.12685, 0.3289]),
('$Recall$', [0.4103, 0.22985, 0.38065]),
(r'$1-FFPI_N$', [0.8858, 0.2469, 0.7457]),
('$MOTA_N$', [0.7587, 0.2675, 0.7256]),
('$MOTP$', [0.6747, 0.6528, 0.7424]),
]))

df_dict = {
    'df_day_long': df_day_long, 'df_day_lat': df_day_lat, 
    'df_night_long': df_night_long, 'df_night_lat': df_night_lat,
    'df_fog_long': df_fog_long, 'df_fog_lat': df_fog_lat,
    'df_rain_long': df_rain_long, 'df_rain_lat':df_rain_lat
    }
df, save_radar = set_config()
