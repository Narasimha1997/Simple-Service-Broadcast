# Simple-Service-Broadcast
A simple UDP broadcast protocol used for service discovery in a local network and an API to add services in real-time.

<h3>Server.py</h3>
Server.py is an actual implementation of SO_BROADCAST protocl using berkely socket API. Server.py reads the content of service.txt and broadcasts
it to local-network's boradcast IP using UDP protocol as it's transport mechanism. The server can broadcast packets at regular time intervals, any changes
to service.txt is automatically updated during the next broadcast cycle. 

<h3> AddService API </h3>

<strong>AddService</strong> API provides procedures to add and remove services from service.txt file, it is by default created in $HOME/.services directory.

call <strong>check_availability()</strong> to make sure the file exists, else a new service file will be created.

<strong>add_service()</strong> will add a new service entry.

<h3> Registering a new service using AddService API </h3>

``` 
from service_discovery import AddService
#import AddService API

#you have to always call this function to make sure service.txt is present
AddService.check_availability()

#create a new service definition:
serv = {
    'name' : 'WaterServer',
    'addr' : '192.168.43.190',
    'description' : "Demo server",
    'port' : 5000
}
#register the service:
AddService.add_service(serv)

#remove method:
AddService.remove_service(serv)
```



