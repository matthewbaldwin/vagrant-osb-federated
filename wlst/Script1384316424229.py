
connect('weblogic','welcome1','t3://localhost:7001')

edit()
startEdit()

cd('/')
cmo.createJDBCSystemResource('jdbc.FODDS')

cd('/JDBCSystemResources/jdbc.FODDS/JDBCResource/jdbc.FODDS')
cmo.setName('jdbc.FODDS')

cd('/JDBCSystemResources/jdbc.FODDS/JDBCResource/jdbc.FODDS/JDBCDataSourceParams/jdbc.FODDS')
set('JNDINames',jarray.array([String('jdbc.FODDS')], String))

cd('/JDBCSystemResources/jdbc.FODDS/JDBCResource/jdbc.FODDS/JDBCDriverParams/jdbc.FODDS')
cmo.setUrl('jdbc:oracle:thin:@192.168.50.5:1521:xe')
cmo.setDriverName('oracle.jdbc.xa.client.OracleXADataSource')
setEncrypted('Password', 'Password_1384316548396', '/vagrant/wlst/Script1384316424229Config', '/vagrant/wlst/Script1384316424229Secret')

cd('/JDBCSystemResources/jdbc.FODDS/JDBCResource/jdbc.FODDS/JDBCConnectionPoolParams/jdbc.FODDS')
cmo.setTestTableName('SQL SELECT 1 FROM DUAL\r\n')

cd('/JDBCSystemResources/jdbc.FODDS/JDBCResource/jdbc.FODDS/JDBCDriverParams/jdbc.FODDS/Properties/jdbc.FODDS')
cmo.createProperty('user')

cd('/JDBCSystemResources/jdbc.FODDS/JDBCResource/jdbc.FODDS/JDBCDriverParams/jdbc.FODDS/Properties/jdbc.FODDS/Properties/user')
cmo.setValue('fod')

cd('/JDBCSystemResources/jdbc.FODDS/JDBCResource/jdbc.FODDS/JDBCDataSourceParams/jdbc.FODDS')
cmo.setGlobalTransactionsProtocol('TwoPhaseCommit')

cd('/SystemResources/jdbc.FODDS')
set('Targets',jarray.array([ObjectName('com.bea:Name=AdminServer,Type=Server'), ObjectName('com.bea:Name=osb_server1,Type=Server')], ObjectName))

activate()

dumpStack()

exit()