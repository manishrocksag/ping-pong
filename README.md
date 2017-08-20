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
*/api/getplayers*
Gets the list of players available for the game.
*/api?getplayers?id=1*
Gets the player details for the particular player id.
*/api/starttournament*
Start the tournament among the player orchestrated by the referee and returns
the results of the game.
*/api/report*
Generates the report for all the tournament held.


# todo
/api/addplayer
/api/dropplayer
/api/configuregame
/api/addreferee

Make all the games run concurrently using multithreading.
Persist the scores of the players.
Write test cases.
Implement authentication.
