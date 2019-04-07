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
        # TODO: Verify and validate file path
        current.submitImg(getFilePath())
           
    except:
        print '** Please check file path! **'    
"""
 JavaDoc needed 
"""
def getFilePath():
    image_path = raw_input()
    image_path = image_path.strip()
    # Validaiton & Verification required. 
    return image_path
   
if __name__ == "__main__":
   main()