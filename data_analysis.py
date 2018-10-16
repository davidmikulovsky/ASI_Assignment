import sqlite3
import requests


def get_ips(db_path, ips):
    conn = sqlite3.connect(db_path)
    c = conn.cursor()
    cursor = c.execute("SELECT IP FROM pytomo_crawl_2018_10_16_04_41_53")
    for each in cursor:
        print(each)
        res = requests.get('http://ip-api.com/json/' + each[0])
        ips.append(res.json())
        print(res.json())

if __name__ == '__main__':
    db_path = './databases/host.localdomain.youtube.2018-10-16.04_41_53.pytomo_database.db'
    ips = []
    get_ips(db_path, ips)
