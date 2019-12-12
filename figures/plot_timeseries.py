#!/usr/bin/env python2
# coding: utf-8

import os
import urllib
import numpy as np
import matplotlib.pyplot as plt

colors = ('#e31a1c', '#1f78b4')  # dark blue, dark red

# data sources
urlbase = 'ftp://ftp.ncdc.noaa.gov/pub/data/paleo/'
urldict = {
    'epica': urlbase + 'icecore/antarctica/epica_domec/edc3deuttemp2007.txt',
    'lr04':  urlbase + 'contributions_by_author/lisiecki2005/lisiecki2005.txt'}

# additional sea-level data sources
# 'contributions_by_author/lea2002/lea2002.txt'
# 'contributions_by_author/siddall2003/siddall2003.txt'

# fetch data
for rec, url in urldict.iteritems():
    filename = '../data/%s.txt' % rec
    print filename
    if not os.path.isfile(filename):
        urllib.urlretrieve(url, filename)


# Initialize figure
figw, figh = 150.0, 75.0
fig, grid = plt.subplots(figsize=(figw/25.4, figh/25.4),
                         nrows=2, ncols=2, sharex=True)
fig.subplots_adjust(left=70.0/figw, right=1-2.5/figw,
                    bottom=10.0/figh, top=1-2.5/figh,
                    hspace=2.5/30.0,
                    width_ratios=(1, 3))

# plot LR04 data (pick only the last 800 ka)
ax = grid[0, 1]
c = colors[0]
age, d18o = np.genfromtxt('../data/lr04.txt', skip_header=89, skip_footer=7973, #9387,
                          unpack=True, usecols=(0, 1))
ax.plot(age, d18o, c)  # alt. wiki color #0978ab

# set LR04 axes properties
ax.set_ylabel(u'$\delta^{18}O$ (\u2030)')
ax.set_yticks([3, 4, 5])
ax.set_ylim(5.5, 2.5)
ax.text(0.04, 0.10, 'LR04 benthic stack',
        color=c, fontweight='bold', transform=ax.transAxes)

# save
ax.set_xlim(5.0e3, 0.0)
fig.savefig('plot_timeseries_01')
ax.set_xlim(2.0e3, 0.0)
fig.savefig('plot_timeseries_02')

# plot EPICA data
ax = grid[1, 1]
c = colors[1]
age, temp = np.genfromtxt('../data/epica.txt', delimiter=(4, 13, 17, 13, 13),
                          skip_header=104, skip_footer=1,
                          unpack=True, usecols=(2, 4))
ax.plot(age/1000.0, temp, c)  # alt. wiki color #e0584e

# set EPICA axes properties
ax.set_xlabel('age (ka)')
ax.set_ylabel('$\Delta T$ (K)', labelpad=0)
ax.set_yticks(range(-12, 6, 4))
ax.set_ylim(-12, 6)
ax.text(0.04, 0.85, 'EPICA ice core',
        color=c, fontweight='bold', transform=ax.transAxes)

# save
ax.set_xlim(2.0e3, 0.0)
fig.savefig('plot_timeseries_03')