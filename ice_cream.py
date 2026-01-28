def reverse_string(s: str):
    """
    Reverse the input string and return it.
    
    Args:
        s (str): The string to reverse.
        
    Returns:
        str: Reversed string.
        
    Example:
        "hello" -> "olleh"
    """
    
    return s[::-1]


def factorial(n: int):
    """
    Return the factorial of a non-negative integer.
    Return None if n is negative.
    
    Args:
        n (int): Non-negative integer.
        
    Returns:
        int or None: Factorial of n, or None if n < 0.
        
    Example:
        5 -> 120
    """
    
    if n < 0:
        return None
    elif n == 0:
        return 1
    else:
        num = n * factorial(n-1)
        return num
        
    
    
    
print(factorial(5))
    
        

def fibonacci(n: int):
    """
    Return the nth Fibonacci number (0-based index).
    Return None if n < 0.
    
    Args:
        n (int): Index of Fibonacci sequence.
        
    Returns:
        int or None: nth Fibonacci number, or None if n < 0.
        
    Example:
        7 -> 13
    """
    
    numbers = []
    while n >= 0:
        if n == 0:
            return 0
        elif n == 1:
            return 1
        else:
            for i in range(n+1):
                if i == 0:
                    numbers.append(i)
                elif i == 1:
                    numbers.append(i)
                else:
                    
                    numbers.append(numbers[i-2]+numbers[i-1])
                    
            return numbers[n]
    else:
        return None
    
print(fibonacci(7))           


def is_prime(n: int):
    """
    Check if the number n is prime.
    
    Args:
        n (int): Number to check.
        
    Returns:
        bool: True if prime, False otherwise.
    """
    # if n < 2:
    #     return False
    # else:
    #     for i in range(n-1):

                
    #         if n % i == 0:
    #             return False
    #         else:
    #             return True

    if n < 2:
        return False
    elif n == 2 :
        return True
    else:
        for i in range(2,n-1):
            if n % i == 0:
                return False
            else:
                return True

print(is_prime(3))

def sum_digits(n: int):
    """
    Return the sum of the digits of n.
    
    Args:
        n (int): Input number.
        
    Returns:
        int: Sum of digits.
        
    Example:
        123 -> 6
    """
    num = 0
    n = str(n)
    for i in n:
        if i.isdigit():
            j = int(i)
            print(i)
            num+= j
        
    return num


def count_words(sentence: str):
    """
    Count the number of words in a sentence.
    
    Words are sequences separated by spaces.
    
    Args:
        sentence (str): Input sentence.
        
    Returns:
        int: Number of words.
        
    Example:
        "Hello world" -> 2
    """
    sentence = sentence.split()
    return len(sentence)


def merge_lists_unique(list1: list, list2: list):
    """
    Merge two lists and return a list of unique elements.
    
    Args:
        list1 (list): First list.
        list2 (list): Second list.
        
    Returns:
        list: Unique elements from both lists.
        
    Example:
        [1,2],[2,3] -> [1,2,3]
    """
    for i in list1:
       list2.append(i)
       
    list2 = set(list2)
    
    return [element for element in list2]


def most_frequent(lst: list):
    """
    Return the most frequent element in a list.
    Return None if the list is empty.
    
    Args:
        lst (list): Input list.
        
    Returns:
        element or None: Most frequent element.
        
    Example:
        [1,1,2,3] -> 1
    """
    dictionary = {}
    
    for i in lst:
        dictionary[i] = dictionary.get(i,0)+1
        
    for key,value in dictionary.items():
        if value == max(dictionary.values()):
            return key


def is_anagram(s1: str, s2: str):
    """
    Check if two strings are anagrams (ignore spaces and case).
    
    Args:
        s1 (str): First string.
        s2 (str): Second string.
        
    Returns:
        bool: True if anagrams, False otherwise.
        
    Example:
        "listen", "silent" -> True
    """
    return True if  sorted(s1.lower().replace(' ','')) == sorted(s2.lower().replace(' ','')) else False


def count_even_odd(numbers: list):
    """
    Count how many numbers are even and how many are odd.
    
    Args:
        numbers (list): List of integers.
        
    Returns:
        tuple: (even_count, odd_count)
        
    Example:
        [1,2,3,4] -> (2,2)
    """
    return (sum(1 for i in numbers if i %2 == 0 ),sum(1 for i in numbers if i%2 !=0))


def reverse_list(lst: list):
    """
    Return a reversed version of the input list.
    
    Args:
        lst (list): Input list.
        
    Returns:
        list: Reversed list.
        
    Example:
        [1,2,3] -> [3,2,1]
    """
    return lst[::-1]


def square_numbers(numbers: list):
    """
    Return a list containing the squares of the input numbers.
    
    Args:
        numbers (list): List of integers.
        
    Returns:
        list: List of squared numbers.
        
    Example:
        [1,2,3] -> [1,4,9]
    """
    return [i*i for i in numbers]


def fibonacci_sequence(n: int):
    """
    Return the first n Fibonacci numbers as a list.
    
    Args:
        n (int): Number of terms to generate.
        
    Returns:
        list: List of the first n Fibonacci numbers.
        
    Example:
        5 -> [0,1,1,2,3]
        
    """
    
    numbers = []
    while n >= 0:
        if n == 0:
            return []
        elif n == 1:
            numbers.append(0)
        else:
            for i in range(n):
                if i == 0:
                    numbers.append(i)
                elif i == 1:
                    numbers.append(i)
                else:
                    
                    numbers.append(numbers[i-2]+numbers[i-1])
                    
            return numbers
    else:
        return None
    
print(fibonacci_sequence(5))
