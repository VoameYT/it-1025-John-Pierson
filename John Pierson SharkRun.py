class Shark:
    #defining swim and printing the shark swimming
    def swim(self):
        print("The shark is swimming.")
    #defining being awesome
    def be_awesome(self):
        print("The shark is being awesome.")
        # defining john as the best programmer
    def john(self):
        print("John is the best programmer")    


def main(): # defining the main function
    sammy = Shark() #setting sammy as the shark
    sammy.swim()
    sammy.be_awesome()
    sammy.john()

#seeing if __name__ is equal to __main__ which will return true and allow the program to run
if __name__ == "__main__":
    main()