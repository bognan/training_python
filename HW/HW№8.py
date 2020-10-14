def new_func(*args):
    return max(*args)


max_number = new_func(20, 10, 1)
print(max_number)
