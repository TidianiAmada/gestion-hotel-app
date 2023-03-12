# To run the 3xMySQL servers with a ProxySQL container :
docker-compose up -d
# To configure the MySQL master node
docker exec -it mysqlmaster mysql -P3308 -uroot -ppasser123 \
  -e "CREATE USER 'repl'@'%' IDENTIFIED BY 'passer123';" \
  -e "GRANT REPLICATION SLAVE ON *.* TO 'repl'@'%';" \
  -e "SHOW MASTER STATUS\G;"
# To configure the MySQL slave nodes
for N in (first,second)
  do docker exec -it '$Nslave' mysql -uroot -ppasser123 \
    -e "CHANGE MASTER TO MASTER_HOST='mysqlmaster', MASTER_PORT=3308, MASTER_USER='repl',  MASTER_PASSWORD='passer123', MASTER_AUTO_POSITION = 1;"

  docker exec -it slave$N mysql -uroot -pmypass -e "START SLAVE;"
done
