# This prints all pairs of numbers from 0 to 2
for i in range(3):          # outer loop, i goes from 0 to 2
    for j in range(3):      # inner loop, j goes from 0 to 2
        print(i, j)         # print the pair (i, j)
        # first iteration: 0 0, 0 1, 0 2
        # second iteration: 1 0, 1 1, 1 2
        # third iteration: 2 0, 2 1, 2 2
