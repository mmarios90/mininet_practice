""" A topology I made for experimental purposes.
    This code creates a topology, consisting 12 hosts, 6 switches and 2 routers.
    Each router, routes three subnets and also connects them to the other's subnets via
    a link (subnet) between them.
    Marios Michalopoulos, May 2020
"""
from mininet.topo import Topo
from mininet.net import Mininet
from mininet.node import Node
from mininet.log import setLogLevel, info
from mininet.cli import CLI
from mininet.link import Link, TCLink


class MyRouter( Node ): # from the Mininet library, linuxrouter.py
    "A Node with IP forwarding enabled."

    def config( self, **params ):
        super(MyRouter, self).config( **params )
        # Enable forwarding on the router
        self.cmd( 'sysctl net.ipv4.ip_forward=1' )

    def terminate( self ):
        self.cmd( 'sysctl net.ipv4.ip_forward=0' )
        super(MyRouter, self ).terminate()


class NetworkTopo( Topo ):

    def build( self, **_opts ):
	
	# create two router objects with their default IPs
        r0 = self.addNode( 'r0', cls=MyRouter, ip= '10.0.1.1/16' )
	r1 = self.addNode( 'r1', cls=MyRouter, ip = '10.2.1.1/16')
	
	# create six switches, three for each router
	s1, s2, s3 = [ self.addSwitch( s ) for s in ( 's1', 's2', 's3' ) ]
	s4, s5, s6 = [ self.addSwitch( s ) for s in ( 's4', 's5', 's6' ) ]
	
	# connect each switch to its router
	# each switch acquires its respective subnet IPs
	self.addLink( s1, r0, intfName2='r0-eth1',params2={ 'ip' : '10.0.1.1/24' } )
	self.addLink( s2, r0, intfName2='r0-eth2',params2={ 'ip' : '10.0.2.1/24' } )
	self.addLink( s3, r0, intfName2='r0-eth3',params2={ 'ip' : '10.0.3.1/24' } )
	
	self.addLink( s4, r1, intfName2='r1-eth1',params2={ 'ip' : '10.2.1.1/24' } )
	self.addLink( s5, r1, intfName2='r1-eth2',params2={ 'ip' : '10.2.2.1/24' } )
	self.addLink( s6, r1, intfName2='r1-eth3',params2={ 'ip' : '10.2.3.1/24' } )


	# create the inbetween link for the routers 
	self.addLink(r0, r1, intfName1='r0-eth4', intfName2='r1-eth4', params1={'ip': '10.100.0.2/24'}, params2={'ip': '10.100.0.1/24'})
	
	
	# create hosts with their IPs
	h1 = self.addHost( 'h1', ip='10.0.1.100/24',defaultRoute='via 10.0.1.1' )
	h2 = self.addHost( 'h2', ip='10.0.1.101/24',defaultRoute='via 10.0.1.1' )

	h3 = self.addHost( 'h3', ip='10.0.2.100/24',defaultRoute='via 10.0.2.1' )
        h4 = self.addHost( 'h4', ip='10.0.2.101/24',defaultRoute='via 10.0.2.1' )

	h5 = self.addHost( 'h5', ip='10.0.3.100/24',defaultRoute='via 10.0.3.1' )
	h6 = self.addHost( 'h6', ip='10.0.3.101/24',defaultRoute='via 10.0.3.1' )

        h7 = self.addHost( 'h7', ip='10.2.1.100/24',defaultRoute='via 10.2.1.1' )
        h8 = self.addHost( 'h8', ip='10.2.1.101/24',defaultRoute='via 10.2.1.1' )

        h9 = self.addHost( 'h9', ip='10.2.2.100/24',defaultRoute='via 10.2.2.1' )
        h10 = self.addHost( 'h10', ip='10.2.2.101/24',defaultRoute='via 10.2.2.1' )

        h11 = self.addHost( 'h11', ip='10.2.3.100/24',defaultRoute='via 10.2.3.1' )
        h12 = self.addHost( 'h12', ip='10.2.3.101/24',defaultRoute='via 10.2.3.1' )


        # connect the hosts to their switches
        for h, s in [ (h1, s1), (h2, s1), (h3, s2), (h4, s2), (h5, s3), (h6, s3) ]:
		self.addLink( h, s )


        for h, s in [ (h7, s4), (h8, s4), (h9, s5), (h10, s5), (h11, s6), (h12, s6) ]:
                self.addLink( h, s )

	

def run():

	"Testing router"
	topo = NetworkTopo()
	net = Mininet( topo=topo )
	net.start()
        
	# call the router objects
	r0 = net['r0']
        r1 = net['r1']

	# implement route for connecting the routers 
	r0.cmd("ip route add 10.2.0.0/16 via 10.100.0.1 dev r0-eth4")
	r1.cmd("ip route add 10.0.0.0/16 via 10.100.0.2 dev r1-eth4")

	# set gateways
	r0.cmd("route add -net 10.2.0.0/16 gw 10.100.0.1")
	r1.cmd("route add -net 10.0.0.0/16 gw 10.100.0.2")

	# print routing table info about the routers	
	info( '*** Routing Table on Router:\n' )
	info( net[ 'r0' ].cmd( 'route' ) )

	info('\nR2:\n')
	info( net[ 'r1' ].cmd( 'route' ) )
	
	CLI( net )     

	net.stop()
        
if __name__ == '__main__':
	setLogLevel( 'info' )
	run()

