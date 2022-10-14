# add all goal tests here

def zero_first_test(state):
    index = 0
    for row in range(3):
        for col in range(3):
            if index != state[row][col]:
                return False
            index += 1
    return True


def zero_last_test(state):
    index = 0
    for row in range(3):
        for col in range(3):
            value = state[row][col]
            if index == 8: # last position
                return value == 0
            elif value != index+1:
                    return False
            index += 1
    return True