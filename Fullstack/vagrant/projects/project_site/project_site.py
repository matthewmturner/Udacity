from flask import Flask, render_template, request, redirect, jsonify, url_for, flash, make_response
from flask import session as login_session
from sqlalchemy import create_engine, asc
from sqlalchemy.orm import sessionmaker
from db_model import Base, Projects, Tasks, Users
import httplib2
import random
import string
import json
from datetime import datetime

# Create Flask web server
app = Flask(__name__)

# Connect to SQLite database and create session
engine = create_engine('sqlite:///projects_v1.db', connect_args={'check_same_thread': False})
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()

@app.route('/')
@app.route('/projects/', methods=['GET', 'POST'])
def showProjects():
    print login_session
    # For showing projects
    if request.method == 'GET':
        # Check if a username is in login session and if not only show projects but dont allow edit/delete or ability to see tasks.
        if 'username' not in login_session:
            state = ''.join(random.choice(string.ascii_uppercase + string.digits) for x in xrange(32))
            login_session['state'] = state
            print 'The current login state is %s' % state
            projects = session.query(Projects).order_by(asc(Projects.project))
            return render_template('publicprojects2.html', projects=projects, STATE=state)
        else:
            project_user_id = getUserID(login_session['email'])
            projects = session.query(Projects).filter_by(project_user_id=project_user_id)
            #login_session.clear()
            return render_template('projects.html', projects=projects, session=login_session)
    # For handling creation of new projects
    elif request.method == 'POST':
        print request.form
        user = getUserID(login_session['email'])
        newProject = Projects(project=request.form['name'], project_description=request.form['project_description'],
                              project_startDate=datetime.strptime(request.form['start_date'], '%Y-%M-%d'), 
                              project_endDate=datetime.strptime(request.form['end_date'], '%Y-%M-%d'),
                              project_user_id=user)
        session.add(newProject)
        session.commit()
        print "New project %s added!" % request.form['name']
        return redirect(url_for('showProjects'))

@app.route('/projects/<int:project_id>/', methods=['GET', 'POST'])
def showProjectDetails(project_id):
    # For displaying project task details
    if request.method == 'GET':
        project = session.query(Projects).filter_by(project_id=project_id).one()
        tasks = session.query(Tasks).filter_by(project_id=project_id)
        return render_template('project.html', project=project, tasks=tasks)
    elif request.method == 'POST':
        newTask = Tasks(task=request.form['task'], task_description=request.form['task_description'],
                        task_startDate = datetime.strptime(request.form['start_date'], '%Y-%M-%d'),
                        task_endDate = datetime.strptime(request.form['end_date'], '%Y-%M-%d'),
                        user_id=login_session['user_id'], project_id=project_id)
        session.add(newTask)
        session.commit()
        print "New task %s added!" % request.form['task']
        return redirect(url_for('showProjectDetails', project_id=project_id))

@app.route('/projects/deleteProject/<int:project_id>', methods=['POST'])
def deleteProject(project_id):
    projectToDelete = session.query(Projects).filter_by(project_id=project_id).one()
    print projectToDelete
    if projectToDelete.project_user_id != login_session['user_id']:
        return "<script>function unauthDelete() {alert('You are not authorized to delete this project.');</script><body onload='unauthDelete()'>"
    else:
        session.delete(projectToDelete)
        session.commit()
        return redirect(url_for('showProjects'))

@app.route('/projects/deleteTask/<int:task_id>', methods=['POST'])
def deleteTask(task_id):
    taskToDelete = session.query(Tasks).filter_by(task_id=task_id).one()
    print taskToDelete
    if taskToDelete.user_id != login_session['user_id']:
        return "<script>function unauthDelete() {alert('You are not authorized to delete this task.');</script><body onload='unauthDelete()'>"
    else:
        session.delete(taskToDelete)
        session.commit()
        return redirect(url_for('showProjectDetails', project_id=taskToDelete.project_id))

@app.route('/projects/editProject/<int:project_id>', methods=['GET', 'POST'])
def editProject(project_id):
    if 'username' not in login_session:
        return redirect('/projects')
    editedProject = session.query(Projects).filter_by(project_id=project_id).one()
    print editedProject
    if login_session['user_id'] != editedProject.project_user_id:
        return "<script>function myfunction() {alert('You are not authorized to edit this project.  Please login to your profile to edit');}</script><bosy onload='myfunction()'>"
    if request.method == 'GET':
        return render_template('edit.html', type='project', project=editedProject)
    elif request.method == 'POST':
        if request.form['name']:
            editedProject.project = request.form['name']
        if request.form['start_date']:
            editedProject.project_startDate = request.form['start_date']
        if request.form['end_date']:
            editedProject.project_endDate = request.form['end_date']
        if request.form['description']:
            editedProject.project_description = request.form['description']
        session.add(editedProject)
        session.commit()
        return redirect('/projects')

@app.route('/projects/<int:project_id>/editTask/<int:task_id>', methods=['GET', 'POST'])
def editTask(project_id, task_id):
    if 'username' not in login_session:
        return redirect('/projects/%s' % project_id)
    editedTask = session.query(Tasks).filter_by(task_id=task_id).one()
    print editedTask
    if login_session['user_id'] != editedTask.user_id:
        return "<script>function myfunction() {alert('You are not authorized to edit this task.  Please login to your profile to edit');}</script><bosy onload='myfunction()'>"
    if request.method == 'GET':
        return render_template('edit.html', type='task', task=editedTask)
    elif request.method == 'POST':
        if request.form['name']:
            editedTask.task = request.form['name']
        if request.form['start_date']:
            editedTask.task_startDate = request.form['start_date']
        if request.form['end_date']:
            editedTask.task_endDate = request.form['end_date']
        if request.form['description']:
            editedTask.task_description = request.form['description']
        session.add(editedTask)
        session.commit()
        return redirect('/projects/%s' % project_id)

@app.route('/projects/json')
def projectsJSON():
    if 'username' not in login_session:
        projects = session.query(Projects).all()
    else:
        user = getUserID(login_session['email'])
        projects = session.query(Projects).filter_by(project_user_id=user).all()
    return jsonify([p.serialize for p in projects])

@app.route('/projects/<int:project_id>/json')
def projectTasksJSON(project_id):
    if 'username' not in login_session:
        return "User not recognized.  Please login to ask task details."
    else:
        project = session.query(Tasks).filter_by(project_id=project_id)
        return jsonify([t.serialize for t in project])

@app.route('/login')
def showLogin():
    state = ''.join(random.choice(string.ascii_uppercase + string.digits) for x in xrange(32))
    login_session['state'] = state
    print 'The current login state is %s' % state
    return render_template('login.html', STATE=state)

@app.route('/fbconnect', methods=['POST'])
def fbconnect():
    print login_session['state']
    if request.args.get('state') != login_session['state']:
        response = make_response(json.dumps('Invalid state parameter.'), 401)
        response.headers['Content-Type'] = 'application/json'
        return response
    access_token = request.data
    print 'Access token received: %s' % access_token

    app_id = json.loads(open('fb_client_secrets.json', 'r').read())['web']['app_id']
    app_secret = json.loads(open('fb_client_secrets.json', 'r').read())['web']['app_secret']
    url = 'https://graph.facebook.com/oauth/access_token?grant_type=fb_exchange_token&client_id=%s&client_secret=%s&fb_exchange_token=%s' % (
    app_id, app_secret, access_token)
    h = httplib2.Http()
    r = h.request(url, 'GET')[1]
    token = r.split(',')[0].split(':')[1].replace('"', '')
    login_session['token'] = token

    api_url = 'https://graph.facebook.com/v2.8/me?access_token=%s&fields=name,id,email' % token
    h = httplib2.Http()
    r = h.request(api_url, 'GET')[1]
    data = json.loads(r)
    print data

    login_session['provider'] = 'facebook'
    login_session['username'] = data['name']
    login_session['email'] = data['email']
    login_session['facebook_id'] = data['id']

    user_id = getUserID(login_session['email'])
    
    if not user_id:
        user_id = createUser(login_session)
    print "User ID is %s" % user_id
    login_session['user_id'] = user_id
    

    output = ''
    output += '<h1>Welcome, '
    output += login_session['username']
    output += '!</h1>'
    flash("Now logged in as %s" % login_session['username'])
    return output

@app.route('/fbdisconnect')
def fbdisconnect():
    print login_session
    facebook_id = login_session['facebook_id']
    token = login_session.get('token')
    print "FBDisconnect Access Token: %s" % token
    if token is None:
        del login_session['facebook_id']
        del login_session['provider']
        del login_session['email']
        del login_session['username']
        del login_session['_flashes']
        response = make_response(json.dumps("Current user not connected."), 401)
        response.headers['Content-Type'] = 'application/json'
        return response
    api_url = 'https://graph.facebook.com/%s/permissions?access_token=%s' % (facebook_id, token)
    h = httplib2.Http()
    r = h.request(api_url, 'DELETE')[0]
    print r
    if r['status'] == '200':
        del login_session['token']
        del login_session['facebook_id']
        del login_session['provider']
        del login_session['email']
        del login_session['username']
        del login_session['_flashes']

        flash("You are now logged out!")

        response = make_response(json.dumps("Successfully disconnected."), 200)
        response.headers['Content-Type'] = 'application/json'
        return redirect(url_for('showProjects'))
    else:
        response = make_response(json.dumps("Failed to revoke token for given user."), 400)
        response.headers['Content-Type'] = 'application/json'
        return response

def createUser(login_session):
    newUser = Users(user_name=login_session['username'], user_email=login_session['email'])
    session.add(newUser)
    session.commit()
    user = session.query(Users).filter_by(user_email=login_session['email']).one()
    return user.user_id

def getUserInfo(user_id):
    user = session.query(Users).filter_by(user_id=user_id).one()
    return user

def getUserID(email):
    try:
        user = session.query(Users).filter_by(user_email=email).one()
        return user.user_id
    except:
        return None



if __name__ == '__main__':
    app.secret_key = 'udacity_fullstack'
    app.debug = True
    app.run(host='0.0.0.0', port=5000, ssl_context=('cert.pem', 'key.pem'))