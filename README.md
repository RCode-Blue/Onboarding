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
<code>
https://github.com/RCode-Blue/Onboarding.git
cd Onboarding
</code>

<h4>Setup and start virtual environment</h4>
<code>
sudo pip install virtualenv
virtualenv venv --python=python3.7
source venv/bin/activate
pip install -r requirements.txt
</code>


<h4>To setup seed data:</h4>
<code>
python create_tables_postgres.py
</code>


<h4>To run:</h4>
<code>
python app.py
</code>

