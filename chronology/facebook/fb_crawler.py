__author__ = 'Lynn'
__email__ = 'lynnn.hong@gmail.com'
__date__ = '2/27/2018'

import os, sys
import time
from datetime import datetime, timedelta
import requests
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
        self.access_token = "338938349924993|BlDmbQBsIcfZzse96Y19v6JcNx0"
        self.graph = facebook.GraphAPI(access_token=self.access_token,
                                       version="2.11")
        self.group_id_list = ['thepsybus', 'biospintalk']
        self.event_sql = "REPLACE INTO event(id, e_title_kor, start_time, end_time, location, e_desc_kor) " \
                         "VALUE(%s, %s, %s, %s, %s, %s);"
        self.profile_pic_sql = "INSERT INTO manager(profile_pic) " \
                         "VALUE(%s);"
        self.now = datetime.now()

    def connect_db(self, autocommit=True):
        logging.info("start reading config file")
        config = configparser.ConfigParser()
        config.read(self.client_file)
        host = config.get('client', 'host')
        database = config.get('client', 'database')
        user = config.get('client', 'user')
        password = config.get('client', 'password')
        encoding = config.get('client', 'default-character-set')
        print("Try to connect to project db")
        self.con = pymysql.connect(host=host, db=database,
                                   user=user, passwd=password, charset=encoding)
        self.cur = self.con.cursor()
        if autocommit is True:
            self.con.autocommit(True)       # turn-on autocummit, be careful!
        print("Connected")

    def insert_mysql(self, sql, val_tuple):
        try:
            self.cur.execute(sql, val_tuple)
        except pymysql.Error as e:
            logging.critical(e)

    def get_fb_event(self):
        for group_id in self.group_id_list:
            # Get the message from a post.
            post = self.graph.get_object(id=group_id, fields='events')['events']
            page = 0
            stop = False
            while True:
                page += 1
                if page % 10 == 0:
                    logging.info(page)
                for data in post['data']:
                    id = "{}_{}".format(group_id, data['id'])
                    e_title_kor = data['name']
                    start_time = parse(data['start_time']).strftime('%Y-%m-%d %H:%M:%S')
                    if self.now > datetime.strptime(start_time, '%Y-%m-%d %H:%M:%S'):
                        print("Stop fetch events.")
                        stop = True
                        break
                    try:
                        end_time = parse(data['end_time']).strftime('%Y-%m-%d %H:%M:%S')
                    except KeyError:
                        end_time = datetime.strptime(start_time, '%Y-%m-%d %H:%M:%S') + timedelta(hours=2)
                    try:
                        location = data['place']['name']
                    except KeyError:
                        location = "본문 참조"
                    try:
                        e_desc_kor = data['description']
                    except KeyError:
                        e_desc_kor = "(내용 없음)"
                    val_tuple = (id, e_title_kor, start_time, end_time, location, e_desc_kor)
                    self.insert_mysql(self.event_sql, val_tuple)
                    print("Inserted")
                if stop:
                    break
                try:
                    post = requests.get(post['paging']['next']).json()
                except KeyError:
                    break

    def get_fb_profile_pic(self):
        fetch_sql = "SELECT id, facebook FROM manager;"
        update_sql = "UPDATE manager SET profile_pic='{}' WHERE id={};"
        self.cur.execute(fetch_sql)
        id_list = self.cur.fetchall()
        for usr_id in id_list:
            if usr_id[1] != "":
                #picture = self.graph.get_object(id=usr_id[1], fields='picture', type='large')
                picture = requests.get("https://graph.facebook.com/{}/picture?access_token={}&redirect=false&type=large".
                                       format(usr_id[1], self.access_token)).json()
                self.cur.execute(update_sql.format(picture['data']['url'], usr_id[0]))
                print("inserted")


if __name__ == "__main__":
    if len(sys.argv) > 1:
        command_type = sys.argv[1]
        mysql_file = "/home/lynn/workspace/django/kcd2018/kcd2018/mysql.cnf"
        fc = Facebook_crawler(mysql_file)
        fc.connect_db()
        if command_type == "event":
            fc.get_fb_event()
        elif command_type == "profile":
            fc.get_fb_profile_pic()
        else:
            print("You have to select type 'event' or 'profile'")
    else:
        print("You have to select type 'event' or 'profile'")
