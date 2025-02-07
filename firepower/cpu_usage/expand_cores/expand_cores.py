# Description: This script expands the core list, whether it's a range (e.g., 10-11) or individual cores (e.g., 10, 48)
# into a list of core numbers.


def expand_cores(cores):
    # Handle ranges like "10-11" and individual core numbers like "10,28"
    expanded_cores = []
    for part in cores.split(','):
        if '-' in part:
            start, end = map(int, part.split('-'))
            expanded_cores.extend(str(i) for i in range(start, end + 1))
        else:
            expanded_cores.append(part.strip())
    return expanded_cores
