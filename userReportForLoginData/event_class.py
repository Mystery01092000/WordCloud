import this


class Event:
    def __init__(self, event_date, event_type, machine_name, user):
        self.date = event_date
        self.type = event_type
        self.machine = machine_name
        self.user = user

    def __str__(self):
        return "On the date-time: {} the user {} from the machine named {}. User :{} ".format(self, self.date,self.type, self.machine, self.user)