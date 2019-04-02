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

class SeefoodAI(object):
    # Single private instance 
    __instance = None
    
    # Initilize global variables. 
    global sess, class_scores, x_input, keep_prob
    
    # Initilize an AI object to be running 
    def __init__(self):
        ''' Virtually private constructor '''
        if SeefoodAI.__instance != None:
            raise Exception("This class is a Signleton!")
        else:
            SeefoodAI.__instance = self
            SeefoodAI.__instance.__setup()
        print "+ Seefood AI instance has been created!"
        
    
    @staticmethod
    def getInstance():
        ''' Static access method '''
        if SeefoodAI.__instance == None:
            SeefoodAI()
        return SeefoodAI.__instance
    
    
    def __setup(self):
        ''' Setting-up the SeefoodAI instance'''
        # try initializing the AI instance attrs, catch possible errors. 
        # TODO: Make it pretty :) 
        global sess, class_scores, x_input, keep_prob    


        try:
            sess = tf.Session() 
            saver = tf.train.import_meta_graph('saved_model/model_epoch5.ckpt.meta')
            saver.restore(sess, tf.train.latest_checkpoint('saved_model/'))
            graph = tf.get_default_graph()
            x_input = graph.get_tensor_by_name('Input_xn/Placeholder:0')
            keep_prob = graph.get_tensor_by_name('Placeholder:0')
            class_scores = graph.get_tensor_by_name("fc8/fc8:0")
        except:
            print '------ [An error occured during initialization] -----'
        else:
            print '++++++ [No errors occured during initialization +++++'

        print("+ Setting up instance ....")
        
        
    
    def submitImg(self, image_path):
        ''' Passing an image to the AI to be analyzed '''
        image = Image.open(image_path).convert('RGB')
        image = image.resize((227, 227), Image.BILINEAR)
        img_tensor = [np.asarray(image, dtype=np.float32)]
        print '+ Looking for food in ' + image_path + ' ...... '

        #Run the image in the model.
        scores = sess.run(class_scores, {x_input: img_tensor, keep_prob: 1.})
        print '+ Statistics: ', scores
        # if np.argmax = 0; then the first class_score was higher, e.g., the model sees food.
        # if np.argmax = 1; then the second class_score was higher, e.g., the model does not see food.
        if np.argmax(scores) == 1:
            print "--> Oops! No food here... :( "
        else:
            print "--> YAY! I see food! :)"
        print("_________ Analyzing image.... Done! __________")