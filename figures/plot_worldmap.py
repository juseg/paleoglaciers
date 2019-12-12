#!/usr/bin/env python2

from matplotlib import pyplot as plt
import cartopy.crs as ccrs
import cartopy.io.shapereader as shpreader
import cartopy.feature as cfeature

# geographic projections
ll = ccrs.PlateCarree()
proj = ccrs.Orthographic(central_longitude=-60.0, central_latitude=90.0)
cal = ccrs.LambertConformal(
    central_longitude=-95.0, central_latitude=49.0,
    false_easting=0.0, false_northing=0.0,
    standard_parallels=(49.0, 77.0), globe=None, cutoff=0)
stere = ccrs.Stereographic(
    central_latitude=90.0, central_longitude=-45.0, true_scale_latitude=70.0)
utm32 = ccrs.UTM(32)
utm50 = ccrs.UTM(50)
ssaea = ccrs.AlbersEqualArea(
    central_longitude=100.0, central_latitude=30.2,
    standard_parallels=(28.75, 31.65))


def draw_glaciers(ax):
    """Add present glaciers."""
    ax.add_feature(cfeature.NaturalEarthFeature(
        category='physical', name='glaciated_areas', scale='50m',
        edgecolor='none', facecolor='#1f78b4', alpha=1.0))


def draw_lgm(ax):
    """Add Ehlers & Gibbard 2003 LGM outline.
    Try to identify duplicates using centroids."""
    centroids = []
    shp = shpreader.Reader('data/lgm_simple.shp')
    for i, geom in enumerate(shp.geometries()):
        x, y = geom.centroid.xy
        x, y = x[0], y[0]
        if y < 0:
            print 'record %i in southern hemisphere' % i
            continue
        if (x, y) in centroids:
            print 'record %i is a duplicate' % i
            continue
        else:
            print 'adding record %i with area %f ...' % (i, geom.area)
            centroids.append((x, y))
            ax.add_geometries(geom, ccrs.PlateCarree(), alpha=1.0,
                              edgecolor='none', facecolor='#a6cee3')
    shp = None
    ax.text(117.0, 57.0, '?', color='#a6cee3', fontweight='bold', transform=ll)


def draw_rect(ax, extent, transform=None):
    """Draw a rectangle with given transform."""
    w, e, s, n = extent
    x = [w, w, e, e, w]
    y = [s, n, n, s, s]
    ax.plot(x, y, c='#e31a1c', lw=1, transform=transform)


def draw_areas(ax):
    """Draw my areas of interest."""
    draw_rect(ax, [-2.5e6, -1e6, 0e6, 3e6], cal)           # Cordillera
    draw_rect(ax, [150e3, 1050e3, 4820e3, 5420e3], utm32)  # Alps
    draw_rect(ax, [-700e3, -400e3, -1300e3, -1000e3], stere)  # Qaanaaq
    draw_rect(ax, [-20e3, 70e3, -155e3, 5e3], ssaea)  # Qaanaaq
    #draw_rect(ax, [-200e3, 800e3, 5900e3, 6700e3], utm50)  # Transbaikalia
    txtkwa = dict(ha='center', va='center', color='#e31a1c', transform=ll)
    ax.text(-85, 86, 'Bowdoin\nGlacier', **txtkwa)
    ax.text(-140, 45, 'Cordilleran\nice sheet', **txtkwa)
    ax.text(025, 45, 'Alps', **txtkwa)
    ax.text(100, 35, 'Haizishan', **txtkwa)
    #ax.text(115, 50, 'Transbaikalia', **txtkwa)


def draw_cities(ax):
    """Draw cities where I worked."""
    props = dict(c='#33a02c', marker='*', markersize=12, transform=ll)
    ax.plot(008.55, 47.37, **props)  # Zurich
    ax.plot(121.55, 29.87, **props)  # Ningbo
    props = dict(ha='center', va='center', color='#33a02c', fontweight='bold',
                 transform=ll)
    ax.text(5, 55, 'Zurich',**props)
    ax.text(125, 35, 'Ningbo', **props)

def make_legend(ax):
    """Make a standalone legend."""
    xy = [[None]*2]
    artists = [plt.Polygon(xy, edgecolor='none', facecolor='#1f78b4'),
               plt.Polygon(xy, edgecolor='none', facecolor='#a6cee3'),
               plt.Polygon(xy, edgecolor='#e31a1c', facecolor='none'),
               plt.Line2D([], [], ls='none', color='#33a02c', marker='*',
                          markersize=12)]
    labels = ['Modern glaciers',
              'Last Glacial Maximum',
              'Areas of interest',
              'Cities']
    ax.legend(artists, labels, numpoints=1, loc='upper left')


if __name__ == '__main__':

    # initialize figure (N. hem.)
    fig = plt.figure(0, (8.0, 8.0))
    ax = fig.add_axes([0.0, 0.0, 1.0, 1.0], projection=proj)
    ax.set_xlim((-6.4e6, 6.4e6))
    ax.set_ylim((-6.4e6, 6.4e6))

    # draw common parts
    draw_lgm(ax)
    draw_glaciers(ax)
    ax.coastlines(edgecolor='k', lw=0.25)
    ax.gridlines(color='0.5', linestyle='-', linewidth=0.1)

    # information
    draw_areas(ax)
    draw_cities(ax)
    make_legend(ax)

    # save
    fig.savefig('plot_worldmap.pdf')
