'''
------------------ SeefoodAI class unit test -------------------

'''
import pytest
import numpy
from iSeefood.SeefoodAI import SeefoodAI

SCOPE ="function"

@pytest.fixture(scope=SCOPE)
def shared_instance():
    current = SeefoodAI.getInstance()
    yield current

def test_process():
    ''' TODO: Test the image processing unit '''
    assert True, "Image Submition Test"


def test_validatePath(shared_instance):
    ''' Test the Validation unit '''
    ''' Expected: only accepts a non empty string'''
    #current = SeefoodAI.getInstance()
    
    ''' Pass an integar '''
    pathState = shared_instance.validatePath(10)
    assert pathState is False, "Parameter type Test #1"

    ''' Pass a string '''
    pathState = shared_instance.validatePath("sample/cookies.png")
    assert pathState is True, "Parameter type Test #2"

    ''' Pass empty '''
    pathState = shared_instance.validatePath("")
    assert pathState is True, "Parameter type Test #2"

    ''' Pass bool '''
    pathState = shared_instance.validatePath(True)
    assert pathState is False, "Parameter type Test #2"


def test_directoryExist(shared_instance):
    ''' TODO: Test the directory existance checker unit '''
    ''' Expected: Only existed directories are accepted '''
    #current = SeefoodAI.getInstance()
    # Valid file path
    result = shared_instance.directoryExist("samples/cookies.png")
    assert result is True, "samples/cookies.png directory exists"
    
    # Invalid file path
    result = shared_instance.directoryExist("samles/cookies.png")
    assert result is False, "/home/ibrahim/Desktop/iSeefood/iSeefood/samples/cookies.png directory exists"
    

def test_CheckFileExtension(shared_instance):
    ''' Test file extension checker '''
    ''' Expected: Only .png .jpg files are accepted '''
    #current = SeefoodAI.getInstance()
    # Valid file ext. PNG
    result = shared_instance.checkFileExtension("image.png")
    assert result is True, "PNG file extention test"
    # Valid file ext. JPG
    result = shared_instance.checkFileExtension("image.jpg")
    assert result is True, "JPG file extention test"
    # Invalid file ext. NO EXT.
    result = shared_instance.checkFileExtension("image")
    assert result is False, "None file extention test"
    # Invalid file ext. Empty 
    result = shared_instance.checkFileExtension("")
    assert result is False, "Empty file test"

def test_setScore(shared_instance):
    ''' TODO: Test setting stat scores unit '''
    #current = SeefoodAI.getInstance()
    ''' FIXME: Check what type of data I should receive?
               print type(current.getScores()) is numpy.ndarray
    '''
    assert True, "Set statistics score Test"


def test_getScore(shared_instance):
    ''' TODO: Test getting the score unit '''
    #current = SeefoodAI.getInstance()

    result = shared_instance.getScores()
    assert result is None, "Score is none!"
