# Extended Kalman Filter to estimate the State of Charge (SoC) 

Here we have 3 main steps: approximation, prediction and update. 

In the prediction step, the algorithm uses a battery model to predict the current state based on the previous state and input. 

Approximation step:

$$
x_k = f(x_{k-1}, u_k) + w_k,
$$

$$
y_k = h(x_k) + v_k,
$$

where $f$ and $h$ are non-linear functions, that describes behaviour of a system.

We use Taylor series:

$$
f(x_{k-1}, u_k) \approx f(\hat{x}{k-1}, u_k) + F_k(x{k-1} - \hat{x}_{k-1}),
$$

$$
h(x_k) \approx h(\hat{x}_k) + H_k(x_k - \hat{x}_k),
$$

where $F_k$, $H_k$ are Jacobi matrices of $f$ , $h$.


The following equations represents the prediction step:

$$
\hat{x}k^- = f(\hat{x}{k-1}, u_k),
$$

$$
P_k^- = F_kP_{k-1}F_k^T + Q_k,
$$

where:

* $\hat{x}_k^-$ is the predicted state at time $k$
* $f$ - nonlinear function of the model
* $\hat{x}_{k-1}$ - state estimation at the previous moment of time $k-1$
* $u_k$ - control action (like battery charging/discharging current)
* $P_k^-$ - predicted error covariance matrix
* $F_k$ is the Jacobi matrix of the function $f$ computed in $\hat{x}_{k-1}$
* $P_{k-1}$ is the error covariance matrix at the previous moment of time $k-1$
* $Q_k$ - covariance matrix of the process noise


In the update step, the algorithm incorporates the actual measurements from the battery sensors to correct the predicted state. The updated equations are:

$$
K_k = P_k^-H_k^T(H_kP_k^-H_k^T + R_k)^{-1},
$$

$$
\hat{x}_k = \hat{x}_k^- + K_k(y_k - h(\hat{x}_k^-)),
$$

$$
P_k = (I - K_kH_k)P_k^-,
$$

where:

* $K_k$ - Kalman gain
* $H_k$ - Jacobi matrix of function $h$ calculated in $\hat{x}_k^-$
* $R_k$ - covariance matrix of measurement noise
* $\hat{x}_k$ - updated state estimate
* $y_k$ - measurement vector
* $h$ - nonlinear function of measurements
* $P_k$ - updated error covariance matrix
