from test_case import TestCase


class WasRun(TestCase):
    
    def __init__(self, name: str) -> None:
        self.wasRun = None
        TestCase.__init__(self, name)

    def setUp(self) -> None:
        # self.wasRun = None
        # self.wanSetUp = 1
        self.log = "setUp "

    def justinMethod(self) -> None:
        # self.wasRun = 1
        self.log = self.log + "justinMethod "

    def tearDown(self):
        self.log = self.log + "tearDown "
