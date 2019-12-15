# Data Makefile
# =============


# Rules
# -----

# default rule
all: external

# retrieve external files
external: retrieve-external.sh
	bash $<

# clean up
.PHONY: clean
clean:
	rm -rf external
