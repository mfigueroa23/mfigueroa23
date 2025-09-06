echo "------------------"
echo "Respaldando Servicios Productos" $(date)
echo "------------------"

sleep 2

echo "\n [1] Generando comprimido del proyecto productivo \n"
tar -czvf /home/FrutosDelMundo/docker-compose.tar.gz /home/FrutosDelMundo/docker-deployments

sleep 2

echo "\n [2] Enviando respaldos a la maquina de BackUps \n"
rsync -vharp /home/FrutosDelMundo/docker-compose.tar.gz sysadmin@4.228.60.161:/home/sysadmin/

sleep 2

echo "\n [3] Elimiando Respaldos generado \n"
rm -rfv /home/FrutosDelMundo/docker-compose.tar.gz

sleep 2

echo "\n [i] Respaldo completado con exito \n"