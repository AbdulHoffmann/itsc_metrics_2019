def set_config ():
    selected_set = day_long  # choose selected scenario
    save = False  # save all images or display $selected_df
    return (selected_set, save)


# Order of classes: Bicycle, Car, Pedestrian, Tlight

'''Day'''

'''Longitudinal'''
real_day_long     = (0.8606, 0.7188, 0.9717, 0.9535)
carmaker_day_long = ( 0.8473, 0.8825, 0.8993, 0.9192)
vtd_day_long      = (0.6413, 0.9092, 0.8799, 0.9167)

day_long = (real_day_long, carmaker_day_long, vtd_day_long)

'''Lateral'''
real_day_lat      = (0.6710, 0.5467, 0.8460, 0.0000)
carmaker_day_lat = (0.0364, 0.7761, 0.6809, 0.0602)
vtd_day_lat     = (0.0000, 0.5422, 0.1189, 0.0000)

day_lat = (real_day_lat, carmaker_day_lat, vtd_day_lat)

'''Night'''

'''Longitudinal'''
real_night_long     = (0.9118, 0.6403, 0.4765, 0.0000)
carmaker_night_long = (0.7269, 0.8688, 0.7114, 0.5166)
vtd_night_long      = (0.5385, 0.6760, 0.7760, 0.9490)

night_long = (real_night_long, carmaker_night_long, vtd_night_long)

'''Lateral'''
real_night_lat      = (0.2886, 0.6164, 0.2228, 0.0000)
carmaker_night_lat = (0.0069, 0.7258, 0.7039, 0.0000)
vtd_night_lat     = (0.0000, 0.8205, 0.7856, 0.0000)

night_lat = (real_night_lat, carmaker_night_lat, vtd_night_lat)

'''Fog'''

'''Longitudinal'''
real_fog_long     = (0.3575, 0.6526, 0.7795, 0.1435)
carmaker_fog_long = (0.5685, 0.6604, 0.4061, 0.2636)
vtd_fog_long      = (0.6132, 0.8023, 0.6656, 0.4022)

fog_long = (real_fog_long, carmaker_fog_long, vtd_fog_long)

'''Lateral'''
real_fog_lat      = (0.6400, 0.8453, 0.3855, 0.0000)
carmaker_fog_lat = (0.0214, 0.8054, 0.7805, 0.0556)
vtd_fog_lat     = (0.0000, 0.7561, 0.0845, 0.0000)

fog_lat = (real_fog_lat, carmaker_fog_lat, vtd_fog_lat)

'''Rain'''

'''Longitudinal'''
real_rain_long     = (0.3164, 0.6132, 0.5684, 0.4916,)
carmaker_rain_long = (0.3746, 0.5994, 0.4356, 0.1721,)
vtd_rain_long      = (0.1168, 0.7453, 0.8744, 0.9189,)

rain_long = (real_rain_long, carmaker_rain_long, vtd_rain_long)

'''Lateral'''
real_rain_lat      = (0.9395, 0.5574, 0.1400, 0.0000)
carmaker_rain_lat  = (0.4575, 0.0632, 0.3303, 0.0000)
vtd_rain_lat       = (0.0000, 0.4580, 0.0274, 0.0231)

rain_lat = (real_rain_lat, carmaker_rain_lat, vtd_rain_lat)

bar_dict = {
    'day_long' : day_long,
    'day_lat' : day_lat,
    'night_long' : night_long,
    'night_lat' : night_lat,
    'fog_long' : fog_long,
    'fog_lat' : fog_lat,
    'rain_long' : rain_long,
    'rain_lat' : rain_lat,
}

(real, carmaker, vtd), save_bars = set_config()
