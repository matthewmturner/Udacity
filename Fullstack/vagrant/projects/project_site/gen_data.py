from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from db_model import Base, Users, Projects, Tasks
from datetime import date

engine = create_engine('sqlite:///projects_v1.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()

# project1 = Projects(project='Home Finances',
#                     project_description='All home related budget, expense, and account tasks',
#                     project_startDate=date(year=2018, month=12, day=17),
#                     project_user_id=1)

# session.add(project1)
# session.commit()

# project2 = Projects(project='Travel',
#                     project_description='All personal and work related travel tasks',
#                     project_startDate=date(year=2019, month=2, day=18),
#                     project_user_id=1)

# session.add(project2)
# session.commit()

# project3 = Projects(project='Clean Garage',
#                     project_description='All work for cleaning and organizing garage by Summer 2019',
#                     project_startDate=date(year=2018, month=12, day=17),
#                     project_endDate=date(year=2020, month=6, day=30),
#                     project_user_id=1)

# session.add(project3)
# session.commit()

project1 = Projects(project='Home Finances',
                    project_description='All home related budget, expense, and account tasks',
                    project_startDate=date(year=2018, month=12, day=17),
                    project_user_id=1)

session.add(project1)
session.commit()

project2 = Projects(project='Travel',
                    project_description='All personal and work related travel tasks',
                    project_startDate=date(year=2019, month=2, day=18),
                    project_user_id=1)

session.add(project2)
session.commit()

project3 = Projects(project='Clean Garage',
                    project_description='All work for cleaning and organizing garage by Summer 2019',
                    project_startDate=date(year=2018, month=12, day=17),
                    project_endDate=date(year=2020, month=6, day=30),
                    project_user_id=1)

session.add(project3)
session.commit()