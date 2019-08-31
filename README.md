# Eatit Restaurant Bot
A conversational bot (chatbot) which can help users discover restaurants across several Indian cities. 
The main purpose of the bot is to help users discover restaurants quickly and efficiently and to provide a good restaurant discovery experience. 
Zomato apis are used for searching the restaurants. https://developers.zomato.com/documentation#/

### Important Notes:
Eatit works only in Tier-1 and Tier-2 cities. You can use the current HRA classification of the cities from here: https://en.wikipedia.org/wiki/Classification_of_Indian_cities. Under the section 'current classification' on this page, the table categorizes cities as X, Y, and Z. Consider 'X ' cities as tier-1 and 'Y' as tier-2. 
The chatbot provides results for tier-1 and tier-2 cities only, while for tier-3 cities, it will reply back with something like "We do not operate in that area yet".

### Prerequisites
Python 3.6.x(except 3.6.9)
Visual studio for python development 
Rasa_nlu version 0.12.3
Rasa_core version 0.10.1 

### Note
Open the command prompt in Administrator Mode.
Right click the command prompt and select Run as Administrator.

### Installation:
1. Python 3.6.x (except 3.6.9)
```
>conda create -n env python=3.6.9
```

2. Visual Studio:
For Windows:
  - Go the Microsoft Visual Studio link: https://visualstudio.microsoft.com/
<<<<<<< HEAD
  Select the ‘Visual Studio IDE’ and from the dropdown, select the ‘Community version 2017’:
=======
	Select the ‘Visual Studio IDE’ and from the dropdown, select the ‘Community version 2017’:
  - Install the downloaded file. Once the Visual Studio is installed, select the Python Development under ‘Web & Cloud’ Environment. Also, on the right side (Summary), in the optional menu select the ‘Python native development tools’.
  - Click on install.

For Mac:
  - Download visual studio code: https://code.visualstudio.com/docs/?dv=osx.
  - Install the python extension for Visual Studio Code from here. After clicking
  ‘Install’, click ‘Open Visual Studio Code’ - it will open a VS Code window that
  you’ve installed in step-1 :
  https://marketplace.visualstudio.com/items?itemName=ms-python.python
  - Install the python extension. If it shows the button ‘Reload’ after installation,
  click ‘Reload’ to reload VS and enable the python extension.

Rasa NLU (Requirements and Rasa NLU with Spacy download)
1. Open Anaconda Prompt/ Windows Command Prompt/ Linux Terminal as
Administrator to install Rasa.
2. Navigate to ‘rasa_nlu-master’ in the command prompt.
cd [path where rasa_nlu-master folder is located] \rasa_nlu-master
(Note: ‘rasa_nlu-master’ folder has rasa_nlu folder. Don’t navigate to that.)
3. Run the following commands in the Command Prompt:
```
pip install -r requirements.txt
pip install -e .
```

(Note for Windows: in case of the error- ‘Microsoft Visual Studio C++ not found’,
run the above commands through ‘x64 Native Tools Command Prompt for VS 2017’.)

(Notes for Mac:
- you can try using virtualenv: https://spacy.io/usage/.
- In case of the following error- ‘Failed building wheel for python-crfsuite’, try
using: pip install https://pypi.python.org/packages/source/p/pythoncrfsuite/
python-crfsuite-0.8.1.tar.gz)

4. If the system asks to upgrade pip, use the following commands:
For windows: 
```
python -m pip install --upgrade pip
```
For Mac: 
```
pip install pip –upgrade
pip install setuptools –upgrade
```

5. Install Rasa NLU & Spacy in the same command prompt:
```
pip install rasa_nlu[spacy]
python -m spacy download en_core_web_md
python -m spacy link en_core_web_md en
```

Note for Mac Users: In case of the following error- “ValueError: unknown locale:
UTF-8”, try resolving it by running the following commands before installing
rasa_nlu[spacy]
```
export LC_ALL=en_US.UTF-8
export LANG=en_US.UTF-8
$ source ~/.bash_profile
And then run:
pip install rasa_nlu[spacy]
python -m spacy download en_core_web_md
```

6. Install pandas
```
>pip install pandas
```

Rasa Core Installation
1. Navigate to the ‘rasa_core-master’ folder path in command prompt
cd rasa_core-master
2. Run the following command to install the Rasa Core requirements:
```
>pip install -r requirements.txt
>pip install -e .
```

Installing Rasa-NLU-Trainer
1. Rasa has an inbuilt GUI tool for adding/editing the training examples: rasa-nlutrainer.
We’ll download it using the npm package manager of node.js environment:
2. Download node.js from https://nodejs.org/en/ (Version: Recommended for most
users)
3. After the installation, run the following command in PowerShell/ Windows Command
Prompt
```
>npm i -g rasa-nlu-trainer
```

For Mac OS: sudo npm i -g rasa-nlu-trainer.

#### How to find rasa_core and rasa_nlu version
```
>python -c "import rasa_nlu; print(rasa_nlu.__version__);"
>python -c "import rasa_core; print(rasa_core.__version__);"
```

## Train the nlu data & train the core conversational flow using the command line

```
cd path <path to Rasa_basic_folder>
```

### train the NLU
```
>python nlu_model.py
```

### train Core
```
>python train_init.py
```

### verify the bot command line
```
>python dialogue_management_model.py
```

### train dialogue flow online and add the strories
```
>python train_online.py
```

Generated stories can be exported to a path and then added to stories.md. Retrain the model and check dialogue flow.

## Deployment to slack

run the bot on local sever and integrate with slack.

Using ngrok (https://ngrok.com/download) as a webhook deploy the bot on slack(https://slack.com/). Create a bot in slack and integrate the credentials in run_app.py program.
```
>python run_app.py  
```
The bot can be accessed from slack. 

## Built With

* Rasa
* Keras Framework
* Tensorflow
* Slack

## Author

* **Sagar Thacker**
* **Bhaskar Nag**
* **Nitin Shukla**
* **Amsuman Gangapuram**

## License

 ---- NA ----------
