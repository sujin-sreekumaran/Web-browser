from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtWidgets import QTabWidget, QPushButton

class TabManager(QTabWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setTabsClosable(True)
        self.tabCloseRequested.connect(self.close_tab)
        
        # Add "+" button for new tabs
        self.new_tab_btn = QPushButton("+")
        self.new_tab_btn.clicked.connect(parent.new_tab)
        self.setCornerWidget(self.new_tab_btn)

    def add_tab(self, web_view, title="New Tab"):
        self.addTab(web_view, title)
        self.setCurrentWidget(web_view)

    def close_tab(self, index):
        if self.count() > 1:
            self.removeTab(index)