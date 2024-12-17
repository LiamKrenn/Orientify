from sqlalchemy import String, ForeignKey, Integer, ARRAY, Float
from datetime import datetime
from sqlalchemy.orm import declarative_base, Mapped, mapped_column
from db.session import engine


Base = declarative_base()

class Data(Base):
    __tablename__ = "data"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    angle: Mapped[float] = mapped_column()
    timestamp: Mapped[datetime] = mapped_column(default=datetime.now)
    
    def __repr__(self) -> str:
        return (
            f"Data(id={self.id!r}, angle={self.angle!r}, timestamp={self.timestamp!r}) "
        )
    
class RawData(Base):
    __tablename__ = "raw_data"
    
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    timestamp: Mapped[datetime] = mapped_column(default=datetime.now)
    
    microphone1Data: Mapped[list[int]] = mapped_column(ARRAY(Integer))
    microphone2Data: Mapped[list[int]] = mapped_column(ARRAY(Integer))
    timeDifference: Mapped[float] = mapped_column(Float)
    microphonesDistance: Mapped[float] = mapped_column(Float, default=0.06)

    def __repr__(self) -> str:
        return (
            f"AudioDatenPacket(id={self.id!r}, timestamp={self.timestamp!r}, "
            f"microphone1Data={self.microphone1Data!r}, microphone2Data={self.microphone2Data!r}, "
            f"timeDifference={self.timeDifference!r}, microphonesDistance={self.microphonesDistance!r})"
        )


Base.metadata.create_all(engine)
