==========
AidEasyPea
==========

AidEasyPea takes data from an Acoustic Doppler Current Profiler (ADCP) and plots it. Both 2D profile plots and 3D bathymetry plots are available.

ADCP data can be provided in a text file, or data can be aquired directly from the ADCP. Our hardware for testing is a Workhorse Rio Grande RiverBoat manufactured by Teledyne RD Instruments (http://www.rdinstruments.com). Text file data is output by their WinRiver II application. The data from the ADCP can also be linked with GPS data, which is especially useful for bathymetry plots.

There are also future plans to include the Argonaut ADV manufactured by Sontek/YSI (http://www.sontek.com/argonautadv.php).

AidEasyPea is written in Python. It uses Qt for the GUI as well as some database drivers etc. The 3D models and 2D charts are done with the Enthought Tool Suite (ETS); specifically Mayavi2 and Chaco. 
