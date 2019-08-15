#!/bin/bash
PRINT_SERVER_ADDRESS="http://localhost:5000"

if (( $# < 4 || $# > 5 )); then
    echo "Illegal number of arguments, it should be either 4 or 5"
    echo "Usage: translation.sh FILENAME COUNTRY_CODE COUNTRY_NAME PRINTER_TYPE [COUNT]"
    echo "  argument COUNT defaults to 1"
    exit 1
fi

FILENAME=$1
COUNTRY_CODE=$2
COUNTRY_NAME=$3
PRINTER_TYPE=$4
COUNT=${5:-1}

if [ ! -f "${FILENAME}" ]; then
    echo "File not found!"
    exit 1
fi

SERVER_FILENAME=`curl --form "pdf=@${FILENAME}" --form "type=translation" ${PRINT_SERVER_ADDRESS}/upload`

curl --data "filename=${SERVER_FILENAME}&country_code=${COUNTRY_CODE}&country_name=${COUNTRY_NAME}&printer_type=${PRINTER_TYPE}&count=${COUNT}" ${PRINT_SERVER_ADDRESS}/translation
