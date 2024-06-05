# Introduction

## Purpose
The purpose of this document is to provide a comprehensive specification for a battery state estimation system using the Extended Kalman Filter (EKF). The system aims to accurately estimate the state of charge (SoC) of a battery in real-time.

## References
- Kalman, R. E. (1960). A new approach to linear filtering and prediction problems. Journal of Basic Engineering.
- [Matplotlib documentation](https://matplotlib.org/stable/contents.html)
- [Numpy documentation](https://numpy.org/doc/stable/)
- [PlantUML documentation](https://plantuml.com/)

# Terminology

## Definitions

| Term                    | Definition                                                |
|-------------------------|------------------------------------------------------------|
| State of Charge (SoC)   | The remaining capacity of a battery expressed as a percentage|
| Extended Kalman Filter (EKF) | A recursive algorithm for estimating the state of a dynamic system|
| Thevenin model | The model describes the fixed parameters in the classic model as variables with the state of charge and temperature dynamics.|

## Abbreviations

| Abbreviation | Description |
|--------------|-------------|
| EKF          | Extended Kalman Filter |
| Open Circuit Voltage (OCV) | The voltage of the battery when no current is flowing. |
| SoC          | State of Charge        |
| OCV          | Open Circuit Voltage   |

# System Overall Description

## Product Overview
The battery state estimation system uses an EKF to estimate the SoC of a battery. It simulates the battery's behavior over time and provides real-time updates on the SoC and voltage.

## Product Functions
- Initialize and configure the EKF
- Simulate battery behavior using the Thevenin model
- Update battery simulation and EKF at each time step
- Plot simulation results

## Constraints

**Implementation restrictions**
- The system must be implemented in Python 3
- Must use standard libraries such as numpy and matplotlib

**Data limits**
- Accurate modeling of battery behavior within practical limits of current and voltage

## Dependencies
- Relies on external libraries: numpy, matplotlib

# Specific Requirements

## Interfaces

- **User Interface:** The system provides visual plots for battery voltage, SoC, and current.

## Functional Requirements

1. **Battery State Estimation**
   - Estimate the state of charge (SoC) of a battery using the EKF.

2. **Simulation and Visualization**
   - Simulate battery behavior over time and update SoC and voltage at each time step. 
   - Simulate battery voltage and current.
   - Plot true voltage, measured voltage, true SoC, estimated SoC, and current over time.

# Component Structure

The project is divided into the following components:

## Main Component (`main.py`)
- **init_EKF**: Initializes the Extended Kalman Filter with the given parameters.
- **plot_simulation_results**: Plots the simulation results including true voltage, measured voltage, true SoC, estimated SoC, and current.
- **update_simulation_step**: Updates the battery simulation and the EKF for the current time step.

## Battery Component (`Battery.py`)
- **Battery**: Simulates battery behavior using the Thevenin model. Includes methods for updating battery state, and properties for current, voltage, state of charge, and OCV.

## Polynomial Component (`Polynomial.py`)
- **Polynomial**: Represents and manipulates polynomials. Includes methods for evaluating the polynomial and computing its derivative.

## Extended Kalman Filter Component (`ExtendedKalmanFilter.py`)
- **ExtendedKalmanFilter**: Implements the EKF algorithm for state estimation of non-linear systems. Includes methods for updating and predicting the state estimate and covariance matrix.

## System Architecture Diagram
![1](https://github.com/Fireman9/SKteam_KLfilter/assets/84972080/c2332f19-e0cc-4365-9dd6-fbdf4f50d6d3)

