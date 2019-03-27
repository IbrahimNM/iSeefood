'''
    --------------- NOTE -------------------------------
    THIS CLASS SHALL BE A SINGLETON. 
    CURRENTLY, WE ONLY NEED A SINGLE INSTANCE
    TO BE RUNNING. 
    ----------------------------------------------------
    [WHY?] AI OBJECT WILL CONSUME A LARGE AMOUNT OF MEMORY
           THUS A SINGLE INSTANCE WOULD BE ENOUGH FOR NOW.
    -------------- CREDIT ------------------------------
    AI IS PROVIDED BY DR.DORAN FROM WRIGHT STATE
    UNIVERSITY.  
    -------------- AUTHOR ------------------------------
          IBRAHIM ALMOHAIMEED 
        ALMOHAIMEED.10@GMAIL.COM
              XX/XX/2019
    ----------------------------------------------------
'''

class SeefoodAI(object):
    # Single private instance 
    __instance = None

    # Initilize an AI object to be running 
    def __init__(self):
        ''' Virtually private constructor '''
        if SeefoodAI.__instance != None:
            raise Exception("This class is a Signleton!")
        else:
            SeefoodAI.__instance = self
            SeefoodAI.__instance.__setup()
        print "Seefood AI instance has been created!"
        
    
    @staticmethod
    def getInstance():
        ''' Static access method '''
        if SeefoodAI.__instance == None:
            SeefoodAI()
        return SeefoodAI.__instance
    
    
    def __setup(self):
        ''' Setting-up the SeefoodAI instance'''
        print("Setting up instance ....")
    
    def submitImg(self, imagePath):
        ''' Passing an image to the AI to be analyzed '''
        print("Analyzing image.... Done!")
        
    
    
    
