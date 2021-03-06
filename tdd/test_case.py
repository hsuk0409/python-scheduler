class TestCase:
    
    def __init__(self, name: str) -> None:
        self.name = name
    
    def setUp(self) -> None:
        pass

    def run(self) -> None:
        self.setUp()
        method = getattr(self, self.name)
        method()
        self.tearDown()

    def tearDown(self):
        pass
