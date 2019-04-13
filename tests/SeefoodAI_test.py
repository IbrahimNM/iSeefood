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
    pathState = current.pathValidation("iSeefood/samples/cookies.png")
    assert pathState == True, "Validation Test"

def test_pathVerification():
    '''  TODO: Test the Verification unit '''
    assert True, "Verification Test"

def test_scoresCalculation():
    ''' TODO: Test the Score Calculation  unit '''
    assert True, "Score Calculation Test"
