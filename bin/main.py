"""
Given a number find the next number
that is divides by 2, 3, or 5.
"""
def max_divide(a, b):
    """
    This function divides a by greatest divisible power of b
    :param a: const number 2, 3, 5
    :param b: current number iteration
    :return: max number 2, 3, 5
    """
    if a % b != 0:
        return a;

    c = a/b;
    return max_divide(c, b);

def is_ugly(n, args, no):
    """
    Function to check if a number is ugly or not
    :param n: index of const list
    :param args: const list of 2,3,5
    :param no: number to test
    :return: is number tested ugly
    """
    if n >= len(args):
        return no == 1

    c = max_divide(no, args[n]);
    return is_ugly(n+1, args, c);

def find_ugly(n, i, count, args):
    """
    Recursively iterate numbers to find first
    ugly number.
    :param n: number to test
    :param i: index of iteration
    :param count: running index of recurcion
    :param args: const list of 2,3,5
    :return: first ugly number found
    """
    if (n < count):
        return i-1

    if is_ugly(0, args, i):
        return find_ugly(n, i+1, count+1, args);
    else:
        return find_ugly(n, i+1, count, args)

def main():
    i = 10
    args = [2,3,5]
    print( "[INPUT] %d" % i)
    output = find_ugly(i, 1, 1, args)
    print( "[OUTPUT] %d" % output)

main()
