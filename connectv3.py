import _mysql
from MySQLdb.constants import FIELD_TYPE
import ast

config = {
  'user': 'scribbler',#'root',
  'password': 'scribbler',#'samuelwu',
  'host': '104.131.18.168',
  'database': 'scribbler',
}
my_conv={FIELD_TYPE.LONG: int}
db=_mysql.connect(host="localhost",port=3306,user="root",passwd="",db="scribbler",conv=my_conv)
#{
db.query("""SELECT * FROM commandlist ORDER BY commandID""")
r=db.store_result()
result=r.fetch_row(how=1)

#Access shit by using stuff like result[0]['DestY']
#Should continuosly loop this program.
db.query("""DELETE FROM commandlist WHERE commandID="""+str(result[0]['commandID']))
#}
db.close()
