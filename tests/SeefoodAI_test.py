'''
------------------ SeefoodAI class unit test -------------------

'''
import pytest
import numpy
from iSeefood.SeefoodAI import SeefoodAI
import os

SCOPE = "function"


@pytest.fixture(scope=SCOPE)
def shared_instance():
    current = SeefoodAI.getInstance()
    yield current


def test_process():
    ''' TODO: Test the image processing unit '''
    assert True, "Image Submition Test"


''' Test the Validation unit '''
''' Expected: only accepts a non empty string'''


def test_validatePath1(shared_instance):
    ''' Pass an integar '''
    pathState = shared_instance.validatePath(10)
    assert pathState is False, "Parameter type Test #1"


def test_validatePath2(shared_instance):
    ''' Pass a string '''
    cwd = os.getcwd()
    pathState = shared_instance.validatePath(cwd+"/iSeefood/samples/cookies.png")
    assert pathState is True, "Parameter type Test #2"


def test_validatePath3(shared_instance):
    ''' Pass empty path'''
    pathState = shared_instance.validatePath("")
    assert pathState is False, "Parameter type Test #2"


def test_validatePath4(shared_instance):
    ''' Pass bool '''
    pathState = shared_instance.validatePath(True)
    assert pathState is False, "Parameter type Test #2"


def test_directoryExist(shared_instance):
    ''' TODO: Test the directory existance checker unit '''
    ''' Expected: Only existed directories are accepted '''
    # get current working directory
    cwd = os.getcwd()
    # Valid file path
    result = shared_instance.directoryExist(
        cwd+"/iSeefood/samples/cookies.png")
    assert result is True, cwd + "/iSeefodd/samples/cookies.png directory exists"

    # Invalid file path
    result = shared_instance.directoryExist("samles/cookies.png")
    assert result is False, "/home/ibrahim/Desktop/iSeefood/iSeefood/samples/cookies.png directory exists"


def test_CheckFileExtension(shared_instance):
    ''' Test file extension checker '''
    ''' Expected: Only .png .jpg files are accepted '''

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

    ''' FIXME: Check what type of data I should receive?
               print type(current.getScores()) is numpy.ndarray
    '''
    assert True, "Set statistics score Test"


def test_getScores1(shared_instance):
    ''' TEST CASE: Getting the score unit w/o setting the score'''
    # Get scores
    result = shared_instance.getScores()
    assert result == 0, "Score is none!"


def test_getScores2(shared_instance):
    ''' TEST CASE: getting the score unit w/ setting the score 
        w/ a valid data type'''
    # Set score value to a correct data type (numpy.ndarray).
    shared_instance.setScores(numpy.array([[1, 2], [3, 4]]))
    # Get score.
    result = shared_instance.getScores()
    # Check that returned value is of type nm.ndarray.
    assert type(result) is numpy.ndarray, "Get score returned valid data type."
