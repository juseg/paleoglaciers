# Copyright (c) 2019, Julien Seguinot <seguinot@vaw.baug.ethz.ch>
# Creative Commons Attribution-ShareAlike 4.0 International License
# (CC BY-SA 4.0, http://creativecommons.org/licenses/by-sa/4.0/)

# Figures Makefile
# ================

# Variables
# ---------

# figures
FIGS = $(addsuffix .png, $(addprefix isotopes-, 01 02 03) \
			 $(addprefix worldmap-, 01 02))


# Rules
# -----

# default rule
all: $(FIGS)

# rules for python figures
%-01.png %-02.png %-03.png : %.py
	python $<

# clean up
.PHONY: clean
clean:
	rm -f $(FIGS)
