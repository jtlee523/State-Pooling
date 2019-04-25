from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)


author = 'Joseph Lee'

doc = """
Task 1

0-2= prior (ex ante urn probability)
3-5= signal structure (black/white ball probability for each urn)
6=ball color (0/1 based on black/white ball color)
"""


class Constants(BaseConstants):
    name_in_url = 'TeresaDuarte'
    players_per_group = None #Single player game
    num_rounds = 1 #as many rounds as there are lines of data



class Subsession(BaseSubsession):

	"""def creating_session(self):
	
		if self.round_number == 1: #if we are on the first round
			self.session.vars['data'] = Constants.data.copy() #we record the data to something on self.
		
		
		for p in self.get_players():
			task1_data = p.current_data()
			
			p.Red_Urn_Given = task1_data[0]
			p.Yellow_Urn_Given = task1_data[1]
			p.Green_Urn_Given = task1_data[2]
			
			p.Assigned_Red = task1_data[3]
			p.Assigned_Yellow = task1_data[4]
			p.Assigned_Green = task1_data[5]

			p.isBlackBall = task1_data[6]"""
	pass

class Group(BaseGroup):
    pass


class Player(BasePlayer):
	BlueRoundChoice = models.StringField(
    	choices=['U', 'M', 'D'],
    	widget=widgets.RadioSelect
		)
	
	GreenRoundChoice = models.StringField(
		
    	choices=['L', 'C', 'R'],
    	widget=widgets.RadioSelect
		)
	Points = models.IntegerField()
	#def current_data(self):
	#	return self.session.vars['data'][self.round_number-1] #returns a row of the data
	
    


#https://media.readthedocs.org/pdf/otree/latest/otree.pdf
#https://otree.readthedocs.io/en/latest/misc/tips_and_tricks.html

"""
PLAN!
make 3 apps, one for each task
THEN, in settings, create a main app that calls task 1 then task 2
"""