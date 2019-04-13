'''
------------------ SeefoodAI class unit test -------------------

'''
import pytest
from iSeefood.SeefoodAI import SeefoodAI

def test_process():
    ''' TODO: Test the image processing unit '''
    assert True, "Image Submition Test"

def test_pathValidation():
    ''' TODO: Test the Validation unit '''
    current = SeefoodAI()
    ''' Pass an integar '''
    pathState = current.pathValidation(10)
    assert pathState == False, "Parameter type Test #1"

    ''' Pass a string '''
    pathState = current.pathValidation("sample/cookies.png")
    assert pathState == True, "Parameter type Test #2"

    ''' Pass empty '''
    pathState = current.pathValidation("")
    assert pathState == True, "Parameter type Test #2"

    ''' Pass bool '''
    pathState = current.pathValidation(True)
    assert pathState == False, "Parameter type Test #2"


def test_pathVerification():
    '''  TODO: Test the Verification unit '''
    assert True, "Verification Test"

def test_scoresCalculation():
    ''' TODO: Test the Score Calculation  unit '''
    assert True, "Score Calculation Test"
