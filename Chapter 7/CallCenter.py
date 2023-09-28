# # Call Center: Imagine you have a call center with three levels of employees: respondent, manager,
# and director. An incoming telephone call must be first allocated to a respondent who is free. If the
# respondent can't handle the call, he or she must escalate the call to a manager. If the manager is not
# free or not able to handle it, then the call should be escalated to a director. Design the classes and
# data structures for this problem. Implement a method dispatchCall () which assigns a call to
# the first available employee.

# Objects: Employee Base Class, Respondent, Manager, Director.
#          CallController Class, to handle call behaviour = 'Main' Class.

from enum import Enum

class Rank(Enum):
    Respondent, Manager, Director = 0, 1, 2


class Call:
    def __init__(self, caller, rank = Rank.Respondent):
        self.min_rank = rank
        self.caller = caller
        self.employee = None

    def set_handler(self, emp: Employee):
        self.employee = emp
    
    def get_rank(self):
        return self.min_rank
    
    def set_rank(self, rank):
        self.min_rank = rank
    
    def end_call(self):
        return 1


class Employee:
    def __init__(self, rank: Rank):
        # self.name = name
        # self.address = address
        # self.age = age
        self.rank = rank

        self.on_call = False

    def get_rank(self):
        return self.rank

    def is_on_call(self):
        return self.on_call

    def receive_call(self, call: Call):
        pass


class Respondent(Employee):
    def __init__(self, rank):
        super().__init__(rank)
        self.rank = Rank.Respondent

class Manager(Employee):
    def __init__(self, rank):
        super().__init__(rank)
        self.rank = Rank.Manager

class Director(Employee):
    def __init__(self, rank):
        super().__init__(rank)
        self.rank = Rank.Director


class Call_Handler:
    def __init__(self):
        self.employees = {Rank.Respondent: [], Rank.Manager: [], Rank.Director: []}
        self.num_respondents = 10
        self.num_managers = 5
        self.num_directors = 3

        self.call_queue = []

    # Find appropriate handler for the call request, if all handlers are busy, returns None 
    def getHandlerForCall(self,call:Call):
        pass

    def dispatch_caller(self,caller):
        self.call = Call(caller)
        # self.call.caller = call.caller
        dispatch_call(self.call)

    def dispatch_call(self, call:Call):
        emp: Employee = self.getHandlerForCall(call)
        if emp:
            emp.receive_call(call)
            call.set_handler(emp)
        else:
            self.call_queue.append(call)


