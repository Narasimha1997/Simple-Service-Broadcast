import os


def check_availability():
    home = os.environ['HOME']
    if not os.path.exists(home+'/.services'):
        os.mkdir(home+'/.services')
    return True


def add_service(service_data):
    home = os.environ['HOME']
    with open(home+'/.services/service.txt', 'a') as service_writer:
        name = service_data['name']
        addr = service_data['addr']
        descr = service_data['description']
        port = service_data['port']

        service_writer.write(
            name+";;"+addr+";;"+descr+";;"+str(port)+'\n'
        )
        print('service added successfully')
        service_writer.close()

def remove_service(service_data):
    path = os.environ['HOME']+'/.services/service.txt'
    if os.path.exists(path):
        data = open(path, 'r').readlines()
        for entry in data:
            splits = entry.split(';;')
            if splits[3] == str(service_data['port'])+'\n':
                data.remove(entry)
                print(entry)
                break
        os.remove(path)
        with open(path, 'a') as append:
            for i in data:
                append.write(i)
            append.close()
        print('Service successfully removed')
        return


        