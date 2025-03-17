from PyQt5.QtWidgets import QMenu, QAction

class BookmarkManager:
    def __init__(self, browser):
        self.browser = browser
        self.bookmarks = []
        self.bookmarks_menu = QMenu("&Bookmarks", self.browser)
        self.browser.menuBar().addMenu(self.bookmarks_menu)

    def add_bookmark(self, url):
        if url not in self.bookmarks:
            self.bookmarks.append(url)
            action = QAction(url, self.browser)
            action.triggered.connect(lambda: self.browser.load_url(url))
            self.bookmarks_menu.addAction(action)

    def remove_bookmark(self, url):
        if url in self.bookmarks:
            self.bookmarks.remove(url)