import abc
import socket
import psutil
import sys
import json


class HostInfo:
    __metaclass__ = abc.ABCMeta

    def __init__(self):
        self.hostname = None
        self.memory = None
        self.cpu = None
        self.ip = None
        self.disk_size = None

    @abc.abstractmethod
    def get_hardware_info(self):
        pass

    def update_param(self, hostname, memory, cpu, ip, disk_size):
        self.hostname = hostname
        self.memory = memory
        self.cpu = cpu
        self.ip = ip
        self.disk_size = disk_size

    def display_hardware_info(self):
        dict_data = {
            "hostname": self.hostname,
            "memory": self.memory,
            "cpu": self.cpu,
            "ip": self.ip,
            "disk_size": self.disk_size
        }

        json_data = json.dumps(dict_data)
        print(json_data)


class LinuxHost(HostInfo):
    def get_hardware_info(self):
        hostname = socket.gethostname()
        memory = str(psutil.virtual_memory()[0]) + " GB"
        cpu = psutil.cpu_count()
        ip = socket.gethostbyname(hostname)
        disk_size = str(psutil.disk_usage("/")[0] // (2**30)) + " GB"
        self.update_param(hostname, memory, cpu, ip, disk_size)


class WindowsHost(HostInfo):
    def get_hardware_info(self):
        hostname = socket.gethostname()
        memory = str(psutil.virtual_memory()[0]) + " GB"
        cpu = psutil.cpu_count()
        ip = socket.gethostbyname(hostname)
        disk_size = str(psutil.disk_usage("/")[0] // (2 ** 30)) + " GB"
        self.update_param(hostname, memory, cpu, ip, disk_size)


is_windows = sys.platform.startswith('win')
if is_windows:
    obj = WindowsHost()
    obj.get_hardware_info()
    obj.display_hardware_info()


is_linux = sys.platform.startswith('lin')
if is_linux:
    obj = LinuxHost()
    obj.get_hardware_info()
    obj.display_hardware_info()

