#!/bin/bash
BASE_DIR="" # Ruta completa carpeta de presets de Vital
OUTPUT_DIR="$BASE_DIR/VitalBanks"

# Crear la carpeta de salida si no existe
mkdir -p "$OUTPUT_DIR"

cd "$BASE_DIR" || exit 1

TOTAL_COUNT=0

echo "=== Creando bancos individuales por carpeta principal ==="

# Un bank por cada subcarpeta del primer nivel
find . -maxdepth 1 -mindepth 1 -type d -print0 | while IFS= read -r -d '' dir; do
    bank_name=$(basename "$dir")
    zip_name="${bank_name}.zip"
    bank_file="${bank_name}.vitalbank"

    # Contar presets en esta carpeta (recursivo)
    count=$(find "$dir" -type f -name '*.vital' | wc -l)
    TOTAL_COUNT=$((TOTAL_COUNT + count))

    echo " Empaquetando: $bank_file    $count presets"

    # Crear el zip solo con archivos .vital
    (cd "$dir" && zip -rq "$OUTPUT_DIR/$zip_name" . -i '*.vital')

    # Renombrar a .vitalbank
    mv "$OUTPUT_DIR/$zip_name" "$OUTPUT_DIR/$bank_file"
done

echo "=== Creando banco nico con TODOS los presets ==="

# Mega-bank con todos los .vital en todas las subcarpetas
ALL_ZIP="$OUTPUT_DIR/All_Presets.zip"
ALL_BANK="$OUTPUT_DIR/All_Presets.vitalbank"

zip -rq "$ALL_ZIP" . -i '*.vital'
mv "$ALL_ZIP" "$ALL_BANK"

# Contar todos los presets globales (por seguridad, independiente del acumulador)
GLOBAL_COUNT=$(find . -type f -name '*.vital' | wc -l)

echo
echo " Todos los bancos fueron creados en: $OUTPUT_DIR"
echo " Total presets contabilizados: $GLOBAL_COUNT"
