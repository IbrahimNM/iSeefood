'''
------------------ SeefoodAI class unit test -------------------

'''
import pytest
import numpy
from iSeefood.SeefoodAI import SeefoodAI


def test_process():
    ''' TODO: Test the image processing unit '''
    assert True, "Image Submition Test"


def test_validatePath():
    ''' Test the Validation unit '''
    ''' Expected: only accepts a non empty string'''
    current = SeefoodAI.getInstance()
    
    ''' Pass an integar '''
    pathState = current.validatePath(10)
    assert pathState == False, "Parameter type Test #1"

    ''' Pass a string '''
    pathState = current.validatePath("sample/cookies.png")
    assert pathState == True, "Parameter type Test #2"

    ''' Pass empty '''
    pathState = current.validatePath("")
    assert pathState == True, "Parameter type Test #2"

    ''' Pass bool '''
    pathState = current.validatePath(True)
    assert pathState == False, "Parameter type Test #2"


def test_directoryExist():
    ''' TODO: Test the directory existance checker unit '''
    ''' Expected: Only existed directories are accepted '''
    current = SeefoodAI.getInstance()
    # Valid file path
    result = current.directoryExist("samples/cookies.png")
    assert result == True, "/home/ibrahim/Desktop/iSeefood/iSeefood/samples/cookies.png directory exists"
    
    # Invalid file path
    result = current.directoryExist("/home/ibrahim/Desktop/iSeefood/iSeefood/samles/cookies.png")
    assert result == False, "/home/ibrahim/Desktop/iSeefood/iSeefood/samples/cookies.png directory exists"
    

def test_CheckFileExtension():
    ''' Test file extension checker '''
    ''' Expected: Only .png .jpg files are accepted '''
    current = SeefoodAI.getInstance()
    # Valid file ext. PNG
    result = current.checkFileExtension("image.png")
    assert result == True, "PNG file extention test"
    # Valid file ext. JPG
    result = current.checkFileExtension("image.jpg")
    assert result == True, "JPG file extention test"
    # Invalid file ext. NO EXT.
    result = current.checkFileExtension("image")
    assert result == False, "None file extention test"
    # Invalid file ext. Empty 
    result = current.checkFileExtension("")
    assert result == False, "Empty file test"
    


def test_setScore():
    ''' TODO: Test setting stat scores unit'''
    ''' FIXME: Check what type of data I should receive?
               print type(current.getScores()) is numpy.ndarray
    '''
    assert True, "Set statistics score Test"


def test_getScore():
    ''' TODO: Test getting the score unit '''
    assert True, "Get latest stat. score Test "
