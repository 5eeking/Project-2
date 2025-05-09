### Game Logic Functions ###

# NOTE: Import Section
# Imports required modules for the file
import math

# Function that returns a position around a circle based on input values
def get_circular_position(pos1, pos2, radius) -> tuple:
    """
    Gets the circular position around a circle using an angle between two points.
    Parameters:
        pos1: The first point for the circle.
        pos2: The second point for the circle.
        radius: The radius of the circle.
    Returns:
        tuple: The position around the circle at the given radius.
    """

    # Gets the disposition between pos1 and pos2
    dx, dy = pos2[0] - pos1[0], pos2[1] - pos1[1]
    # Gets the angle from pos1 to pos2
    angle = (math.atan2(dy, dx) * 180) / math.pi
    # Gets the correct position around a point using radius and the disposition
    x, y = pos1[0] + radius * math.cos(math.radians(angle)), pos1[1] + radius * math.sin(math.radians(angle))
    # Returns the calculated position
    return x, y

# Function that returns a Unit Vector of the based on input positions
def get_unit_vector(pos1, pos2) -> tuple:
    """
    Gets the normalized unit vector between two points.
    Parameters:
        pos1: The first point for the unit vector.
        pos2: The second point for the unit vector.
    Returns:
        tuple: The normalized unit vector.
    """

    # Gets the disposition between pos1 and pos2
    dx, dy = pos2[0] - pos1[0], pos2[1] - pos1[1]
    # Calculates the vector unit from pos1 to pos2
    vector = math.sqrt(math.pow(dx, 2) + math.pow(dy, 2))
    # Gets the Unit Vector for both x and y
    x_unit, y_unit = dx / vector, dy / vector
    # Returns the calculated Unit Vectors
    return x_unit, y_unit

# Checks the collision between two objects using a center, point from center, and a radius
def check_collide(center, point, radius) -> bool:
    """
    Checks if a circle is colliding with another circle.
    Parameters:
        center: The center of the circle.
        point: The point of the other circle.
        radius: The radius of the collision.
    Returns:
        bool: True if the circle is colliding with another circle.
    """

    # Gets the disposition from center to the point
    dx, dy = center[0] - point[0], center[1] - point[1]
    # Gets the distance the point is from the center
    d = math.sqrt(math.pow(dx, 2) + math.pow(dy, 2))
    # Checks if the point is within the radius
    result = True if d <= radius else False
    # Returns the result of the collision
    return result

def get_direction(pos1, pos2) -> int:
    """
    Gets the direction between two points.
    Parameters:
        pos1: The first point for the direction.
        pos2: The second point for the direction.
    Returns:
        tuple: The direction animation action.
    """

    # Finds the direction between two points and returns the action for the sprites.
    disposition = 30
    if (pos1[0] < pos2[0] - disposition) and (pos1[1] < pos2[1] - disposition):
        return 2
    elif (pos1[0] < pos2[0] - disposition) and (pos1[1] > pos2[1] + disposition):
        return 8
    elif (pos1[0] > pos2[0] + disposition) and (pos1[1] < pos2[1] - disposition):
        return 3
    elif (pos1[0] > pos2[0] + disposition) and (pos1[1] > pos2[1] + disposition):
        return 8
    else:
        if (pos1[0] >= pos2[0] - disposition) and (pos1[0] <= pos2[0] + disposition) and (
                pos1[1] <= pos2[1]):
            return 0
        elif (pos1[0] >= pos2[0] - disposition) and (pos1[0] <= pos2[0] + disposition) and (
                pos1[1] >= pos2[1]):
            return 6
        elif (pos1[0] <= pos2[0]) and (pos1[1] <= pos2[1] + disposition) and (
                pos1[1] >= pos2[1] - disposition):
            return 4
        elif (pos1[0] >= pos2[0]) and (pos1[1] <= pos2[1] + disposition) and (
                pos1[1] >= pos2[1] - disposition):
            return 5
        else:
            return 0