import pandas as pd
import folium
state = folium.Map(location=[35.843861, 127.140127], zoom_start=17, tiles='Stamen toner')
state
state.save('C:/Users/home/PycharmProjects/untitled/map1.html')