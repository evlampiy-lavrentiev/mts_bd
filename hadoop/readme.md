  # Инструкция по настройке

1. на мастер ноде запускаете hadoop/init.sh под sudo. В том числе в нём создаётся user `hadoop`, под него нужно будет указать пароль
2. сконфигурировать /etc/hosts
3. конфигурируете
- /usr/local/hadoop/etc/hadoop/core-site.xml
- /usr/local/hadoop/etc/hadoop/hdfs-site.xml
- /usr/local/hadoop/etc/hadoop/mapred-site.xml
- /usr/local/hadoop/etc/hadoop/yarn-site.xml

TODO: написать что именно в этих файликах

4. то же самое проделать ещё и на slave нодах
5. запустить на мастер ноде `/usr/local/hadoop/sbin/start-all.sh`
6. запустить на слейв нодах `/usr/local/hadoop/bin/hdfs --daemon start datanode`
