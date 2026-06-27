import lightkurve as lk
from astropy.timeseries import BoxLeastSquares
import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path

DATA_FILE = Path(__file__).parent.parent / "data" / "kepler10_q2.fits"

lc = lk.read(DATA_FILE)

# Clean the light curve
clean_lc = lc.remove_nans()
flat_lc = clean_lc.flatten()

# BLS Transit Search
time = flat_lc.time.value
flux = flat_lc.flux.value

bls = BoxLeastSquares(time, flux)

periods = np.linspace(0.5, 5, 10000)

power = bls.power(periods, 0.1)

best_period = periods[np.argmax(power.power)]

print("Best Period =", best_period, "days")

# Find transit time
transit_time = power.transit_time[np.argmax(power.power)]

# Fold the light curve
folded = flat_lc.fold(
    period=best_period,
    epoch_time=transit_time
)

# Bin the folded light curve
binned = folded.bin(time_bin_size=0.005)

# Calculate transit depth
minimum_flux = binned.flux.value.min()

transit_depth = 1 - minimum_flux

print("Minimum Binned Flux =", minimum_flux)

print("Transit Depth =", transit_depth)

print("Transit Depth (ppm) =", transit_depth * 1_000_000)

# Estimate planet radius
stellar_radius = 1.06        # Solar radii

planet_radius_solar = stellar_radius * np.sqrt(transit_depth)

planet_radius_earth = planet_radius_solar * 109

print("Planet Radius =", planet_radius_solar, "Solar Radii")

print("Planet Radius =", planet_radius_earth, "Earth Radii")

# Plot
plt.figure(figsize=(10, 6))

plt.scatter(
    folded.phase.value,
    folded.flux.value,
    s=2,
    alpha=0.2,
    label="Raw Data"
)

plt.plot(
    binned.phase.value,
    binned.flux.value,
    linewidth=2,
    label="Binned Data"
)

plt.xlabel("Phase")

plt.ylabel("Normalized Flux")

plt.title(
    f"Phase Folded Light Curve (P = {best_period:.5f} days)"
)

plt.legend()

plt.grid(True)

plt.show()