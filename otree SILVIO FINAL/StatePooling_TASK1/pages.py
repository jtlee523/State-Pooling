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
	form_fields=['Choice_NoQ', 
			'Choice_RedYes',
			'Choice_RedNo', 
			'Choice_YellowYes',
			'Choice_YellowNo',
			'Choice_GreenYes',
			'Choice_GreenNo',
			'Choice_RainbowRed',
			'Choice_RainbowYellow',
			'Choice_RainbowGreen']
	pass


class Task1_PageRED(Page):
	form_model = 'player'
	form_fields=['Red_Q0', 
				'Red_Q1',
				'Red_Q2',
				'Red_Q3',
				'Red_Q4',
				'Red_Q5',
				'Red_Q6',
				'Red_Q7',
				'Red_Q8',
				'Red_Q9',
				'Red_Q10']
	pass	

class Task1_PageGREEN(Page):
	form_model = 'player'
	form_fields=['Green_Q0', 
				'Green_Q1',
				'Green_Q2',
				'Green_Q3',
				'Green_Q4',
				'Green_Q5',
				'Green_Q6',
				'Green_Q7',
				'Green_Q8',
				'Green_Q9',
				'Green_Q10']	
	pass	
	
class Task1_PageYELLOW(Page):
	form_model = 'player'
	form_fields=['Yellow_Q0', 
				'Yellow_Q1',
				'Yellow_Q2',
				'Yellow_Q3',
				'Yellow_Q4',
				'Yellow_Q5',
				'Yellow_Q6',
				'Yellow_Q7',
				'Yellow_Q8',
				'Yellow_Q9',
				'Yellow_Q10']	
	pass	
	
class Task1_PageRainbow(Page):
	form_model = 'player'
	form_fields=['Rainbow_Q0', 
				'Rainbow_Q1',
				'Rainbow_Q2',
				'Rainbow_Q3',
				'Rainbow_Q4',
				'Rainbow_Q5',
				'Rainbow_Q6',
				'Rainbow_Q7',
				'Rainbow_Q8',
				'Rainbow_Q9',
				'Rainbow_Q10']	
	pass		
	



page_sequence = [
	Task1_Page1,
	Task1_PageRED,
	Task1_PageGREEN,
	Task1_PageYELLOW,
	Task1_PageRainbow,
]

