from models.base import SessionLocal

def get_db():
    """
    Gerenciador de sessão com o banco de dados.
    Uso com 'with' ou manualmente.
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()