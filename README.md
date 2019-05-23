## Behave Test Structure

```sh
├── conf            //< store all configurations related (user infos, environment parameters,..)
├── features        //< home folder (following BDD Style)
│   ├── hooks
│   ├───── api      //< api helpers 
│   ├── steps       //< python steps implementation files for the scenarios
```

## Getting Started

This is the quick and easy getting started assuming you already have git and pip installed.

```sh

# navigate into directory
cd ~/API-Test-Automation

# Install the required libraries
sudo pip install -r requirements.txt

# Rename sample_users.json to users.json in conf/
{
  "Test User": {
    "email": "hashaha2212014@gmail.com",
    "password": "mypassword123!",
    "username": "@duynguyenhvn",
    "location": "NashTech"
  }
}

# to run all the test scenarios (replace env variable with the desired url):
export API_HOST='https://unsplash.com/napi'; behave

# to run scenarios with specific tags:
export API_HOST='https://unsplash.com/napi'; behave -k --tags=tag_name
```

## Behave Test Runner

Behave support several [command-line arguments](https://pythonhosted.org/behave/behave.html) that you can use for your convenience, like so:

## IDE

### PyCharm

We prefer to use the new [PyCharm](https://www.jetbrains.com/pycharm/) 4.0+ Professional Edition since it is the most intelligent python IDE which supports Behavior-Driven Development (BDD) such as behave and lettuce.

For working in PyCharm, I would also recommend:

* [Setup, Configure and Execute Behave](http://blog.jetbrains.com/pycharm/2014/09/feature-spotlight-behavior-driven-development-in-pycharm/)


### VSCode

For working in VSCode, I would also recommend:

* [Getting Started with Python in VS Code](https://code.visualstudio.com/docs/python/python-tutorial)