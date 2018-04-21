import numpy as np

# Write your list_stats function here.

def list_stats(numbers):
    numbers.sort()
    if len(numbers) % 2 == 0:
        # even nummers
        mid = len(numbers) // 2
        median = (numbers[mid -1] + numbers[mid]) / 2
    else:
        # oneven nummers
        mid = len(numbers) // 2
        median = numbers[mid]
                  
    mean = float(str(round(np.sum(numbers) / len(numbers),3)))
    
    return(median, mean)

# You can use this to test your function.
# Any code inside this `if` statement will be ignored by the automarker.
if __name__ == '__main__':
    # Run your function with the first example in the question.
    m = list_stats([1.3, 2.4, 20.6, 0.95, 3.1, 2.7])
    print(m)

    # Run your function with the second example in the question
    m = list_stats([1.5])
    print(m)