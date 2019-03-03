# table_3.py
import sys
from abc import ABC, abstractmethod

def print_table(objects, colnames, formatter):
    '''
    Make a nicely formatted table showing attributes from a list of objects
    '''
    if not isinstance(formatter, TableFormatter):
        raise TypeError('formatter must be a TableFormatter')

    formatter.headings(colnames)
    for obj in objects:
        rowdata = [str(getattr(obj, colname)) for colname in colnames ]
        formatter.row(rowdata)

class TableFormatter(ABC):
    def __init__(self, outfile=None):
        if outfile == None:
            outfile = sys.stdout
        self.outfile = outfile

    # Serves a design spec for making tables (use inheritance to customize)
    @abstractmethod
    def headings(self, headers):
        pass

    @abstractmethod
    def row(self, rowdata):
        pass

class TextTableFormatter(TableFormatter):
    def __init__(self, outfile=None, width=10):
        super().__init__(outfile)   # Initialize parent
        self.width = width

    def headings(self, headers):
        for header in headers:
            print('{:>{}s}'.format(header, self.width), end=' ', file=self.outfile)
        print(file=self.outfile)
    
    def row(self, rowdata):
        for item in rowdata:
            print('{:>{}s}'.format(item, self.width), end=' ', file=self.outfile)
        print(file=self.outfile)

class CSVTableFormatter(TableFormatter):
    def headings(self, headers):
        print(','.join(headers))

    def row(self, rowdata):
        print(','.join(rowdata))

class HTMLTableFormatter(TableFormatter):
    def headings(self, headers):
        print('<tr>', end='')
        for h in headers:
            print('<th>{}</th>'.format(h), end='')
        print('</tr>')

    def row(self, rowdata):
        print('<tr>', end='')
        for d in rowdata:
            print('<td>{}</td>'.format(d), end='')
        print('</tr>')

class QuotedMixin(object):
    def row(self, rowdata):
        quoted = [ '"{}"'.format(d) for d in rowdata ]
        super().row(quoted)

