from PyQt5.QtCore import QUrl
from PyQt5.QtWidgets import QMainWindow, QToolBar, QLineEdit, QAction
from PyQt5.QtWebEngineWidgets import QWebEngineView

class Browser(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My Browser")
        self.setGeometry(100, 100, 1024, 768)
        
        # Create a web view widget
        self.web_view = QWebEngineView()
        self.setCentralWidget(self.web_view)
        
        # Add toolbar with navigation buttons
        toolbar = QToolBar()
        self.addToolBar(toolbar)
        
        # Back button
        back_btn = QAction("←", self)
        back_btn.triggered.connect(self.web_view.back)
        toolbar.addAction(back_btn)
        
        # Forward button
        forward_btn = QAction("→", self)
        forward_btn.triggered.connect(self.web_view.forward)
        toolbar.addAction(forward_btn)
        
        # Address bar
        self.url_bar = QLineEdit()
        self.url_bar.returnPressed.connect(self.navigate_to_url)
        toolbar.addWidget(self.url_bar)
        
        # Load homepage
        self.load_url("https://google.com")
    
    def load_url(self, url):
        """Load the given URL in the web view."""
        if not url.startswith(("http://", "https://")):
            url = "http://" + url
        self.web_view.load(QUrl(url))
        self.url_bar.setText(url)
    
    def navigate_to_url(self):
        """Navigate to the URL entered in the address bar."""
        url = self.url_bar.text()
        self.load_url(url)