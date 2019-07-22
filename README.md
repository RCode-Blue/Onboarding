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
<h2>How to Use</h2>
Click login on the front page:
![Login](/assets/img/Front.png)


***
<h2>Back End Details</h2>
<ul>
<li>Language: Python</li>
<li>Framework: Flask</li>
<li>Authentication: Flask-OAuthlib</li>
<li>Database adapter: psycopg2</li>
<li>Object-Relational mapper: SQLAlchemy, Flask-SQLAlchemy</li>
</ul>

***

<h2>Installation</h2>
<h4>Download</h4>

- Browse to: https://github.com/RCode-Blue/Onboarding.git
- cd Onboarding


<h4>Setup and start virtual environment</h4>

    sudo pip install virtualenv
    virtualenv venv --python=python3.7
    source venv/bin/activate
    pip install -r requirements.txt



<h4>To setup seed data:</h4>

    python create_tables_postgres.py


<h4>To setup Google authentication:</h4>

- Browse to the [Google API console](https://console.developers.google.com) 
- Rename oa_sample.py to oa.py
- Put your keys in the appropriate locations


<h4>To run:</h4>

    python app.py


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




