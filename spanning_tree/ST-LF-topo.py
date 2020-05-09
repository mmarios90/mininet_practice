"""A simple Spanning Tree (Leaf-Spine) topology of 16 hosts and 20 switched
organised in three layers(1.access-edge layer, 2.aggregation layerand 3.the
core-spine layer)."""

#before running the ST topo, run the pox controller as follows:
#sudo pox/pox.py forwarding.l2_learning openflow.discovery --eat-early-packets openflow.spanning_tree --no-flood --hold-down

from mininet.cli import CLI
from mininet.net import Mininet
from mininet.node import RemoteController
from mininet.term import makeTerm
from mininet.link import Link, TCLink

if '__main__' == __name__:

	net = Mininet(controller=RemoteController)

	c0 = net.addController('c0', port=6633)

	#inserting hosts (16)	
	host1 = net.addHost( 'h1' )
	host2 = net.addHost('h2')
	host3 = net.addHost('h3')
	host4 = net.addHost('h4')
	host5 = net.addHost('h5')
	host6 = net.addHost('h6')
	host7 = net.addHost('h7')
	host8 = net.addHost('h8')
	host9 = net.addHost('h9')
	host10 = net.addHost('h10')
	host11 = net.addHost('h11')
	host12 = net.addHost('h12')
	host13 = net.addHost('h13')
	host14 = net.addHost('h14')
	host15 = net.addHost('h15')
	host16 = net.addHost('h16')

	#access/edge layer switches
	switch1 = net.addSwitch('s1')
	switch2 = net.addSwitch('s2')
	switch3 = net.addSwitch('s3')
	switch4 = net.addSwitch('s4')		
	switch5 = net.addSwitch('s5')
	switch6 = net.addSwitch('s6')
	switch7 = net.addSwitch('s7')
	switch8 = net.addSwitch('s8')

	#aggregation layer switches
	switch9 = net.addSwitch('s9')
	switch10 = net.addSwitch('s10')
	switch11 = net.addSwitch('s11')
	switch12 = net.addSwitch('s12')
	switch13 = net.addSwitch('s13')
	switch14 = net.addSwitch('s14')		
	switch15 = net.addSwitch('s15')
	switch16 = net.addSwitch('s16')

	#core switches
	switch17 = net.addSwitch('s17')
	switch18 = net.addSwitch('s18')
	switch19 = net.addSwitch('s19')
	switch20 = net.addSwitch('s20')


	#adding the appropriate links
	net.addLink(host1, switch1)
	net.addLink(host2, switch1)
		
	net.addLink(host3, switch2)
	net.addLink(host4, switch2)

	net.addLink(host5, switch3)
	net.addLink(host6, switch3)

	net.addLink(host7, switch4)
	net.addLink(host8, switch4)

	net.addLink(host9, switch5)
	net.addLink(host10, switch5)

	net.addLink(host11, switch6)
	net.addLink(host12, switch6)

	net.addLink(host13, switch7)
	net.addLink(host14, switch7)

	net.addLink(host15, switch8)
	net.addLink(host16, switch8)

		
		
	net.addLink(switch1, switch9)
	net.addLink(switch1, switch10)
	net.addLink(switch2, switch9)
	net.addLink(switch2, switch10)

	net.addLink(switch3, switch11)
	net.addLink(switch3, switch12)
	net.addLink(switch4, switch11)
	net.addLink(switch4, switch12)

	net.addLink(switch5, switch13)
	net.addLink(switch5, switch14)
	net.addLink(switch6, switch13)
	net.addLink(switch6, switch14)

	net.addLink(switch7, switch15)
	net.addLink(switch7, switch16)
	net.addLink(switch8, switch15)
	net.addLink(switch8, switch16)


		
	net.addLink(switch9, switch17)
	net.addLink(switch9, switch18)
	net.addLink(switch10, switch19)
	net.addLink(switch10, switch20)

	net.addLink(switch11, switch17)
	net.addLink(switch11, switch18)
	net.addLink(switch12, switch19)
	net.addLink(switch12, switch20)

	net.addLink(switch13, switch17)
	net.addLink(switch13, switch18)
	net.addLink(switch14, switch19)
	net.addLink(switch14, switch20)

	net.addLink(switch15, switch17)
	net.addLink(switch15, switch18)
	net.addLink(switch16, switch19)
	net.addLink(switch16, switch20)


	net.build()
        c0.start()
        
	switch1.start([c0])
        switch2.start([c0])
        switch3.start([c0])
	switch4.start([c0])
	switch5.start([c0])
	switch6.start([c0])
	switch7.start([c0])
	switch8.start([c0])
	switch9.start([c0])
	switch10.start([c0])	
	switch11.start([c0])
        switch12.start([c0])
	switch13.start([c0])
	switch14.start([c0])
	switch15.start([c0])
	switch16.start([c0])
	switch17.start([c0])
	switch18.start([c0])
	switch19.start([c0])
	switch20.start([c0])

        CLI(net)
        net.stop()

