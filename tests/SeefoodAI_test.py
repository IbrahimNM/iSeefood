'''
------------------ SeefoodAI class unit test -------------------

'''
import pytest
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
    assert True, "Directory existance Test"


def test_CheckFileExtension():
    ''' TODO: Test file extension checker '''
    ''' Expected: Only .png .jpg files are accepted '''
    assert True, "File extension Test"


def test_setScore():
    ''' TODO: Test setting stat scores unit'''
    assert True, "Set statistics score Test"


def test_getScore():
    ''' TODO: Test getting the score unit '''
    assert True, "Get latest stat. score Test "
