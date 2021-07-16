<<<<<<< HEAD
class TestingConfig(Config):
    TESTING = True
    SECRET_KEY="GGggjjjfk887856$%kk"
    # Disable CSRF protection in the testing configuration
    WTF_CSRF_ENABLED = False
    SQLALCHEMY_DATABASE_URI = "sqlite:///" + os.path.join(basedir, "test.sqlite")
=======
GOOGLE_CIENT_ID = ${{ secrets.GOOGLE_CLIENT_ID }}
GOOGLE_CLIENT_SECRET = ${{ secrets.GOOGLE_CLIENT_SECRET }}
>>>>>>> f18a6b05ee3e9f24c8452f80d2f540e2dd11d4d2
