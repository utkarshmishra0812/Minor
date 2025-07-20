# 🔬 Autopsy – Minor Project (Dec’24)
**Project Title:**  
**Prediction of Semiconductor Wavelengths from UV-Induced Color Emission**

**Status:** ✅ _Completed_

## 📌 Overview

This project focuses on the development of a machine learning model to **predict the emission wavelength of semiconductor materials** under UV light based on their visible color response. The aim is to bridge visual observation with quantitative spectral analysis using a lightweight, data-driven approach.

## 🎯 Objectives

- Develop a system that can estimate the **wavelength of light emitted** by semiconductor samples under UV exposure.
- Leverage computer vision for **color detection** from UV-illuminated images.
- Use a regression model to map **RGB values to physical wavelengths** in the visible spectrum.

## 🧠 Key Features

- 📷 **Frame Extraction** using OpenCV2 from UV-illuminated video clips or images.
- 🎨 **Color Detection & Normalization** using color space conversion and averaging.
- 📈 **Linear Regression Model** trained to predict **wavelength (in nm)** from color data.
- 📊 Achieved **90%+ prediction accuracy** on test samples within the visible range (approximately 380–750 nm).

## 🧰 Tools & Technologies

- **Python 3.x**
- **OpenCV2** – for image/frame processing
- **NumPy / Pandas** – for data handling
- **Scikit-learn** – for building and evaluating the regression model
- **Matplotlib / Seaborn** – for data visualization and result interpretation

## 📂 Project Structure

