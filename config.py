import os

# For a production app, you should use a secret key set in the environment
# The recommended way to generate a 64char secret key is to run:
# python -c 'import secrets; print(secrets.token_hex())'
SECRET_KEY = os.getenv('SECRET_KEY', 'not-set')

# When deploying, set in the environment to the PostgreSQL URL
#connection_string = 'postgresql://postgres:1212334@localhost:5432/postgres'
connection_string = 'postgresql://patryk:snwVKN7q9CHzhJ7IXsuZQz5wJUU0ny3C@dpg-crauefdds78s73dacmdg-a.oregon-postgres.render.com/test_dx6x'
SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', connection_string)
