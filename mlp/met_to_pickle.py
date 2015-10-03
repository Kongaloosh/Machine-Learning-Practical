import cPickle
import gzip

__author__ = 'kongaloosh'

path = 'data/HadSSP_daily_qc.txt'

with open(path) as f:
    text = f.read()                                     # open file
    text = text.split('\n')                             # split on the newlines
    text = text[3:]                                     # get rid of the header (we don't care about labels)
    text = [i.split('   ') for i in text]               # split on crappy formatting

    for line in text:                                   # we have to deal with one weird line that has odd spacing
        badly_formatted = line.pop(len(line)-1)         # get the last element, which isn't formatted correctly
        badly_formatted = badly_formatted.split("  ")   # split it into proper attributes
        for i in badly_formatted:
            line.append(i)                              # re-append so we can use the data


    text = [(line[:-1],line[len(line)-1]) for line in text]     # split into tuple of form (feature, target)

    file = gzip.GzipFile('data/met_data.pkl.gz', 'wb')
    file.write(cPickle.dumps(text, 1))
    file.close()