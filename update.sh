#!/bin/sh
DATE=`date "+%Y%m%d.%H"`
FILE=data/$DATE.csv
mkdir -p data
if [ ! -e $FILE ]
then
    curl --silent --max-redirs 4 "http://earthquake.usgs.gov/earthquakes/catalogs/eqs1hour-M1.txt" > $FILE
    ln -s $FILE data/latest.csv
    cat $FILE | egrep -v "^Src" >> data/all.csv
    python geojson.py data/latest.csv > data/latest.json
    python geojson.py data/all.csv > data/all.json
fi
