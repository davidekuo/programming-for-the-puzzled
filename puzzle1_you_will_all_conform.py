# Puzzle 1: You Will All Conform
# https://ocw.mit.edu/courses/6-s095-programming-for-the-puzzled-january-iap-2018/pages/puzzle-1-you-will-all-conform/
# Input is a vector of F's and B's, in terms of forwards and backwards caps
# Output is a set of commands (printed out) to get either all F's or all B's
# Fewest commands is the goal


def intervals_to_flip(caps):
    intervals = {'F': [], 'B': []}
    start = 0
    end = start + 1

    for i in range(1, len(caps)):
        if caps[i] == caps[start]:  # still in same interval as start index
            end = i  # index i is new end of current interval
        else:  # now in new interval starting with caps[i]
            # save prev interval
            intervals[caps[start]].append((start, end))
            # reset params for new interval
            start = i
            end = i

    # save interval for last element (not processed in for-loop)
    intervals[caps[start]].append((start, end))

    print(caps, "\nPeople in positions ", end="")
    orientation_to_flip = 'F' if len(intervals['F']) <= len(intervals['B']) else 'B'
    for interval in intervals[orientation_to_flip]:
        print(f"({interval[0]} to {interval[1]}), ", end="")
    print("please flip your caps!\n")


def preprocessed_intervals_to_flip(caps):
    """
    Adding a dummy element to the end of the list (not 'F' or 'B')
    allows us to process the last element of the original list
    within the for-loop -> no need to handle end of list separately!
    """
    caps.copy().append('END')  # caps is passed by reference - changes here also change caps in main()

    intervals = {'F': [], 'B': []}
    start = 0
    end = start + 1

    # same as original method
    for i in range(1, len(caps)):
        if caps[i] == caps[start]:  # still in same interval as start index
            end = i  # index i is new end of current interval
        else:  # now in new interval starting with caps[i]
            # save prev interval
            intervals[caps[start]].append((start, end))
            # reset params for new interval
            start = i
            end = i

    # no need to handle end of list separately!

    print(caps, "\nPeople in positions ", end="")
    orientation_to_flip = 'F' if len(intervals['F']) <= len(intervals['B']) else 'B'
    for interval in intervals[orientation_to_flip]:
        print(f"({interval[0]} to {interval[1]}), ", end="")
    print("please flip your caps!\n")


def one_pass_intervals_to_flip(caps):
    """
    Key insight: the orientation to flip is the opposite of the orientation of the first person
    To illustrate, let {F} and {B} represent arbitrary intervals of 'F' and 'B' respectively
        - [{F}, {B}] -> flipping either orientation is the same
        - [{F}, {B}, {F}] -> flipping 'B' requires the fewest commands
        - [{F}, {B}, {F}, {B}] -> flipping either orientation is again the same
        - ...
    Thus, flipping the opposite orientation is always optimal
    """
    # we now only compare caps[-1] with caps[-2] and caps[0], so dummy variable can be anything
    caps.copy().append(caps[0])
    start = 0
    end = start + 1

    print(caps, "\nPeople in positions ", end="")
    for i in range(1, len(caps)):
        if caps[i] == caps[start]:  # still in same interval as start index
            end = i  # index i is new end of current interval
        else:  # now in new interval starting with caps[i]
            # if prev interval !match orientation of first person (index 0), print interval
            if caps[start] != caps[0]:
                print(f"({start} to {end}), ", end="")
            # reset params for new interval
            start = i
            end = i
    print("please flip your caps!\n")


def efficient_one_pass_intervals_to_flip(caps):
    """
    By being clever with our print statements, i.e.
        printing "({i} to " when starting a new interval with opposite orientation
        printing " {i-1}), " when starting a new interval with same orientation
    we can avoid explicitly tracking interval start/end indices
    """
    # we now only compare caps[-1] with caps[-2] and caps[0], so dummy variable can be anything
    caps.copy().append('END')  # I still think this is cleaner though

    print(caps, "\nPeople in positions ", end="")
    for i in range(1, len(caps)):
        if caps[i] != caps[i - 1]:
            if caps[i] != caps[0]:  # i marks start of new interval with opposite orientation
                print(f"({i} to ", end="")
            else:  # caps[i] == caps[0], i-1 marks end of interval with opposite orientation
                print(f"{i - 1}), ", end="")
    print("please flip your caps!\n")


def main():
    caps = ['F', 'F', 'B', 'B', 'B', 'F', 'B', 'B', 'B', 'F', 'F', 'B', 'F']
    caps2 = ['F', 'F', 'B', 'B', 'B', 'F', 'B', 'B', 'B', 'F', 'F', 'F', 'F']

    print("Original method:")
    intervals_to_flip(caps)
    intervals_to_flip(caps2)

    print("Preprocessing trick:")
    preprocessed_intervals_to_flip(caps)
    preprocessed_intervals_to_flip(caps2)

    print("One pass:")
    one_pass_intervals_to_flip(caps)
    one_pass_intervals_to_flip(caps2)

    print("Efficient one pass:")
    efficient_one_pass_intervals_to_flip(caps)
    efficient_one_pass_intervals_to_flip(caps2)


if __name__ == "__main__":
    main()
