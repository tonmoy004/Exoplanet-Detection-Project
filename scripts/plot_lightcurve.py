import lightkurve as lk
import matplotlib.pyplot as plt
from pathlib import Path

DATA_FILE = Path(__file__).parent.parent / "data" / "kepler10_q2.fits"

# Read the saved Kepler light curve
lc = lk.read(DATA_FILE)

# Display information about the FITS file
print("Mission :", lc.meta.get("MISSION"))
print("Quarter :", lc.meta.get("QUARTER"))
print("Target  :", lc.meta.get("OBJECT"))

# Clean the data
clean_lc = lc.remove_nans()

# Remove long-term trends
flat_lc = clean_lc.flatten()

# Plot
plt.figure(figsize=(12,6))

plt.scatter(
    flat_lc.time.value,
    flat_lc.flux.value,
    s=1,
    alpha=0.5
)

plt.xlabel("Time (days)")
plt.ylabel("Normalized Flux")
plt.title("Kepler-10 Light Curve (Quarter 2)")
plt.grid(True)

plt.show()

print("Minimum Flux =", flat_lc.flux.min())
print("Maximum Flux =", flat_lc.flux.max())