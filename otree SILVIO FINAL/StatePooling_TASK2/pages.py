from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


"""
Task 2

Task 2 has 2 pages
-------------------
-Task2_Page1: This page uses Advisor_LorR. On this page the player selects which advisor they want, and this data
	is stored as a 0 or 1 in the variable Advisor_LorR
	
-Task2_PageSELECTED:
	This page depends on the Advisor_VAR from Page1. It loads the LHS or RHS bpx depending on
	what the player selected.

"""

class Task2_Page1(Page):
	form_model = 'player'
	form_fields=['Advisor_LorR']
	pass	
	
	
class Task2_PageSELECTED(Page):
	form_model = 'player'
	form_fields=['Advisor_SaysWhite', 'Advisor_SaysBlack']
	pass	


page_sequence = [
	Task2_Page1,
	Task2_PageSELECTED,
]

