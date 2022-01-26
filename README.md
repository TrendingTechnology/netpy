# netpy
more than implementation of netcat  🐱‍👤🔥


## Featutres 💻
- [ ] core written in `C`
- [ ] TCP & UDP
- [ ] Backdoor (Reverse Shell)
- [ ] Honeypot
- [ ] File transfer
- [ ] Port forwarding
- [ ] Proxy
- [ ] Web Server
- [ ] Port scanning
- [ ] Authentication
- [ ] Middelware
- [ ] Encription Connection
- [ ] `allow` & `deny` specific remote IP-address.
- [ ] Multi-Client


## Available Commands:
- listen mode, for inbound connects
```bash
$ netpy -l 567
```
- Connecting to that port from another machine:
```bash
$ netpy -1.2.3.4 5676
```
- Setting up a remote shell listener:
```bash
$ netpy -v -e '/bin/bash' -l -p 1234 -t
```
