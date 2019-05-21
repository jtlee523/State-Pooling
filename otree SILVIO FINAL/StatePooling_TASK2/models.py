from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)


author = 'Joseph Lee'

doc = """
#TASK 2

DATA:

0-2: colored ball values: RED, YELLOW, GREEN
3: GRAY ball values

4-6: Advisor 1 percentages (LHS)
7-9: Advisor 2 percentages (RHS)

"""



class Constants(BaseConstants):
	name_in_url = 'StatePooling_TASK2'
	data = [ [10, 30, 80, 60, 20, 30, 40, 25, 35, 45], 
		[15, 35, 85, 55, 20, 30, 40, 25, 35, 45], 
		[5, 25, 75, 50, 20, 30, 40, 25, 35, 45], 
		[10, 60, 80, 40, 20, 30, 40, 25, 35, 45], 
		[10, 60, 80, 30, 20, 30, 40, 25, 35, 45]]
		
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
			
			p.LHSAdvisor_Red = task1_data[4]
			p.LHSAdvisor_Yellow = task1_data[5]
			p.LHSAdvisor_Green = task1_data[6]
	
			p.RHSAdvisor_Red = task1_data[7]
			p.RHSAdvisor_Yellow = task1_data[8]
			p.RHSAdvisor_Green = task1_data[9]



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
	
	
	#===========TASK 2 VARIABLES============#
	Advisor_VAR = models.IntegerField() #Variable that tracks LHS or RHS advisor
	#0 if LHS, 1 if RHS
	
	Advisor_SaysWhite = models.IntegerField()
	Advisor_SaysBlack = models.IntegerField()
	#On page 2, player picks colored/gray depending on if the advisor says black/white
	#0 if they pick colored, 1 if they pick gray.
	
	
	RedPoints = models.FloatField()
	YellowPoints = models.FloatField()
	GreenPoints = models.FloatField()
	GrayPoints = models.FloatField()
	
	
	LHSAdvisor_Red = models.FloatField()
	LHSAdvisor_Yellow = models.FloatField()	
	LHSAdvisor_Green = models.FloatField()
	
	RHSAdvisor_Red = models.FloatField()
	RHSAdvisor_Yellow = models.FloatField()	
	RHSAdvisor_Green = models.FloatField()
	
		
	def current_data(self):
		return self.session.vars['data'][self.round_number-1] #returns a row of the data
	
    

	
	#colored is 0, gray is 1