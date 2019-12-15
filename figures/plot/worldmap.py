#!/usr/bin/env python
# Copyright (c) 2015--2019, Julien Seguinot <seguinot@vaw.baug.ethz.ch>
# Creative Commons Attribution-ShareAlike 4.0 International License
# (CC BY-SA 4.0, http://creativecommons.org/licenses/by-sa/4.0/)

"""Plot World map of present and LGM ice extent."""

import matplotlib as mpl
import matplotlib.pyplot as plt
import cartopy.crs as ccrs
import cartopy.io.shapereader as cshp
import cartowik.naturalearth as cne


def draw_shapefile_nodups(filename, ax=None, crs=None, **kwargs):
    # FIXME add this to cartowik?
    """Add shapefile geometries without duplicates."""
    ax = ax or plt.gca()
    crs = crs or ccrs.PlateCarree()
    shp = cshp.Reader(filename)
    geometries = []
    for geom in shp.geometries():
        if geom not in geometries:
            geometries.append(geom)
    ax.add_geometries(geometries, crs, **kwargs)
    shp = None


def main():
    """Main program called during execution."""

    # initialize figure
    fig = plt.figure(figsize=(12, 6))

    # for each hemisphere
    for i in range(2):

        # add axes
        ax = fig.add_axes([i/2, 0, 0.5, 1], projection=ccrs.Orthographic(
            central_longitude=0, central_latitude=90*(1-2*i)))

        # add physical elements
        cne.add_rivers(ax=ax, edgecolor='0.25', scale='110m')
        cne.add_lakes(ax=ax, edgecolor='0.25', facecolor='0.75', scale='110m')
        cne.add_coastline(ax=ax, edgecolor='0.25', scale='110m')
        cne.add_glaciers(ax=ax, edgecolor='none', facecolor='C0', scale='50m',
                         zorder=2)
        cne.add_graticules(ax=ax, interval=15, scale='110m', zorder=2)

        # ax.set_extent does not work well with ortho proj
        ax.set_xlim((-6.5e6, 6.5e6))
        ax.set_ylim((-6.5e6, 6.5e6))

    # save first frame
    fig.savefig('worldmap-01')

    # add last glacial cycle glaciers
    for ax in fig.axes:
        draw_shapefile_nodups('../../data/external/lgm_simple.shp',
                              ax=ax, alpha=0.75, facecolor='C3', zorder=1)

    # add legend
    fig.legend(
        [mpl.patches.Patch(facecolor=c, alpha=0.75) for c in ['C0', 'C3']],
        ['Modern Glaciers', 'Last Glacial Cycle'])

    # save second frame
    fig.savefig('worldmap-02')


if __name__ == '__main__':
    main()
