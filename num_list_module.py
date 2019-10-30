'''
def backwardslist(array):
    new_array = array[::-1]
    print(new_array)


def minimun(array):
    print(min(array))
'''

def firsthalfsum(array):
    if len(array) % 2 == 0:
        mid= len(array)//2
        first_half = array[:mid+1]
        first_half_sum = sum(first_half)
        print("This array is even so the sum is: ",first_half_sum)
    else:
        mid = len(array) // 2
        still_half = array[:mid + 1]
        still_half_sum = sum(still_half)
        print("This sum is odd so the sum is: ",still_half_sum)

firsthalfsum([1,3,5,6,3,9,10])










'''
def divisibleby(array, divisor):
    """ Returns each element divisible by the paramater 'divisor'

    """

def max(array):
    print(max(array))

def avg(array):
    """ Returns the average of a list of numbers"""

def suprise():
    """ Create a surprise function for the person that receives your code.
        Feel free to get creative change parameters, print out shapes,  etc.

        """


################################
####    BONUS FUNCTION       ###
################################
def gcd(array):
    """ Returns the greatest common Divisor of a list of numbers """
    """ Greatest Common Divisor is the greatest number that each number in the list is 
        divisible by. 
        EXAMPLE: [500, 50, 20] Greatest Common Divisor = 10
                 [18, 30, 42]  Greatest Common Divisor = 6
                 [33, 66, 99, 101] Greatest Common Divisor = 1
                 
                 """
'''

