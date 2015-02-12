from services import linux

class BaseTemplate:
    name = None
    services = None
    hostname = None
    ip_address = None
    port = None
    os = None

class LinuxGeneraiServices(BaseTemplate):
    def __init__(self):
        self.name = 'Linux General Services'
        self.services = {
                    'cpu': linux.cpu(),
                    'load': linux.load(),
                    'memory': linux.memory(),
                    }

class WindowsGeneralService(BaseTemplate):
    def __init__(self):
        self.name = 'Windows General Service'
        self.services = {
                     'cpu': linux.cpu(),
                    'load': linux.load(),
                    'memory': linux.memory(),
                    }
    