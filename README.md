# rest_api_server_python_flask

This is a git repository for a cloud based server providing REST API service and storage running on flask and hosted on pythonanywhere.

The project consists of two components:

  - A Book viewer REST API server with AJAX web interface
  - A Raspberry PI application with a sensor HAT collecting weather data and pushing it to the cloud server using the REST API

http://jattie.pythonanywhere.com/bookviewer.html

http://jattie.pythonanywhere.com/pigraph.html

Both Applications are hosted on PythonAnywhere.

The Raspberry PI code is available here: https://github.com/G00364778/rest_client_pi

More information on a raspberry pi is here: https://www.raspberrypi.org/

The sensor board information is here:

https://wiki.52pi.com/index.php/DockerPi_Sensor_Hub_Development_Board_SKU:_EP-0106


## Files in the repository

|File DateTime    |File Bytes        |File Name         |File Description|
|-----------------|------------------|------------------|-------------------------------------------|
|06/12/2019  17:42|                19| .gitignore       |Ignore the sources for revision tracking   |
|02/12/2019  10:39|               305| app.py           |Basic Flask server test setup              |
|11/12/2019  22:31|             3,868| bookDAO.py       |MySQL database interface functionalities   |
|11/12/2019  22:47|             9,500| bookviewer.html  |The Bookviewer HTML and Java/AJAX Scripts  |
|06/12/2019  17:39|               104| config.py        |The file to be created on the target server|
|06/12/2019  17:39|                82| configtemplate.py|The template file for config               |
|12/12/2019  11:43|             2,159| dump_book.sql    |The SQL dump file for the book table       |
|12/12/2019  11:44|             3,182| dump_pisense.sql |The SQL dump file for the pisense table    |
|07/12/2019  12:25|                82| index.html       |The index file that redirect to bookviewer |
|02/12/2019  08:40|             1,099| LICENSE          |The License file for the code              |
|11/12/2019  22:34|               602| pigraph.html     |The HTML file for the pi data graphing     |
|12/12/2019  11:58|               846| README.md        |The Readme for the project                 |
|12/12/2019  11:59|            59,558| README.pdf       |The pdf generated from the readme          |
|01/12/2019  19:01|              248 |requirements.txt  |The python requirements for running it all |
|11/12/2019  22:31|             4,653| server1.py       |The main flask server file in python       |