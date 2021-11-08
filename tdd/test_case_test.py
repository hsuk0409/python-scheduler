from test_case import TestCase
from was_run import WasRun


class TestCaseTest(TestCase):
    def testRunning(self) -> None:
        test = WasRun("justinMethod")
        assert not test.wasRun

        test.run()
        assert test.wasRun

    def testSetUp(self) -> None:
        test = WasRun("justinMethod")
        test.run()
        print(f"was set up :: {test.wasSetUp}")
        assert(test.wasSetUp)

TestCaseTest("testRunning").run()
TestCaseTest("testSetUp").run()
