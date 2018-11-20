- Open bash terminal
- Change directory to lab06 if not already set
- Install mininet and enter sudo mn --custom mrip_topo.py --topo MRIP
- open a terminal in the mininet cli on the node you want to test (ex. "xterm h1")
- Enter "python mrip.py" to compile and run the program

Edit the config file to link different nodes and try out other topologies.  It is currently set to the ring topology

Since this project is not fully implemented, the results will not drastically vary between topologies as they should.

Here is an example of my programs output using the ring topology:
source = 10.0.0.1
dest   = 10.0.0.2
UDP target IP: 10.0.0.2
UDP target port: 5353
message: MRIP REQUEST 10.0.0.1
Wait time: 58 secs

source = 10.0.0.2
dest   = 10.0.0.3
UDP target IP: 10.0.0.3
UDP target port: 5353
message: MRIP REQUEST 10.0.0.2
Wait time: 52 secs

source = 10.0.0.3
dest   = 10.0.0.4
UDP target IP: 10.0.0.4
UDP target port: 5353
message: MRIP REQUEST 10.0.0.3
Wait time: 49 secs

source = 10.0.0.4
dest   = 10.0.0.5
UDP target IP: 10.0.0.5
UDP target port: 5353
message: MRIP REQUEST 10.0.0.4
Wait time: 42 secs

source = 10.0.0.5
dest   = 10.0.0.6
UDP target IP: 10.0.0.6
UDP target port: 5353
message: MRIP REQUEST 10.0.0.5
Wait time: 37 secs

source = 10.0.0.6
dest   = 10.0.0.7
UDP target IP: 10.0.0.7
UDP target port: 5353
message: MRIP REQUEST 10.0.0.6
Wait time: 35 secs

source = 10.0.0.8
dest   = 10.0.0.9
UDP target IP: 10.0.0.9
UDP target port: 5353
message: MRIP REQUEST 10.0.0.8
Wait time: 48 secs

source = 10.0.0.9
dest   = 10.0.0.1
UDP target IP: 10.0.0.1
UDP target port: 5353
message: MRIP REQUEST 10.0.0.9
Wait time: 39 secs 
