# two dice simulation

from random import randrange

NUM_RUNS = 1000
D_MAX = 6

# rolls two dice and returns the total
def twoDice():
    d1 = randrange(1,D_MAX + 1)
    d2 = randrange(1,D_MAX + 1)
    return d1 + d2

# simulate many rolls and displays the result
def main():
    # creates a dictionary of expected proportions
    expected = {2 : 1/36, 3 : 2/36, 4 : 3/36, 5 : 4/36, \
                6 : 5/36, 7 : 6/36, 8 : 5/36, 9 : 4/36, \
                10 : 3/36, 11 : 2/36, 12 : 1/36}

    # creates a dictionary that maps the total of two dice
    # to the number of occurences
    counts = {2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0, 9:0, 10:0,\
              11:0, 12:0}

    # simulate NUM_RUN rolls and count each rolls
    for i in range(NUM_RUNS):
        t = twoDice()
        counts[t] += 1

    # Displays the simulated proportions and expected results
    print("Total    Simulated   Expected")
    print("           percent    percent")
    for i in sorted(counts.keys()):
        print("%5d %11.2f %8.2f" % \
         (i, counts[i] / NUM_RUNS * 100, expected[i] * 100))

main()