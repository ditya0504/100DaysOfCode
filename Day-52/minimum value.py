MAX = 100000


def Print3Smallest(arr, n):
    firstmin = MAX
    secmin = MAX
    thirdmin = MAX

    for i in range(0, n):



        if arr[i] < firstmin:
            thirdmin = secmin
            secmin = firstmin
            firstmin = arr[i]

        # Check if current element is
        # less than secmin then update
        # second and third
        elif arr[i] < secmin:
            thirdmin = secmin
            secmin = arr[i]

        # Check if current element is
        # less than,then upadte third
        elif arr[i] < thirdmin:
            thirdmin = arr[i]

    print("First min = ", firstmin)
    print("Second min = ", secmin)
    print("Third min = ", thirdmin)


# driver program
arr = [4, 9, 1, 32, 12]
n = len(arr)
Print3Smallest(arr, n)
