#import zomatopy
#import json
#import pandas as pd
import smtplib

# config={ "user_key":"9469d03762259512674c98779178cbf9"}

# zomato = zomatopy.initialize_app(config)
# # loc = tracker.get_slot('location')
# # cuisine = tracker.get_slot('cuisine')
# # avg_budget_2_ppl = tracker.get_slot('avg_budget_2_ppl')
# location_detail=zomato.get_location('mumbai', 1)
# d1 = json.loads(location_detail)
# lat=d1["location_suggestions"][0]["latitude"]
# lon=d1["location_suggestions"][0]["longitude"]
# cuisine = 'chinese'
# avg_budget_2_ppl = 'more than 700'
# cuisines_dict={'bakery':5,'chinese':25,'cafe':30,'italian':55,'biryani':7,'north indian':50,'south indian':85}
# budget = {'lesser than 300': 300,'rs. 300 to 700': 500, 'more than 700': 700}
# results=zomato.restaurant_search("", lat, lon, str(cuisines_dict.get(cuisine)), 50)
# d = json.loads(results)
# # response=""
# # if d['results_found'] == 0:
# # 	response= "no results"
# # else:
# # 	for restaurant in d['restaurants']:
# # 		response=response+ "Found "+ restaurant['restaurant']['name']+ " in "+ restaurant['restaurant']['location']['address']+"\n"
# # print(response)

# # for restaurant in d['restaurants']:
# # 	print(restaurant['restaurant']['name'], restaurant['restaurant']['average_cost_for_two'], restaurant['restaurant']['price_range'])

# avg_budget = budget.get(avg_budget_2_ppl)
# flag = 0
# restro = pd.DataFrame(columns=['Restaurant Name', 'Address', 'Rating', 'Budget'])
# for restaurant in d['restaurants']:
# 	flag = 0
# 	if avg_budget == 300:
# 		if restaurant['restaurant']['average_cost_for_two'] > 300:
# 			del restaurant
# 			flag = 1
# 	elif avg_budget == 700:
# 		if restaurant['restaurant']['average_cost_for_two'] < 700:
# 			del restaurant
# 			flag = 1
# 	elif avg_budget == 500:
# 		if (restaurant['restaurant']['average_cost_for_two'] < 300) or (restaurant['restaurant']['average_cost_for_two'] > 700):
# 			del restaurant
# 			flag = 1
# 	if flag == 0:
# 		restro = restro.append({'Restaurant Name': restaurant['restaurant']['name'], 
# 			'Address': restaurant['restaurant']['location']['address'], 
# 			'Rating': restaurant['restaurant']['user_rating']['aggregate_rating'], 
# 			'Budget': restaurant['restaurant']['average_cost_for_two']}, ignore_index=True)
# restro = restro.sort_values(by=['Rating'], ascending=False)
	
# response = ""
# for i in restro.head(10).index:
# 	# print(i)
# 	response += restro['Restaurant Name'][i]+ " in "+ restro['Address'][i] + " has been rated " + restro['Rating'][i] +".\n"


# # # avg cost of 2 ppl
# # for restaurant in d['restaurants']:
# # 	print(restaurant['restaurant']['average_cost_for_two'], restaurant['restaurant']['price_range'])

# # # restaurant rating
# # for restaurant in d['restaurants']:
# # 	print(restaurant['restaurant']['user_rating']['aggregate_rating'])	

sent_from = "support@eatit.com"
to = ["sagarthacker961118@gmail.com"]
subject = 'Top 10 restaurants'
body = "gurukripa"

gmail_user = 'csi.sagar.thacker@gmail.com'
gmail_password = 'Kindness#118'

email_text = """\
From: %s
To: %s
Subject: %s

The top 10 restaurants are:\n
%s
""" % (sent_from, ", ".join(to), subject, body)
# try:
# 	s = smtplib.SMTP('localhost')
# 	s.sendmail(sent_from, to, email_text)
# 	# s.quit()
# 	# dispatcher.utter_template("utter_email_sent", tracker)
# 	print("sent")
# except SMTPException:
# 		print("Error: unable to send email")

try:
    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.ehlo()
    server.login(gmail_user, gmail_password)
    server.sendmail(sent_from, to, email_text)
    server.close()

    print('Email sent!')
except:
    print('Something went wrong...')