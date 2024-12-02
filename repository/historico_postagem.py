from sqlalchemy.orm import Session
from models.historico_postagem import HistoricoPostagem

class HistoricoPostagemRepository:
    @staticmethod
    def get_historico_postagem_by_id(db: Session, postagem_id: int):
        return db.query(HistoricoPostagem).filter(HistoricoPostagem.postagem_id == postagem_id).all()


    @staticmethod
    def create_historico_postagem(db: Session, postagem_id: int, status: str, mensagem: str = "Postagem Solicitada"):
        db_historico = HistoricoPostagem(
            postagem_id=postagem_id,
            status=status,
            mensagem=mensagem
        )
        db.add(db_historico)
        db.commit()
        db.refresh(db_historico)
        return db_historico