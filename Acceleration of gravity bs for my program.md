# Acceleration of gravity bs for my program.md

---

Formula for finding the gravitational force between two objects,

$F=\dfrac{G\cdot m1\cdot m2}{d^2}$ -> (1)

---

Formula for finding force using mass and acceleration is,

$F=ma$ 

Which in this case would look like,

$F=m1\cdot g$ -> (2)

>[!note] Why $m1$? Why not $m2$?
>I used $m1$ because in my code that's the object that we're checking the velocity for.

---

Combining (1) and (2),

$m1\cdot a=\dfrac{G\cdot m1\cdot m2}{d^2}$ -> (3)

---

Since the time between the gravity checks is 1, acceleration is velocity.

Therefore,

$m1\cdot v=\dfrac{G\cdot m1\cdot m2}{d^2}$ -> (4)

---

Rearranging (4),

$v=\bigg(\dfrac{G\cdot m1\cdot m2}{d^2}\bigg)\div m1$ , i.e.,

$v=\bigg(\dfrac{G\cdot m1\cdot m2}{d^2}\bigg)\cdot \dfrac{1}{m1}$, i.e.,

$v=\dfrac{G\cdot m1\cdot m2}{d^2\cdot m1}$

Simplifying that will give us,

$v=\dfrac{G\cdot m2}{d^2}$ -> (5)

---

Now lets get the direction of the vector in (-1 or 1),

$\hat{dx}=\dfrac{x1-x2}{|x1-x2|}$ -> (6)

$\hat{dy}=\dfrac{y1-y2}{|y1-y2|}$ -> (7)

---

Lets convert (5) into a vector based formula using (6) and (7),

$\hat{vx}=\dfrac{G\cdot m2}{\hat{dx}^2}\cdot \hat{d_x}$ -> (8)

$\hat{vy}=\dfrac{G\cdot m2}{\hat{dy}^2}\cdot \hat{d_y}$ -> (9)

---

(8) and (9) is to be added to the past velocity of the object to be added to $\hat{vx}$ and $\hat{vy}$,

$\hat{vx_1}=\hat{vx_0}+\hat{vx}$

$\hat{vy_1}=\hat{vy_0}+\hat{vy}$
