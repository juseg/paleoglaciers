#!/bin/bash
# Copyright (c) 2019, Julien Seguinot <seguinot@vaw.baug.ethz.ch>
# Creative Commons Attribution-ShareAlike 4.0 International License
# (CC BY-SA 4.0, http://creativecommons.org/licenses/by-sa/4.0/)

# Download project external data
# ------------------------------


# make directory or update modification date
mkdir -p external
touch external
cd external

# Ehlers et al. (2011) simplified LGM outline
wdir="http://static.us.elsevierhealth.com/ehlers_digital_maps/"
file="digital_maps_02_all_other_files.zip"
if [ ! -f lgm_simple.shp ]
then
    wget -nc $wdir/$file
    unzip -jn $file lgm.??? lgm_alpen.???
    ogr2ogr -where "OGR_GEOM_AREA > 1e-3" -simplify 0.01 lgm_simple.shp lgm.shp
    ogr2ogr -where "OGR_GEOM_AREA > 1e-3" -simplify 0.01 \
            -append lgm_simple.shp lgm_alpen.shp
fi
