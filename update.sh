#!/bin/sh
DATE=`date "+%Y%m%d.%H"`
DAY=`date "+%Y%m%d"`
FILE=data/$DATE.csv
mkdir -p data
if [ ! -e $FILE ]
then
    curl --silent --max-redirs 4 "http://earthquake.usgs.gov/earthquakes/catalogs/eqs1hour-M1.txt" > $FILE
    rm -f data/latest.csv
    cp $FILE data/latest.csv
    cat $FILE | egrep -v "^Src" >> data/all.csv
    python geojson.py data/$DAY.??.csv > data/$DAY.json
    cp data/$DAY.json data/today.json
    python geojson.py data/latest.csv > data/latest.json
    python geojson.py data/all.csv > data/all.json
fi
