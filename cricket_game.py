'''start
selecting team()
selecting players()
toss()
over selection()
bat()
bowl()
score()
result()
commentary()
'''


#Select the players 
import random

def Match_result(Total_your_score,Total_opp_score,your_team,opponent_team):
	print("\nTotal score of your team %s is %s "%(your_team,Total_your_score))
	print("\nTotal score of your opponent team %s is %s"%(opponent_team,Total_opp_score))

	if(Total_your_score>Total_opp_score):
		print("\n \t\t\bWWhattt a match today,  You won it")

	elif(Total_your_score<Total_opp_score):
		print("\n \t\t\bBad day again, better luck next time")

	else:
		print("\n \t\t\bUnbelievable....never saw a tie match")


def Score_random(Number_of_overs):
	if(Number_of_overs<=20):
		List_Runs=[1,1,1,1,1,1,0,2,1,0,1,0,1,0,2,3,4,4,'W',4,6,0,4,'W',1,1,0,0,6,1,1,1,0,1,1,'W',0,4,0,3,0,0,4,0,4,'W',2,2,2,1,1,1,1,0,0,1,1,1,6,0,'W',0,0,2,0,6,4,2,3,1,0]
	elif(Number_of_overs<=50):
		List_Runs=[1,1,1,1,1,1,1,2,2,0,1,0,1,0,2,3,4,4,'W',4,6,0,6,'W',1,1,0,0,6,1,1,1,1,1,1,0,0,0,0,0,0,0,4,0,4,0,0,2,2,2,1,1,1,1,0,0,1,1,1,0,0,'W',0,0,0,0,0,4,2,3,1,0,0]	
	else:
		List_Runs=[1,1,1,1,1,1,0,2,2,0,1,0,1,0,2,1,4,0,'W',6,0,0,2,0,0,1,1,0,0,2,1,1,1,0,1,0,0,'W',0,0,0,0,0,0,4,0,1,0,0,2,2,2,1,4,1,1,0,0,1,1,1,0,0,6,0,0,0,0,0,4,2,1,1,0,0]

	return (random.choice(List_Runs))
	# for test match kind add more 0's and less W's 
	#get overs, if over less than 20 no 0's more Ws 
	#for limited over add more runs and wickets
	#take the bowler's value and select the probablity list   
	#imp batting should be done once score reached..not till entire match


def Batting(your_team,your_players,opponent_team,opponent_players,Number_of_overs,selection,Total_score):
	
	if(selection==0):
		Total_score=100000000
	else:
		print("")

	print("\n You are Batting now!!")
	inp=input("n Enter to start batting")
	Overs_played=0
	Total_your_score=0
	Total_your_wicket=0

	
	while(Overs_played<Number_of_overs and Total_your_wicket<10 and Total_your_score<Total_score+1):      #pause over once 
		for i in range(1,7):
			Current_Ball=str(Overs_played)+"."+str(i)
				
			Dict_Score={}


			Dict_Score[Current_Ball]=Score_random(Number_of_overs)
			Current_score=Dict_Score[Current_Ball]
			print("scored %s on Ball %s"%(Current_score,Current_Ball))
			if(Current_score=='W'):                   #pass here and ask for next player in the dict to get down and delete that plyer from list
				Total_your_wicket=Total_your_wicket+1
				print("")
				if(Total_your_wicket==10):
					break
				else:
					print("")
			else:
				Total_your_score=Total_your_score+Current_score
				if(Total_your_score>Total_score):
					break
				else:
					print("")


		Overs_played=Overs_played+1
	print("Your score is %s with the %s wickets down"%(Total_your_score,Total_your_wicket))

	if(selection==0):
		selection=1
		Bowling(your_team,your_players,opponent_team,opponent_players,Number_of_overs,selection,Total_your_score)
	else:
		Total_opp_score=Total_score
		Match_result(Total_your_score,Total_opp_score,your_team,opponent_team)
		print("\n Press 1 to play it again \t Enter to exit")
		To_play_again=input()
		if(To_play_again=='1'):
			Main()
		else:
			print("Thanks for playing")
		
		
	

def Bowling(your_team,your_players,opponent_team,opponent_players,Number_of_overs,selection,Total_score):
	print("\n Please Focus on your Bowling!!")
	print("")
	if(selection==0):
		Total_score=100000000
	else:
		print("")
#choose bowler over once or select 5 bowlers at the start
	inp=input("\n Enter to start bowling")
	Overs_played=0
	Total_opp_score=0
	Total_opp_wicket=0
	while(Overs_played<Number_of_overs and Total_opp_wicket<10 and Total_score+3>Total_opp_score):      #pause over once 
		for i in range(1,7):
			Current_Ball=str(Overs_played)+"."+str(i)
				
			Dict_Score={}

			Dict_Score[Current_Ball]=Score_random(Number_of_overs)
			Current_score=Dict_Score[Current_Ball]
			print("scored %s on Ball %s"%(Current_score,Current_Ball))
			if(Current_score=='W'):                   #pass here and ask for next player in the dict to get down and delete that plyer from list
				Total_opp_wicket=Total_opp_wicket+1
				print("")
				if(Total_opp_wicket==10):
					break
				else:
					print("")
			else:
				Total_opp_score=Total_opp_score+Current_score
				if(Total_opp_score>Total_score):
					break
				else:
					print("")


		Overs_played=Overs_played+1
	print("Your opponent score is %s with the %s wickets down"%(Total_opp_score,Total_opp_wicket))

	if(selection==0):
		selection=1
		Batting(your_team,your_players,opponent_team,opponent_players,Number_of_overs,selection,Total_opp_score)
	else:
		Total_your_score=Total_score
		Match_result(Total_your_score,Total_opp_score,your_team,opponent_team)
		print("\n Press 1 to play it again \t Enter to exit")
		
		To_play_again=int(input())
		if(To_play_again==1):
			Main()
		else:
			print("Thanks for playing")
	

def Over_Selection():
	print("\n Select number of overs you would like to play")
	
	Overs=input('>>') #select from 5,10,15,20
	try:
		number=int(Overs)
		return Overs
	except ValueError:
		print("Select the overs in numerals")
		Over_Selection()

def Toss(your_team,your_players,opponent_team,opponent_players,Number_of_overs):
	Dict_Toss={'1':'Heads','2':'Tails'}
	
	condition1=True
	condition2=True
	while(condition1):
		print("\n Choose the Toss \n\n\t",Dict_Toss)
		Toss_selected=input('>>')
		if(Toss_selected in Dict_Toss):
			#print("Toss_selected is in Dict")
			List_Toss = list(Dict_Toss.keys()) 
			selection=0
			Toss_random=random.choice(List_Toss)
			print("\n It's a",Dict_Toss[Toss_random])
			if(Dict_Toss[Toss_selected]==Dict_Toss[Toss_random]):
				print("\n AAHAA You have won the Toss...")
				
				
				while(condition2):
					print("\n You are going with Batting or Bowling?, CHOOSE 1 For Batting and 2 for bowling")
					Toss_Choose=input('>>')
					condition1=False
					if(Toss_Choose in Dict_Toss):
						Batting(your_team,your_players,opponent_team,opponent_players,int(Number_of_overs),selection,selection) if Toss_Choose=='1' else Bowling(your_team,your_players,opponent_team,opponent_players,int(Number_of_overs),selection,selection)
						condition2=False

					else:
						print("Kindly choose Batting/Bowling properly")
			else:
				print("Opponent won the Toss and selected to Bowl")
				#use random to select batting/bowling
				Batting(your_team,your_players,opponent_team,opponent_players,int(Number_of_overs),selection,selection) 
				condition1=False
			#need to do random for batting/bowling
		else:
			print("Please select the toss properly 1 for Heads ; 2 for Tails")







def Select_players(team):
	India={'1':'Dhawan','2':'Rohit sharma','3':'Rahul','4':'Virat kohli','5':'Raina','6':'MS Dhoni','7':'Murali Vijay','8':'Rahanea','9':'Jadeja','10':'Ashwin','11':'Umesh Yadav','12':'Ishanth sharma','13':'Bhuvanesh kumar','14':'kuladeep yadav','15':'Mishra'}
	Australia={'1':'Steve Smith','2':'David Warner','3':'Jackson Bird','4':'Matthew Wade','5':'Shaun Marsh','6':'Peter Handscomb','7':'Josh Hazlewood','8':'Glenn Maxwell','9':'Mitchell Starc','10':'Nathan Lyon','11':'Josh Hazlewood','12':'Pat Cummins','13':'Jackson Bird','14':'Ashton Agar','15':'Mitchell Swepson'}
	if (team=='India'):
		index=0
	elif(team=='Australia'):
		index=1
		#if ypuadd team we need to add indexes and in the list aswell
	else:
		print("nothing")
		#Add other countries as well.....
	Teams=[India,Australia]
	
	print("\n")
	Players_Added={}   
	count=0
	country=Teams[index]
	print (country)
	while(count<11):
		Player_input=input('>>')            
		if(Player_input  in country):     
			print("Added to the Team",country[Player_input])
			count=count+1
			Players_Added[count]=country[Player_input]
			print (Players_Added)
			del country[Player_input]
		else:
			print("\n Players added as of now to your Team", Players_Added)
			print("\nEnter the appropriate number based on the player listed below...if you selected the player before..it won't be lised here")
			print("\n ",country)
	print("\n So you have done with selecting the Players")
	#print ("\n Players in XI ==>",Players_Added)
	return Players_Added


def select_TopXI_Auto(team)	:
	India={1:'Dhawan',2:'Rohit sharma',3:'Rahul',4:'Virat kohli',5:'Rahanea',6:'MS Dhoni',7:'Jadeja ',8:'Bhuvanesh kumar',9:'kuladeep yadav',10:'Ashwin',11:'Umesh Yadav'}
	Australia={1:'Steve Smith',2:'David Warner',3:'Peter Handscomb',4:'Matthew Wade',5:'Shaun Marsh',6:'Jackson Bird',7:'Josh Hazlewood',8:'Glenn Maxwell',9:'Mitchell Starc',10:'Nathan Lyon',11:'Pat Cummins'}

	if (team=='India'):
		index=0
	elif(team=='Australia'):
		index=1
	else:
		print("nothing")
		#Add other countries as well.....
	Teams=[India,Australia]
	
	print("\n")
	Players_Added={}   
	count=0
	country=Teams[index]
	print (country)
	return country




#selecting your team and opponent team here
def Select_Team():
	Teams={'1':"India",'2':"Australia"}
	print("Select Your Team")
	print (Teams)				# need to print key for value ex: select 1 for india
	print("\n")
	Team_input=input('>>')
	if(Team_input  in Teams):
		your_team=Teams[Team_input]
		print("Good choice! you have choosed to play as \n\t",your_team)
		del Teams[Team_input]                       #once selected delete from the dict
	else:
		print("Kindly select the Team properly \n")
		Select_Team()
	
	print("\n")
	print("Select Your opponent Team")
	print (Teams)
	print("\n")
	To_check=True
	while (To_check):
		Team_input=input('>>')
		if(Team_input  in Teams):
			opponent_team=Teams[Team_input]
			print("you choosed to play against \t",opponent_team)
			To_check=False
			your_players={}
			opponent_players={}
			condition3=True
			while(condition3):
				print("\n To Proceed with Top XI Enter 1")
				print("To select the players manually Enter 2")
				Choose_way_selectingplayers=input('>>>')	
				if(Choose_way_selectingplayers=='2'):
					print("\n select your team \"%s\" players"%your_team)
					your_players=Select_players(your_team)
					print ("\n Players in XI ==>",your_players)
					print("\n select opponent team \"%s\" players"%opponent_team)
					opponent_players=Select_players(opponent_team)
					print ("\n Players in XI ==>",opponent_players)
					# Call the Toss and select the number of overs here
					Number_of_overs=Over_Selection()
					print("You have choosed to play %s  overs"%Number_of_overs)
					Toss(your_team,your_players,opponent_team,opponent_players,Number_of_overs)
					condition3=False
				elif(Choose_way_selectingplayers=='1'):
					print("you are proceeding with Top XI players")
					your_players=select_TopXI_Auto(your_team)
					opponent_players=select_TopXI_Auto(opponent_team)
					Number_of_overs=Over_Selection()
					print("You have choosed to play %s  overs"%Number_of_overs)
					Toss(your_team,your_players,opponent_team,opponent_players,Number_of_overs)
					condition3=False
				else:
					print("Do you want to play with Top XI/ you want to manually choose...kindly select")

			
		else:
			print("Kindly select the Team properly \n")
			print (Teams)

			
#starting the game here
def Game_start(input_start):
	print('--'*10)
	if input_start=='1':
		print("Game started")
		Select_Team()
	elif input_start=='0':
		print("\n You pressed 0 and Game is over")
	else:
		print("Kindly Enter 1 / 0")
		Main()
print("Welcome to the Game")

#main program
def Main():
	print("Enter 1 to start the game and 0 to exit")
	To_Start=input('>>')
	Game_start(To_Start)

Main()