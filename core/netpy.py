import socket
import subprocess
import sys
import threading
import time
from pymitter import EventEmitter

from .constants import *

class NetPy(EventEmitter):
    def __init__(self):
        super().__init__()
        self.port = 0
        self.ports = []
        self.ip = "0.0.0.0"
        self.method = ScanMethod.TCP
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.BUFFER_SIZE = 1024
        self.process = None
        pass

    def set_port(self, ports: int):
        self.port_start = 0
        self.port_end = 0

        if "-" in ports:
            self.port_start, self.port_end = ports.split("-")
            self.port_start = int(self.port_start)
            self.port_end = int(self.port_end)

        else:
            self.port_start = int(ports)
            self.port_end = int(ports)

    def set_ip(self, ip: str):
        self.ip = ip

    def set_timeout(self, timeout=0.5):
        self.timeout = timeout
        self.socket.settimeout(timeout)

    def set_verbose(self, verbose: bool):
        self.verbose = verbose

    def set_udp(self, udp: bool):
        if udp:
            self.socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            self.socket.settimeout(self.timeout)
            self.method = ScanMethod.UDP

    def set_prog(self):
        self.process = subprocess.Popen(['C:\\Windows\\system32\\cmd.exe'])

    def _scan(self, ports, port):
        result = {"port": port,"stat": ScanStatus.FILTERED}
        try:
            self.socket.connect((self.ip, port))
            if self.method == ScanMethod.UDP:
                self.socket.send(bytes(0))
                self.socket.recv(1024)

            result["stat"] = ScanStatus.OPEN
            ports.append(result)
            self.emit("scan", result)

        except socket.timeout:
            if self.method == ScanMethod.UDP:
                result["stat"] = ScanStatus.OPEN_FILTERED
            elif self.method == ScanMethod.TCP:
                result["stat"] = ScanStatus.FILTERED
            ports.append(result)
            self.emit("scan", result)

        except socket.error:
            if self.method == ScanMethod.UDP:
                result["stat"] = ScanStatus.CLOSED_FILTERED
            elif self.method == ScanMethod.TCP:
                result["stat"] = ScanStatus.CLOSED
            ports.append(result)
            self.emit("scan", result)

        finally:
            pass

    def scan(self):
        ports = []
        count = 0

        if self.port_start == self.port_end:
            self._scan(ports, self.port_start)

        for port in range(self.port_start, self.port_end):
            # threading.Thread(target=self._scan, args=(ports, port,)).start()
            self._scan(ports, port)
            time.sleep(0.1)
            count += 1

        # while len(ports) != count:
        #     time.sleep(0.1)

        self.emit("scan_end", ports)
        self.stop()

        return ports

    def listen(self):
        self.socket.bind((self.ip, self.port_start))
        self.socket.listen(1)
        print('listening on {}:{}'.format(self.ip, self.port_start))

        conn, _ = self.socket.accept()

        while 1:
            data = conn.recv(1024)

            if not data:
                break

            print("recived:", self.s(data))

            if self.prog:
                self.process()

            msg = input("send: ")
            if msg == "q":
                break

            conn.send(self.p(msg).encode())
        conn.close()

    def readlines(self, process):
        while process.poll() is None:
            time.sleep(1)
            sys.stdout.write(process.stdout.readline().decode())

    def connect(self):
        # self.socket.connect((self.ip,  self.port_start))
        print('connected to {}:{}'.format(self.ip, self.port_start))
        process = subprocess.Popen(['C:\\Windows\\system32\\cmd.exe', ''],
                                   stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

        print(process.stdout.readline().decode())

    def stop(self):
        self.socket.close()
        # self.process.kill()
        self.emit("stop")

    def p(self, msg: str) -> str:
        return msg + " " * (self.BUFFER_SIZE - len(msg))

    def s(self, msg: bytes) -> str:
        return msg.decode("utf-8").strip()

    def __str__(self):
        return 'netcat({}:{})'.format(self.ip, self.port_start)

    def __repr__(self):
        return '<{}>'.format(self)

    def run(self):
        pass