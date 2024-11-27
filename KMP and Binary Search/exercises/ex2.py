def calculate_partial_match_table(sequence):
    table = [0] * len(sequence)
    for index in range(1, len(sequence)):
        position = table[index - 1]
        while position > 0 and sequence[index] != sequence[position]:
            position = table[position - 1]
        if sequence[index] == sequence[position]:
            position += 1
        table[index] = position
    return table


def get_minimum_circular_shift(base, rotated):
    if len(base) != len(rotated) or sorted(base) != sorted(rotated):
        return -1
    if base == rotated:
        return 0

    combined = rotated + base
    partial_match_table = calculate_partial_match_table(combined)
    longest_match = partial_match_table[-1]

    original_length = len(base)
    if combined[longest_match:original_length] == combined[original_length:len(combined) - longest_match]:
        return longest_match
    return -1


base_string = input()
rotated_string = input()
shift_count = get_minimum_circular_shift(base_string, rotated_string)
print(shift_count)
