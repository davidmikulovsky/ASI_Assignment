import sqlite3
import requests
from main import map_function

class VidoeInfo:
    def __init__(self, ip, url, ping, lat, lon):
        self.ip = ip
        self.url = url
        self.ping_avg = ping
        self.lat = lat
        self.lon = lon


def get_ips(db_path, ips):
    conn = sqlite3.connect(db_path)
    c = conn.cursor()
    cursor = c.execute("SELECT IP FROM pytomo_crawl_2018_10_16_13_49_49")
    for each in cursor:
        #print(each)
        res = requests.get('http://ip-api.com/json/' + each[0])
        ips.append(res.json())


def get_info(db_path, infos):
    conn = sqlite3.connect(db_path)
    c = conn.cursor()
    date =  db_path.split('.')[4].replace('-', '_')
    time = db_path.split('.')[5]
    db_path.split('.')[5]
    cursor = c.execute("SELECT Url, PingAvg, IP FROM pytomo_crawl_"+ date +"_"+time)
    for each in cursor:
        res = requests.get('http://ip-api.com/json/' + each[2])
        infos.append(VidoeInfo(each[2], each[0], each[1], res.json()['lat'], res.json()['lon']))

def get_delays(db_path, delays):
    conn = sqlite3.connect(db_path)
    c = conn.cursor()
    cursor = c.execute("SELECT PingAvg FROM pytomo_crawl_2018_10_16_13_49_49")
    for each in cursor:
        delays.append(each[0])

if __name__ == '__main__':
    db_path = './databases/host.localdomain.youtube.2018-10-17.12_26_40.pytomo_database.db'
    ip_json = []
    infos = []
    get_info(db_path, infos)
    for each in infos:
        pass
        #print each.url, each.ip, each.ping_avg, each.lat, each.lon

    map_function(infos)

