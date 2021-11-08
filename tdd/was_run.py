from test_case import TestCase


class WasRun(TestCase):
    
    def __init__(self, name: str) -> None:
        TestCase.__init__(self, name)
        self.wasRun = None

    def justinMethod(self) -> None:
        self.wasRun = 1

    def setUp(self) -> None:
        self.wasSetUp = 1
