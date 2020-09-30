from mininet.topo import Topo
from mininet.net import Mininet
from mininet.cli import CLI
from mininet.log import setLogLevel
from mininet.node import RemoteController

class MyTopo(Topo):
    def __init__(self):
        Topo.__init__(self)

        # Topology:
        #
        #        h2
        #        |
        #        s2
        #     1 /  \ 2
        #      / 1  \
        # h1-s1 ----- s3-h3
        #      \    /
        #     3 \  / 4
        #        s4
        #        |
        #        h4
        #
        # Run 'net' in the mininet CLI to verify this

        host1 = self.addHost('h1')
        host2 = self.addHost('h2')
        host3 = self.addHost('h3')
        host4 = self.addHost('h4')

        switch1 = self.addSwitch('s1')
        switch2 = self.addSwitch('s2')
        switch3 = self.addSwitch('s3')
        switch4 = self.addSwitch('s4')

        self.addLink(host1, switch1)
        self.addLink(host2, switch2)
        self.addLink(host3, switch3)
        self.addLink(host4, switch4)

        self.addLink(switch1, switch3, delay=1)
        self.addLink(switch1, switch2, delay=1)
        self.addLink(switch1, switch4, delay=3)
        self.addLink(switch2, switch3, delay=2)
        self.addLink(switch4, switch3, delay=4)

if __name__=="__main__":
    setLogLevel("info")
    topo = MyTopo()
    net = Mininet(topo=topo, controller=RemoteController)
    net.start()
    CLI(mininet=net)
    net.stop()
