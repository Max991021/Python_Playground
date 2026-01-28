'''These are answers, feel free to reachout if there is something you don't understand or I amde a mistake so we can both learn'''

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
    
    s = s[::-1]
    return s


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
    elif n== 0:
        return 1
    else:
        return n*factorial(n-1)


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
    fib = []
    num = 0
    num2 = 0
    if n == 0:
        return 0
    elif n == 1:
        return 1
    elif n < 0:
        return None
            
    else:
        for i in range(n+1):
            if i == 0:
                fib.append(0)
            elif i == 1:
                fib.append(1)
            else:
                num =fib[i-2]+fib[i-1]
                fib.append(num)
            
            
            
    return num

print(fibonacci(1))

def is_prime(n: int):
    """
    Check if the number n is prime.
    
    Args:
        n (int): Number to check.
        
    Returns:
        bool: True if prime, False otherwise.
    """
    if n <2:
        return False
    else:
        for i in range(n):
            if n%i == 0:
                return False
            else:
                return True


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
    pass


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
    pass


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
    pass


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
    pass


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
    pass


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
    pass


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
    pass


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
    pass


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
    pass
