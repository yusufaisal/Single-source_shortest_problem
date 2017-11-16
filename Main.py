from copy import deepcopy

class Route:
    def __init__(self,route,weight):
        self.weight = weight
        self.route = route
class childNode:
    def __init__(self,node=None,weight=None):
        self.node = node
        self.weight = weight
        self.next = None
class node:
    def __init__(self,label=None):
        self.label = label
        self.next = None
        self.connected = None
class LinkedList:
    def __init__(self):
        self.head = node()

    def append(self,data):
        new_node = node(data)
        cur = self.head
        while cur.next!=None:
            cur = cur.next
        cur.next = new_node

    def find(self,label):
        cur = self.head
        while cur.next != None:
            cur = cur.next
            if cur.label == label:
                return cur

    def display(self):
        cur = self.head
        while cur.next !=None:
            cur = cur.next
            print "-->",cur.label
            cur.connected.display()
class ConnectedList:
    def __init__(self):
        self.head = childNode()

    def append(self,node,weight):
        new_node = childNode(node,weight)
        cur = self.head
        while cur.next!=None:
            cur = cur.next
        cur.next = new_node

    def find(self,label):
        cur = self.head
        while cur.next != None:
            cur = cur.next
            if cur.node.label == label:
                return cur

    def display(self):
        cur = self.head
        while cur.next !=None:
            cur = cur.next
            print "------>",cur.node.label,cur.weight

def createGrafA(linkedList):
    linkedList.append("S")  # Start
    linkedList.append("A")
    linkedList.append("B")
    linkedList.append("C")
    linkedList.append("D")
    linkedList.append("E")
    linkedList.append("F")
    linkedList.append("G")  # Finish
    linkedList.append("X")

    S = linkedList.head.next
    S.connected = ConnectedList()

    get = linkedList.find("A")
    S.connected.append(get, 10)
    get = linkedList.find("B")
    S.connected.append(get, 13)

    A = S.next
    A.connected = ConnectedList()
    get = linkedList.find("S")
    A.connected.append(get, 10)
    get = linkedList.find("D")
    A.connected.append(get, 4)
    get = linkedList.find("F")
    A.connected.append(get, 14)
    get = linkedList.find("X")
    A.connected.append(get, 15)

    B = A.next
    B.connected = ConnectedList()
    get = linkedList.find("S")
    B.connected.append(get, 13)
    get = linkedList.find("C")
    B.connected.append(get, 12)

    C = B.next
    C.connected = ConnectedList()
    get = linkedList.find("B")
    C.connected.append(get, 12)
    get = linkedList.find("E")
    C.connected.append(get, 5)
    get = linkedList.find("D")
    C.connected.append(get, 4)

    D = C.next
    D.connected = ConnectedList()
    get = linkedList.find("A")
    D.connected.append(get, 4)
    get = linkedList.find("G")
    D.connected.append(get, 17)
    get = linkedList.find("C")
    D.connected.append(get, 4)

    E = D.next
    E.connected = ConnectedList()
    get = linkedList.find("C")
    E.connected.append(get, 5)
    get = linkedList.find("G")
    E.connected.append(get, 6)

    F = E.next
    F.connected = ConnectedList()
    get = linkedList.find("A")
    F.connected.append(get, 14)
    get = linkedList.find("G")
    F.connected.append(get, 4)

    G = F.next
    G.connected = ConnectedList()
    get = linkedList.find("D")
    G.connected.append(get, 17)
    get = linkedList.find("E")
    G.connected.append(get, 6)
    get = linkedList.find("F")
    G.connected.append(get, 4)

    X = G.next
    X.connected = ConnectedList()
def createGrafB(linkedList):
    linkedList.append("S")  # Start
    linkedList.append("A")
    linkedList.append("B")
    linkedList.append("C")
    linkedList.append("D")
    linkedList.append("E")
    linkedList.append("F")
    linkedList.append("G")  # Finish
    linkedList.append("H")
    linkedList.append("I")
    linkedList.append("J")
    linkedList.append("K")
    linkedList.append("L")

    S = linkedList.head.next

    S.connected = ConnectedList()
    get = linkedList.find("A")
    S.connected.append(get, 99)
    get = linkedList.find("B")
    S.connected.append(get, 100)
    get = linkedList.find("C")
    S.connected.append(get, 82)

    A=S.next
    A.connected = ConnectedList()
    get = linkedList.find("S")
    A.connected.append(get, 99)
    get = linkedList.find("F")
    A.connected.append(get, 120)
    get = linkedList.find("D")
    A.connected.append(get, 70)

    B = A.next
    B.connected = ConnectedList()
    get = linkedList.find("S")
    B.connected.append(get, 100)
    get = linkedList.find("D")
    B.connected.append(get, 80)
    get = linkedList.find("E")
    B.connected.append(get, 100)

    C = B.next
    C.connected = ConnectedList()
    get = linkedList.find("S")
    C.connected.append(get, 82)
    get = linkedList.find("F")
    C.connected.append(get, 101)
    get = linkedList.find("H")
    C.connected.append(get, 29)

    D = C.next
    D.connected = ConnectedList()
    get = linkedList.find("A")
    D.connected.append(get, 70)
    get = linkedList.find("B")
    D.connected.append(get, 80)

    E = D.next
    E.connected = ConnectedList()
    get = linkedList.find("B")
    E.connected.append(get, 100)
    get = linkedList.find("K")
    E.connected.append(get, 90)
    get = linkedList.find("J")
    E.connected.append(get, 49)
    get = linkedList.find("G")
    E.connected.append(get, 129)

    F = E.next
    F.connected = ConnectedList()
    get = linkedList.find("A")
    F.connected.append(get, 120)
    get = linkedList.find("C")
    F.connected.append(get, 101)
    get = linkedList.find("I")
    F.connected.append(get, 20)
    get = linkedList.find("K")
    F.connected.append(get, 91)

    G = F.next
    G.connected = ConnectedList()
    get = linkedList.find("E")
    G.connected.append(get, 129)
    get = linkedList.find("J")
    G.connected.append(get, 69)

    H = G.next
    H.connected = ConnectedList()
    get = linkedList.find("L")
    H.connected.append(get, 130)
    get = linkedList.find("C")
    H.connected.append(get, 29)
    get = linkedList.find("I")
    H.connected.append(get, 73)

    I = H.next
    I.connected = ConnectedList()
    get = linkedList.find("F")
    I.connected.append(get, 20)
    get = linkedList.find("H")
    I.connected.append(get, 73)
    get = linkedList.find("J")
    I.connected.append(get, 50)
    get = linkedList.find("K")
    I.connected.append(get, 100)

    J = I.next
    J.connected = ConnectedList()
    get = linkedList.find("E")
    J.connected.append(get, 49)
    get = linkedList.find("G")
    J.connected.append(get, 69)
    get = linkedList.find("I")
    J.connected.append(get, 50)
    get = linkedList.find("K")
    J.connected.append(get, 70)

    K = J.next
    K.connected = ConnectedList()
    get = linkedList.find("E")
    K.connected.append(get, 90)
    get = linkedList.find("F")
    K.connected.append(get, 50)
    get = linkedList.find("I")
    K.connected.append(get, 100)
    get = linkedList.find("J")
    K.connected.append(get, 70)
    get = linkedList.find("L")
    K.connected.append(get, 99)

    L = K.next
    L.connected = ConnectedList()
    get = linkedList.find("K")
    L.connected.append(get, 99)
    get = linkedList.find("H")
    L.connected.append(get, 130)

def find(arr, item):
    for i in range(len(arr)):
        if arr[i]==item:
            return True
    return False
def walkingWalking(node,goal,verboden,w,route):
    cur  = node.connected.head

    #Pass by Value using Deepcopy
    new_route = deepcopy(route)
    new_verboden = deepcopy(verboden)
    new_route.append(node.label)

    while cur.next!=None and node.label != goal:
        cur = cur.next
        if not find(new_verboden, cur.node.label):
            new_verboden.append(node.label)
            new_w = deepcopy(w)+cur.weight

            walkingWalking(cur.node,goal,new_verboden,new_w,new_route)

    if node.label==goal:
        RouteSet.append(Route(new_route,w))
        return 0
    else:
        return 1

if __name__=="__main__":
    #Initialize
    L = LinkedList()
    verboden = []
    route = []
    RouteSet = []

    #Create Graf
    createGrafB(L)
    L.display()

    #Find the Shortest Route
    V = L.find("S") #Set Starting Node
    G = "G"         #Set Goal Node
    walkingWalking(V,G,verboden,0,route)

    #Show All Available Route
    for i in range(len(RouteSet)):
        print RouteSet[i].route,RouteSet[i].weight
    print

    #Show the Optimum Route
    RouteSet.sort(key=lambda Route: Route.weight)
    print "Optimum Route Solution: "
    print RouteSet[0].route, RouteSet[0].weight