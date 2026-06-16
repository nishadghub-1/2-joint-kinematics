import math


def set_robot(theta1, theta2, l1, l2):
    """Collect joint angles (degrees) and link lengths, return end-effector (x, y)."""
    t1 = math.radians(theta1)
    t2 = math.radians(theta2)

    x = l1 * math.cos(t1) + l2 * math.cos(t1 + t2)
    y = l1 * math.sin(t1) + l2 * math.sin(t1 + t2)

    return (x, y)


if __name__ == "__main__":
    position = set_robot(45, 30, 1.0, 0.8)
    print(f"End-effector: x = {position[0]:.4f}, y = {position[1]:.4f}")
