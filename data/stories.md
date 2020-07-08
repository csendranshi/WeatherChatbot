## happy path
* greet
  - utter_greet
* mood_great
  - utter_happy

## sad path 1
* greet
  - utter_greet
* mood_unhappy
  - utter_cheer_up
  - utter_did_that_help
* affirm
  - utter_happy

## sad path 2
* greet
  - utter_greet
* mood_unhappy
  - utter_cheer_up
  - utter_did_that_help
* deny
  - utter_goodbye

## say goodbye
* goodbye
  - utter_goodbye

## bot challenge
* bot_challenge
  - utter_iamabot
 
## Story001
* greet
    - utter_greet
* inform
    - utter_ask_location
* inform{"location":"italy"}
    - slot{"location":"italy"}
    - action_weather
    - slot{"location":"italy"}
* goodbye
    - utter_goodbye
## Story001
* greet
    - utter_greet
* inform
    - utter_ask_location
* inform{"location":"italy"}
    - slot{"location":"italy"}
    - action_weather
    - slot{"location":"italy"}
* goodbye
    - utter_goodbye
    
## Story002
* greet
    - utter_greet
* inform
    - utter_ask_location
* inform{"location":"delhi"}
    - slot{"location":"delhi"}
    - action_weather
    - slot{"location":"delhi"}
* goodbye
    - utter_goodbye
    
## Story003
* greet
    - utter_greet
* inform
    - utter_ask_location
* inform{"location":"mumbai"}
    - slot{"location":"mumbai"}
    - action_weather
    - slot{"location":"mumbai"}
* goodbye
    - utter_goodbye
## Story004
* greet
    - utter_greet
* inform
    - utter_ask_location
* inform{"location":"lucknow"}
    - slot{"location":"lucknow"}
    - action_weather
    - slot{"location":"lucknow"}
* goodbye
    - utter_goodbye

