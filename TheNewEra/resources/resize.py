def calnewcord(original_x, original_y, original_width, original_height, new_width, new_height):
    # Calculate the scaling factors
    scale_x = new_width / original_width
    scale_y = new_height / original_height

    # Calculate the new coordinates for the object
    new_x = original_x * scale_x
    new_y = original_y * scale_y

    return new_x, new_y