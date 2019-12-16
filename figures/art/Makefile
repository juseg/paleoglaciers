# Copyright (c) 2019, Julien Seguinot <seguinot@vaw.baug.ethz.ch>
# Creative Commons Attribution-ShareAlike 4.0 International License
# (CC BY-SA 4.0, http://creativecommons.org/licenses/by-sa/4.0/)

# Artworks Makefile
# =================

COMMONS = "https://upload.wikimedia.org/wikipedia/commons/"
FIGS = $(addsuffix .jpg, cole-1829 heer-1865 hodel-1927 hogard-1848 \
                         fearnley-1838 nansen-1888 triner-1865)

# default rule
all: $(FIGS)
	@echo $(FIGS)

# individual downloads
cole-1829.jpg:
	wget -nc $(COMMONS)/2/27/Cole_Thomas_The_Subsiding_of_the_Waters_of_the_Deluge_1829.jpg -O $@

heer-1865.jpg:
	wget -nc $(COMMONS)/5/50/Linthgletscher_koloriert.jpg -O $@ 

hodel-1927.jpg:
	wget -nc https://gletschergarten.ch/images/medien/Luzern_zur_Eiszeit.jpg -O $@

hogard-1848.jpg:
	wget -nc $(COMMONS)/4/45/Henri_Hogard-Glaciers_du_Rh%C3%B4ne.jpg -O $@

fearnley-1838.jpg:
	wget -nc $(COMMONS)/0/04/Thomas_Fearnley_-_Grindelwaldgletscher_-_Google_Art_Project.jpg -O $@

nansen-1888.jpg:
	wget -nc $(COMMONS)/f/f0/Nansen%27s_Greenland_expedition_crossing.jpg -O $@

triner-1865.jpg:
	wget -nc 'https://www.ag.ch/staatsarchiv/suche/getimage.aspx?VEID=84843&DEID=10&SQNZNR=0&SIZE=100' -O $@
	mogrify -crop 744x488+10+10 $@

# clean up
.PHONY: clean
clean:
	rm $(FIGS)
