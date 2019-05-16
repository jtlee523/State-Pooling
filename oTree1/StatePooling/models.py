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
	name_in_url = 'StatePooling'
	data = [ [10, 30, 80, 60], [10, 30, 80, 50], [10, 30, 80, 50], [10, 60, 80, 40], [10, 60, 80, 30]]
	num_rounds=len(data)
	players_per_group = None #single player game
	
class Subsession(BaseSubsession):
	def creating_session(self):
	
		if self.round_number == 1: #if we are on the first round
			self.session.vars['data'] = Constants.data.copy() #we record the data to something on self.
		
		
		for p in self.get_players():
			task1_data = p.current_data()
			
			p.RedPoints = task1_data[0]
			p.YellowPoints = task1_data[1]
			p.GreenPoints = task1_data[2]
			p.GrayPoints = task1_data[3]


class Group(BaseGroup):
	pass
	
class Player(BasePlayer):

	Var0 = models.IntegerField()
	Var1 = models.IntegerField()
	Var2 = models.IntegerField()
	Var3 = models.IntegerField()
	Var4 = models.IntegerField()
	Var5 = models.IntegerField()
	Var6 = models.IntegerField()
	Advisor_VAR = models.IntegerField()
	
	RedPoints = models.FloatField()
	YellowPoints = models.FloatField()
	GreenPoints = models.FloatField()
	GrayPoints = models.FloatField()
	
	def current_data(self):
		return self.session.vars['data'][self.round_number-1] #returns a row of the data
	
    

	
	#colored is 0, gray is 1