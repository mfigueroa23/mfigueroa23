echo "------------------"
echo "Eliminando respaldo" $(date)
echo "------------------"

sleep 3

echo "\n 1: Eliminando respaldo generado \n"
rm -rfv /home/sysadmin/bkp/*

sleep 3

echo "\n 2: Verificacion de eliminacion \n"
las -lah /home/sysadmin/bkp/

sleep 3

echo "\n 3: ELIMINACION FINALIZADA $(date) \n"