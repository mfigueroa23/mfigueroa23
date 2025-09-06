echo "------------------"
echo "Obteniendo respaldo" $(date)
echo "------------------"

sleep 3

echo "\n 1: Obteniendo respaldo de la imagen maquina master \n"
rsync -vharp --progress sysadmin@10.0.0.4:/home/sysadmin/bkp/httpd_cl_bkp.tar /home/sysadmin/bkp/

sleep 3

echo "\n 2: Obteniendo respaldos del Web Content \n"
rsync -vharp --progress sysadmin@10.0.0.4:/home/sysadmin/web-content/ /home/sysadmin/web-content/

sleep 3

echo "\n 3: Verificacion del respaldo obtenido \n"
ls -lah /home/sysadmin/bkp/
echo "\n"
ls -lah /home/sysadmin/web-content

sleep 3

echo "\n 3: OBTENCION FINALIZADA $(date) \n"
