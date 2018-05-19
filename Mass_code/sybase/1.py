import sqlanydb
conn = sqlanydb.connect(uid='dba', pwd='sql', eng='demo', dbn='demo' )
curs = conn.cursor()
curs.execute("select 'Hello, world!'")
print "SQL Anywhere says: %s" % curs.fetchone()
curs.close()
conn.close()