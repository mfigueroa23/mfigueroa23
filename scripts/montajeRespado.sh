echo "------------------"
echo "Desplegando Servicios Productos" $(date)
echo "------------------"

sleep 2

echo "\n [1] Descomprimiendo respaldo obtenido \n"
tar -xzvf /home/FrutosDelMundo/docker-compose.tar.gz

sleep 2

echo "\n [2] Despliegue de los servicios \n"
docker compose -f /home/sysadmin/docker-deployments/docker-compose.yml up -d

sleep 2

echo "\n [3] Elimiando respaldos obtenido \n"
rm -rfv /home/sysadmin/docker-compose.tar.gz

sleep 2

echo "\n [i] Despliegue completado con exito \n"