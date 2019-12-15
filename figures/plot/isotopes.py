#!/usr/bin/env python
# Copyright (c) 2015--2019, Julien Seguinot <seguinot@vaw.baug.ethz.ch>
# Creative Commons Attribution-ShareAlike 4.0 International License
# (CC BY-SA 4.0, http://creativecommons.org/licenses/by-sa/4.0/)

"""Plot EPICA and LR04 isotopic records time series."""

import numpy as np
import matplotlib.pyplot as plt


def main():
    """Main program called during execution."""

    # Initialize figure
    fig, grid = plt.subplots(
        figsize=(9, 6), nrows=2, sharex=True, gridspec_kw=dict(
            left=0.6/9, right=1-0.2/9, bottom=0.6/6, top=1-0.2/6, hspace=0.08))

    # plot LR04 data (pick only the last 800 ka)
    ax = grid[0]
    age, d18o = np.genfromtxt(
        '../../data/external/lisiecki2005.txt', encoding='latin-1',
        skip_header=89, skip_footer=7973, unpack=True, usecols=(0, 1))
    ax.plot(age, d18o, color='C0')

    # set LR04 axes properties
    ax.set_ylabel(r'$\delta^{18}O$ (‰)')
    ax.set_yticks([3, 4, 5])
    ax.set_ylim(5.5, 2.5)
    ax.text(0.04, 0.10, 'LR04 benthic stack',
            color='C0', fontweight='bold', transform=ax.transAxes)

    # save
    ax.set_xlim(5.0e3, 0.0)
    fig.savefig('plot_timeseries_01')
    ax.set_xlim(2.0e3, 0.0)
    fig.savefig('plot_timeseries_02')

    # plot EPICA data
    ax = grid[1]
    age, temp = np.genfromtxt(
        '../../data/external/edc3deuttemp2007.txt',
        delimiter=(4, 13, 17, 13, 13), encoding='latin-1',
        skip_header=104, skip_footer=1, unpack=True, usecols=(2, 4))
    ax.plot(age/1000.0, temp, color='C3')

    # set EPICA axes properties
    ax.set_xlabel('age (ka)')
    ax.set_ylabel(r'$\Delta T$ (K)', labelpad=0)
    ax.set_yticks(range(-12, 6, 4))
    ax.set_ylim(-12, 6)
    ax.text(0.04, 0.85, 'EPICA ice core',
            color='C3', fontweight='bold', transform=ax.transAxes)

    # save
    ax.set_xlim(2.0e3, 0.0)
    fig.savefig('plot_timeseries_03')


if __name__ == '__main__':
    main()
