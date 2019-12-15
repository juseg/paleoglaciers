#!/usr/bin/env python
# Copyright (c) 2015--2019, Julien Seguinot <seguinot@vaw.baug.ethz.ch>
# Creative Commons Attribution-ShareAlike 4.0 International License
# (CC BY-SA 4.0, http://creativecommons.org/licenses/by-sa/4.0/)

"""Plot World map of present and LGM ice extent."""

from matplotlib import pyplot as plt
import cartopy.crs as ccrs
import cartopy.io.shapereader as cshp
import cartowik.naturalearth as cne

# geographic projections
ll = ccrs.PlateCarree()
npo = ccrs.Orthographic(central_longitude=-60.0, central_latitude=90.0)
spo = ccrs.Orthographic(central_longitude=-60.0, central_latitude=-90.0)
nps = ccrs.NorthPolarStereo(central_longitude=-45.0)
ssaea = ccrs.AlbersEqualArea(
    central_longitude=100.0, central_latitude=30.2,
    standard_parallels=(28.75, 31.65))


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


def draw_rect(ax, extent, transform=None):
    """Draw a rectangle with given transform."""
    w, e, s, n = extent
    x = [w, w, e, e, w]
    y = [s, n, n, s, s]
    ax.plot(x, y, c='#e31a1c', lw=1, transform=transform)


def make_legend(ax):
    """Make a standalone legend."""
    xy = [[None]*2]
    artists = [plt.Polygon(xy, edgecolor='none', facecolor='#1f78b4'),
               plt.Polygon(xy, edgecolor='none', facecolor='#a6cee3'),
               ]
    labels = ['Modern glaciers',
              'Last Glacial Maximum',
              ]
    ax.legend(artists, labels, loc='lower center', bbox_to_anchor=(0, 0, 1, 1),
              bbox_transform=ax.figure.transFigure)


def main():
    """Main program called during execution."""

    # initialize figure
    fig = plt.figure(figsize=(12, 6))
    grid = [fig.add_axes([0.0, 0.0, 0.5, 1.0], projection=spo),
            fig.add_axes([0.5, 0.0, 0.5, 1.0], projection=npo)]

    # for each hemisphere
    for ax in grid:

        # add physical elements
        cne.add_rivers(ax=ax, edgecolor='0.25', scale='110m')
        cne.add_lakes(ax=ax, edgecolor='0.25', facecolor='0.75', scale='110m')
        cne.add_coastline(ax=ax, edgecolor='0.25', scale='110m')
        draw_shapefile_nodups('../../data/external/lgm_simple.shp',
                              ax=ax, alpha=0.5, facecolor='C0')
        cne.add_glaciers(ax=ax, edgecolor='none', facecolor='C0', scale='110m')
        cne.add_graticules(ax=ax, interval=15, scale='110m', zorder=2)

        # ax.set_extent does not work well with ortho proj
        ax.set_xlim((-6.5e6, 6.5e6))
        ax.set_ylim((-6.5e6, 6.5e6))

    # add legend
    make_legend(ax)

    # save
    fig.savefig('worldmap')


if __name__ == '__main__':
    main()
