
### Check open issues 

https://github.com/danionescu0/docker-flask-mongodb-example/issues consider taking on an issue, or adding a new one.

### Working on a issue 

* To start developing locally using anaconda:
````bash
cd docker--mongodb-example
conda create --name dockerflaskmongodbexample python=3.8.0
conda activate dockerflaskmongodbexample
pip install -r python/requirements.txt
pip install -r python/requirements-fastapi.txt
pip install -r python/requirements-mqtt.txt
pip install -r python/requirements-photo.txt
pip install -r python/requirements-restplus.txt
pip install -r python/requirements-dev.txt
````


* If you created a new service or modified some connexions between services, you may **generate a new diagram**.
I have created a diagram using this tool: https://diagrams.mingrammer.com 


To generate a new one install diagrams and graphviz packages inside your conda env:
````
pip install -r python/requirements-dev.txt
````
Now you're ready to modify "diagrams_generator.py" inside python folder then run the generator
````
cd python
python diagrams_generator.py
````
It will replace the ./resources/autogenerated.png file

* Run unit tests with pytest and fix the tests if they are failing, if it's new feature create a new test insite /tests folder

- first run the app locally
- install testing requirements
- run a specific test

````
docker-compose up
pip install -r tests/requirements.txt
pytest -q tests/test_users.py  -s
````

* Work on branch, modify what you need
* Run black () to format the code properly (if not the build will fail on push)
````
cd docker--mongodb-example
pip install -r python/requirements-dev.txt
black --exclude stresstest-locusts/ .
````

* Push and create a pull request

