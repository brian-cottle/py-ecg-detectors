# %%
import numpy as np
import matplotlib.pyplot as plt
import pathlib
from ecgdetectors import Detectors
import sys

example_dir = './example_data/ECG.tsv'
unfiltered_ecg_dat = np.loadtxt(example_dir) 
unfiltered_ecg = unfiltered_ecg_dat[:, 0]
fs = 250

detectors = Detectors(fs)

r_peaks = detectors.wqrs_detector(unfiltered_ecg)

plt.figure()
plt.plot(unfiltered_ecg)
plt.plot(r_peaks, unfiltered_ecg[r_peaks], 'ro')
plt.title("Detected R peaks")

plt.show()
# %%

g_ecg = np.loadtxt('./+trichostatin A -0.txt') 
g_subsection = g_ecg[5000:8000,1]
r_peaks = detectors.wqrs_detector(g_subsection)

plt.figure()
plt.plot(g_subsection)
plt.plot(r_peaks, g_subsection[r_peaks], 'ro')
plt.title("Detected R peaks")

plt.show()
# %%
