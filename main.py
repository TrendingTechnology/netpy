import argparse
from netpy.netpy import NetPy


# exmaples:
# netpy -l
# netpy -l -p 8080
# netpy -l -p 8080 -t 5
# netpy -l -p 8080 -t 5 -i
# netpy -l -p 8080 -t 5 -i -v

# -z
# -v	Enables verbose mode
# -w	Used when there is a need to specify a time-out condition

def main():
    parser = argparse.ArgumentParser(
        prog="netpy", description='more than implementation of netcat 🐱🔥')

    # listening
    parser.add_argument('-l', '--listen', action='store_true', help='listen on [host]:[port]')
    parser.add_argument('-L', '--force-listen', action='store_true', help='listen harder, re-listen on socket close')

    # scan for open ports
    parser.add_argument('-z', '--scan', action='store_true', help=' zero-I/O mode [used for scanning]')
    parser.add_argument('-w', '--timeout', action='store_const', const=0, help='timeout for connects and final net reads')
    parser.add_argument('-v', '--verbose', action='store_true', help='verbose [use twice to be more verbose]')

    # udp
    parser.add_argument('-u', '--udp', action='store_true', help='UDP mode')

    # execute
    parser.add_argument('-e', '--prog', action='store_true', help='inbound program to exec [dangerous!!]')

    parser.add_argument('-r', '--random', action='store_true', help='randomize local and remote ports')

    # hostname
    parser.add_argument(
        'addr', type=str,default="127.0.0.1",  help="computes cube for the given value", nargs='?')

    # port
    parser.add_argument('port', nargs=1, help='port to listen on')



    args = parser.parse_args()

    netpy = NetPy()


    if args.addr:
        netpy.set_ip(args.addr)

    if args.port:
        netpy.set_port(args.port[0])

    if args.timeout:
        netpy.set_timeout(args.timeout)

    if args.verbose:
        netpy.set_verbose(args.verbose)

    if args.prog:
        netpy.set_prog("C:\\Windows\\system32\\cmd.exe")

    if args.listen:
        netpy.listen()
    elif args.scan:
        netpy.scan()
    else:
        netpy.connect()

if __name__ == '__main__':
    main()
