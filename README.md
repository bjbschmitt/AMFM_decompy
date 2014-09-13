AM-FM_decompy
=============

version 1.0.0

(The pypi page is recommended for a quick installation. But you can also copy all directories here and then run the setup.py file.)

This python package provides the tools necessary to decompose the voiced part of a speech signal into its modulated components, aka AM-FM decomposition. This designation is used due the fact that, in this method, the signal is modeled as a sum of amplitude- and frequency-modulated components. 

The goal is to overcome the drawbacks from Fourier-alike techniques, e.g. SFFT, wavelets, etc, which are limited in the time-frequency analysis by the so-called Heisenberg-Gabor inequality.

The algorithms here implemented are the QHM (Quasi-Harmonic Model), and its upgrades, aQHM (adaptive Quasi-Harmonic Model) and eaQHM (extended adaptive Quasi-Harmonic Model). Their formulation can be found at references [2-4].

Since that the tools mentioned above require a fundamental frequency reference, the package also includes the pitch tracker YAAPT (Yet Another Algorithm for Pitch Tracking) [1], which is extermely robust for both high quality and telephone speech. 

The study of the AM-FM decomposition algorithms was the theme from my Master Thesis. The original YAAPT program in MATLAB is provided for free by its authors, while the QHM algorithms I implemented by myself also in MATLAB. I'm porting them now to python because:

* the python language is easier to share, read and understand, making it a better way to distribute the codes;
* is more resourceful than MATLAB (with different data structures, scripting options, etc), which will be usuful for me in future studies;
* the computational performance from its numeric and scientific packages (numpy and scipy) is equivalent to MATLAB;
* python is free-to-use, while MATLAB is a propertary software;

Evaluations and future expansions
=============

As for the algorithms computational performance, I optimized the YAAPT code, so that my pyhton version runs now about twice as fast as the original MATLAB one. However, the QHM algorithms still run as fast as thier counterparts in MATLAB. That's because the main bottleneck of both versions are the matrix dot and least-squares operations. Since numpy and MATLAB are already optimized to perform these tasks using internal Fortran functions, as far as I investigated, there's no way to speed them up. Nevertheless, I still looking for ways to make my code faster.

YAAPT formulation contact its authors
 
How to use
=============

Check the pYAAPT and pyQHM pdf documentations included in their respective folders.

Credits and Publications
=============

The original MATLAB YAAPT program was written by Hongbing Hu and Stephen A.Zahorian from the Speech Communication Laboratory of the State University of New York at Binghamton. 

It is available at http://www.ws.binghamton.edu/zahorian as free software. Further information about the program could be found at

    [1] "A spectral/temporal method for robust fundamental frequency tracking," 
        J.Acosut.Soc.Am. 123(6), June 2008.

The QHM algorithm and its upgrades are formulated and presented in the following publications:

    [2] Y. Pantazis, “Decomposition of AM-FM signals with applications in speech 
        processing”, PhD Thesis, University of Creta, 2010.

    [3] Y. Pantazis, O. Rosec and Y. Stylianou, “Adaptive AM-FM signal decomposition 
        with application to speech analysis”, IEEE Transactions on Audio, Speech and 
        Language Processing, vol. 19, n 2, 2011.

    [4] G. P. Kafentzis, Y. Pantazis, O. Rosec and Y. Stylianou, “An extension of the 
        adaptive quasi-harmonic model”, em IEEE International Conference on Acoustics, 
        Speech and Signal Processing (ICASSP), 2012.
  
Copyright and contact
=============

The AM-FM_decompy is free to use, share and modify under the terms of the MIT license.

Questions, comments, suggestions, and contributions are welcome. Please contact me at bernardo.jb.schmitt@gmail.com.
