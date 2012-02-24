import csv
import os

from artworks.models import Artwork

def run():
    print "hello"

    contents = csv.reader(open("%s/../data/gallery.csv" % os.path.dirname(__file__)), 
                          dialect='excel', delimiter=',', quotechar='"')

    header = contents.next()
    for row in contents:
        aw = Artwork()
        aw.level = row[0].strip()
        aw.work_num = row[1].strip()
        aw.artist = ' '.join((row[2].strip(), row[3].strip()))
        aw.title = row[4].strip()
        aw.year = row[5].strip()
        aw.medium = row[6].strip()
        aw.credit = row[7].strip()
        aw.website = row[8].strip()
        aw.save()
