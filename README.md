# Exoplanet Detection Using the Transit Method

## Project Description

This project was carried out to study the detection of an exoplanet using the **Transit Method**. The analysis was performed using publicly available light curve data from the **NASA Kepler Mission**. The target star selected for this project is **Kepler-10**, which is known to host the exoplanet **Kepler-10b**.

The project uses Python along with scientific libraries such as **Lightkurve**, **Astropy**, **NumPy**, and **Matplotlib** to process the light curve, detect the transit signal, determine the orbital period, and estimate the radius of the planet.


# Objectives

The objectives of this project are:

* To download Kepler light curve data.
* To clean and process the observational data.
* To detect the transit signal using the Box Least Squares (BLS) algorithm.
* To determine the orbital period of the exoplanet.
* To fold the light curve using the detected period.
* To calculate the transit depth.
* To estimate the radius of the exoplanet.
* To visualize the results using different plots.


# Project Structure

Exoplanet Detection Project/

    .venv/
    data/
       kepler10_q2.fits
    plots/
       lightcurve.png
       bls_periodogram.png
       folded_lightcurve.png
    scripts/
       download_data.py
       plot_lightcurve.py
       bls_search.py
       fold_lightcurve.py
       results_summary.py
    requirements.txt
    README.md




# Python Libraries Used

The following Python libraries were used in this project:

* Lightkurve
* Astropy
* NumPy
* SciPy
* Pandas
* Matplotlib



# Installation

### Create a virtual environment
python -m venv .venv


### Activate the virtual environment (Windows)
.\.venv\Scripts\activate.bat

### Install the required packages
pip install -r requirements.txt




# Running the Project

### Step 1: Download the light curve data
python scripts/download_data.py

This downloads the Kepler Quarter 2 light curve and stores it in the `data` folder as a FITS file.

### Step 2: Plot the original light curve
python scripts/plot_lightcurve.py


### Step 3: Perform the Box Least Squares (BLS) search
python scripts/bls_search.py


### Step 4: Generate the folded light curve
python scripts/fold_lightcurve.py


### Step 5: Display the final results
python scripts/results_summary.py



# Methodology

The following procedure was followed in this project:

1. Download the Kepler Quarter 2 light curve of Kepler-10.
2. Store the data locally in FITS format.
3. Remove missing values from the light curve.
4. Flatten the light curve to remove long-term trends.
5. Apply the Box Least Squares (BLS) algorithm to detect the periodic transit signal.
6. Determine the orbital period of the exoplanet.
7. Fold the light curve using the detected orbital period.
8. Calculate the transit depth from the folded light curve.
9. Estimate the planetary radius using the measured transit depth.


# Sample Output

Target Star          : Kepler-10

Planet Candidate     : Kepler-10b

Orbital Period       : 0.83753 days

Transit Depth        : 202.86 ppm

Estimated Radius     : 1.65 Earth Radii


# Data Source

The observational data used in this project were obtained from the **NASA Kepler Mission** through the **Lightkurve** Python package. The downloaded dataset corresponds to **Quarter 2** observations of **Kepler-10 (KIC 11904151)**.


# Conclusion

This project demonstrates how the transit method can be used to detect an exoplanet using real observational data. By analysing the Kepler light curve, the orbital period and transit depth of Kepler-10b were successfully determined, and the planetary radius was estimated. The project provides a practical introduction to computational techniques used in modern observational astronomy.


# Author
**Tonmoy Goswami**
  M.Sc. Physics
  National Institute of Technology Meghalaya
  tonmoygoswami111@gmail.com
