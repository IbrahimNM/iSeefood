from SeefoodAI import SeefoodAI
import argparse
import sys
import numpy

def main():
    print 'Hello friend, welcome to iSeefood AI sample... '
    
    # Get the singleton object of the SeefoodAI object.
    current = SeefoodAI.getInstance()
    try:
        
        print 'Enter image path: '
        current.process(getFilePath())
        print '+ Statistics: ', current.getScores()
        print '+ Result: ', current.getResult(current.getScores())
    except IOError as e:
        print '** Please check file path! **'  
"""
 JavaDoc needed 
"""
def getFilePath():
    ''' Get image path from user'''
    image_path = raw_input()
    image_path = image_path.strip()
    # TODO: Validaiton & Verification required (X.png, Y.jpg). 
    return image_path
    
   
if __name__ == "__main__":
   main()
