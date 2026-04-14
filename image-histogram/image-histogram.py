def image_histogram(image):
    """
    Compute the intensity histogram of a grayscale image.
    """
    # Write code 
    a = [0 for i in range(256)]
    for list in image:
        for i in list:
            a[i] += 1
            
    return a