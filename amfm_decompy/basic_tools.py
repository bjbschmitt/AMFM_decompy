# -*- coding: utf-8 -*-
"""
Auxiliary classes and functions for used by the other AMFM_decompy modules.

Version 1.0.11
23/Jan/2021 Bernardo J.B. Schmitt - bernardo.jb.schmitt@gmail.com
"""

import numpy as np
from scipy.signal import lfilter


"""
Creates a signal object.
"""

class SignalObj(object):

    def __init__(self, *args, **kwargs):
        output_dtype = kwargs.get('output_dtype', 'f')

        # Read the signal data from the path of a wav file.
        if len(args) == 1 or 'name' in kwargs:
            name = args[0] if len(args) == 1 else kwargs['name']

            try:
                from scipy.io import wavfile
            except:
                print("ERROR: Wav modules could not loaded!")
                raise KeyboardInterrupt
            self.fs, self.data = wavfile.read(name)
            self.name = name

        # Alternatively, read the signal from a Numpy array.
        elif len(args) == 2 or all (k in kwargs.keys() for k in ('data','fs')):
            data = args[0] if len(args) == 2 else kwargs['data']
            fs = args[1] if len(args) == 2 else kwargs['fs']

            self.data = data
            self.fs = fs


        # If the signal data is in the signed integer format (PCM), convert it
        # to float.
        if self.data.dtype.kind == 'i':
            self.nbits = self.data.itemsize*8
            self.data = pcm2float(self.data, output_dtype)

        self.size = len(self.data)
        self.fs = float(self.fs)

        # Check if the wav file is stereo.
        if self.size == self.data.size/2:
            print("Warning: stereo wav file. Converting it to mono for the analysis.")
            self.data = (self.data[:,0]+self.data[:,1])/2


    """
    Filters the signal data by a bandpass filter object and decimate it.
    """
    def filtered_version(self, bp_filter):

        # Filter the signal.
        tempData = lfilter(bp_filter.b, bp_filter.a, self.data)

        # Decimate the filtered output.
        self.filtered = tempData[0:self.size:bp_filter.dec_factor]
        self.new_fs = self.fs/bp_filter.dec_factor

    """
    Method that uses the pitch values to estimate the number of modulated
    components in the signal.
    """

    def set_nharm(self, pitch_track, n_harm_max):

        n_harm = (self.fs/2)/np.amax(pitch_track) - 0.5
        self.n_harm = int(np.floor(min(n_harm, n_harm_max)))

    """
    Adds a zero-mean gaussian noise to the signal.
    """

    def noiser(self, pitch_track, SNR):

        self.clean = np.empty((self.size))
        self.clean[:] = self.data

        RMS = np.std(self.data[pitch_track > 0])
        noise = np.random.normal(0, RMS/(10**(SNR/20)), self.size)
        self.data += noise

"""
Transform a pcm raw signal into a float one, with values limited between -1 and
1.
"""

def pcm2float(sig, output_dtype=np.float64):

     # Make sure it's a NumPy array.
    sig = np.asarray(sig)

    # Check if it is an array of signed integers.
    assert sig.dtype.kind == 'i', "'sig' must be an array of signed integers!"
    # Set the array output format. Accepts string as input argument for the
    # desired output format (e.g. 'f').
    out_dtype = np.dtype(output_dtype)

    # Note that 'min' has a greater (by 1) absolute value than 'max'!
    # Therefore, we use 'min' here to avoid clipping.
    return sig.astype(out_dtype) / out_dtype.type(-np.iinfo(sig.dtype).min)

