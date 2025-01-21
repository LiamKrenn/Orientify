from sqlalchemy import String, ForeignKey, Integer, ARRAY, Float
from datetime import datetime
from sqlalchemy.orm import declarative_base, Mapped, mapped_column


Base = declarative_base()

class Data(Base):
    __tablename__ = "data"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    angle: Mapped[float] = mapped_column()
    timestamp: Mapped[datetime] = mapped_column(default=datetime.now)

    
class RawData(Base):
    __tablename__ = "raw_data"
    
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    timestamp: Mapped[datetime] = mapped_column(default=datetime.now)
    
    microphone1Data: Mapped[list[int]] = mapped_column(ARRAY(Integer))
    microphone2Data: Mapped[list[int]] = mapped_column(ARRAY(Integer))
    timeDifference: Mapped[float] = mapped_column(Float)
    microphonesDistance: Mapped[float] = mapped_column(Float, default=0.06)