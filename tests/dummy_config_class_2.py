from config_parsing import BaseConfig
from dummy_config_class import DummyConfigClass

class DummyConfigClass2(BaseConfig):    
    def __init__(self) -> None:
        super().__init__()
        self.a = 0
        self.b = 0
        self.c = 0
        self.sub_config = DummyConfigClass()

