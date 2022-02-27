#QUESTION 1
#This program uses matplotlib to plot a pie chart showing how money was spent in a month
#it reads a text file to determine the expenses

import matplotlib.pyplot as plt

#for use when changing colours of pie chart
#np.linspace returns evenly spaced numbers over interval number (of expenses)
import numpy as np

def main():

    #Set a variable to control if the user would like to loop the program
    again = 'y'

    while again == 'y':

        #Get the file to be read
        infile = get_file_path()

        #Read the contents of the file into a list - one line per list element
        expenses = infile.readlines()

        #Pass the expenses list into the function to separate into categories & values lists
        expense_categories, expense_values, correct_format, correct_values = get_categories_and_values(expenses)

        # Close file
        infile.close()

        #Confirm that the number of categories and values is the same in order to prevent errors in the pie chart
        if (correct_format == True) and (correct_values == True):
        
            #call the function to create the pie chart
            create_pie_chart(expense_categories, expense_values)

        else: #There was an error in reading the text file
            print('Please ensure all lines contain only one Expense Category title and value')


        #Ask the usesr if they would like to run the program again
        print('Would you like to start again? y/n')
        again = y_n_check(input())

    print('Thanks for using this program to view your expenses!')

#------------------------------------------------------------------------------------------------------------------------
#FUNCTIONS

#This function asks the user which file to use and returns the file path using the infile variable
def get_file_path():

    #Set a variable to determine if the user wants to customize the program
    default = 'y'

    #Set a variable to allow the user to select a menu item
    menu_selection = 0

    #Set a default value for income, to be set if option 3 selected
    income = 0

    #Ask the user if they would like to customize the program
    print('Would you like to run the default program? y/n')
    answer = input()

    #check the validity of the user input (must be y/n)
    default = y_n_check(answer)

    if default == 'y': #the user wants to run the default program
        #Relative path of test file
        #assuming zipped folder is downloaded and paths are not altered
        file_path = '..\Q1_Test_Files\Expenses.txt'

        # Open the file for reading
        infile = open(file_path, 'r')

    else: #the user does not want to run the default program
        #print a list of options
        print('~~~~~MENU~~~~~')
        print('1. Choose A Test Program')
        print('2. Select a Different Text File')

        #get selection from user
        menu_selection = input()

        #check the user entered a valid input
        #Pass an argument of the input of the user and the max value allowed
        menu_selection = number_validity_check(menu_selection, 2)

        is_valid = False

        if menu_selection == '1':
            print()
            print()
            print('Which program would you like to run?')
            print('1. Default Expenses')
            print('2. Expenses More Categories')
            print('3. Expenses Zero Values')
            print('4. Expenses Negative Values')
            print('5. Expenses Blank Lines')
            print('6. Expenses With Multiple on One Line')
            print('7. Expenses Format Error')
            print('8. Go Back')

            #get selection from user
            selection = input()

            #check the user entered a valid input
            #Pass an argument of the input of the user and the max value allowed
            selection = number_validity_check(selection, 8)

            #assign the appropriate file name to file_path based on what the user has selected
            if selection == '2':
                file_path = '..\Q1_Test_Files\Expenses_More_Categories.txt'

            elif selection == '3':
                file_path = '..\Q1_Test_Files\Expenses_Zero_Values.txt'

            elif selection == '4':
                file_path = '..\Q1_Test_Files\Expenses_Negative_Values.txt'

            elif selection == '5':
                file_path = '..\Q1_Test_Files\Expenses_Blank_Lines.txt'

            elif selection == '6':
                file_path = '..\Q1_Test_Files\Expenses_2on1_Line.txt'

            elif selection == '7':
                file_path = '..\Q1_Test_Files\Expenses_Format_Error.txt'

            elif selection == '8':
                #reset to default values
                file_path = '..\Q1_Test_Files\Expenses.txt'
                #call the function again from the start
                infile = get_file_path()

            else: #default (chose number 1)
                file_path = '..\Q1_Test_Files\Expenses.txt'


            # Open the file for reading
            infile = open(file_path, 'r')

        elif menu_selection == '2':
            print('Please enter the absolute path (including file name) of the file you wish to read (b to go back): ')
            answer = input()

            #Loop to check that the file path entered is correct, 
            #or trigger b for back 
            while is_valid == False and answer.lower() != 'b':
                try:
                    infile = open(answer, 'r')
                    is_valid = True
                except:
                    print('That is not a valid file path')
                    print('Please enter the absolute path (including file name) of the file you wish to read (b to go back): ')
                    answer = input()

            #Call the function to display the first steps as the user selected to go back
            if answer.lower() == 'b':
               infile = get_file_path()
    
    
    return infile


#------------------------------------------------------------------------------------------------------------------------


#This function takes an agrument of a list (expenses) containing the values of each line that was read from the file
#It seperates these values into categories (strings) and values (floats)
def get_categories_and_values(expenses):
    # Create an empty list for what will contain the labels
    expense_categories = []

    # Create an empty list for what will contain the value of the expense
    expense_values = []

    #Initialize the sorted_index variable
    #Set again in the inner for loop to ensure expense & category is kept together
    sorted_index = 0

    #Create a variable to count the line number - for the purpose of error check message
    line_number = 0

    #Initialize variables for error checking
    correct_format = False
    correct_format = False

    # Convert the expenses list with titles & values into labels & values lists
    for expense in expenses:

        #increase the line number by 1
        line_number += 1

        # Create a variable to hold the string containing the expense title
        category = ""

        #check if the line is empty or contains only spaces
        if expense != '\n' and not expense.isspace():
        
            #For loop to seperate each word ( split at white space)
            for word in expense.split():

                #Check to see if the word is a float (decimal number)
                try:
                    is_float = float(word)

                    #add the value to the expense_values list
                    expense_values.append(float(word))
                    #sort the list 
                    #Used to enhance the readability of the pie chart later
                    expense_values.sort()

                    #get the new (sorted) index of the added value 
                    #to ensure the category title is added in the same place of its list
                    sorted_index = expense_values.index(float(word))

                #If the word is not a float (ie is a title, store word in the variable category
                #use the variable instead of appending right away, incase there is more than one word in the title
                except ValueError:
                    category = category + word + ' '

            #store the full title of the expense into the expense_categories list
            #Use the sorted_index as the index to ensure matching of titles/values
            expense_categories.insert(sorted_index, category)

        #confirm that the length of each list (values and categories) is the same
        #if not the same, display a message to the user asking them to fix the txt document.
        if len(expense_values) != len(expense_categories):
            print('The text file is not formatted correctly')
            print('Please check line ', line_number, ' and then try again')
            correct_format = False
            break
        else:
            correct_format = True


    #confirm that all expenses entered are greater than 0 to preven errors when creating the pie chart
    for expense in expense_values:
        if expense >= 0:
            correct_values= True
        else:
            print('The expenses must be greater than 0.')
            print('Please check the txt file and try again.')
            correct_values = False
            break

    return expense_categories, expense_values, correct_format, correct_values


#------------------------------------------------------------------------------------------------------------------------


#This function creates and displayes a pie chart
#it takes two arguments - the expense_categories & expense_values
def create_pie_chart(expense_categories, expense_values):

    #Use better colours for the map - easier to read
    #Referenced https://stackoverflow.com/questions/16006572/plotting-different-colors-in-matplotlib
    #The number of colours needed (equal to the number of items in the expense_categories list
    number_of_colours = len(expense_categories)
    #use colours from an existing colour map
    cmap = plt.get_cmap('summer')
    #Set a list of colours to use
    #np.linspace returns evenly spaced numbers over interval number (of expenses)
    #https://numpy.org/doc/stable/reference/generated/numpy.linspace.html
    colors = [cmap(i) for i in np.linspace(0, 1, number_of_colours)]

    
    #Check if any of the wedges will be less than 5%
    #if so display a ledgend for readability
    for expense in expense_values:
        if expense < (sum(expense_values)*.05):

            plt.pie(expense_values, colors=colors, radius = .5, textprops={'color':'#404040'}, wedgeprops={'edgecolor':'#202020', 'linewidth':1})
    
            #Add a legend, ensure that there is no overlapping
            #Reference https://stackoverflow.com/questions/43272206/python-legend-overlaps-with-the-pie-chart
            plt.subplots_adjust(left=0.1, bottom=0.1, right=0.75)
            plt.legend(loc='lower left', labels=expense_categories, bbox_to_anchor=(1,0))

            break

        else: 
            #Create a pie chart from the values
            plt.pie(expense_values, labels=expense_categories, autopct='%1.1f%%', colors=colors, textprops={'color':'#404040'})
   
    #Ensure drawn as a circle
    #https://matplotlib.org/stable/gallery/subplots_axes_and_figures/axis_equal_demo.html
    plt.axis('equal')


    #Title for pie chart
    plt.title('Monthly Expenses', loc='center', fontsize=18, pad=25)


    #Display the chart
    plt.show()

    return None
 
#------------------------------------------------------------------------------------------------------------------------


#This function checks to ensure valid imput of y or n is entered when required
#it takes an argument of "answer" - representing the user input to be checked 
def y_n_check(answer):

    #set variable to determine if valid
    is_valid = False

    #while the answer is not valid prompt the user for a valid input
    while is_valid == False:
        if answer.lower() != 'n' and answer.lower() != 'y':
            print('That is not a valid answer')
            print('Please enter y / n: ')
            answer = input()

        else:
            is_valid = True

    #return the valid answer - either y or n (lowercase)
    return answer.lower()


#------------------------------------------------------------------------------------------------------------------------


#This method checks to ensure valid number input is entered when required
#it takes an argument of the user selection, and the max value allowed (assume the min value is always 1
def number_validity_check(selection, max):

    #set variable to determine if valid
    is_valid = False

    #while the answer is not valid prompt the user for a valid input
    while is_valid == False:
        #check if user input an integer value
        try:
            int(selection)

            #if the selection is an int, check it is within the allowed values
            if (int(selection) < 1) or (int(selection) > max):
                print('That is not a valid answer')
                print('Please enter a number between 1 and', max)
                selection = input()
            else:
                is_valid = True

        except ValueError:
            print('That is not a valid input')
            selection = input()
            is_valid = False

    #return the valid answer - either y or n (lowercase)
    return selection




main()