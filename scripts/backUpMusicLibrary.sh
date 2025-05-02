# Variables
dateFormatted=$(date +"%d-%m-%Y")
musicDir="$HOME/Workspace/MusicLibrary"
backupDir="$HOME/Workspace/OneDrive/Documents/MusicProduction/Backups/"

echo "Iniciando Backup MusicLibrary"
echo "Fecha: $(date +"%d-%m-%Y")"
echo "-------------------------------------"

# Verifica si el directorio de respaldo existe, si no lo crea
if [ ! -d "$backupDir" ]; then
    echo "El directorio de respaldo no existe. Creando..."
    mkdir -p "$backupDir"
    echo "-------------------------------------"
fi

# Crando backup en formato zip
echo "Creando backup en formato zip..."
echo "-------------------------------------"
zip -r "$backupDir/MusicLibrary-$dateFormatted.zip" "$musicDir" -x "*.DS_Store" "*.asd"
echo "-------------------------------------"

echo "Backup MusicLibrary Finalizado"
echo "Fecha: $(date +"%d-%m-%Y")"
echo "[i] El backup se ha creado en: $backupDir"
echo "[i] El tamañp del backup es: $(du -sh "$backupDir/MusicLibrary-$dateFormatted.zip" | cut -f1)"
echo "-------------------------------------"
