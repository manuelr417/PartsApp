# PartsApp
Parts Demo App for Database access.

This simple app shows how to build a REST API for the backend of a database application using Flask. The Database engine is PostgreSQL. the application manages data from three tables:
1. Parts - information about the parts in the system.
2. Suppliers - information about the suppliers.
3. Supplies - information on which suppliers supply a set of parts. 

The application is organized in three broad layers:
1. Main - the main app module takes care to setup the routes for the REST API and calling the proper handler objects to process the request.
2. Handlers - the handler modules takes care of implementing the logic of each REST call. In this sense, a handler is a Facade for accessing a given operation on a data collection. Each object handles a particular type of request for a data collection (e.g. Parts). The handlers rely upon the Data Access Objects (DAOs) to extact data from the database. The handlers encode the responses to the client with JSON and provide the appropriate HTTP response code.
3. DAOs = 
