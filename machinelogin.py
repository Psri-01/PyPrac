'''Imagine that you're an IT specialist working in a medium-sized company, your manager wants to create a daily report that tracks the use of machines. 
Specifically, she wants to know which users are currently connected to which machines, it's your job to create the report. 
In your company, there's a system that collects every event that happens on the machines on the network. 
Among the many events collected it records each time a user logs in or out of a computer. 
With this information, we want to write a script that generates a report of which users are logged in to which machines at that time.
Before we jump into solving that problem, we need to know what information we'll use as input and what information we'll have as output.
We can work this out by looking at the rest of the system where our script will live. 
In our report scenario, the input is a list of events, each event is an instance of the event class. 
An event class contains the date when the event happened, the name of the machine where it happened, the user involved, and the event type. 
In this scenario, we care about the login and logout event type. 
But we need to know exact names of the attributes, otherwise, we won't be able to access them. 
The attributes are called date, user, machine, and type. The event types are strings and the ones we care about are login and logout. 
With that we should have enough information about the input of our script. Our script will receive a list of event objects and we'll access the events attributes. 
We'll then use that information to know if a user is currently logged into a machine or not.'''

"""We've identified our problem statement which is we need to process a list of event objects using 
their date, type, machine, and user attributes to generate a report that lists all users currently logged into the machines."""

def get_event_date(event):
  return event.date

def current_users(events):
  events.sort(key=get_event_date)
  machines = {}
  for event in events:
    if event.machine not in machines:
      machines[event.machine] = set()
    if event.type == "login":
      machines[event.machine].add(event.user)
    elif event.type == "logout" and event.user in machines[event.machine]:
      machines[event.machine].remove(event.user)
  return machines

def generate_report(machines):
  for machine, users in machines.items():
    if len(users) > 0: # prevents lists with zero users from being printed
      user_list = ", ".join(users)
      #The join() function of str gathers the user attributes (which is a string) into a single string, with commas separating the users.
      print("{}: {}".format(machine, user_list))

class Event:
  def __init__(self, event_date, event_type, machine_name, user):
    self.date = event_date
    self.type = event_type
    self.machine = machine_name
    self.user = user
    
events = [
    Event('2023-02-04 12:45:56', 'login', 'myworkstation.local', 'joe'),
    Event('2023-02-04 13:45:56', 'login', 'webserver.local', 'lane'),
    Event('2023-02-04 13:45:56', 'logout', 'webserver.local', 'lane'),
    Event('2023-02-04 14:45:56', 'login', 'myworkstation.local', 'kane'),
    Event('2023-02-04 10:45:56', 'login', 'mailserver.local', 'john'),
]

users = current_users(events)
print(users)

generate_report(users)
