def is_it_odd(num):
    if(num % 2 !=0):
        return True
    return False
def print_n_times(text):
    how_many = int(input("how many times? "))
    for num in range(0,how_many):
        print(text)