**PING PONG CHAMPIONSHIP**

*Dependencies*
- cherrypy

To install the dependencies:
'''pip install -r requirements.txt'''

To start the application:
'''python app.py'''

The server runs on the default port of 1007.
To hit any api from the local system after starting the system:
*localhost:10007/api_routes*

**List of APIs available**
1. /api/getplayers
Gets the list of players available for the game.
2. /api?getplayers?id=1
Gets the player details for the particular player id.
3. /api/starttournament*
Start the tournament among the player orchestrated by the referee and returns
the results of the game.
4. /api/report
Generates the report for all the tournament held.


# todo
1. /api/addplayer
2. /api/dropplayer
3. /api/configuregame
4. /api/addreferee

5. Make all the games run concurrently using multithreading.
6. Persist the scores of the players.
7. Write test cases.
8. Implement authentication.
