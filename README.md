<h1>Onboarding</h1>
Onboarding is a web application that organises activities and tasks for new employees as part of their onboarding process. This repository is the front end.

<h2>Purpose</h2>
Current onboarding processes for new employees were done on paper. This presents a problem with portability and storage. A web application was proposed to facilitate this, plus enable collaboration and customisation across offices in different states.

<h3>Application Features</h3>
<ul>
<li>User authentication using Google accounts</li>
<li>An custom onboarding template for each state office</li>
<li>Administrators have authority to:
  <ul>
  <li>create a new task and assign an instructor to the task</li>
  <li>edit an existing task</li>
  <li>edit template tasks and their order</li>
  </ul>
<li>Managers can assign a template to a new subordinate and also an onboarding buddy</li>
<li>The new employee has access to their assigned tasks</li>
<li>Instructors and employee are able to mark a task as complete</li>
</ul>

***
<h2>Screenshots</h2>
<p>Login Page:</p>
<img src = "https://raw.githubusercontent.com/RCode-Blue/Onboarding/master/assets/img/Front.png">

<p>Logged In:</p>
<img src = "https://raw.githubusercontent.com/RCode-Blue/Onboarding/master/assets/img/LoggedIn.png">

<p>Task List</p>
<img src = "https://raw.githubusercontent.com/RCode-Blue/Onboarding/master/assets/img/TasksList.png">

<p>Editing a Task</p>
<img src = "https://raw.githubusercontent.com/RCode-Blue/Onboarding/master/assets/img/EditATask.png">

***
<h2>Built using</h2>
<ul>
<li>Python</li>
<li>Flask</li>
<li>Flask-OAuthlib</li>
<li>psycopg2</li>
<li>SQLAlchemy, Flask-SQLAlchemy</li>
</ul>

***

<h2>Installation</h2>
<h4>Download</h4>

- Browse to: https://github.com/RCode-Blue/Onboarding.git
- cd Onboarding


<h4>Setup virtual environment</h4>

<code>
pip install --user virtualenv<br />
virtualenv venv --python=python3.7
</code>


<br />
<h4>Start virtual environment</h4>

<code>
source venv/bin/activate <br />
pip install -r requirements.txt
</code>

<br />
<h4>To setup seed data:</h4>

<code>python create_tables_postgres.py</code>

<br />
<h4>To setup Google authentication:</h4>

- Browse to the [Google API console](https://console.developers.google.com) 
- Rename oa_sample.py to oa.py
- Put your keys in the appropriate locations

<br />
<h4>To run, type the following:</h4>
<code>
    export FLASK_ENV=development<br /></br />
    python app.py
</code>

***

<h2>Architecture Overview</h2>
<h3>Models</h3>
The back end consists of the following models:

| Name     | Description                                                                                                                                                                                            |
| -------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| task     | An individual task                                                                                                                                                                                     |
| template | A template of task sequences                                                                                                                                                                           |
| position | A table of task / template combinations                                                                                                                                                                |
| user     | A list of logged-in users                                                                                                                                                                              |
| set      | Links a template to a user                                                                                                                                                                             |
| sequence | A list of tasks assigned to a user.                                                                                                                                                                    |
|          | When a user is assigned to a template, the template, task and user information are obtained and new rows are created. When a user ticks a task as complete, this is the table that they are working on |


<h3> Key API Endpoints</h3>

| Path                       | Description                                                                        |
| -------------------------- | ---------------------------------------------------------------------------------- |
| /api/user/<string:userid>  | Returns a user given an id                                                         |
| /api/template              | Returns a template, given an id                                                    |
| /api/task                  | Returns a task given an id                                                         |
| /api/tasklist/<int:set_id> | Returns a user's onboarding tasks given a set id                                   |
| /addsequence/<int:set_id>  | Creates a list of onboarding tasks specific      to a selected user given a set id |




