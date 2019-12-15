# Copyright (c) 2019, Julien Seguinot <seguinot@vaw.baug.ethz.ch>
# Creative Commons Attribution-ShareAlike 4.0 International License
# (CC BY-SA 4.0, http://creativecommons.org/licenses/by-sa/4.0/)

# Figures Makefile
# ================

# figure subdirectories
SUBDIRS = plot
CLEANDIRS = $(SUBDIRS:%=clean-%)

# make subdirectories
.PHONY: all $(SUBDIRS)
all: $(SUBDIRS)
$(SUBDIRS):
	$(MAKE) -C $@

# clean subdirectories
.PHONY: clean $(CLEANDIRS)
clean: $(CLEANDIRS)
$(CLEANDIRS):
	$(MAKE) -C $(@:clean-%=%) clean
