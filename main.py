
import plotly.plotly as py
import plotly.graph_objs as go

import plotly


plotly.tools.set_credentials_file(username='david.miku', api_key='6ypMWtmqzdzXbQwAzS6b')

plotly.tools.set_config_file(world_readable=True, sharing='public')

mapbox_access_token = 'pk.eyJ1IjoiZGF2aWRtaWt1bG92c2t5IiwiYSI6ImNqbmJwM3Z3NjAzM3Qzdm51NWVicG9vcnkifQ.5Xfyd1tTznVFRJm-Fsp4zQ'


data = [
    go.Scattermapbox(
        lat=['45.5017'],
        lon=['-73.5673'],
        mode='markers',
        marker=dict(
            size=14
        ),
        text=['Montreal'],
    )
]

layout = go.Layout(
    autosize=True,
    hovermode='closest',
    mapbox=dict(
        accesstoken=mapbox_access_token,
        bearing=0,
        center=dict(
            lat=45,
            lon=-73
        ),
        pitch=0,
        zoom=3
    ),
)

fig = dict(data=data, layout=layout)


#f1 = plotly.offline.plot(fig, filename= 'map.html')



py.plot(fig, filename='Montreal Mapbox')

