CREATE DATABASE testdb DEFAULT charset utf8 
collate utf8_general_ci;

# 把表改成utf-8
alter table testdb.testtable  character set utf8;

# 把表中的某个字段改成utf-8
alter table testdb.testtable change name name varchar(2000)  character set utf8;
alter table testdb.testtable change url url varchar(2000)  character set utf8;