# Task List API

Link to my deployed Heroku app: https://jaime-task-list-api.herokuapp.com/ (May be turned off now that it's not free). It will need the appropriate paths to run, such as /tasks, /tasks<task_id>, /goals, /goals/<goals_id>/tasks The id is always an integer in these routes.

## Project Directions

This project is designed to fulfill the features described in detail in each wave. The tests are meant to only guide your development.

1. [Setup](ada-project-docs/setup.md)
1. [Testing](ada-project-docs/testing.md)
1. [Wave 1: CRUD for one model](ada-project-docs/wave_01.md)
1. [Wave 2: Using query params](ada-project-docs/wave_02.md)
1. [Wave 3: Creating custom endpoints](ada-project-docs/wave_03.md)
1. [Wave 4: Using an external web API](ada-project-docs/wave_04.md)
1. [Wave 5: Creating a second model](ada-project-docs/wave_05.md)
1. [Wave 6: Establishing a one-to-many relationship between two models](ada-project-docs/wave_06.md)
1. [Wave 7: Deployment](ada-project-docs/wave_07.md)
1. [Optional Enhancements](ada-project-docs/optional-enhancements.md)

## How to store data in database using postman:

To add tasks, send a POST to
https://jaime-task-list-api.herokuapp.com/goals

In POST, go to 'body' chose 'raw' then in drop down menu chose 'json'
with a HTTP request body:

{
"title": "A Brand New Task",
"description": "Test Description",
"completed_at": null
}

To get all tasks send a GET request to https://jaime-task-list-api.herokuapp.com/tasks:
To get all tasks send a GET request to https://jaime-task-list-api.herokuapp.com/tasks/<task_id>/

For adding goals, send a POST to
https://jaime-task-list-api.herokuapp.com/goals
With a HTTP request body:

{
"title": "My New Goal"
}

To get all tasks send a GET request to https://jaime-task-list-api.herokuapp.com/goals:
To get a task for ONE task send a GET to https://jaime-task-list-api.herokuapp.com/goals/<goal_id>:

For adding a list of Tasks to Goals, send a POST request https://jaime-task-list-api.herokuapp.com/goals/1/tasks:
Request Body:
{
"task_ids": [1, 2, 3]
}

or
create a task in a list more directly in one POST https://jaime-task-list-api.herokuapp.com/goals/1/tasks:
{
"title": "Build a habit of going outside daily",
"tasks": [
{
"goal_id": 1,
"title": "Go on my daily walk 🏞",
"description": "Notice something new every day",
"is_complete": false
}
]
}

To put tasks in ascending order:
Set to GET, no request body needed
https://jaime-task-list-api.herokuapp.com/tasks?sort=asc

To put tasks in descending order:
Set to GET, no request body needed
https://jaime-task-list-api.herokuapp.com/tasks?sort=desc

To mark complete:
set to PATCH, no request body needed
https://jaime-task-list-api.herokuapp.com/tasks/1/mark_complete

To mark incompete:
set to PATCH, no request body needed
https://jaime-task-list-api.herokuapp.com/tasks/1/mark_incomplete

future features would add similar route features to goals

Other CRUD routes:
UPDATE /tasks/<tasks_id>
DELETE /tasks/<tasks_id>
UPDATE /goals/<goal_id>
DELETE /goals/<goal_id>

future docstring instructions will include how to send response bodies to a clients Slack API channel.
'''

## Skills Assessed

- Following directions and reading comprehension
- Reading, writing, and using tests
- Demonstrating understanding of the client-server model, request-response cycle and conventional RESTful routes
- Driving development with independent research, experimentation, and collaboration
- Reading and using existing external web APIs
- Using Postman as part of the development workflow
- Using git as part of the development workflow

Working with the Flask package:

- Creating models
- Creating conventional RESTful CRUD routes for a model
- Reading query parameters to create custom behavior
- Create unconventional routes for custom behavior
- Apply knowledge about making requests in Python, to call an API inside of an API
- Apply knowledge about environment variables
- Creating a one-to-many relationship between two models

## Goals

There's so much we want to do in the world! When we organize our goals into smaller, bite-sized tasks, we'll be able to track them more easily, and complete them!

If we make a web API to organize our tasks, we'll be able to create, read, update, and delete tasks as long as we have access to the Internet and our API is running!

We also want to do some interesting features with our tasks. We want to be able to:

- Sort tasks
- Mark them as complete
- Get feedback about our task list through Slack
- Organize tasks with goals

... and more!

## How to Complete and Submit

Go through the waves one-by-one and build the features of this API.

At submission time, no matter where you are, submit the project via Learn.
