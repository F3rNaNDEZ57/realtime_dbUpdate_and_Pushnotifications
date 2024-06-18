from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


DATABASE_URI = "postgresql://kavindu:ZwACcUT9i9XZLkW48T5nUZj3qGhtWLhI@dpg-cpmtjso8fa8c73aofvu0-a.singapore-postgres.render.com/testdb_v5qd"

engine = create_engine(DATABASE_URI)
Session = sessionmaker(bind=engine)