def unittest(data_path, temp_path):
    import image
    lab = image.rgb_to_lab((120, 200, 120))
    return  (lab[0] == 74 and lab[1] == -38 and lab[2] == 30)
