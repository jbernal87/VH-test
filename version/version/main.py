def compare_versions(string_a, string_b):
    version_parts1 = [x for x in str(string_a).split('.')]
    version_parts2 = [x for x in str(string_b).split('.')]

    difference = len(version_parts1) - len(version_parts2)
    if difference > 0:
        version_parts2.extend(['0'] * difference)
    elif difference < 0:
        version_parts1.extend(['0']*(abs(difference)))

    for element1, element2 in zip(version_parts1, version_parts2):
        if element1 > element2:
            return 1
        elif element2 > element1:
            return -1
        else:
            pass

    return 0
