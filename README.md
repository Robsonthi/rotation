# rotation
 How to rotate a point around axis

## How to use?

Main file: rotation.py

Choose the point_inicial, point_ref, vector_ref, k_points, theta_end and rotation_type (option: 'x', 'y', 'z' and 'custom').

## Examples
![Figure_x](https://github.com/user-attachments/assets/6b07eff2-b6ce-4397-b9a8-e0dc8239dc7d) ![Figure_y](https://github.com/user-attachments/assets/4db2e375-cf93-4f7e-b4ce-92d8ef2ddac8)

![Figure_z](https://github.com/user-attachments/assets/239129e1-1849-4e2a-af9b-e3d130d7e428) ![Figure_custom](https://github.com/user-attachments/assets/49e4e3aa-5261-46b1-a9ac-0ec562d60293)

## Rotation
The points in the space might be represented as a vector of size 4:

$$P=\begin{bmatrix}
p_x & p_y & p_z & 1 \\
\end{bmatrix}^T$$

Why size 4? Because a point with direction is represented as a matrix 4x4 (homogeneous matrix):

$$P=\begin{bmatrix}
n_x & o_x & a_x & p_x \\
n_y & o_y & a_y & p_y \\
n_z & o_z & a_z & p_z \\
0 & 0 & 0 & 1
\end{bmatrix}$$

To rotate a point around an axis, X, Y or Z, it’s simple, just perceive a matrix multiplication $$R(\theta) \cdot P$$.

To x-axis, we have $$P_{new}=R_x(\theta) \cdot P_{old}$$

$$R_x(\theta)=\begin{bmatrix}
1 & 0 & 0 & 0 \\
0 & cos(\theta) & -sin(\theta) & 0 \\
0 & sin(\theta) & cos(\theta) & 0 \\
0 & 0 & 0 & 1
\end{bmatrix}$$

To y-axis, we have $$P_{new}=R_y(\theta) \cdot P_{old}$$

$$R_y(\theta)=\begin{bmatrix}
cos(\theta) & 0 & sin(\theta) & 0 \\
0 & 1 & 0 & 0 \\
-sin(\theta) & 0 & cos(\theta) & 0 \\
0 & 0 & 0 & 1
\end{bmatrix}$$

To z-axis, we have $$P_{new}=R_z(\theta) \cdot P_{old}$$

$$R_z(\theta)=\begin{bmatrix}
cos(\theta) & -sin(\theta) & 0 & 0 \\
sin(\theta) & cos(\theta) & 0 & 0 \\
0 & 0 & 1 & 0 \\
0 & 0 & 0 & 1
\end{bmatrix}$$

What if you wanted to rotate a point around an arbitrary axis? If you know the point $$(a,b,c)$$ and direction of an axis $$(u,v,w)$$, you can rotate your point, using this matrix:

To custom-axis, we have $$P_{new}=R_\alpha(\theta,a,b,c,u,v,w) \cdot P_{old}$$

$$R_\alpha(\theta,a,b,c,u,v,w)=\begin{bmatrix}
u^2+(v^2+w^2)cos\theta & uv(1-cos\theta)-wsin\theta & uw(1-cos\theta)+vcos\theta & (a(v^2+w^2)-u(bv+cw))(1-cos\theta)+(bw-cv)sin\theta \\
uv(1-cos\theta)+wsin\theta & v^2+(u^2+w^2)cos\theta & vw(1-cos\theta)-usin\theta & (b(u^2+w^2)-v(au+cw))(1-cos\theta)+(cu-aw)sin\theta \\
uw(1-cos\theta)-vsin\theta & vw(1-cos\theta)+usin\theta & w^2+(u^2+v^2)cos\theta & (c(u^2+v^2)-w(au+bv))(1-cos\theta)+(av-bu)sin\theta \\
0 & 0 & 0 & 1
\end{bmatrix}$$

Reference: Glenn Murray, PhD (https://www.linkedin.com/in/glennmurrayphd/), His work: https://sites.google.com/site/glennmurray/Home/rotation-matrices-and-formulas
