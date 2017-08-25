**PING PONG CHAMPIONSHIP**

*Dependencies*
- cherrypy

To install the dependencies:
'''pip install -r requirements.txt'''

To start the application:
'''python app.py'''

The server runs on the default port of 5000.
To hit any api from the local system after starting the system:
*localhost:5000/api_routes*

*The app is hosted in HEROKU. It can also be accessed
through **https://ping-pong-ping.herokuapp.com***

**List of General APIs available**
1. /api/getplayers
Gets the list of players available for the game.
2. /api?getplayers?id=1
Gets the player details for the particular player id.
3. /api/starttournament
Start the tournament among the player orchestrated by the referee and returns
the results of the game.
4. /api/report
Generates the report for all the tournament held.

**To play a game by user**
1. /api/createnewtournament
2. /api/registerplayers
3. /api/registerreferee
4. /api/getplayers
5. /api/startmatch?player1=Joey&player2=Nick
6. /api/winnerslist
7. /api/getremainingplayers
8. /api/currentwinner

*The start match has to be called multiple times among
players and also between winners*

**MISC**
1. /api/addplayer?no=1&name=Jack&defence_set_length=6

**TODO**
1. /api/dropplayer
2. /api/configuregame
3. Make all the games run concurrently using multithreading.
4. Persist the scores of the players.
5. Write test cases.
6. Implement authentication.




