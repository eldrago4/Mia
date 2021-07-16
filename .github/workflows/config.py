class TestingConfig(Config):
    TESTING = True
    SECRET_KEY="GGggjjjfk887856$%kk"
    # Disable CSRF protection in the testing configuration
    WTF_CSRF_ENABLED = False
    SQLALCHEMY_DATABASE_URI = "sqlite:///" + os.path.join(basedir, "test.sqlite")