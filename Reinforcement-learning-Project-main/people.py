"""
We'll try to understand classes in python. 
Check the resources on google classroom to ensure you have gone through everything expected.

"""
###### THESE LISTS HAVE ALREADY BEEN DEFINED FOR YOU ###############
engineer_roster = [] # A list of all instantiated engineer objects
sales_roster = [] # List of all instantiated sales objects
branchmap = {  # A dictionary of dictionaries -> Maps branchcodes to cities and branch names
    0:  { "city": "NYC", "name": "Hudson Yards"},
    1:  { "city": "NYC" , "name": "Silicon Alley"},
    2:  { "city": "Mumbai", "name": "BKC"},
    3:  { "city": "Tokyo", "name": "Shibuya"},
    4:  { "city": "Mumbai", "name": "Goregaon"},
    5:  { "city": "Mumbai", "name": "Fort"}
}
####################################################################

class Employee:
    name : str 
    age : int
    ID : int
    city : int
    branches : list[int] # This is a list of branches (as branch codes) to which the employee may report
    salary : int 

    def __init__(self, name, age, ID, city,\
                 branchcodes, salary = None):
        self.name = name
        self.age = age 
        self.ID = ID
        self.city = city
        self.branches = branchcodes
        if salary is not None: self.salary = salary
        else: self.salary = 10000 
    
    def change_city(self, new_city:str) -> bool:
        # Change the city 
        # Return true if city change, successful, return false if city same as old city
        if(self.city==new_city):
            return False
        else:
            self.city=new_city
            return True
        pass

    def migrate_branch(self, new_code:int) -> bool:
        # Should work only on those employees who have a single 
        # branch to report to. Fail for others.
        # Change old branch to new if it is in the same city, else return false.
        if(len(self.branches)==1 and branchmap[self.branches]["city"]==branchmap[new_code]["city"]):
            self.branches=new_code
            return True
        else:
            return False
        pass

    def increment(self, increment_amt: int) -> None:
        # Increment salary by amount specified.
        self.salary= self.salary+increment_amt
        pass





class Engineer(Employee):
    position : str # Position in organization Hierarchy

    def __init__(self, name, age, ID, city,\
                 branchcodes, position= "Junior", salary = None):
        # Call the parent's constructor
        super().__init__(name, age, ID, city, branchcodes, salary)
        
        # Check if position is one of  "Junior", "Senior", "Team Lead", or "Director" 
        # Only then set the position. 
        pos=["Junior", "Senior", "Team Lead",  "Director"]
        if position in pos:
            self.position=position

    
    def increment(self, amt:int) -> None:
        # While other functions are the same for and engineer,
        # and increment to an engineer's salary should add a 10% bonus on to "amt"
        bonus =0.1*amt
        self.salary=self.salary+bonus+amt
        pass
        
    def promote(self, position:str) -> bool:
        # Return false for a demotion or an invalid promotion
        # Promotion can only be to a higher position and
        # it should call the increment function with 30% of the present salary
        # as "amt". Thereafter return True.
        pos=["Junior", "Senior", "Team Lead",  "Director"]
        if position not in pos:
            return False
        idx1=0
        idx2=0
        for i in range(len(pos)):
            if(position==pos[i]):
                idx1=i
        for i in range(len(pos)):
            if(self.position==pos[i]):
                idx2=i
        if(idx1>=idx2):
            return False
        else:
            self.position=position
            self.increment(0.3*(self.salary))
            return True
        pass



class Salesman(Employee):
    """ 
    This class is to be entirely designed by you.

    Add increment (this time only a 5% bonus) and a promotion function
    This time the positions are: Rep -> Manager -> Head.

    Add an argument in init which tracks who is the superior
    that the employee reports to. This argument should be the ID of the superior
    It should be None for a "Head" and so, the argument should be optional in init.
    """
    
    # An extra member variable!
    superior : int # EMPLOYEE ID of the superior this guy reports to

    def __init__(self, name, age, ID, city,\
                 branchcodes,superior = None ,  position= "Rep",salary = None):
        super().__init__(name, age, ID, city, branchcodes, salary)
        pos=[ "Rep", "Manager" , "Head" ]
        if position in pos:
            self.position=position
        self.superior=superior

    def promote(self, position:str) -> bool:
        # Return false for a demotion or an invalid promotion
        # Promotion can only be to a higher position and
        # it should call the increment function with 30% of the present salary
        # as "amt". Thereafter return True.
        pos=["Rep", "Manager" , "Head"]
        if position not in pos:
            return False
        idx1=0
        idx2=0
        for i in range(len(pos)):
            if(position==pos[i]):
                idx1=i
        for i in range(len(pos)):
            if(self.position==pos[i]):
                idx2=i
        if(idx1<=idx2):
            return False
        else:
            self.position=position
            self.increment(0.3*(self.salary))
            return True
        pass

    def increment(self, amt:int) -> None:
        # While other functions are the same for and engineer,
        # and increment to an engineer's salary should add a 10% bonus on to "amt"
        bonus =0.05*amt
        self.salary=self.salary+bonus+amt
        pass

    def find_superior(self) -> tuple[int, str]:
        # Return the employee ID and name of the superior
        # Report a tuple of None, None if no superior.
        if self.position == "Head" or self.superior is None:
            return (None, None)
        if(self.position!="Head"):
            for emp in sales_roster:
                if emp.ID==self.superior:
                    return (self.superior,emp.name)
        else:
            return (None,None)
    
        pass

    def add_superior(self) -> bool:
        # Add superior of immediately higher rank.
        # If superior doesn't exist return false,
        pos=["Rep", "Manager" , "Head"]
        idx=0
        for i in range(len(pos)):
            if(self.position==pos[i]):
                idx=i
        if(idx != 2):
            for emp in sales_roster:
                if emp.position==pos[idx+1]:
                    self.superior=emp.ID
                    return True
        else:
            return False
        return False 
        pass


    def migrate_branch(self, new_code: int) -> bool:
        # This should simply add a branch to the list; even different cities are fine
        self.branches.append(new_code)
        return True

        pass

    





    
    