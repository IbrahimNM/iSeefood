from SeefoodAI import SeefoodAI
import argparse

parser = argparse.ArgumentParser(description="Ask SeeFood if there is food in the image provided.")
parser.add_argument('image_path', help="The full path to an image file stored on disk.")


def main():
    print 'Hello friend, glad to see you here ... '
    
    # Get the singleton object of the SeefoodAI object.
    current = SeefoodAI.getInstance()

    # Args handling 
    '''
        - Check for args:
        - If there's no args passed, display message for user. 
        - If there're args passed, check their validity then continue
    '''

    args = parser.parse_args() 
    image_path = args.image_path
    current.submitImg(image_path)
    

if __name__ == "__main__":
   main()