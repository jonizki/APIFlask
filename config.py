class Config:
    DEBUG = True

    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://joni_database:jorpankos1@localhost:5432/smilecook'
    SQLALCHEMY_TRACK_MODIFICATIONS = False