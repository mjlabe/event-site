### Starting application via docker

* `docker-compose down && docker-compose build && docker-compose up -d`
* Navigate to localhost:8000
* Login wagtail/wagtail

### TODO's
* Create a Makefile for easy start commands like `make start`, `make test` etc
* Allow using a committed docker container on docker-compose startup
* * I.e. Save a container full of data and then use it between runs


### Pycharm
* If you go to Settings->Build,Execution,Deployment->Docker you can create a local docker ~thingy~
* * Once that is created you can go to Views->Toolbars->Docker
* Now if you right click on the "docker-compose.yml" file and select "Run" it will start up your containers but it will also create a configuration much like the "Debug" one's we are accustomed to using
* * You can now adjust the configuration just like you do a debug configuration
* * Select the force build flag and add to the services list `web, db`