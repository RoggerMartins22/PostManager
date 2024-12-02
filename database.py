from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models.usuario import Base
DATABASE_URL = "postgresql://root:22082003@db:5432/postagens"
#db_redis = redis.Redis(host='localhost', port=6379, db=0, decode_responses=True)

engine = create_engine(DATABASE_URL)

Base.metadata.create_all(bind=engine)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
