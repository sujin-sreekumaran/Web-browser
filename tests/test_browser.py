import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from PyQt5.QtWidgets import QApplication
from src.browser_window import Browser
import pytest

@pytest.fixture
def app():
    return QApplication([])

def test_browser_initialization(app):
    browser = Browser()
    assert browser.windowTitle() == "My Browser"