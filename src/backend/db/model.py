from sqlalchemy import String, ForeignKey
from datetime import datetime
from sqlalchemy.orm import declarative_base, Mapped, mapped_column
from db.session import engine


Base = declarative_base()

class Compass(Base):
    __tablename__ = "compass"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    angle: Mapped[float] = mapped_column()
    timestamp: Mapped[datetime] = mapped_column(default=datetime.now)
    
    def __repr__(self) -> str:
        return (
            f"Compass(id={self.id!r}, angle={self.angle!r}, timestamp={self.timestamp!r}) "
        )
    
class RawData(Base):
    __tablename__ = "raw_data"
    
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    timestamp: Mapped[datetime] = mapped_column(default=datetime.now)
    value: Mapped[float] = mapped_column()

    def __repr__(self) -> str:
        return (
            f"RawData(id={self.id!r}, value={self.value!r}, timestamp={self.timestamp!r}) "
        )


Base.metadata.create_all(engine)
