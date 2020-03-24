import MySQLdb
import json

sql = "SELECT * FROM AquaSaying; "

Loginfo = {
    'Username': '',
    'Password': '',
    'Host': 'localost',
    'Port': ''
}

connect_sql = MySQLdb.connect(host=Loginfo['Host'], user=Loginfo['Username'], passwd=Loginfo['Password'], port=Loginfo['Port'], charset='utf8')
cur = connect_sql.cursor()
cur.execute(sql)
jsondata = cur.fetchall()
fields = cur.discription
cur.close()
connect_sql.close()

column_list = []
for i in