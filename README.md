# Github repository for Silvio

This repository includes the state pooling and belief divergence. Currently, the main project of this folder is State pooling.
As of 5/21, the Belief Divergence project is simply idle in this folder. 

### Dependencies
The following repository requires both Python and oTree. For detailed explanations on what each subfolder and file does, please refer to oTree's documentation.

## State Pooling Task 1
(Needs to be updated)

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

4-6: Advisor 1 percentages (LHS)

7-9: Advisor 2 percentages (RHS)




### pages.py
(To be finished)

### templates
(To be finished)