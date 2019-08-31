from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_literals

from rasa_core.actions.action import Action
from rasa_core.events import SlotSet
import zomatopy
import json
import pandas as pd
import smtplib
from email.message import EmailMessage

from check_location import check_loc

config={ "user_key":"9469d03762259512674c98779178cbf9"}
response = ""
result_of_last_query = ""

class ActionSearchRestaurants(Action):
	def name(self):
		return 'action_restaurant'
		
	def filterRestaurantBasedOnBudget(self, userbudget, allRestaurants):
		budget = {'lesser than 300': [0,300], 'between 300 to 700': [300,700], 'more than 700': [700,10000]}
		min_price = budget.get(userbudget)[0]
		max_price = budget.get(userbudget)[1]
		count = 0

		restaurants_df = pd.DataFrame(columns=['Restaurant Name', 'Address', 'Rating', 'Budget'])
		for restaurant in allRestaurants:
			count += 1
			avg_c_2 = restaurant['restaurant']['average_cost_for_two']
			if avg_c_2 <= max_price and avg_c_2 >= min_price:
				restaurants_df = restaurants_df.append({'Restaurant Name': restaurant['restaurant']['name'], 
					'Address': restaurant['restaurant']['location']['address'], 
					'Rating': restaurant['restaurant']['user_rating']['aggregate_rating'], 
					'Budget': restaurant['restaurant']['average_cost_for_two']}, ignore_index=True)

		restaurants_df['Rating'] = pd.to_numeric(restaurants_df['Rating'])
		restaurants_df = restaurants_df.sort_values(by=['Rating'], ascending=False)
        
		no_of_records = len(restaurants_df.index)

		global result_of_last_query

		if no_of_records == 0:
			response = "Oops! no restaurant found for this query. " + " search results = " + str(count)
		else:
			response = 'Showing you top results:' + "\n"
			for i in restaurants_df.head(10).index:
					if i < 5:
						response += restaurants_df['Restaurant Name'][i]+ " in "+ restaurants_df['Address'][i] + " has been rated " + str(restaurants_df['Rating'][i]) +".\n"
					result_of_last_query +=	"- " + restaurants_df['Restaurant Name'][i]+ " in "+ restaurants_df['Address'][i] + " has been rated " + str(restaurants_df['Rating'][i]) +".\n"
			if no_of_records <= 5 :
					response = response + "\n \nFor more results please search in higher budget range...\n \n"

		restaurants_df = restaurants_df.iloc[0:0]
		return response

	def run(self, dispatcher, tracker, domain):
		zomato = zomatopy.initialize_app(config)
		
		loc = tracker.get_slot('location')
		cuisine = tracker.get_slot('cuisine')
		budget = tracker.get_slot('budget')

		cuisines_dict={
		'american': 1, 
		'chinese':25, 
		'italian':55, 
		'north indian':50, 
		'south indian':85, 
		'mexican': 73}

		location_detail=zomato.get_location(loc, 1)	
		d1 = json.loads(location_detail)
		lat=d1["location_suggestions"][0]["latitude"]
		lon=d1["location_suggestions"][0]["longitude"]
		
		results=zomato.restaurant_search("", lat, lon, str(cuisines_dict.get(cuisine)), 50)
		
		global response

		data = json.loads(results)

		if data['results_found'] == 0:
			response= "Sorry, we didn't find any results for this query."
		else:
			response = self.filterRestaurantBasedOnBudget(budget, data['restaurants'])

		dispatcher.utter_message(str(response))
		if response[:5] == "Oops!":
			dispatcher.utter_template("utter_choose_budget_again", tracker)
			return [SlotSet('results_found',"not found")]
		else:
			return [SlotSet('results_found',"found")]

class EmailRestaurantDetails(Action):
	def name(self):
		return 'action_send_email'
		
	def run(self, dispatcher, tracker, domain):
		email_id = str(tracker.get_slot('email_id'))

		# for slack handling
		if len(email_id.split("|")) == 2:
			email_id = email_id.split("|")[1]

		global result_of_last_query

		to = [email_id]
		body = result_of_last_query

		gmail_user = 'eatit.foodie@gmail.com'
		gmail_password = 'Eatit118'

		email_text = "The details of all the restaurants you inquired \n \n"

		email_text = email_text + body

		try:
		    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
		    server.ehlo()
		    server.login(gmail_user, gmail_password)
		    server.sendmail(gmail_user, to, email_text)
		    server.quit()
		    dispatcher.utter_template("utter_email_sent", tracker)
		except:
		    dispatcher.utter_template("utter_no_email_sent", tracker)
		
		response = ""
		return [SlotSet('email_id',email_id)]

class CheckLocation(Action):
	def name(self):
		return 'action_check_location'

	def run(self, dispatcher, tracker, domain):
		location = tracker.get_slot('location')
		
		dispatcher.utter_template("utter_check_location", tracker)
		
		# Call the check_loc method to check if the location is in Tier 1 or 2
		loc_status = check_loc(location)

		# Set the slot of location_match based on the loc_status
		if loc_status == "found location":
			dispatcher.utter_template("utter_location_found", tracker)
			return [SlotSet('location_match',"found")]
		elif loc_status == "dont operate":
			dispatcher.utter_template("utter_sorry_dont_operate", tracker)
			return [SlotSet('location_match',"not found")]
		elif loc_status == "not found":
			dispatcher.utter_template("utter_location_not_found", tracker)
			return [SlotSet('location_match',"not found")]

# class ActionRestarted(Action): 	
# 	def name(self):
# 		return 'action_restart'
# 	def run(self, dispatcher, tracker, domain):
# 		return[Restarted()] 

# class ActionSlotReset(Action): 
# 	def name(self): 
# 		return 'action_slot_reset' 
# 	def run(self, dispatcher, tracker, domain): 
# 		return[AllSlotsReset()]

class ResetSlot(Action):
	def name(self):
		return "action_reset_slot"

	def run(self, dispatcher, tracker, domain):
		return [SlotSet("location", None), SlotSet("location_match", None), SlotSet("email_id", None), 
		SlotSet("cuisine", None), SlotSet("budget", None)]