import zomatopy
import json

def check_loc(location):
	config={ "user_key":"9469d03762259512674c98779178cbf9"}
	
	city_list = ["agra", "ajmer", "aligarh", "amravati", "amritsar", "asansol", "aurangabad", "bareilly", "belgaum", "bhavnagar", 
	"bhiwandi", "bhopal", "bhubaneswar", "bikaner", "bokaro steel city", "chandigarh", "nagpur", "cuttack", "dehradun", 
	"dhanbad", "bhilai", "durgapur", "erode", "faridabad", "firozabad", "ghaziabad", "gorakhpur", "gulbarga", "guntur",
	"gwalior", "gurgaon", "guwahati", "hubli–dharwad", "indore", "jabalpur", "jaipur", "jalandhar", "jammu", "jamnagar", 
	"jamshedpur", "jhansi", "jodhpur", "kakinada", "kannur", "kanpur", "kochi", "kottayam", "kolhapur", "kollam", "kota", 
	"kozhikode", "kurnool", "ludhiana", "lucknow", "madurai", "malappuram", "mathura", "goa", "mangalore", "meerut", 
	"moradabad", "mysore", "nanded", "nashik", "nellore", "noida", "palakkad", "patna", "pondicherry", "allahabad", 
	"raipur", "rajkot", "rajahmundry", "ranchi", "rourkela", "salem", "sangli", "siliguri", "solapur", "srinagar", 
	"thiruvananthapuram", "thrissur", "tiruchirappalli", "tirupati", "tirunelveli", "tiruppur", "tiruvannamalai", "ujjain", 
	"bijapur", "vadodara", "varanasi", "vasai-virar city", "vijayawada", "vellore", "warangal", "surat", "visakhapatnam",
	"coimbatore", "bangalore", "chennai", "delhi", "hyderabad", "kolkata", "mumbai", "ahmedabad", "pune"]

	city = str(location)
	if city.lower() in city_list:
		return "found location"
	else:
		zomato = zomatopy.initialize_app(config)
		try:
			location_detail = zomato.get_city_ID(city)
			return "dont operate"
		except:
			return "not found"
