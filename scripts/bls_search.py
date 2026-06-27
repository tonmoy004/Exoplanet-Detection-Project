import lightkurve as lk
from astropy.timeseries import BoxLeastSquares
import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path

DATA_FILE = Path(__file__).parent.parent / "data" / "kepler10_q2.fits"

lc = lk.read(DATA_FILE)

# Clean data
clean_lc = lc.remove_nans()
flat_lc = clean_lc.flatten()

# Prepare arrays
time = flat_lc.time.value
flux = flat_lc.flux.value

# BLS search
bls = BoxLeastSquares(time, flux)

periods = np.linspace(0.5, 5, 10000)

power = bls.power(periods, 0.1)

best_period = periods[np.argmax(power.power)]

print("Best period =", best_period, "days")

# Plot periodogram
plt.figure(figsize=(10,5))
plt.plot(periods, power.power)
plt.xlabel("Period (days)")
plt.ylabel("BLS Power")
plt.title("BLS Periodogram")
plt.grid(True)
plt.show()