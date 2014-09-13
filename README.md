AM-FM_decompy
=============

version 1.0.0 
(The pypi page is recommended for a quick installation. But you can also copy all directories here and then run the setup.py file.)

This package provides the tools necessary to decompose the voiced part of a speech signal into its modulated components, aka AM-FM decomposition. This designation is used due the fact that, in this method, the signal is modeled as a sum of amplitude- and frequency-modulated components. 

The goal is to overcome the drawbacks from Fourier-alike techniques, e.g. SFFT, wavelets, etc, which are limited in the time-frequency analysis by the so-called Heisenberg-Gabor inequality.

The algorithms here implemented are the QHM (Quasi-Harmonic Model), and its upgrades, aQHM (adaptive Quasi-Harmonic Model) and eaQHM (extended adaptive Quasi-Harmonic Model). Their formulation can be found at references [2-4].

Since that the tools mentioned above require a fundamental frequency reference, the package also includes the pitch tracker YAAPT (Yet Another Algorithm for Pitch Tracking), which is extermely robust for both high quality and telephone speech. 

Originally the YAAPT program in Matlab is provided for free by its authors, while the QHM algorithms I implemented by myself. The study of the AM-FM decomposition algorithms was the theme from my Master Thesis. I'm porting now them to python because:

1- the python language is easier to share and read, making 
2- is more resourceful than MATLAB script
3- the performance from its numeric and scientific packages (numpy and scipy) is equivalent to MATLAB.
4- python is free-to-use, while MATLAB is a propertary software.
  
Future expansions
=============
 
How to use
=============

Check the pYAAPT and pyQHM pdf documentation included in the respective folders.

Credits and Publications
=============

The original MATLAB YAAPT program was written by Hongbing Hu and Stephen A.Zahorian from the Speech Communication Laboratory of the State University of New York at Binghamton. 

It is available at http://www.ws.binghamton.edu/zahorian as free software. Further information about the program could be found at

    [1] "A spectral/temporal method for robust fundamental frequency tracking," 
        J.Acosut.Soc.Am. 123(6), June 2008.

The QHM algorithm and its upgrades are formulated and presented in the following publications:

    [2] Y. Pantazis, “Decomposition of AM-FM signals with applications in speech processing”, 
        PhD Thesis, University of Creta, 2010.

    [3] Y. Pantazis, O. Rosec and Y. Stylianou, “Adaptive AM-FM signal decomposition 
        with application to speech analysis”, IEEE Transactions on Audio, Speech and 
        Language Processing, vol. 19, n 2, 2011.

    [4] G. P. Kafentzis, Y. Pantazis, O. Rosec and Y. Stylianou, “An extension of the 
        adaptive quasi-harmonic model”, em IEEE International Conference on Acoustics, 
        Speech and Signal Processing (ICASSP), 2012.
  
Copyright and contact
=============
