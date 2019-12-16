# Copyright (c) 2019, Julien Seguinot <seguinot@vaw.baug.ethz.ch>
# Creative Commons Attribution-ShareAlike 4.0 International License
# (CC BY-SA 4.0, http://creativecommons.org/licenses/by-sa/4.0/)

# Web images Makefile
# ===================

FIGS = $(addsuffix .jpg, hodell-2016-01 wirsig-etal-2016-05)

# default rule
all: $(FIGS)

# Hodell (2016) pacemaker of the ice ages cartoon
# FIXME I think I want to draw my own pacemaker cartoon
hodell-2016-01.jpg:
	wget -nc https://science.sciencemag.org/content/sci/354/6317/1235/F1.large.jpg -O $@
	mogrify -crop x840+0+0 -gravity south $@

# Wirsig et al. (2016) LGM cosmogenic ages in the Alps
wirsig-etal-2016-05.jpg:
	wget -nc https://ars.els-cdn.com/content/image/1-s2.0-S027737911630138X-gr5_lrg.jpg -O $@

# clean up
.PHONY: clean
clean:
	rm $(FIGS)
