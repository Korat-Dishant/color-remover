from project import removal_range, new_dimensions
from PIL import Image
import pytest

test1 = Image.open('test/test1.png')
test2 = Image.open('test/test2.png')
test3 = Image.open('test/test3.png')
test4 = Image.open('test/test4.png')

#  checking for true cases


def test_new_dimensions():
    assert new_dimensions(test1) == (598, 600)
    assert new_dimensions(test2) == (600, 585)
    assert new_dimensions(test3) == (272, 600)
    assert new_dimensions(test4) == (600, 112)

# checking for undefinded images


def test_path():
    with pytest.raises(NameError):
        new_dimensions(testn)
    with pytest.raises(NameError):
        new_dimensions(test66)


def test_removal_range_white():
    assert removal_range({'color': (255, 255, 255, 255), 'range': [25, 20, 10]}) == [
        [230, 255], [235, 255], [245, 255]]
    assert removal_range({'color': (255, 255, 255, 255), 'range': [2, 20, 10]}) == [
        [253, 255], [235, 255], [245, 255]]
    assert removal_range({'color': (255, 255, 255, 255), 'range': [1, 1, 1]}) == [
        [254, 255], [254, 255], [254, 255]]
    assert removal_range({'color': (255, 255, 255, 255), 'range': [1, 0, 0]}) == [
        [254, 255], [255, 255], [255, 255]]
    assert removal_range({'color': (255, 255, 255, 255), 'range': [0, 0, 0]}) == [
        [255, 255], [255, 255], [255, 255]]


def test_removal_range_black():
    assert removal_range({'color': (0, 0, 0, 255), 'range': [25, 20, 10]}) == [
        [0, 25], [0, 20], [0, 10]]
    assert removal_range({'color': (0, 0, 0, 255), 'range': [2, 20, 10]}) == [
        [0, 2], [0, 20], [0, 10]]
    assert removal_range({'color': (0, 0, 0, 255), 'range': [1, 1, 1]}) == [
        [0, 1], [0, 1], [0, 1]]
    assert removal_range({'color': (0, 0, 0, 255), 'range': [1, 0, 0]}) == [
        [0, 1], [0, 0], [0, 0]]
    assert removal_range({'color': (0, 0, 0, 255), 'range': [0, 0, 0]}) == [
        [0, 0], [0, 0], [0, 0]]


def test_removal_range_red():
    assert removal_range({'color': (255, 0, 0, 255), 'range': [25, 20, 10]}) == [
        [230, 255], [0, 20], [0, 10]]
    assert removal_range({'color': (255, 0, 0, 255), 'range': [1, 1, 1]}) == [
        [254, 255], [0, 1], [0, 1]]
    assert removal_range({'color': (255, 0, 0, 255), 'range': [1, 0, 0]}) == [
        [254, 255], [0, 0], [0, 0]]


def test_removal_range_randomColor():
    assert removal_range({'color': (255, 152, 78, 255), 'range': [2, 20, 12]}) == [
        [253, 255], [132, 172], [66, 90]]
    assert removal_range({'color': (255, 80, 9, 255), 'range': [10, 10, 1]}) == [
        [245, 255], [70, 90], [8, 10]]
    assert removal_range({'color': (255, 76, 12, 255), 'range': [1, 11, 0]}) == [
        [254, 255], [65, 87], [12, 12]]
