echo "------------------"
echo "Desplegando servicio" $(date)
echo "------------------"

sleep 3

echo "\n 1: Cargando la Imagen en Docker Engine \n"
docker load -i /home/sysadmin/bkp/httpd_cl_bkp.tar

sleep 3

echo "\n 2: Ejecutando contenedor \n"
docker run -d --name=httpd_cl_bkp -p80:80 -v /home/sysadmin/web-content:/usr/local/apache2/htdocs/ httpd_cl_bkp

sleep 3

echo "\n 3: Eliminando TAR obtenido \n"
rm -rfv /home/sysadmin/bkp/httpd_cl_bkp.tar

sleep 3

echo "\n 4: DESPLIEGUE FINALIZADO \n"
