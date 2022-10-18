#!/usr/bin/env python3

"""
CHN_2_TXT.py

Converts ORTEC .Chn files to .txt files.

To run this file, you'll need python3 installed and all of the .Chn files in a
directory named "CHN_Files" as well as an empty directory named "TXT_Files".
Both of these directories should be located in the same parent directory as
this file.
"""

import os
import struct

import numpy as np


class gamma_data:
    def __init__(self, filename):
        try:
            self.infile = open(filename, "rb")
            self.read_chn_binary()
        except ValueError:
            print("Unable to load file " + filename)

    def read_chn_binary(self):  # We start by reading the 32 byte header
        self.CHECK_BIT = struct.unpack("h", self.infile.read(2))[0]
        if self.CHECK_BIT != -1:
            print("Error in reading CHN file.\n")
            self.infile.close()
            return None
        self.mca_detector_id = struct.unpack("h", self.infile.read(2))[0]
        self.segment_number = struct.unpack("h", self.infile.read(2))[0]
        self.start_time_ss = self.infile.read(2)
        self.real_time = struct.unpack("I", self.infile.read(4))[0]
        self.live_time = struct.unpack("I", self.infile.read(4))[0]
        self.start_date = self.infile.read(8)  # Ascii type date in
        # DDMMMYY* where * == 1 means 21th century
        self.start_time_hhmm = self.infile.read(4)
        self.chan_offset = struct.unpack("h", self.infile.read(2))[0]
        self.no_channels = struct.unpack("h", self.infile.read(2))[0]
        self.hist_array = np.zeros(self.no_channels)  # Init hist_array
        # Read the binary data
        for index in range(len(self.hist_array)):
            self.hist_array[index] = struct.unpack("I", self.infile.read(4))[0]
        assert struct.unpack("h", self.infile.read(2))[0] == -102
        self.infile.read(2)
        self.en_zero_inter = struct.unpack("f", self.infile.read(4))[0]
        self.en_slope = struct.unpack("f", self.infile.read(4))[0]
        self.en_quad = struct.unpack("f", self.infile.read(4))[0]
        self.infile.close()

    def write_txt(self, fname):
        tf = open(fname[:-4] + ".txt", "w")
        tf.writelines(
            [
                "# Filename : " + fname,
                "\n# MCA detector ID: " + str(self.mca_detector_id),
                "\n# Start time : "
                + str(self.start_time_hhmm[:2])
                + ":"
                + str(self.start_time_hhmm[:2])
                + ":"
                + str(self.start_time_ss),
                "\n# Start date : " + str(self.start_date),
                "\n# No channels : " + str(self.no_channels),
                "\n# Live time : " + str(self.live_time),
                "\n# Real time : " + str(self.real_time),
                "\n# En cal factors A + B*x + C*x*x",
                "\n# A : " + str(self.en_zero_inter),
                "\n# B : " + str(self.en_slope),
                "\n# C : " + str(self.en_quad),
            ]
        )
        for i in self.hist_array:
            tf.write(str(int(i)) + "\n")
        tf.close()


if __name__ == "__main__":
    input_directory = "CHN_Files"
    output_directory = "TXT_Files"
    for file in os.listdir(input_directory):
        input_filename = os.path.join(input_directory, file)
        if os.path.isfile(input_filename):
            if input_filename[-3:] != "Chn":
                continue
            gamma_object = gamma_data(os.path.join(input_directory, file))
            gamma_object.write_txt(os.path.join(output_directory, file))