#!/bin/bash

BUCKET_NAME="mi-bucket-gabo123"
BACKUP_FILE="backup_$(date +%F).tar.gz"
LOG_FILE="backup.log"

echo "Iniciando respaldo..." >> $LOG_FILE

# Crear carpeta de prueba
mkdir -p respaldo_test
echo "archivo prueba" > respaldo_test/test.txt

# Comprimir carpeta
tar -czf $BACKUP_FILE respaldo_test >> $LOG_FILE 2>&1

# Subir a S3
if aws s3 cp $BACKUP_FILE s3://$BUCKET_NAME/ >> $LOG_FILE 2>&1; then
    echo "Respaldo subido exitosamente" >> $LOG_FILE
else
    echo "Error al subir respaldo" >> $LOG_FILE
fi
