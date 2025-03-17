from PyQt5.QtCore import QUrl
from PyQt5.QtWidgets import (QMainWindow, QToolBar, QLineEdit, QAction, 
                            QMenuBar, QStatusBar)
from PyQt5.QtWebEngineWidgets import QWebEngineView
from src.tabs import TabManager
from src.bookmarks import BookmarkManager
from src.history import HistoryManager


class Browser(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My Browser")
        self.setGeometry(100, 100, 1024, 768)
        
        # Initialize components
        self.tabs = TabManager(self)
        self.bookmarks = BookmarkManager(self)
        self.history = HistoryManager(self)
        
        self.setCentralWidget(self.tabs)
        self.create_ui()
        self.new_tab()

    def create_ui(self):
        # Menu Bar
        self.menu_bar = QMenuBar(self)
        self.setMenuBar(self.menu_bar)
        
        # Navigation Toolbar
        toolbar = QToolBar()
        self.addToolBar(toolbar)
        
        # Back/Forward buttons
        back_btn = QAction("←", self)
        back_btn.triggered.connect(lambda: self.current_web_view().back())
        toolbar.addAction(back_btn)
        
        forward_btn = QAction("→", self)
        forward_btn.triggered.connect(lambda: self.current_web_view().forward())
        toolbar.addAction(forward_btn)
        
        # Address Bar
        self.url_bar = QLineEdit()
        self.url_bar.returnPressed.connect(self.navigate_to_url)
        toolbar.addWidget(self.url_bar)
        
        # Bookmarks Button
        bookmark_btn = QAction("★", self)
        bookmark_btn.triggered.connect(self.toggle_bookmark)
        toolbar.addAction(bookmark_btn)
        
        # Status Bar
        self.status_bar = QStatusBar()
        self.setStatusBar(self.status_bar)

    def new_tab(self):
        web_view = QWebEngineView()
        web_view.load(QUrl("https://google.com"))
        web_view.urlChanged.connect(self.update_ui)
        self.tabs.add_tab(web_view, "New Tab")

    def current_web_view(self):
        return self.tabs.currentWidget()

    def navigate_to_url(self):
        url = self.url_bar.text()
        self.load_url(url)
        self.history.add_to_history(url)

    def load_url(self, url):
        if not url.startswith(("http://", "https://")):
            url = "http://" + url
        self.current_web_view().load(QUrl(url))
        self.url_bar.setText(url)

    def update_ui(self, q):
        url = q.toString()
        self.url_bar.setText(url)
        self.status_bar.showMessage(f"Loaded: {url}")

    def toggle_bookmark(self):
        current_url = self.url_bar.text()
        if current_url in self.bookmarks.bookmarks:
            self.bookmarks.remove_bookmark(current_url)
        else:
            self.bookmarks.add_bookmark(current_url)