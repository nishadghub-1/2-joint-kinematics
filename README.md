# 2-Joint Kinematics

A Python implementation of forward kinematics for a 2-joint planar robotic arm.

## What it does

Given two joint angles and two link lengths, calculates the (x, y) position of the end-effector using standard planar forward kinematics equations.

```
Base ──(l1)──○──(l2)──> End-effector
          θ1       θ2
```

## Usage

```python
from kinematics import set_robot

x, y = set_robot(theta1=45, theta2=30, l1=1.0, l2=0.8)
print(f"End-effector: x = {x:.4f}, y = {y:.4f}")
```

**Output:**
```
End-effector: x = 0.9142, y = 1.4798
```

## Parameters

| Parameter | Type  | Description                        |
|-----------|-------|------------------------------------|
| `theta1`  | float | Joint 1 angle in degrees           |
| `theta2`  | float | Joint 2 angle in degrees           |
| `l1`      | float | Length of link 1                   |
| `l2`      | float | Length of link 2                   |

**Returns:** `(x, y)` tuple — end-effector position in the same units as `l1`/`l2`.

## Requirements

No external dependencies — uses Python's built-in `math` module only.

Requires Python 3.6+.

## License

MIT
