#!/usr/bin/env python
# Copyright (c) 2015--2019, Julien Seguinot <seguinot@vaw.baug.ethz.ch>
# Creative Commons Attribution-ShareAlike 4.0 International License
# (CC BY-SA 4.0, http://creativecommons.org/licenses/by-sa/4.0/)

"""Plot EPICA and LR04 isotopic records time series."""

import numpy as np
import matplotlib.pyplot as plt

plt.rc('mathtext', default='regular')


def main():
    """Main program called during execution."""

    # Initialize figure
    fig, (ax0, ax1) = plt.subplots(
        figsize=(9, 6), nrows=2, sharex=True, gridspec_kw=dict(
            left=0.6/9, right=1-0.2/9, bottom=0.6/6, top=1-0.2/6, hspace=0.08))

    # plot EPICA data
    age, data = np.genfromtxt(
        '../../data/external/edc3deuttemp2007.txt',
        delimiter=(4, 13, 17, 13, 13), encoding='latin-1',
        skip_header=104, skip_footer=1, unpack=True, usecols=(2, 4))
    ax0.plot(age/1e3, data, color='C3')

    # set EPICA axes properties
    ax0.locator_params(nbins=6)
    ax0.set_ylabel(r'$\Delta T$ (K)', labelpad=0)
    ax0.text(0.04, 0.05, 'EPICA ice core', color='C3', fontweight='bold',
             va='bottom', transform=ax0.transAxes)

    # plot LR04 data
    age, data = np.genfromtxt(
        '../../data/external/lisiecki2005.txt', encoding='latin-1',
        skip_header=89, skip_footer=7973, unpack=True, usecols=(0, 1))
    ax1.plot(age, data, color='C0')

    # set LR04 axes properties
    ax0.locator_params(nbins=6)
    ax1.set_xlabel('age (ka)')
    ax1.set_ylabel(r'$\delta^{18}O$ (‰)')
    ax1.set_xlim(2e3, 0)
    ax1.text(0.04, 0.95, 'LR04 benthic stack', color='C0', fontweight='bold',
             va='top', transform=ax1.transAxes)

    # save
    fig.savefig('isotopes-03')
    ax0.set_visible(False)
    fig.savefig('isotopes-02')
    ax0.set_xlim(5e3, 0)
    fig.savefig('isotopes-01')


if __name__ == '__main__':
    main()
