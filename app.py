## ==== Import frontend ==== ##
from Frontend import appFrame
## ==== Import backend ==== ##

class App:
    def __init__(self) -> None:
        self.displayMainframe()
        
    def displayMainframe(self):
        appFrame.appFrame()
        
App()
