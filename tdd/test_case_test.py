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
        print(self.test.log)
        assert "setUp justinMethod tearDown " == self.test.log

    def testTemplateMethod(self):
        test = WasRun("justinMethod")
        test.run()
        assert "setUp justinMethod tearDown " == test.log


TestCaseTest("testRunning").run()
TestCaseTest("testSetUp").run()
