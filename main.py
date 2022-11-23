def powers_of_two():           # note the while True, this function, if allowed would run forever and keep getting more powers of two, this won't happen as this is a generator function
    x = 1
    while True:
        yield x                # this is not a return but does return a value, the function can continue to run once it has done this. it instead adds this value to a list which is technically inifitely long but because we never need the whole list, the whole list is never created and only the bit we need is ever created
        x *= 2


def example_powers_of_two():
    gen = powers_of_two()      # the function isn't actually called here, it's turned into an object that we will use later 
    for i in range(72):        # any number could be used here but I only wanted the first 72 powers of two, you can subsititute it for any number and it wills till work
        print(next(gen))       # this loop will go through every power of 2 upto the 72nd power and print it. the list of powers is only ever as big as the amount we have printed so far, therefore a bigger number than 72 could eventually cause memory problems but  the issue won't occur until we get a lot
    
    
def main():                    # I won't explain the rest of this code but if you don't understand it then watch this https://www.youtube.com/watch?v=sugvnHA7ElY&t=124s&ab_channel=CoreySchafer
    example_powers_of_two()


if __name__ == "__main__":
    main()
