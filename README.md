# SimpleDragonTideBot

This project was made out of boredom for user on reddit. He wanted a bot that could automate resting and hunting inside the game [Dragon Tide](https://dragontide.com/).

## Built With

* Python
* Regex
* Beautiful Soup 4

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

Note that this is still in development.

### Prerequisites

Install the software below before proceeding to the next step. Links provided.

Required
* [Git (Version Control System)](https://git-scm.com/)
* [Python 3.8 or Higher](https://www.python.org/downloads/)

Not Required
* [Visual Studio Code](https://code.visualstudio.com/) (Or a Python IDE of your choice.)

### Installing

A step by step series of examples that tell you how to get a development env running.

1. Clone or Download the Repository to a location on your computer and open a terminal at that location.
```
git clone https://github.com/William-Avery/SimpleDragonTideBot.git
```

2. Install Packages Required
```
python -m pip install -r packages.txt
```

### Running

Lets take a look at our **main.py**:

```
from SessionManager.Session import Session

# Define Required Variables
username=''
password=''
charID = ''

# Create Session
s = Session(username,password,charID)

# Run Login to Establish Session
s.Login()

# Start Bot
s.Start()
```

1. Enter your username:
```
username=''
```

2. Enter your password:
```
password=''
```

3. Enter CharacterID:

* Go to your character selection screen.
* Right Click > Copy link address of the character your want to login as.
* When you paste, it should look something like this.

```
# Paste Results
https://www.dragontide.com/logincheck3.aspx?char=12345

# Set charID to the number at the end of the URL
charID = '12345'
```

4. Starting the Application:

* Open a terminal at the **main.py** location and run the following.

```
python main.py
```

## Authors

* **William Avery**

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* Hat tip to anyone whose code was used
