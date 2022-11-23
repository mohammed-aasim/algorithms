#reversing number using slice method

def reverse_slicing(s):
    return s[::-1]
my_number = '123456'
if __name__ == "__main__":
    print('Reversing the given number using slicing =', reverse_slicing(my_number))