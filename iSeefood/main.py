from SeefoodAI import SeefoodAI

def main():
    print 'Hello Ibrahim ... '
    # Get the singleton object of the SeefoodAI object.
    current = SeefoodAI.getInstance()
    print current
    current.submitImg('ibrahim/')
    

if __name__ == "__main__":
   main()