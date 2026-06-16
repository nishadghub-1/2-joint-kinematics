import math


def set_joint_angles(theta1, theta2):
    """Set the two joint angles in degrees."""
    return (math.radians(theta1), math.radians(theta2))


def set_link_lengths(l1, l2):
    """Set the two link lengths."""
    return (l1, l2)


def forward_kinematics(angles, lengths):
    """
    Calculate end-effector (x, y) position using planar 2-joint forward kinematics.

    angles:  tuple of (theta1, theta2) in radians
    lengths: tuple of (l1, l2)
    """
    theta1, theta2 = angles
    l1, l2 = lengths

    x = l1 * math.cos(theta1) + l2 * math.cos(theta1 + theta2)
    y = l1 * math.sin(theta1) + l2 * math.sin(theta1 + theta2)

    return (x, y)


if __name__ == "__main__":
    angles = set_joint_angles(45, 30)
    lengths = set_link_lengths(1.0, 0.8)
    position = forward_kinematics(angles, lengths)

    print(f"Joint 1 angle : 45°, Joint 2 angle : 30°")
    print(f"Link 1 length : {lengths[0]}, Link 2 length : {lengths[1]}")
    print(f"End-effector  : x = {position[0]:.4f}, y = {position[1]:.4f}")
