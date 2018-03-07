__author__ = 'Lynn'
__email__ = 'lynnn.hong@gmail.com'
__date__ = '2/27/2018'

import os
import time
import logging
from pprint import pprint

import pymysql
import configparser
from dateutil.parser import parse
import facebook


class Facebook_crawler():
    # represent mysql connector

    def __init__(self, client_file):
        os.environ['TZ'] = 'Asia/Seoul'
        time.tzset()
        self.client_file = client_file
        self.connect_db()
        self.graph = facebook.GraphAPI(access_token="338938349924993|BlDmbQBsIcfZzse96Y19v6JcNx0",
                                       version="2.11")
        self.group_id_list = ['thepsybus']
        self.event_sql = "INSERT INTO event(id, e_title_kor, start_time, end_time, location, e_desc_kor) " \
                         "VALUE(%s, %s, %s, %s, %s, %s);"

    def connect_db(self, autocommit=True):
        logging.info("start reading config file")
        config = configparser.ConfigParser()
        config.read(self.client_file)
        host = config.get('client', 'host')
        database = config.get('client', 'database')
        user = config.get('client', 'user')
        password = config.get('client', 'password')
        encoding = config.get('client', 'default-character-set')
        logging.info("try to connect to project db")
        self.con = pymysql.connect(host=host, db=database,
                                   user=user, passwd=password, charset=encoding)
        self.cur = self.con.cursor()
        if autocommit is True:
            self.con.autocommit(True)       # turn-on autocummit, be careful!
        logging.info("Connected")

    def insert_mysql(self, sql, val_tuple):
        try:
            self.cur.execute(sql, val_tuple)
        except pymysql.Error as e:
            logging.critical(e)

    def get_fb_event(self):
        for group_id in self.group_id_list:
            # Get the message from a post.
            post = self.graph.get_object(id=group_id, fields='events',
                                         after="QVFIUkM2cUZArbjh0cU1tMnFuVS1GUlY5WmpBRENmY2NYejUtN2lHdVZATbjRvVFhRcWpfOXM0LTJHVnlEUFo3Vkw2WnUyaDlSaEtkb1Rhd1J1YzlzZAVJIUXBR")
            pprint(post['events']['paging'])
            for data in post['events']['data']:
                id = "{}_{}".format(group_id, data['id'])
                e_title_kor = data['name']
                start_time = parse(data['start_time']).strftime('%Y-%m-%d %H:%M:%S')
                end_time = parse(data['end_time']).strftime('%Y-%m-%d %H:%M:%S')
                location = data['place']['name']
                e_desc_kor = data['description']
                val_tuple = (id, e_title_kor, start_time, end_time, location, e_desc_kor)
                self.insert_mysql(self.event_sql, val_tuple)
            logging.info("Inserted")
            #break

if __name__ == "__main__":
    mysql_file = "/home/lynn/workspace/django/kcd2018/kcd2018/mysql.cnf"
    fc = Facebook_crawler(mysql_file)
    fc.connect_db()
    fc.get_fb_event()
