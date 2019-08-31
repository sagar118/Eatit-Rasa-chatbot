from rasa_core.channels import HttpInputChannel
from rasa_core.agent import Agent
from rasa_core.interpreter import RasaNLUInterpreter
from rasa_slack_connector import SlackInput
import warnings

# warnings.simplefilter('ignore', ruamel.yaml.error.UnsafeLoaderWarning)

nlu_interpreter = RasaNLUInterpreter('./models/nlu/default/restaurantnlu')
agent = Agent.load('./models/dialogue', interpreter = nlu_interpreter)

input_channel = SlackInput('xoxp-737606528176-739472173687-739798419894-bfb1650233e9ffb3bb06288b15152bf2', #app verification token
							'xoxb-737606528176-726169875683-J2dMnFsG2P555fglDekEQpV1', # bot verification token
							'n0NUnuVaxnThPfszFbLR116b', # slack verification token
							True)

agent.handle_channel(HttpInputChannel(5004, '/', input_channel))