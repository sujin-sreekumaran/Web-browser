from PyQt5.QtWidgets import QListWidget, QDockWidget

class HistoryManager:
    def __init__(self, browser):
        self.browser = browser
        self.history = []
        self.history_dock = QDockWidget("History", self.browser)
        self.history_list = QListWidget()
        self.history_dock.setWidget(self.history_list)
        self.browser.addDockWidget(2, self.history_dock)  # Right dock

    def add_to_history(self, url):
        self.history.append(url)
        self.history_list.insertItem(0, url)