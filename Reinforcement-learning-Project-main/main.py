"""
This is where the actual working of the program will happen!
We'll be Querying stuff for testing whether your classes were defined correctly

Whenever something inappropriate happens (like a function returning false in people.py),
raise a Value Error.
"""
from people import * # import everything!

if __name__ == "__main__":  # Equivalent to int main() {} in C++.
    last_input = 99
    while last_input != 0:
        last_input = int(input("Please enter a query number:"))
        def string_2_arr(branchcodes):
            count_comma = branchcodes.count(',')
            branchcodes_list = [0] * (count_comma + 1)
            comma_idx = 0
            count = 0
            for i in range(len(branchcodes)):
                if branchcodes[i] == ',':
                    for j in range(comma_idx, i):
                        branchcodes_list[count] += int(branchcodes[j]) * (10 ** (i - j - 1))
                        count += 1
                        comma_idx = i + 1  # move past the comma

            # Handle the last number (after last comma)
            for j in range(comma_idx, len(branchcodes)):
                branchcodes_list[count] += int(branchcodes[j]) * (10 ** (len(branchcodes) - j - 1))
            return branchcodes_list

        if last_input == 1:
            name = input("Name:")
            ID = input("ID:")
            city = input("City:")
            branchcodes = input("Branch(es):")
            # How will you conver this to a list, given that
            # the user will always enter a comma separated list of branch codes?
            # eg>   2,5
            branchcodes_list=string_2_arr(branchcodes)
            salary = input("Salary:")
            age=input("age:")
            position=input("position:")
            # Create a new Engineer with given details.
            engineer = Engineer(name, age , ID, city,branchcodes, position , salary) # Change this

            engineer_roster.append(engineer) # Add him to the list! See people.py for definiton
            
        
        elif last_input == 2:
            # Gather input to create a Salesperson
            # Then add them to the roster
            name = input("Name:")
            ID = input("ID:")
            city = input("City:")
            branchcodes = input("Branch(es):")
            # How will you conver this to a list, given that
            # the user will always enter a comma separated list of branch codes?
            # eg>   2,5
            branchcodes_list=string_2_arr(branchcodes)
            salary = input("Salary:")
            age=input("age:")
            position=input("position:")
            salesperson = Salesman(name, age , ID, city,branchcodes, position , salary) # Change this
            sales_roster.append(salesperson)
            pass

        elif last_input == 3:
            ID = int(input("ID: "))
            # Print employee details for the given employee ID that is given. 
            
            found_employee = None
            for employee in engineer_roster + sales_roster:
                if employee.ID == int(ID):
                    found_employee = employee
                    break
            
            if not found_employee: print("No such employee")
            else:
                print(f"Name: {found_employee.name} and Age: {found_employee.age}")
                print(f"City of Work: {found_employee.city}")
                ## Write code here to list the branch names to
                ## which the employee reports as a comma separated list
                ## eg> Branches: Goregaon,Fort
                branch_names = []
                count_comma = branchcodes.count(',')
                branchcodes_list = [0] * (count_comma + 1)
                branchcodes_list=string_2_arr(branchcodes)
                ## ???? what comes here??
                print(f"Branches: {', '.join(branch_names)}")
                print(f"Salary: {found_employee.salary}")


        elif last_input == 4:
            #### NO IF ELSE ZONE ######################################################
            # Change branch to new branch or add a new branch depending on class
            # Inheritance should automatically do this. 
            # There should be no IF-ELSE or ternary operators in this zone
            ID = int(input("Enter Employee ID to migrate branch: "))
            new_code = int(input("Enter new branch code: "))

            found_employee = None
            for employee in engineer_roster + sales_roster:
                if employee.ID == ID:
                    found_employee = employee
                    break
            
            if not found_employee:
                raise ValueError("Employee not found")

            result = found_employee.migrate_branch(new_code)
            if result is False:
                raise ValueError("Branch migration failed")

            pass
            #### NO IF ELSE ZONE ENDS #################################################

        elif last_input == 5:
            ID = int(input("Enter Employee ID to promote: "))
            promoted_pos=input("Enter the position to which you want to promote:")
            found_employee = None
            for employee in engineer_roster + sales_roster:
                if employee.ID == ID:
                    found_employee = employee
                    break
            
            if not found_employee:
                raise ValueError("Employee not found")

            result = found_employee.promote(promoted_pos)
            if result is False:
                raise ValueError("Branch migration failed")
            # promote employee to next position

        elif last_input == 6:
            ID = int(input("Enter Employee ID to give increment: "))
            amt=int(input("Enter the amt:"))
            for employee in engineer_roster + sales_roster:
                if employee.ID == ID:
                    found_employee = employee
                    break
            
            if not found_employee:
                raise ValueError("Employee not found")

            found_employee.increment(amt)
            
            # Increment salary of employee.
        
        elif last_input == 7:
            ID = int(input("Enter Employee ID to find superior: "))
            found_employee = None
            for employee in sales_roster:
                if employee.ID == ID:
                    found_employee = employee
                    break

            if not found_employee:
                raise ValueError("Employee not found")

            super_id, super_name = found_employee.find_superior()
            print(f"superID: {super_id}, superName: {super_name}")
            # Print superior of the sales employee.
        
        elif last_input == 8:
            ID = int(input("Enter Employee ID to add superior: "))
            found_employee = None
            for employee in sales_roster:
                if employee.ID == ID:
                    found_employee = employee
                    break

            if not found_employee:
                raise ValueError("Employee not found")

            result = found_employee.add_superior(promoted_pos)
            if result is False:
                raise ValueError("Branch migration failed")


            # Add superior of a sales employee

        else:
            raise ValueError("No such query number defined")

            
            

            


            


        






