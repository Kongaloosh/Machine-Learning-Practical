import cPickle
import gzip
import numpy
import re

__author__ = 'kongaloosh'

path = 'data/HadSSP_daily_qc.txt'

with open(path) as f:
    text = f.read()                                     # open file
    text = text.split('\n')                             # split on the newlines
    text = text[3:]                                     # get rid of the header (we don't care about labels)

    # regex for all the values
    text = [[float(i) for i in re.findall(r"[-+]?\d*\.\d+|\d+", line)] for line in text ][:-1]

    # format into a (features, targets)
    text = (
        numpy.array([line[:-1] for line in text]),
        numpy.array([line[len(line)-1] for line in text])
    )

    # zip and dump it!
    file = gzip.GzipFile('data/met_data.pkl.gz', 'wb')
    file.write(cPickle.dumps(text, 1))
    file.close()