# Puzzle 2: The Best Time to Party
# https://ocw.mit.edu/courses/6-s095-programming-for-the-puzzled-january-iap-2018/pages/puzzle-2-the-best-time-to-party/
# Given a list of intervals [i, j) when celebrities will be at the party
# such that the celebrity is present through the ith hour but gone by the jth hour,
# find the time that you want to go the party i.e. when the maximum number of celebrities are there.

from collections import Counter


def best_time_to_party(schedule):
    hrs_celeb_present = []
    for interval in schedule:
        hrs_celeb_present += list(range(interval[0], interval[1]))
    print(Counter(hrs_celeb_present).most_common())
    return Counter(hrs_celeb_present).most_common(1)[0][0]
    # Counter(data).most_common(n) returns the n most common items in data
    # as a list of n (item, count) tuples -> [0][0] to get item


def best_time_to_party_fractional(schedule):
    """
    Multiply by factor of 10^(# decimal places) to convert fractions to ints so that we can use range()
    Divide by same factor in list comprehension to convert back to fractions and use Counter as usual
    """
    num_decimal_places = str(schedule[0][0])[::-1].find('.')

    if num_decimal_places == -1:  # not a fraction, use original method
        return best_time_to_party(schedule)

    factor = 10 * num_decimal_places
    hrs_celeb_present = []
    for interval in schedule:
        hrs_celeb_present += [x/factor for x in range(int(interval[0]*factor), int(interval[1]*factor))]
    print(Counter(hrs_celeb_present).most_common())
    return Counter(hrs_celeb_present).most_common(1)[0][0]
    # Counter(data).most_common(n) returns the n most common items in data
    # as a list of n (item, count) tuples -> [0][0] to get item


# Key in-class insight: # of celebrities present only changes if celebrities joining != celebrities leaving at a given hour
# Can create 2 lists (hr_joining, hr_leaving), sort them, and then keep a running count of # celebrities present
# while iterating through the 2 lists


def main():
    sched1 = [(6, 8), (6, 12), (6, 7), (7, 8), (7, 10), (8, 9), (8, 10), (9, 12),
             (9, 10), (10, 11), (10, 12), (11, 12)]
    sched2 = [(6.0, 8.0), (6.5, 12.0), (6.5, 7.0), (7.0, 8.0), (7.5, 10.0), (8.0, 9.0),
              (8.0, 10.0), (9.0, 12.0), (9.5, 10.0), (10.0, 11.0), (10.0, 12.0), (11.0, 12.0)]
    sched3 = [(6, 7), (7, 9), (10, 11), (10, 12), (8, 10), (9, 11), (6, 8),
              (9, 10), (11, 12), (11, 13), (11, 14)]

    print("Schedule 1:")
    print(best_time_to_party_fractional(sched1), '\n')

    print("Schedule 2:")
    print(best_time_to_party_fractional(sched2), '\n')

    print("Schedule 3:")
    print(best_time_to_party_fractional(sched3), '\n')


if __name__ == "__main__":
    main()