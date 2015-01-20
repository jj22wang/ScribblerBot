import _mysql
from MySQLdb.constants import FIELD_TYPE
from movement4 import *
from path_testing2 import *
config = {
  'user': 'scribbler',
  'password': 'scribbler',
  'host': '104.236.34.115',
  #'host':'http://cloud.digitalocean.com/droplets/3158590',
  'database': 'scribbler',
}
my_conv={FIELD_TYPE.LONG: int}
#db=_mysql.connect(host="localhost",port=3306,user="root",passwd="",db="scribbler",conv=my_conv)
#db.query("""SELECT * FROM commandlist ORDER BY commandID""")

db=_mysql.connect(host=config['host'],port=3306,user=config['user'],passwd=config['password'],db=config['database'])
a = Movement(0.2, 3.22, 0.15, 11.6)
#This continous loop takes
grid = [[0,0,0,0], [0,0,0,0], [0,0,0,0],
            [0,0,0,0],
            [0,0,0,0]]
beep(0.166, 988)
beep(0.166, 988)
beep(0.166, 988)
beep(0.5, 988)
beep(0.5, 784)
beep(0.5, 880)
beep(0.07, 988)
beep(0.07, 988)
beep(0.07, 988)
beep(0.07, 988)
beep(0.14, 988)
beep(0.07, 988)
beep(0.07, 988)
beep(0.07, 988)
beep(0.07, 988)
beep(0.07, 988)
beep(0.07, 988)
beep(0.14, 988)
beep(0.07, 1319)
beep(0.07, 1319)
beep(0.07, 1319)
beep(0.07, 1319)
beep(0.07, 1319)
beep(0.07, 1319)
beep(0.14, 1319)
beep(0.07, 1175)
beep(0.07, 1175)
beep(0.07, 1175)
beep(0.07, 1175)
beep(0.07, 1175)
beep(0.07, 1175)
beep(0.14, 1175)
beep(0.14, 880)
beep(0.07, 988)
beep(0.07, 988)
beep(0.07, 988)
beep(0.07, 988)
beep(0.14, 988)
beep(0.07, 988)
beep(0.07, 988)
beep(0.07, 988)
beep(0.07, 988)
beep(0.07, 988)
beep(0.07, 988)
beep(0.14, 988)
beep(0.14, 1319)
beep(0.07, 988)
beep(0.07, 988)
beep(0.07, 988)
beep(0.07, 988)
beep(0.14, 988)
beep(0.07, 988)
beep(0.07, 988)
beep(0.07, 988)
beep(0.07, 988)
beep(0.07, 988)
beep(0.07, 988)
beep(0.14, 988)
beep(0.07, 1975.5)

while (True):
    db.query("""SELECT * FROM commandList""")
    print "HI"
    print a.x
    print a.y
    r=db.store_result()
    d=r.fetch_row(1,how=1)
    if len(d) > 0:
        x = d[0]['DestX']
        y = d[0]['DestY']
        print x
        print y
        move_path(grid, a, a.x, a.y, int(x), int(y))
        db.query("DELETE FROM commandList WHERE commandID="+d[0]['commandID'])
    time.sleep(10)
db.close()
