# import to rasp pi and try to execute main on crontabs

import connect
mycursor = connect.mysql.cursor()
sql = "TRUNCATE tbl_Library;"
mycursor.execute(sql)
connect.mysql.commit()

sql = "SELECT * INTO tbl_Library from tbl_Probes WHERE UserTime >= DATE_ADD(CURRENT_TIMESTAMP, INTERVAL 15 MINUTE) AND Location = 'Library';"
mycursor.execute(sql)
connect.mysql.commit()
