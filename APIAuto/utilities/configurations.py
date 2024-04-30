import configparser
import mysql.connector

def getconfig():
    config=configparser.ConfigParser()
    config.read('utilities/properties.ini')
    return config


def getConnection():
    conn = mysql.connector.connect()
    c=getconfig()
    #conn.connect(host=c['SQL']['host'],database=c['SQL']['database'],user=c['SQL']['user'],password=c['SQL']['password'])
    dict={'host' : c['SQL']['host'],
          'database' : c['SQL']['database'],
          'user':c['SQL']['user'],
          'password':c['SQL']['password']}
    conn.connect(**dict)
    return conn

def getQuery(query):
    conn=getConnection()
    cursor=conn.cursor()
    cursor.execute(query)
    row =cursor.fetchone()
    conn.close()
    return row
