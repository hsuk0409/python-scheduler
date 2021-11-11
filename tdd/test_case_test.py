from test_case import TestCase
from was_run import WasRun


class TestCaseTest(TestCase):

    def setUp(self) -> None:
        self.test = WasRun("justinMethod")

    def testRunning(self) -> None:
        self.test.run()
        assert self.test.wasRun

    def testSetUp(self) -> None:
        self.test.run()
        assert self.test.wasSetUp


TestCaseTest("testRunning").run()
TestCaseTest("testSetUp").run()
