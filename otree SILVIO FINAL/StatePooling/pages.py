from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


"""
TASK 1

Task 1 has 5 pages
------------------
-Task1_Page1: First page the players see.
-Task1_Page(ADVISORTYPE): (x4)
	These pages are advisor specific. 
"""

class Task1_Page1(Page):
	form_model = 'player'
	form_fields=['Var6', 'Var0','Var1', 'Var2','Var3','Var4','Var5' ]
	pass


class Task1_PageRED(Page):
	pass	

class Task1_PageGREEN(Page):
	pass	
	
class Task1_PageYELLOW(Page):
	pass	
	
class Task1_PageRainbow(Page):
	pass		
	


"""
Task 2

Task 2 has 2 pages
-------------------
-Task2_Page1: This page uses Advisor_VAR. On this page the player selects which advisor they want, and this data
	is stored as a 0 or 1 in the variable Advisor_VAR
	
-Task2_PageSELECTED:
	This page depends on the Advisor_VAR from Page1. It loads the LHS or RHS bpx depending on
	what the player selected.

"""

class Task2_Page1(Page):
	form_model = 'player'
	form_fields=['Advisor_VAR']
	pass	
	
	
class Task2_PageSELECTED(Page):
	form_model = 'player'
	form_fields=['Advisor_SaysWhite', 'Advisor_SaysBlack']
	pass	

	


"""
I may separate the page sequence into two instances.
"""
page_sequence = [
	Task2_Page1,
	Task2_PageSELECTED,
	Task1_Page1,
	Task1_PageRED,
	Task1_PageGREEN,
	Task1_PageYELLOW,
	Task1_PageRainbow,
	

]

