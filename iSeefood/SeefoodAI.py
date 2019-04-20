'''
    ------------------- NOTE ---------------------------
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

import argparse
import numpy as np
import tensorflow as tf
from PIL import Image
import os
import logging



class SeefoodAI(object):
    # Single private instance
    __instance = None
    # Initilize global variables.
    

    # Initilize an AI object to be running
    def __init__(self):
        ''' Virtually private constructor '''
        if SeefoodAI.__instance != None:
            raise Exception("This class is a Signleton!")
        else:
            SeefoodAI.__instance = self
            self.sess = self.class_scores = self.x_input = self.keep_prob = None
            self.scores = 0
            SeefoodAI.__instance.__setup()
        # Seefood AI instance has been created!

    @staticmethod
    def getInstance():
        ''' Static access method '''
        if SeefoodAI.__instance is None:
            SeefoodAI()
        return SeefoodAI.__instance

    def __setup(self):
        ''' Setting-up the SeefoodAI instance'''
        # try initializing the AI instance attrs, catch possible errors.
        
        try:
            self.sess = tf.Session()
            saver = tf.train.import_meta_graph(
                'saved_model/model_epoch5.ckpt.meta')
            saver.restore(self.sess, tf.train.latest_checkpoint('saved_model/'))
            graph = tf.get_default_graph()
            self.x_input = graph.get_tensor_by_name('Input_xn/Placeholder:0')
            self.keep_prob = graph.get_tensor_by_name('Placeholder:0')
            self.class_scores = graph.get_tensor_by_name("fc8/fc8:0")
        except IOError as e:
            print "--- Error: Trained model files cannot be found. Please check README file for info. ---"

        # Instance has been configured 

    def process(self, image_path):
        '''TODO: Accept file path '''

        if not self.validatePath(image_path):  # Validate given path.
            return -1

        # Open passed image, then convert it to RGB
        image = Image.open(image_path).convert('RGB')
        # Resize image to 227x227
        image = image.resize((227, 227), Image.BILINEAR)
        # Create a tensor
        img_tensor = [np.asarray(image, dtype=np.float32)]
        print '+ Looking for food in ' + image_path + ' ...... '

        if self.class_scores is not None:
            # Run the image in the model.
            stat = self.sess.run(self.class_scores, {self.x_input: img_tensor, self.keep_prob: 1.})
            # Update score variable
            self.setScores(stat)
            print("[--------------** Given Image Has Been Analyzed **----------------]")

    def validatePath(self, filePath):
        ''' Validate given file path '''
        if isinstance(filePath, basestring):  # Verify that instance is a string type & !empty.
            if self.checkFileExtension(filePath) and self.directoryExist(filePath):  # Verify path existance
                print 'Good'
                return True # check if given path ends with .png || .jpg
        
        return False

    def directoryExist(self, filePath):
        ''' Verify the existance of the given path '''
        if os.path.exists(filePath):
            return True  # return true when file/directory exist
        return False # retunr false otherwise 

    def checkFileExtension(self, filePath):
        ''' Verify that the given path points to an image file (png, jpg) '''
        if filePath.endswith('.png') or filePath.endswith('.jpg'):
            return True # return true if file is valide
        return False # return false otherwise

    def setScores(self, stat):
        ''' Allow the AI to set the score variable '''
        # BUG: scores accepts all data types!
        self.scores = stat

    def getScores(self):
        ''' Return last analyzed image stat. '''
        
        return self.scores
        

    def getResult(self, scores):
        ''' TODO: Optimaze and generate a final score'''
        # BUG: getResult will return result when there's no result!
        # if np.argmax = 0; then the first class_score was higher, e.g., the model sees food.
        # if np.argmax = 1; then the second class_score was higher, e.g., the model does not see food.
        if np.argmax(scores) == 1:
            return "+ Result:  Oops! No food here... :("
        else:
            return "+ Result: YAY! I see food! :)"
