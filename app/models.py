from sqlalchemy import TIMESTAMP, Column, Integer, String, ARRAY, DATE, Enum, DateTime
from sqlalchemy.sql.schema import Identity
from sqlalchemy.ext.declarative import declarative_base
import enum

Base = declarative_base()


class User(Base):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, nullable=False)
    fullstory_link = Column(String, nullable=True)
    mixpanel_link = Column(String, nullable=True)
    primary_email = Column(String, nullable=True)
    other_email = Column(ARRAY(String), nullable=True)
    events = Column(ARRAY(String), nullable=True)
    msg_id = Column(String, unique=True, nullable=False)
    timestamp = Column(TIMESTAMP)

    def __repr__(self):
        return "<User(id='%d, username='%s', fullstory_link='%s', mixpanel_link='%s, msg_id='%s', timestamp='%s')>" % (
            self.id, self.username, self.fullstory_link, self.mixpanel_link,
            self.msg_id, self.timestamp)

    def toDict(self):
        return {
            'id': self.id,
            'username': self.username,
            'fullstory_link': self.fullstory_link,
            'mixpanel_link': self.mixpanel_link,
            'primary_email': self.primary_email,
            'other_email': self.other_email,
            'events': self.events,
            'msg_id': self.msg_id,
            'timestamp': self.timestamp
        }


class Event(Base):
    __tablename__ = "event"

    id = Column(Integer, primary_key=True, index=True)
    date = Column(DATE, nullable=False)
    username = Column(String, nullable=False)
    parent_event_count = Column(Integer, nullable=False)
    events = Column(ARRAY(String), nullable=False)
    msg_id = Column(String, unique=True)

    def toDict(self):
        return {
            'id': self.id,
            'date': self.date,
            'username': self.username,
            'events': self.events,
            'parent_event_count': self.parent_event_count,
            'msg_id': self.msg_id,
        }


class statusEnum(enum.Enum):
    running = 0
    fail = 1
    success = 2


class Job(Base):
    __tablename__ = "job"

    id = Column(Integer, Identity(start=1), primary_key=True, index=True)
    start_time = Column(DateTime(timezone=True))
    end_time = Column(DateTime(timezone=True))
    logdna_start_time = Column(String)  #ms
    logdna_end_time = Column(String)  #ms
    duration = Column(String)
    logdna_duration = Column(String)  #sec
    event_count = Column(Integer)
    status = Column('status', Enum(statusEnum))


class Error(Base):
    __tablename__ = "error"

    id = Column(Integer, Identity(start=1), primary_key=True, index=True)
    time = Column(DateTime(timezone=True))
    type = Column(String)
    error = Column(String)
