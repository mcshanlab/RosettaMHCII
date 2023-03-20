#!/usr/bin/python

'''

MHC class contains all the necessary functionalities required to fetch
necessary mhc sequences and their respective headers.

'''

# Load the Rosetta commands for use in the Python shell
from database.mhciibeta import mhciibeta
from database.mhciibeta_trim import mhciibeta_trim
from input_output.input.header_readers import HEADER_READER

# inherit from HEADER_READER, a generic class that reads
# headers from a file
class MHCIIBETA(HEADER_READER):

    # class member
    trim_mhc = True # to check if mhc sequence needs to be trimmed

    # constructor
    def __init__(self, filename, trim_mhc):
        super().__init__(filename)
        super().read_headers()
        self.trim_mhc = trim_mhc

    # getter methods
    # based on the trim flag, a full sequencce or a trimmed
    # sequence is returned
    def get_sequence(self, header):
        if self.trim_mhc == True:
            return mhciibeta_trim[header]
        else:
            return mhciibeta[header]

    # a user can just specify all in the input mhc list file
    # if it is specified, a full list of headers is returned
    # otherwise, only a requested subset of headers is returned
    def get_headers(self):
        if super().get_headers()[0].lower != "all":
            return super().get_headers()
        else:
            if self.trim_mhc == True:
                return mhciibeta_trim.keys()
            else:
                return mhciibeta.keys()
