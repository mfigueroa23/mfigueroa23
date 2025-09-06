echo "------------------"
echo "generando respaldo" $(date)
echo "------------------"

sleep 3

echo "\n 1: Generando commit del contenedor \n"
docker commit httpd_cl httpd_cl_bkp

sleep 3

echo "\n 2: Generando TAR de la Imagen \n"
docker save -o /home/sysadmin/bkp/httpd_cl_bkp.tar httpd_cl_bkp

echo "\n 3: Verificacion del respaldo generado \n"
ls -lha /home/sysadmin/bkp/

sleep 3

echo "\n 4: RESPALDO FINALIZADO $(date) \n"
