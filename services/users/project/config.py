# services/users/project/config.py

class BaseConfig:
    """Base Config"""
    TESTING = False

class DevelopmentConfig(BaseConfig):
    """ Development Config"""
    pass

class TestingConfig(BaseConfig):
    """ Testing Config """
    Testing = True

class ProductionConfig(BaseConfig):
    """ Production config """
    pass

