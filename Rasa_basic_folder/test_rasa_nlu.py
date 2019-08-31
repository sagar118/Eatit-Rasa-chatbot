from rasa_nlu.model import Interpreter
import json
interpreter = Interpreter.load(".\\models\\nlu\\default\\restaurantnlu")
message = "find me some restaurants in bombay in the range of 300"
#"find me some restaurants in mysuru having budget more than 700"
# "I want to find a restaurant in Trivandrum"
result = interpreter.parse(message)
print(json.dumps(result, indent=2))