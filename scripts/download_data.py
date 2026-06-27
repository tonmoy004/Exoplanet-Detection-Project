import lightkurve as lk
import os

# Search for Kepler-10 data
search_result = lk.search_lightcurve(
    "Kepler-10",
    mission="Kepler",
    quarter=2,
    exptime=1800
)

# Download
lc = search_result.download()

# Create data folder if it doesn't exist
os.makedirs("../data", exist_ok=True)

# Save as FITS file
filename = "../data/kepler10_q2.fits"
lc.to_fits(path=filename, overwrite=True)

print("Light curve saved successfully!")
print("Location:", filename)