import os
from termcolor import colored
from core.cli.cli import Cli
from core.netpy import NetPy


cli = Cli(command=os.sys.argv[1:], name="netpy", description="more than implementation of netcat 🐱🔥")

cli.add_argument(args=("-s", "--addr"), name="address", type=str, required=False,
                 positional=True, optional=True, position=-2, default="127.0.0.1", help="computes cube for the given value")

cli.add_argument(args=("-p", "--port"), name="port", required=True,
                 positional=True, optional=True, position=-1, help="port to listen on")

## scan for open ports
cli.add_argument(args=("-z", "--scan"), name="scan", required=False, type=bool, default=False, help="zero-I/O mode [used for scanning]")
cli.add_argument(args=("-w", "--timeout"), name="timeout", required=False, default=False, help="timeout for connects and final net reads")
cli.add_argument(args=("-v", "--verbose"), name="verbose", required=False, default=False, help="verbose [use twice to be more verbose]")

## udp
cli.add_argument(args=("-u", "--udp"), name="udp", required=False, default=False, help="UDP mode")

## execute
cli.add_argument(args=("-e", "--prog"), name="prog", required=False, default=False, help="inbound program to exec")

## listening
cli.add_argument(args=("-l", "--listen"), name="listen", type=bool, required=False, default=False, help="listen on [host]:[port]")
cli.add_argument(args=("-L", "--force-listen"), name="force_listen",type=bool, default=False, required=False, help="listen harder, re-listen on socket close")

## connect
cli.add_argument(args=("-r", "--random"), name="random", required=False, default=False, help="randomize local and remote ports")
cli.add_argument(args=("-c", "--connect"), name="connect", required=False, default=False, help="connect to [host]:[port]")

## Authentication
cli.add_argument(args=("-a", "--auth"), name="auth", required=False, help="authentication mode")
cli.add_argument(args=("-u", "--username"), name="username", required=False, default=False, help="username")
cli.add_argument(args=("-pw", "--password"), name="password", required=False, default=False, help="password")

cli.run()

netpy = NetPy()


netpy.set_ip(cli.values.get("address"))
netpy.set_port(cli.values.get("port"))

if cli.values.get("listen"):
    print("listening on {}:{}".format(cli.values.get("address"), cli.values.get("port")))
elif cli.values.get("scan"):
    ports = netpy.scan()
    closed = 0

    print("scanning {} {}".format(cli.values.get("address"), cli.values.get("port")))

    print("open ports:")
    for port in ports:
        stat = port.get("stat")
        port = port.get("port")

        if stat == "opened":
            print("{} {}".format(port, colored(stat, "green")))

        elif stat == "closed":
            closed += 1

    print()

    print("closed ports: {}".format(closed))
    print("{} {} ports".format(closed, colored("closed", "red")))
