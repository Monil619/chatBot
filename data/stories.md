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
* goodbye
  - utter_goodbye

## say goodbye
* goodbye
  - utter_goodbye

## utter_default
* utter_default
  - action_default_fallback

## find_counsilor
* find_counsilor
  - utter_counsilor
  
## chitchat
* ask_builder OR ask_howdoing OR ask_languagesbot OR ask_howold OR ask_restaurant OR ask_time OR ask_wherefrom OR ask_whoami OR handleinsult OR telljoke OR ask_whatismyname
    - action_chitchat

## happy weather
* greet
  - utter_greet
* weather
  - utter_city
* city
  - action_weather_api
  
## about_OMN
* about_OMN_website
  - action_about_omn_website
  
## deny
* deny
  - utter_deny
  
## about_bot
* bot_name
  - utter_iamabot
  
## bot_complement
* complement
  - utter_noworries

## bot_training
* bot_training
    - utter_bot_training

## omn_services
* omn_services
    - utter_omn_services

## abt_rasa
* abt_rasa
    - utter_abt_rasa
