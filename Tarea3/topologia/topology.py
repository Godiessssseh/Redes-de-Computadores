#Ejecucion: sudo mn --custom topologia1.py --topo MyTopo --controller remote --switch ovsk --mac
from mininet.topo import Topo
#from mininet.node import RemoteController
#from mininet.net import Mininet


class Red1(Topo):
    "Topologia numero 1"

    def __init__(self):
        "Creacion de topologia personalizada"
        Topo.__init__(self)
        #net = Mininet(controller = RemoteController)
        #net.addController('c0')

        #Hosts y switches
        h1 = self.addHost( 'h1', mac = '00:00:00:00:00:01')
        h2 = self.addHost( 'h2', mac = '00:00:00:00:00:02')
        h3 = self.addHost( 'h3', mac = '00:00:00:00:00:03')
        h4 = self.addHost( 'h4', mac = '00:00:00:00:00:04')
        h5 = self.addHost( 'h5', mac = '00:00:00:00:00:05')
        h6 = self.addHost( 'h6', mac = '00:00:00:00:00:06')
        h7 = self.addHost( 'h7', mac = '00:00:00:00:00:07')
        h8 = self.addHost( 'h8', mac = '00:00:00:00:00:08')
        h9 = self.addHost( 'h9', mac = '00:00:00:00:00:09')
        h10 = self.addHost( 'h10', mac = '00:00:00:00:00:0A')

        s1 = self.addSwitch( 's1', dpid = '1')
        s2 = self.addSwitch( 's2', dpid = '2')
        s3 = self.addSwitch( 's3', dpid = '3')
        s4 = self.addSwitch( 's4', dpid = '4')
        s5 = self.addSwitch( 's5', dpid = '5')

        #Anadir links 
        #h1 con h2 y s1
        self.addLink( h1, s1, 1, 11)
        self.addLink( h2, s1, 2, 12)
        self.addLink( s1, s2, 22, 23)
        #h3, h4 y s2
        self.addLink( h3, s2, 3, 13)
        self.addLink( h4, s2, 4, 14)
        self.addLink( s2, s3, 24, 25)
        #h5, h6 y s3
        self.addLink( h5, s3, 5, 15)
        self.addLink( h6, s3, 6, 16)
        self.addLink( s3, s4, 26, 30)
        #h7,h8 y s4
        self.addLink( h7, s4, 7, 17)
        self.addLink( h8, s4, 8, 18)
        self.addLink( s4, s1, 27, 21)
        #h9, h10 y s5
        self.addLink( h9, s5, 9, 19)
        self.addLink( h10, s5, 10, 20)
        self.addLink( s5, s4, 29, 28)


class Red2(Topo):
    "Topologia numero 2"

    def __init__(self):
        "Creacion de topologia personalizada"
        Topo.__init__(self)
        #net = Mininet(controller = RemoteController)
        #net.addController('c0')

        #Hosts y switches
        h1 = self.addHost( 'h1', mac = '00:00:00:00:00:01')
        h2 = self.addHost( 'h2', mac = '00:00:00:00:00:02')
        h3 = self.addHost( 'h3', mac = '00:00:00:00:00:03')
        h4 = self.addHost( 'h4', mac = '00:00:00:00:00:04')
        h5 = self.addHost( 'h5', mac = '00:00:00:00:00:05')
        h6 = self.addHost( 'h6', mac = '00:00:00:00:00:06')
        h7 = self.addHost( 'h7', mac = '00:00:00:00:00:07')
        h8 = self.addHost( 'h8', mac = '00:00:00:00:00:08')
        
        s1 = self.addSwitch( 's1', dpid = '1')
        s2 = self.addSwitch( 's2', dpid = '2')
        s3 = self.addSwitch( 's3', dpid = '3')
        s4 = self.addSwitch( 's4', dpid = '4')
        s5 = self.addSwitch( 's5', dpid = '5')

        #Anadir links 
        #h1 con h2 y s1
        self.addLink( h1, s1, 1, 9)
        self.addLink( h2, s1, 2, 10)
        self.addLink( s1, s2, 17, 18)
        #h3, h4 y s2
        self.addLink( h3, s2, 3, 11)
        self.addLink( h4, s2, 4, 12)
        self.addLink( s2, s3, 19, 20)
        #h5, h6 y s3
        self.addLink( h5, s3, 5, 13)
        self.addLink( h6, s3, 6, 14)
        self.addLink( s3, s4, 21, 22)
        #s4, s1 y s5
        self.addLink( s4, s5, 23, 24)
        self.addLink( s4, s1, 27, 28)
        #h7 y h8, s5
        self.addLink( h7, s5, 7, 15)    #HTTPS
        self.addLink( h8, s5, 8, 16)    #HTTPS
        self.addLink( s5, s1, 25, 26 )

        
class MyTopo(Topo):

    "Topologia testing"

    def __init__(self):
        "Creacion de topologia personalizada"
        Topo.__init__(self)
        #net = Mininet(controller = RemoteController)
        #net.addController('c0')
        #Hosts y switches
        
        h1 = self.addHost( 'h1', mac = '00:00:00:00:00:01')
        h2 = self.addHost( 'h2', mac = '00:00:00:00:00:02')
        h3 = self.addHost( 'h3', mac = '00:00:00:00:00:03')
        h4 = self.addHost( 'h4', mac = '00:00:00:00:00:04')
        h5 = self.addHost( 'h5', mac = '00:00:00:00:00:05')
        h6 = self.addHost( 'h6', mac = '00:00:00:00:00:06')
        h7 = self.addHost( 'h7', mac = '00:00:00:00:00:07')
        h8 = self.addHost( 'h8', mac = '00:00:00:00:00:08')
        s1 = self.addSwitch( 's1', dpid = '1')
        s2 = self.addSwitch( 's2', dpid = '2')
        s3 = self.addSwitch( 's3', dpid = '3')
        s4 = self.addSwitch( 's4', dpid = '4')

        #Anadir links 
        self.addLink( h1, s1, 1, 2)
        self.addLink( h2, s1, 4, 3)
        self.addLink( s1, s2, 5, 6)
        self.addLink( h3, s2, 8, 7)
        self.addLink( h4, s2, 10, 9)
        self.addLink( s2, s3, 11, 12)
        self.addLink( h5, s3, 14, 13)
        self.addLink( h6, s3, 16, 15)
        self.addLink( s3, s4, 17, 18)
        self.addLink( h7, s4, 22, 21)
        self.addLink( h8, s4, 20, 19)
        self.addLink( s4, s1, 23, 24)

topos = {'MyTopo': (lambda: MyTopo()), "Red1":(lambda: Red1() ), "Red2":(lambda: Red2() )}
