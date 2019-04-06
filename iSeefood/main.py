from SeefoodAI import SeefoodAI
import argparse
import sys


def main():
    print 'Hello friend, glad to see you here ... '
    

    # Args handling 
    '''
        - Check for args:
        - If there's no args passed, display message for user. 
        - If there're args passed, check their validity then continue
    '''
    

    
    # Get the singleton object of the SeefoodAI object.
    current = SeefoodAI.getInstance()
    try:
        
        print 'Enter image path: '
        image_path = raw_input() # get file path from user
        image_path = image_path.strip() # remove white spaces.
        # TODO: Verify and validate file path
        current.submitImg(image_path)
           
    except:
        print '** Please check file path! **'    

   
if __name__ == "__main__":
   main()