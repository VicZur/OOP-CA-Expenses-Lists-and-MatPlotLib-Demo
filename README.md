# OOP-CA-Lists-and-MatPlotLib-Demo

This program was created as part of the Assessment Project for an Object Oriented Programming module (Level 8) at the Dublin Business School.

It received a pending grade of 90-95%, earned for demonstrating a high standard of coding practices and adding additional features.

### The project requirements
A program that reads data in a text file containing expenses for 6 pre-specified categories.

It then plots a pie chart using MatPlotLib.

### Additional Functionality Added
My program added increased functionality, such as allowing the user to select from multiple test files, or choose a location to use their own text file. The program also loops to allow ease of use if the user wishes to look at another file of expenses. 

I achieved these additional elements by having a function to display a menu if the user decides to not run the default program. This function is recursive and calls itself if the user decides to “go back” when prompted.

I included error checking, including:
*	Ensuring the file path is valid (if the user enters their own)
*	Ensuring all expense values are greater than 0
*	Ensuring when prompted for input the user enters a valid choice (y or n, valid number)
*	Checking the file that is being read in for formatting issues
* Can handle 0 value for expense, blank lines
* Displays a message if there is too many items on one line, or if the number of category titles and expense values differ

I also included additional matplotlib features to enhance the readability of the pie chart. I used an if statement to determine if any of the wedges would be below 5%. If this is the case, the percentage labels used for larger wedges would be difficult to read. I therefore remove the percentage and labels and switch to a legend when the wedges are too small. In this case I also add in dark grey lines to separate the wedges for readability. For pie charts of all sizes, I used a colour map to select colours related to money, yellow being high values and green being low. The intervals of these colours are determined by the total number of wedges. I changed the colour of the labels to be less harsh than black. 
