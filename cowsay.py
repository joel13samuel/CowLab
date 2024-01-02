import sys

from dragon import Dragon
from heifer_generator import HeiferGenerator


# goes through cows list to see all available cows, and uses the get_name function in cow to print name
def list_cows(cows):
    print("Cows available:", end=' ')
    for cow in cows:
        print(cow.get_name(), end=' ')


# goes through cows to find the cow that user wants to print out and if it cant find the name, it returns none
def find_cow(name, cows):
    for cow in cows:
        if cow.get_name() == name:
            return cow
    return None


# main function for everything to run
if __name__ == "__main__":
    # if -l is seen will return the list of cows
    cows = HeiferGenerator.get_cows()
    if sys.argv[1] == '-l':
        list_cows(cows)
        # call list_cows(cows)

    # if -n is seen will find the cow that user wants, return it and return it with a message
    elif sys.argv[1] == '-n':
        cow = find_cow(sys.argv[2], cows)
        say = ' '.join(sys.argv[3:])
        if cow:
            print(say)
            print(cow.get_image())
            # checks if it is a dragon to print out the following statement
            if isinstance(cow, Dragon):
                print(f"This dragon {'can breathe fire.' if cow.can_breathe_fire() else 'cannot breathe fire.'}")
        else:
            print(f'Could not find {sys.argv[2]} cow!')

    # will return the normal cow and print the message 
    else:
        say = ''.join(sys.argv[1:])
        cow = find_cow("heifer", cows)
        if cow:
            print(say)
            print(cow.get_image())
