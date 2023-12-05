# django_celery_routing
The simple example Celery routing in Django Framework

The simple project figure out how using Celery routing

route config  -> core/celery.py
```
app.conf.task_routes = {
    "semple.tasks.semple_task": {"queue": "general-queue"},
    "semple.tasks.semple_task_sorted": {"queue": "helper-queue"},
    "semple.tasks.semple_task_send_email": {"queue": "email-queue"},
}
```
Run docker-compose

```
docker-compose build 
after
docker-compose up
```
OR Local 

```
# install pkg
pdm sync
# run server
pdm start 
# run celery queue
pdm helper
pdm genera
pdm email
```