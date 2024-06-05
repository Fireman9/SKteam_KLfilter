## Software Design Document: Battery State Estimation using Extended Kalman Filter

# Introduction

## Purpose

The purpose of this document is to provide a comprehensive design for the battery state estimation software using the Extended Kalman Filter (EKF). This software aims to estimate the state of charge (SoC) of a battery accurately by implementing the EKF algorithm and simulating battery behavior based on a Thevenin model.

## References

- Kalman, R. E. (1960). A new approach to linear filtering and prediction problems.
- [Python Documentation](https://docs.python.org/3/)

# Terminology

## Definitions

| Term                  | Definition                                              |
|-----------------------|---------------------------------------------------------|
| State of Charge (SoC) | The current charge of the battery as a percentage of its total capacity. |
| Open Circuit Voltage (OCV) | The voltage of the battery when no current is flowing. |
| Extended Kalman Filter (EKF) | A recursive algorithm for estimating the state of a dynamic system|
| Thevenin model | The model describes the fixed parameters in the classic model as variables with the state of charge and temperature dynamics.|

## Abbreviations

| Abbreviation | Description                               |
|--------------|-------------------------------------------|
| EKF          | Extended Kalman Filter                    |
| SoC          | State of Charge                           |
| OCV          | Open Circuit Voltage                      |

# System Overview

## Features

- Estimation of battery state of charge using EKF.
- Simulation of battery behavior.
- Visualization of battery voltage, SoC, and current over time.

## System Components

1. **Battery Simulation (`Battery.py`)**
    - Simulates battery behavior.
    - Provides methods to update the battery state and calculate the terminal voltage.

2. **Polynomial Class (`Polynomial.py`)**
    - Represents polynomials and provides methods to evaluate and differentiate them.
  
3. **Extended Kalman Filter (`ExtendedKalmanFilter.py`)**
    - Implements the EKF algorithm for state estimation.
  
4. **Main Program (`main.py`)**
    - Initializes the EKF and battery simulation.
    - Runs the experiment protocol and plots the results.

## Communication between Subsystems

- The main program initializes and configures the EKF and battery simulation objects.
- The EKF uses the battery model to predict and update the state of charge based on measured voltages.
- The battery simulation provides the actual state and voltage for comparison with EKF estimates.

## System Characteristics

- Modular design allowing easy updates and maintenance.
- Configurable parameters for battery model and EKF settings.

## Input/Output

- **Input:** Battery parameters, current values, measurement noise.
- **Output:** Estimated state of charge, battery voltage, current, and plots of the results.

### Charts

- SoC over time
- Voltage over time
- Current over time

## User Interface

- The program uses `matplotlib` for plotting the results.
- No interactive GUI is provided; it is a command-line application.

# Sequence Diagrams

![2](https://github.com/Fireman9/SKteam_KLfilter/assets/84972080/6bcaa157-6dfb-452d-be36-a56036df838f)

# Interfaces

## Battery Simulation

### Methods

- **`update(time_delta)`**
    - **Description:** Updates the battery's state after a given time step.
    - **Parameters:**
        - `time_delta` (float): Time step in seconds.

- **`current` (property)**
    - **Getter:**
        - **Description:** Returns the current flowing through the battery (positive for discharge).
    - **Setter:**
        - **Description:** Sets the current flowing through the battery (positive for discharge).
        - **Parameters:**
            - `current` (float): Current value in Amps.

- **`voltage` (property)**
    - **Description:** Returns the terminal voltage of the battery.

- **`state_of_charge` (property)**
    - **Description:** Returns the State of Charge (SoC) of the battery as a fraction between 0 and 1.

- **`OCV_model` (property)**
    - **Description:** Returns the polynomial representation of the Open Circuit Voltage (OCV) as a function of State of Charge (SoC).

- **`OCV` (property)**
    - **Description:** Returns the Open Circuit Voltage (OCV) of the battery at the current State of Charge (SoC).

## Polynomial

### Methods

- **`__call__(x)`**
    - **Description:** Evaluates the polynomial at the given value of `x`.
    - **Parameters:**
        - `x` (float or int): Value at which to evaluate the polynomial.
    - **Returns:**
        - `float`: Value of the polynomial at `x`.

- **`deriv` (property)**
    - **Description:** Returns the derivative of the polynomial as a new Polynomial object.

## Extended Kalman Filter

### Methods

- **`update(z)`**
    - **Description:** Updates the state estimate and covariance matrix using the measurement `z`.
    - **Parameters:**
        - `z` (numpy.ndarray): Measurement vector.

- **`predict(u=0)`**
    - **Description:** Predicts the next state estimate and covariance matrix using the control input `u`.
    - **Parameters:**
        - `u` (numpy.ndarray or scalar, optional): Control input vector. Default is 0.

### Properties

- **`x`**
    - **Description:** Returns the current state estimate.
