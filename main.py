
import plotly.plotly as py
import plotly.graph_objs as go

import plotly


plotly.tools.set_credentials_file(username='david.miku', api_key='6ypMWtmqzdzXbQwAzS6b')
plotly.tools.set_config_file(world_readable=True, sharing='public')
mapbox_access_token = 'pk.eyJ1IjoiZGF2aWRtaWt1bG92c2t5IiwiYSI6ImNqbmJwM3Z3NjAzM3Qzdm51NWVicG9vcnkifQ.5Xfyd1tTznVFRJm-Fsp4zQ'

def map_function(infos):
    lat=[]
    lon=[]
    url=[]

    for each in infos:
        lat.append(str(each.lat))
        lon.append(str(each.lon))
        url.append(str(each.url))


    lat.append(str(34.0584))
    lon.append(str(-118.278))
    url.append('Client')
    print len(lat)

    data = [
        go.Scattermapbox(
            lat = lat,
            lon = lon,
            mode='markers+text',
            marker=dict(
                size=len(url)
            ),
            text=url,
        )
    ]

    layout = go.Layout(
        autosize=True,
        hovermode='closest',
        mapbox=dict(
            accesstoken=mapbox_access_token,
            bearing=0,
            center=dict(
                lat=38.92,
                lon=-77.07
            ),
            pitch=0,
            zoom=10
        ),
    )

    fig = dict(data=data, layout=layout)
    py.plot(fig, filename='Multiple Mapbox')

#
# def map_function():
#
#     data = [
#         go.Scattermapbox(
#             lat=['38.91427','38.91538','38.91458',],
#             lon=['-77.02827','-77.02013','-77.03155'],
#             mode='markers',
#             marker=dict(
#                 size=14
#             ),
#             text=["The coffee bar","Bistro Bohem","Black Cat"]
#         )
#     ]
#
#     layout = go.Layout(
#         autosize=True,
#         hovermode='closest',
#         mapbox=dict(
#             accesstoken=mapbox_access_token,
#             bearing=0,
#             center=dict(
#                 lat=45,
#                 lon=-73
#             ),
#             pitch=0,
#             zoom=3
#         ),
#     )
#
#     fig = dict(data=data, layout=layout)
#     #f1 = plotly.offline.plot(fig, filename= 'map.html')
#     py.plot(fig, filename='Montreal Mapbox')
#
