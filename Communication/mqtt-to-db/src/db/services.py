from db.model import RawData, Data
from db.session import session


def save_angle(data):
    data = Data(
            angle=data
        )
    session.add(data)
    session.commit()
    return data

def save_raw(data):
    """data = RawData(
        microphone1Data=,
        microphone1Data=,
        timeDifference=,
        microphonesDistance=
    )
    session.add(data)
    session.commit()
    return data"""
    pass
