# Tracking parcel
# Tech stack: Django, celery (async result), rabbitmq

How to run with docker:
In the first time:   
1. docker-compose build   
2. docker-compose up -d   

Follow the status task in container:   
```celery flower --broker=amqp://guest:guest@rabbitmq//```   
And see all task status in: http://192.168.99.100:5555/   


API add task, get result...
http://192.168.99.100:8000/docs/


Task is created and result of the task will be response async util done


