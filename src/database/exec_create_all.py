from src.database.base import Base
from src.database.engine import engine

from src.models.sport_session_model import SportSessionModel

table_objects = [SportSessionModel.__table__]

if __name__ == "__main__":
    Base.metadata.create_all(
        bind = engine(), 
        tables=table_objects,
        checkfirst=True
    )