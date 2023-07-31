from config_parsing import BaseConfig

class DummyConfigClass(BaseConfig):    
    def __init__(self) -> None:
        super().__init__()
        self.a = 0
        self.b = 0
        self.c = 0

