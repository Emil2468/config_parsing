from config_parsing import config_parser
from dummy_config_class import DummyConfigClass
from dummy_config_class_2 import DummyConfigClass2

class TestParsing:
    def test_flat_parsing(self):
        configuration = {
            "a": 1,
            "c": 10
        }
        config_object = DummyConfigClass()
        fresh_config_object = DummyConfigClass()
        config_parser._overwrite_default_values_with_dict(configuration, config_object)
        assert config_object.a == configuration["a"]
        assert config_object.a != fresh_config_object.a
        assert config_object.b == fresh_config_object.b
        assert config_object.c == configuration["c"]
        assert config_object.c != fresh_config_object.c

    def test_layered_parsing(self):
        configuration = {
            "a": 1598,
            "c": 10,
            "sub_config": {
                "b": 100,
                "a": -10
            }
        }
        config_object = DummyConfigClass2()
        fresh_config_object = DummyConfigClass2()
        config_parser._overwrite_default_values_with_dict(configuration, config_object)
        assert config_object.a == configuration["a"]
        assert config_object.a != fresh_config_object.a
        assert config_object.b == fresh_config_object.b
        assert config_object.c == configuration["c"]
        assert config_object.c != fresh_config_object.c
        assert config_object.sub_config.a == configuration["sub_config"]["a"]
        assert config_object.sub_config.b == configuration["sub_config"]["b"]
        assert config_object.sub_config.c == fresh_config_object.sub_config.c

