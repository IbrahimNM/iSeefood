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


class SeefoodAI(object):
    
    def __init__(self):
        ''' private constructor '''
        self.sess = self.class_scores = self.x_input = self.keep_prob = None
        self.scores = 0
        self.__setup()

    def __setup(self):
        ''' Setting-up the SeefoodAI instance'''
        # try initializing the AI instance attrs, catch possible errors.
        try:
            self.sess = tf.Session()
            cwd = os.getcwd()
            saver = tf.train.import_meta_graph(
                cwd+'/iSeefood/saved_model/model_epoch5.ckpt.meta')
            saver.restore(self.sess, tf.train.latest_checkpoint(
                cwd+'/iSeefood/saved_model/'))
            graph = tf.get_default_graph()
            self.x_input = graph.get_tensor_by_name('Input_xn/Placeholder:0')
            self.keep_prob = graph.get_tensor_by_name('Placeholder:0')
            self.class_scores = graph.get_tensor_by_name("fc8/fc8:0")
        except IOError as e:
            print "--- Error: Trained model files cannot be found. Please check README file for info. ---"

        # Instance has been configured

    def process(self, image_path):
        ''' Process valid, existed file'''
        if self.validatePath(image_path) and self.class_scores is not None:  # Validate given path.
            # Open passed image, then convert it to RGB
            image = Image.open(image_path).convert('RGB')
            # Resize image to 227x227
            image = image.resize((227, 227), Image.BILINEAR)
            # Create a tensor
            img_tensor = [np.asarray(image, dtype=np.float32)]
            print '+ Looking for food in ' + image_path + ' ...... '
            # Run the image in the model.
            stat = self.sess.run(self.class_scores, {
                self.x_input: img_tensor, self.keep_prob: 1.})
            # Update score variable
            # Scores shall reset to == 0, whenever a new image is process.
            self.setScores(stat)
            print("[--------------** Given Image Has Been Analyzed **----------------]")
            # return true when an image is processed.
            return True

        return False

    def validatePath(self, filePath):
        ''' Validate given file path '''
        # Verify that instance is a string type & !empty && Verify path existance && given path ends with .png || .jpg.
        return isinstance(filePath, basestring) and self.validateExtension(filePath) and self.validateExistence(filePath)

    def validateExistence(self, filePath):
        ''' Verify the existance of the given path '''
        return os.path.exists(filePath)  # retunr false otherwise

    def validateExtension(self, filePath):
        ''' Verify that the given path points to an image file (png, jpg) '''
        if filePath.endswith('.png') or filePath.endswith('.jpg'):
            return True  # return true if file is valide
        return False  # return false otherwise

    def setScores(self, stat):
        ''' Allow the AI to set the score variable '''
        # Set Score is not a public def., therefore no need to check data type.
        self.scores = stat

    def getScores(self):
        ''' Return last analyzed image stat. '''
        return self.scores

    def getResult(self, scores):
        ''' Optimaze and generate a final score'''
        # if np.argmax = 0; then the first class_score was higher, e.g., the model sees food.
        # if np.argmax = 1; then the second class_score was higher, e.g., the model does not see food.
        if np.argmax(scores) == 1:
            return False
        return True
