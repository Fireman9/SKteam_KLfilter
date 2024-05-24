---
title: Battery State Estimation using Extended Kalman Filter
author: [Your Name]
version: 1.0
---

# Introduction

## Purpose
The purpose of this document is to provide a comprehensive specification for a battery state estimation system using the Extended Kalman Filter (EKF). The system aims to accurately estimate the state of charge (SoC) of a battery in real-time.

## References {#ref}
- Kalman, R. E. (1960). A new approach to linear filtering and prediction problems. Journal of Basic Engineering.
- [Matplotlib documentation](https://matplotlib.org/stable/contents.html)
- [Numpy documentation](https://numpy.org/doc/stable/)
- [PlantUML documentation](https://plantuml.com/)

# Terminology {#term}

## Definitions

| Term                    | Definition                                                |
|-------------------------|------------------------------------------------------------|
| State of Charge (SoC)   | The remaining capacity of a battery expressed as a percentage|
| Extended Kalman Filter (EKF) | A recursive algorithm for estimating the state of a dynamic system|

## Abbreviations

| Abbreviation | Description |
|--------------|-------------|
| EKF          | Extended Kalman Filter |
| SoC          | State of Charge        |
| OCV          | Open Circuit Voltage   |

# System Overall Description {#overall}

## Product Overview
The battery state estimation system uses an EKF to estimate the SoC of a battery. It simulates the battery's behavior over time and provides real-time updates on the SoC and voltage.

## Product Functions
- Initialize and configure the EKF
- Simulate battery behavior using the Thevenin model
- Update battery simulation and EKF at each time step
- Plot simulation results

## Constraints

**Implementation restrictions**
- The system must be implemented in Python 3.x
- Must use standard libraries such as numpy and matplotlib

**Resource limits**
- Must run efficiently on a typical personal computer
- Real-time execution requirements for EKF updates

**Data limits**
- Accurate modeling of battery behavior within practical limits of current and voltage

## Assumptions and Dependencies
- Assumes availability of accurate OCV vs SoC data for the battery
- Relies on external libraries: numpy, matplotlib

# Specific Requirements

## Interfaces

- **User Interface:** The system provides visual plots for battery voltage, SoC, and current.
- **Software Interface:** Interfaces with numpy for numerical calculations and matplotlib for plotting.

## Functional Requirements

1. **Battery State Estimation**
   - Estimate the state of charge (SoC) of a battery using the EKF.
   - Simulate battery voltage and current using the Thevenin model.

2. **Simulation and Visualization**
   - Simulate battery behavior over time and update SoC and voltage at each time step.
   - Plot true voltage, measured voltage, true SoC, estimated SoC, and current over time.

3. **Polynomial Operations**
   - Evaluate the OCV polynomial at a given SoC.
   - Compute the derivative of the OCV polynomial.

# Data requirements
- Accurate polynomial coefficients for the OCV model.
- Initial battery parameters: capacity, resistance, and capacitance values.

## System Architecture Diagram
```plantuml
@startuml
!define RECTANGLE class

package "Battery State Estimation System" {
    RECTANGLE main {
        def init_EKF(R0, R1, C1, std_dev, time_step, Q_tot)
        def plot_simulation_results(time, true_voltage, mes_voltage, true_SoC, estim_SoC, current)
        def update_simulation_step(actual_current)
    }

    RECTANGLE Battery {
        +total_capacity: float
        +actual_capacity: float
        +R0: float
        +R1: float
        +C1: float
        +current: float
        +RC_voltage: float
        +OCV_model: Polynomial

        +update(time_delta)
        +current: float
        +voltage: float
        +state_of_charge: float
        +OCV_model: Polynomial
        +OCV: float
    }

    RECTANGLE Polynomial {
        +_coeffs: list
        +_deg: int

        +__call__(x)
        +deriv()
    }

    RECTANGLE ExtendedKalmanFilter {
        +_x: numpy.ndarray
        +_F: numpy.ndarray
        +_B: numpy.ndarray
        +_P: numpy.ndarray
        +_Q: numpy.ndarray
        +_R: numpy.ndarray
        +_Hx: callable
        +_HJacobian: callable

        +update(z)
        +predict(u=0)
        +x: numpy.ndarray
    }

    RECTANGLE launch_experiment_protocol {
        +launch_experiment_protocol(Q_tot, time_step, experiment_callback)
    }

    main --> Battery
    main --> Polynomial
    main --> ExtendedKalmanFilter
    main --> launch_experiment_protocol
    Battery --> Polynomial
}
@enduml

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

## Experiment Protocol Component (`launch_experiment_protocol.py`)
- **launch_experiment_protocol**: Simulates a battery charge and discharge experiment by calling an external callback function with the desired current values at each time step.