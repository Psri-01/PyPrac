'''simulate a server that's taking connections from the outside and then a load balancer that ensures that there are enough servers to serve those connections.
To represent the servers that are taking care of the connections, we'll use a Server class. 
Each connection is represented by an id, that could, for example, be the IP address of the computer connecting to the server. 
For our simulation, each connection creates a random amount of load in the server, between 1 and 10.'''

# the Loadbalancing class starts with only one server available. 
# When a connection gets added, it will randomly select a server to serve that connection, and then pass on the connection to the server. 
# The LoadBalancing class also needs to keep track of the ongoing connections to be able to close them. 
import random

class Server:
    def __init__(self):
        """Creates a new server instance, with no active connections."""
        self.connections = {}

    def add_connection(self, connection_id):
        """Adds a new connection to this server."""
        connection_load = random.random()*10+1
        # Add the connection to the dictionary with the calculated load
        self.connections[connection_id] = connection_load
    def close_connection(self, connection_id):
        """Closes a connection on this server."""
        # Remove the connection from the dictionary
        if connection_id in self.connections:
            del self.connections[connection_id]
    def load(self):
        """Calculates the current load for all connections."""
        total = 0
        # Add up the load for each of the connections
        for load in self.connections.values():
            total += load
        return total

    def __str__(self):
        """Returns a string with the current load of the server"""
        return "{:.2f}%".format(self.load())

server = Server()
server.add_connection("192.168.1.1")
print(server.load())

server.close_connection("192.168.1.1")
print(server.load())

class LoadBalancing:
    def __init__(self):
        """Initialize the load balancing system with one server"""
        self.connections = {}
        self.servers = [Server()]

    def add_connection(self, connection_id):
        """Randomly selects a server and adds a connection to it."""
        server = random.choice(self.servers)
        # Add the connection to the dictionary with the selected server
        server.add_connection(connection_id)
        # Add the connection to the server
        self.ensure_availability()
        
    def close_connection(self, connection_id):
        """Closes the connection on the the server corresponding to connection_id."""
        # Find out the right server
        # Close the connection on the server
        # Remove the connection from the load balancer
        for server in self.servers:
            if connection_id in server.connections:
                server.close_connection(connection_id)
                break

    def avg_load(self):
        """Calculates the average load of all servers"""
        # Sum the load of each server and divide by the amount of servers
        total_load = 0
        total_server = 0
        for server in self.servers:
            total_load += server.load()
            total_server += 1
        return total_load/total_server
        return 0

    def ensure_availability(self):
        """If the average load is higher than 50, spin up a new server"""
        if self.avg_load()> 50:
            self.servers.append(Server())

    def __str__(self):
        """Returns a string with the load for each server."""
        loads = [str(server) for server in self.servers]
        return "[{}]".format(",".join(loads))
      
'''create a connection in the load balancer, assign it to a running server and then the load should be more than zero'''   
l = LoadBalancing()
l.add_connection("fdca:83d2::f20d")
print(l.avg_load())

# add a new server manually
l.servers.append(Server())
print(l.avg_load())

# closing the connection
l.close_connection("fdca:83d2::f20d")
print(l.avg_load())

#auto server addition
for connection in range(20):
    l.add_connection(connection)
print(l)

#verify that the average load of the load balancer is not more than 50%.
print(l.avg_load())
