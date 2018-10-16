import sqlite3
import requests


def get_ips(db_path, ips, time_stamp):
    conn = sqlite3.connect(db_path)
    c = conn.cursor()
    cursor = c.execute("SELECT IP FROM pytomo_crawl_+")
    for each in cursor:
        print(each)
        res = requests.get('http://ip-api.com/json/' + each[0])
        ips.append(res.json())
        print(res.json())

if __name__ == '__main__':
    db_path = './databases/DingdeMacBook-Pro.local.youtube.2018-10-16.10_21_56.pytomo_database.db'
    ips = []
    get_ips(db_path, ips)
