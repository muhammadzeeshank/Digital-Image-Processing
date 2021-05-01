import numpy as np
import cv2


def constructMask():
    """
    Purpose: A function that will take input from user and build a required mask
    : return: mask, size of mask
    """
    # Taking size and value of mask from user
    # Enforcing the user to enter size of mask only in odd number
    while(True):
        size = int(input("Enter mask size(only odd number): "))
        if (size % 2) != 0:
            break
        else:
            print("[-] ERROR. Please Enter odd number!")
    mask = np.zeros([size, size])
    while(True):
        opt = input(
            "Chose one option: \n 1) Mask with constant value \n 2) Mask with variable values \n")
        if opt == '1':
            value = input("Enter maske value(fraction/float/int):")
            value = fractionToFloat(value)
            # filling mask of (size, size) with value
            mask = np.full([size, size], value)
            break
        elif opt == '2':
            for i in range(size):
                for j in range(size):
                    value = input(
                        f"Enter maske value(fraction/float/int) at ({i}, {j}):")
                    mask[i][j] = fractionToFloat(value)
            break
        else:
            print("[-] INVALID INPUT! Please chose 1 or 2")
    return mask, size


def fractionToFloat(value):
    '''
    value: fraction e.g(a/b)
    return: float value
    '''
    if '/' in value:
        num, den = value.split('/')
        value = float(num)/float(den)
    else:
        value = float(value)
    return value
