### Existing projects on SoC est. (KF algorithms)

1. **Extended Kalman Filter for Electric Vehicles (EKF-EV)** [[Article](https://www.mdpi.com/2313-0105/9/12/583)]:
    - **Upsides**: Utilizes the robustness of model-driven methods and the extended Kalman filter (EKF) for optimal SOC estimation based on an equivalent circuit model (ECM). It benefits from model accuracy, even with imprecise initial SOC values and possible measurement noise.
    - **Downsides**: Depends largely on the underlying battery model's accuracy and can be computationally intensive due to the necessary iterations within the Bayesian framework[].

2. **Dual Extended Kalman Filter for Lithium-Sulfur Batteries** [[Article](https://www.mdpi.com/1996-1073/15/19/6989)]:
    - **Upsides**: Addresses large non-observable regions that may hinder the state estimation algorithm's convergence, improving accuracy and reducing instability by incorporating cell degradation and temperature effects.
    - **Downsides**: Complexity increases due to the dual filtering approach and the need for parameter estimation algorithms alongside cell models.

3. **Adaptive Infinite Kalman Filter (AUKF) for Lithium Batteries** [[Article](https://www.mdpi.com/1996-1944/15/24/8744)]:
    - **Upsides**: Demonstrates faster convergence and lower mean absolute error compared to other methods, making it highly suitable for real-time SOC estimation under varying conditions.
    - **Downsides**: The implementation complexity and requirement for accurate initial parameters could limit its immediate application without extensive testing.

### Our function set:

Based on the insights from existing projects, we introduce an example of the potential function set:

1. **Model Accuracy and Robustness**: We can employ model-driven methods for enhanced robustness against measurement noise and imprecise SOC initialization, as seen in EKF-based systems.

2. **Real-Time Processing**: Let's ensure that the algorithm can perform real-time SOC estimation, balancing computational efficiency with estimation accuracy.

3. **Scalability and Compatibility**: Let's ensure that the solution is scalable to different battery types and compatible with various BMS architectures to maximize its applicability.

By integrating these features, the new project aims to overcome the downsides observed in existing systems while enhancing their upsides for better performance and reliability.
