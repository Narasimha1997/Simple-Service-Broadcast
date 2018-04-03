import AddService

serv = {
    'name' : 'WaterServer',
    'addr' : '192.168.43.190',
    'description' : "Demo server",
    'port' : 5000
}

AddService.check_availability()
#AddService.add_service(serv)
AddService.remove_service(serv)
