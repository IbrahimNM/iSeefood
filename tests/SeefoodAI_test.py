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
    current = SeefoodAI()
    yield current


''' Test the Process unit '''
''' Expected: only accepts valid file type & path '''


def test_process1(shared_instance):
    ''' TEST CASE: Pass valid file-type-path to be processed'''
    cwd = os.getcwd()  # get current-working-directory
    test = shared_instance.process(cwd+"/iSeefood/samples/cookies.png")
    assert test is True, "Process1: Valid image to be processed." + cwd


def test_process2(shared_instance):
    ''' TEST CASE: Pass invalid file-type-path to be processed'''
    cwd = os.getcwd()
    test = shared_instance.process(cwd+"/invalid/samples/path.pg")
    assert test is False, "Process2: Invalid image path/type to be processed."


def test_process3(shared_instance):
    ''' TEST CASE: Pass non-existed file-path to be processed'''
    cwd = os.getcwd()
    test = shared_instance.process(cwd+"/anywhere/file.png")
    assert test is False, "Process3: Invalid image path to be processed."


def test_process4(shared_instance):
    ''' TEST CASE: Pass invalid file-type to be processed'''
    cwd = os.getcwd()
    test = shared_instance.process(cwd+"/iSeefood/samples/cookies.gif")
    assert test is False, "Process4: Invalid image path to be processed."


''' Test the Validation unit '''
''' Expected: only accepts a non empty string'''


def test_validatePath1(shared_instance):
    ''' Pass an integar '''
    pathState = shared_instance.validatePath(10)
    assert pathState is False, "Parameter type Test #1"


def test_validatePath2(shared_instance):
    ''' Pass a string '''
    cwd = os.getcwd()
    pathState = shared_instance.validatePath(
        cwd+"/iSeefood/samples/cookies.png")
    assert pathState is True, "Parameter type Test #2"


def test_validatePath3(shared_instance):
    ''' Pass empty path'''
    pathState = shared_instance.validatePath("")
    assert pathState is False, "Parameter type Test #2"


def test_validatePath4(shared_instance):
    ''' Pass bool '''
    pathState = shared_instance.validatePath(True)
    assert pathState is False, "Parameter type Test #2"


''' Test the directory existance checker unit '''
''' Expected: Only existed directories are accepted '''


def test_validateExistence(shared_instance):

    # get current working directory
    cwd = os.getcwd()
    # Valid file path
    result = shared_instance.validateExistence(
        cwd+"/iSeefood/samples/cookies.png")
    assert result is True, cwd + "/iSeefodd/samples/cookies.png directory exists"


def test_validateExistence1(shared_instance):
    # Invalid file path
    result = shared_instance.validateExistence("samles/cookies.png")
    assert result is False, "/home/ibrahim/Desktop/iSeefood/iSeefood/samples/cookies.png directory exists"


''' Test file extension checker '''
''' Expected: Only .png .jpg files are accepted '''


def test_validateExtension(shared_instance):
    # Valid file ext. PNG
    result = shared_instance.validateExtension("image.png")
    assert result is True, "PNG file extention test"


def test_validateExtension1(shared_instance):
    # Valid file ext. JPG
    result = shared_instance.validateExtension("image.jpg")
    assert result is True, "JPG file extention test"


def test_validateExtension2(shared_instance):
    # Invalid file ext. NO EXT.
    result = shared_instance.validateExtension("image")
    assert result is False, "None file extention test"


def test_validateExtension3(shared_instance):
    # Invalid file ext. Empty
    result = shared_instance.validateExtension("")
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
    assert not isinstance(result, numpy.ndarray), "Score is none!"


def test_getScores2(shared_instance):
    ''' TEST CASE: getting the score unit w/ setting the score 
        w/ a valid data type'''
    # Set score value to a correct data type (numpy.ndarray).
    shared_instance.setScores(numpy.array([[1, 2], [3, 4]]))
    # Get score.
    result = shared_instance.getScores()
    # Check that returned value is of type nm.ndarray.
    assert isinstance(
        result, numpy.ndarray), "Get score returned valid data type."


def test_getResult(shared_instance):
    lastStat = shared_instance.getScores()
    assert shared_instance.getResult(lastStat) is True, "Positive results."


def test_getResult1(shared_instance):
    # run an image without food.
    test = shared_instance.process(os.getcwd()+"/iSeefood/samples/poodle.jpg")
    lastStat = shared_instance.getScores()
    assert shared_instance.getResult(lastStat) is False, "Negative results. "
