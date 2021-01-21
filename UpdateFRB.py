# This script converts the online catalog of Fast Radio Bursts into a VOTable
# that can then be easily processed using the Digistar Utility VOTableToDSA.

# To run this script, first download the newest FRB Catalog from frbcat.org
# Just click Export to CSV - do not alter columns. Save to the same directory
# where this script is located. Run this script with the command line:
# python UpdateFRB.py <frbcat_date.csv>

# Mariarosa Marinelli
# mmarinelli@smv.org

import sys
import numpy as np
import astropy
from astropy.io import ascii
from astropy.table import Table
from astropy.coordinates import SkyCoord
from astropy.io.votable import parse

filenames = []

if (len(sys.argv) == 2):
    for fname in sys.argv[1:]:
        try:
            file = open(fname, 'r')
            file.close()
            filenames.append(fname)

            filename = sys.argv[1]

            print("%s is valid, thank you." % fname)
        except:
            print("%s not found." % fname)

else:
    print("Please include the FRB Catalog datafile.")

def first():
    data = ascii.read(filename, format='csv', fast_reader=False)

    na = np.array(data[0][:])
    di = np.array(data[2][:])
    r = np.array(data[3][:])
    d = np.array(data[4][:])

    coord = SkyCoord(r, d, unit='deg')
    ra = coord.ra.degree
    de = coord.dec.degree

    tbl = Table(data=(na, di, ra, de),
                names=('FRBname', 'discoloc', 'ra', 'dec'),
                dtype=('str', 'str', 'float64', 'float64'))

    astropy.io.votable.writeto(tbl, '%s.xml' % filename[0:-4], tabledata_format=None)
    print("VOTable has been created.")

def second():
    votable = parse('FRBUpdate.xml')

    mytable = votable.get_first_table()

    rafield = mytable.get_field_by_id('ra')
    rafield.ucd = 'pos.eq.ra'
    rafield.unit = 'deg'

    decfield = mytable.get_field_by_id('dec')
    decfield.ucd = 'pos.eq.dec'
    decfield.unit = 'deg'

    votable.to_xml('%s.xml' % filename[0:-4])
    print("VOTable has been updated. Good job!")

if __name__ == '__main__':
    if (len(sys.argv) > 1):
        first()
        second()
    else:
        print("Something went wrong.")
