[![Build Status](https://travis-ci.com/ccbndh/trackit.svg?token=A6u9nWoL1AULJQHGeii4&branch=master)](https://travis-ci.com/ccbndh/trackit)   



# Track order status
# Tech: Django, celery, rabbitmq, reactjs

How to run with docker:
1. docker-compose build
2. docker-compose up -d   

API add task, get result...
http://127.0.0.1:8000/docs/

Follow the status task by flower:   
http://127.0.0.1:5555/




Task is created and result of the task will be response async util done, js polling result by task_id



