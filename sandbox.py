#Author: Terry Su
#Date: June 17, 2021
#Purpose: a coding sandbox to test out algorithms or datastructures

def reverse(s):
    
    if s == '':
        return ''
    
    return s[-1] + reverse(s[:-1])

def reverse2(s):
    return s[::-1]

def bubble_sort(arr):
    
    count = len(arr) - 1
    
    while count != 0:
        
        for i in range(0,count):
            if arr[i] > arr[i+1]:
                arr[i],arr[i+1] = arr[i+1],arr[i]

        count -= 1

    return arr
