CS 03B - Intermediate Software Design in Python
ASSIGNMENT 1
*** Important ***
• Assignment 1’s Repl.it link is at https://repl.it/@trinhviet/CS03BAssignment1. Once
you access the link, Repl.it will automatically fork a new environment for you to work
• Do not modify the main.py file in the provided Repl.it link. Your code could be placed
inside the run function of each other Python file
• Your submission must include your Repl.it shared link to your solution



Question #3 - Employee and Production Worker (40pts)
In q3.py, before the run method, write an Employee class that keeps data attributes for
the following pieces of information: Employee name, and Employee number
Next, write a class named ProductionWorker that is a subclass of the Employee class.
The ProductionWorker class should keep data attributes for the following information:
• Shift number (an integer, such as 1, 2, or 3)
• Hourly pay rate
The workday is divided into two shifts: day and night. The shift attribute will hold an
integer value representing the shift that the employee works. The day shift is shift 1 and
the night shift is shift 2. Write the appropriate accessor and mutator methods for each
class.
Once you have written the classes, in the run method of q3.py, create an object of the
ProductionWorker class and prompts the user to enter data for each of the object’s
data attributes. Store the data in the object, then use the object’s accessor methods to
retrieve it and display it on the screen
Page of2 3
