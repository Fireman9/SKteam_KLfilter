# Kalman Filter algorithm to estimate the State of Charge (SoC) 

Here we have 2 main steps: prediction and update. 

In the prediction step, the algorithm uses a battery model to predict the current state based on the previous state and input. 

The following equations represents the prediction step:

$$
x_k = Ax_{k-1} + Bu_k + w_k
$$

$$
y_k = Cx_k + v_k
$$

where:

* $x_k$ is the state vector at time step $k$
* $A$ is the state transition matrix
* $B$ is the input matrix
* $u_k$ is the input vector at time step $k$
* $w_k$ is the process noise
* $y_k$ is the measurement vector at time step $k$
* $C$ is the measurement matrix
* $v_k$ is the measurement noise

In the update step, the algorithm incorporates the actual measurements from the battery sensors to correct the predicted state. The updated equations are:

$$
K_k = P_k^-C^T(CP_k^-C^T + R)^{-1},
$$

$$
\hat{x}_k = \hat{x}_k^- + K_k(y_k - C\hat{x}_k^-),
$$

$$
P_k = (I - K_kC)P_k^-,
$$

where:

* $K_k$ is the Kalman gain at time step $k$
* $P_k^-$ is the predicted error covariance matrix at time step $k$
* $R$ is the measurement noise covariance matrix
* $\hat{x}_k^-$ is the predicted state estimate at time step $k$
* $\hat{x}_k$ is the updated state estimate at time step $k$
* $P_k$ is the updated error covariance matrix at time step $k$
