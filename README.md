# bio131
A repo containing my small project for Bio131. In order to run or open any of these files
you must have NumPy/SciPy installed, along with Python >= 3.5 and iPython/iPython
notebooks. To run, simply clone the repository (using `git clone https://github.com/guillean/bio131.git`)
and then open any of the files with the iPython notebook interface (by calling `ipython notebook` on
the current directory and opening the file you wish to read).

The content under `Gasket Color.ipynb` is based on the FLAM3 paper by Draves and Reckase, which can
be [found here](http://flam3.com/flame_draves.pdf) and is *well worth* a read. It's only slightly
mathematical, but not a difficult read and is quite nice.

For one, this is mostly a simple implementation meant to be generally understood. It has relatively
poor performance since most of the code uses very little BLAS, etc. implementations, and should
definitely not be used in production. For any kind of useful performance, this should be rewritten
in C (or, alternatively, there are many, many, many open source flame fractal renderers out there,
Google is your friend!).
