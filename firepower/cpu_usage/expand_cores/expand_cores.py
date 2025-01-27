# Description: This script expands the core list, whether it's a range (e.g., 10-11) or individual cores (e.g., 10, 48) into a list of core numbers.


def expand_cores(cores):
    """
    Expands the core list, whether it's a range (e.g., 10-11) or individual cores (e.g., 10, 48) into a list of core numbers.
    """
    expanded_cores = []
    for part in cores.split(','):
        if '-' in part:
            # If it's a range (e.g., 10-11), expand the range
            start, end = map(int, part.split('-'))
            expanded_cores.extend(range(start, end + 1))
        else:
            # If it's an individual core, just add it
            expanded_cores.append(int(part))
    return expanded_cores
