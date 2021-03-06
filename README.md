# Github repository for Silvio

This repository includes the state pooling and belief divergence. Currently, the main project of this folder is State pooling.
As of 5/21, the Belief Divergence project is simply idle in this folder. 

### Dependencies
The following repository requires both Python and oTree. For detailed explanations on what each subfolder and file does, please refer to oTree's documentation.

## State Pooling Task 1

### models.py
In this page, we can edit parameters for task 1. We use a list of lists, and there are four numbers per sublist.
The first three numbers (0-2) give the values of the colored balls (Red, Yellow, Green) and the last number (3) is for the gray ball. For example, [10, 30, 80, 60] would have the red, yellow, and green balls be 10, 30, and 80 respectively. The gray ball would be 60.

#### variables
There are a lot of variables for this task, but many of them repeat.

##### Choice_[xxx]
The choice variables are for the first page. The player is asked what their urn choice would be when the advisor says a certain option. The value is 0 if colored is picked, and 1 if gray.

##### [Color]_Q[number]
The following pages, the player is asked how many points they would give up per the advisor. The first question corresponds with Q0, etc.


##### Other
The other variables store the point values (numbers 0-3 on the sublist) for the experiment.

### pages.py
There are four pages: Task1_Page1, Task1_Page[COLOR] (x 4). The first page asks what the player would choose depending on what each advisor says. The following pages ask how many points a player would give up per having each colored advisor.


## StatePooling_TASK2
The folders/files that are relevant for the experiment are as follows:
models.py, pages.py, and the folder: templates.

### models.py
In this page, you can edit the parameters for the experiment for task 2.
The player section loads the necessary variables for both data collection and for the data on each page.
Subsessions creates the various sessions. This loops depending on the length of the data.

Data is loaded in the class constants. In the variable, data, a list of lists is the data. The sublists have length 10:

0-2: colored ball values: RED, YELLOW, GREEN

3: GRAY ball values

4-6: Advisor 1 percentages (LHS) (Red, Yellow, Green)

7-9: Advisor 2 percentages (RHS) (Red, Yellow, Green)

Though I haven't figured out how to do this, if one could read a csv as a list of list with the same ordering as stated above, then that may be more effective.

For example, [10, 30, 80, 60, 20, 30, 40, 25, 35, 45] gives us colored values for the balls as 10, 30, and 80. The value of the gray ball is 60. The left hand side advisor will have percentages 20, 30, and 40, and the right hand side advisor will have 25, 35, and 45.

#### variables
The document has comments indicating what each variable does in the Player class.

##### Advisor_LorR
On the first page of the task, the player has a choice from the left or right advisor. If the player picks the LEFT, the value is 0. If the player picks RIGHT, the value is1

##### Advisor_SaysWhite, Advisor_SaysBlack
On the 2nd page, the player has to choose what urn they would pick if the advisor says white, and if the advisor says black. The value is 0 if colored is picked, and 1 if gray is picked.

##### Other variables 

The rest of the variables are used for data storage. [COLOR]points stores the values of the first 0-3 numbers for the colored and gray balls. LHSadvisor_[COLOR] and RHSadvisor_[COLOR] store the numbers for the percentages.

### pages.py
The page sequence is set as Task2_Page1, and Task2_PageSELECTED. Task2_Page1 is the first page of the experiment, constituting advisor choice. Task2_PageSELECTED is the page in which the player picks the urns.


## Other

There is an option to change font size. On the beginning of every page, there is a block <font size="+2"> The number can be adjusted to any value.
