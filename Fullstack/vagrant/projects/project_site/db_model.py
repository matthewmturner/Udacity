from sqlalchemy import Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from datetime import datetime

Base = declarative_base()


class Users(Base):
    __tablename__ = 'users'

    user_id = Column(Integer, primary_key=True)
    user_name = Column(String, nullable=False)
    user_email = Column(String, nullable=False)


class Projects(Base):
    __tablename__ = 'projects'

    project_id = Column(Integer, primary_key=True)
    project = Column(String, nullable=False)
    project_description = Column(String, nullable=False)
    project_startDate = Column(Date, nullable=False)
    project_endDate = Column(Date, nullable=True)
    project_user = relationship(Users)
    project_user_id = Column(Integer, ForeignKey('users.user_id'))

    @property
    def serialize(self):
        return {
            'project_id': self.project_id,
            'project': self.project,
            'project_description': self.project_description,
            'project_startDate': self.project_startDate,
            'project_endDate': self.project_endDate,
            'project_user_id': self.project_user_id
        }


class Tasks(Base):
    __tablename__ = 'tasks'

    task_id = Column(Integer, primary_key=True)
    task = Column(String, nullable=False)
    task_description = Column(String, nullable=False)
    task_startDate = Column(Date, nullable=False)
    task_endDate = Column(Date, nullable=True)
    project = relationship(Projects)
    project_id = Column(Integer, ForeignKey('projects.project_id'))
    user = relationship(Users)
    user_id = Column(Integer, ForeignKey('users.user_id'))

    @property
    def serialize(self):
        return {
            'task_id': self.task_id,
            'task': self.task,
            'task_description': self.task_description,
            'task_startDate': self.task_startDate,
            'task_endDate': self.task_endDate,
            'project_id': self.project_id,
            'user_id': self.user_id
        }


engine = create_engine('sqlite:///projects_v1.db')
Base.metadata.create_all(engine)

