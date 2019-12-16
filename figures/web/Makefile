# Copyright (c) 2019, Julien Seguinot <seguinot@vaw.baug.ethz.ch>
# Creative Commons Attribution-ShareAlike 4.0 International License
# (CC BY-SA 4.0, http://creativecommons.org/licenses/by-sa/4.0/)

# Web images Makefile
# ===================

COMMONS = 'https://upload.wikimedia.org/wikipedia/commons/'
FIGS = $(addsuffix .jpg, chamberlin-1882 coutterand-2015 csiro-2000-bubbles \
			 decharpentier-1841 \
			 jaggin-2008-01 jaggin-2008-05 penck-bruckner-1909)

# default rule
all: $(FIGS)
	@echo $(FIGS)

# Chamberlin (1882) Wisonsin moraines map
# FIXME high-res in https://pubs.er.usgs.gov/publication/ar3
chamberlin-1882.jpg:
	wget -nc https://etc.usf.edu/maps/pages/10600/10623/10623.jpg -O $@

# Coutterand (2015) Alps LGM ice extent map
coutterand-2015.jpg:
	wget -nc https://www.glaciers-climat.com/wp-content/uploads/LGM-Alpes-Glaciers-Web.jpeg -O $@

# CSIRO science image (2000) air bubbles
# FIXME crop to a square maybe
csiro-2000-bubbles.jpg:
	wget -nc $(COMMONS)/d/d0/CSIRO_ScienceImage_521_Bubbles_in_Ice.jpg -O $@

# De Charpentier (1841) Rhone Glacier erratic terrain map
# FIXME hig-res in https://antiqueprintmaproom.com/media/catalog/product/cache/1/image/9df78eab33525d08d6e5fb8d27136e95/_/m/_mg_3118_copy_1.jpg
decharpentier-1841.jpg:
	wget -nc http://shipseducation.net/glaciers/Charpentier_files/image008.jpg -O $@

# Jäggin (2008) Zürich reconstruction maps
jaggin-2008-01.jpg:
	wget -nc "https://www.stadt-zuerich.ch/content/dam/stzh/hbd/Deutsch/Archaeologie_Denkmalpflege/Grafik%20und%20Foto/Stadtarchaeologie/Projekte_Auswertungen/Seespiegel/B01_ZH_See%20404p00_Deltabildung1_.jpg" -O $@
jaggin-2008-05.jpg:
	wget -nc "https://www.stadt-zuerich.ch/content/dam/stzh/hbd/Deutsch/Archaeologie_Denkmalpflege/Grafik%20und%20Foto/Stadtarchaeologie/Projekte_Auswertungen/Seespiegel/B06_ZH_See%20405p50_Normalstand%20(sp%C3%A4tm)1_.jpg" -O $@

# Penck and Brückner (1909) Alps glaciations map
penck-bruckner-1909.jpg:
	wget -nc https://www.glaciers-climat.com/wp-content/uploads/6-Carte-Penck-et-Bruckner-1909.jpg -O $@


# FIXME missing univ Michigan dO18 cartoon

# clean up
.PHONY: clean
clean:
	rm $(FIGS)
