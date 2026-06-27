import lightkurve as lk
from astropy.timeseries import BoxLeastSquares
import numpy as np
from pathlib import Path

# Read the saved FITS file
DATA_FILE = Path(__file__).parent.parent / "data" / "kepler10_q2.fits"

lc = lk.read(DATA_FILE)

# Clean data
clean_lc = lc.remove_nans()
flat_lc = clean_lc.flatten()

# BLS Search
time = flat_lc.time.value
flux = flat_lc.flux.value

bls = BoxLeastSquares(time, flux)

periods = np.linspace(0.5, 5, 10000)

power = bls.power(periods, 0.1)

best_period = periods[np.argmax(power.power)]

# Transit time
transit_time = power.transit_time[np.argmax(power.power)]

# Fold light curve
folded = flat_lc.fold(
    period=best_period,
    epoch_time=transit_time
)

# Bin folded light curve
binned = folded.bin(time_bin_size=0.005)

# Transit depth
minimum_flux = binned.flux.value.min()

transit_depth = 1 - minimum_flux

# Planet radius estimation
stellar_radius = 1.06  # Solar radii

planet_radius_solar = stellar_radius * np.sqrt(transit_depth)

planet_radius_earth = planet_radius_solar * 109

# Results Summary
print("\n")
print("======================================")
print("     EXOPLANET DETECTION RESULTS")
print("======================================")
print(f"Target Star           : Kepler-10")
print(f"Planet Candidate      : Kepler-10b")
print(f"Orbital Period        : {best_period:.5f} days")
print(f"Minimum Binned Flux   : {minimum_flux:.9f}")
print(f"Transit Depth         : {transit_depth:.9f}")
print(f"Transit Depth (ppm)   : {transit_depth*1e6:.2f}")
print(f"Planet Radius         : {planet_radius_solar:.5f} Solar Radii")
print(f"Planet Radius         : {planet_radius_earth:.2f} Earth Radii")
print("======================================")