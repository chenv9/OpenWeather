import json, requests, sys
import pprint

api_key = 'Api-key'


if len(sys.argv) < 2:
    print('Enter city name')
    sys.exit()
location = ','.join(sys.argv[1:])



url = 'http://api.openweathermap.org/data/2.5/forecast?q=' + location +'&appid='+api_key
response = requests.get(url)
response.raise_for_status()


file = json.loads(response.text)
w = file['list']
print('Today:')
print('Min Temp: ' +str(round((w[0]['main']['temp_min'] - 273.13) * (9/5) + 32, 2))+ ' Max Temp: ' +str(round((w[0]['main']['temp_max'] - 273.13) * (9/5) + 32, 2)))
print(w[0]['weather'][0]['main'] + ' - '+ w[0]['weather'][0]['description'] )
print()
print('Day 1:')
print('Min Temp: ' +str(round((w[1]['main']['temp_min'] - 273.13) * (9/5) + 32, 2))+ ' Max Temp: ' +str(round((w[1]['main']['temp_max'] - 273.13) * (9/5) + 32, 2)))
print(w[1]['weather'][0]['main'], '-', w[1]['weather'][0]['description'])
print()
print('Day 2:')
print('Min Temp: ' +str(round((w[2]['main']['temp_min'] - 273.13) * (9/5) + 32, 2))+ ' Max Temp: ' +str(round((w[2]['main']['temp_max'] - 273.13) * (9/5) + 32, 2)))
print(w[2]['weather'][0]['main'], '-', w[2]['weather'][0]['description'])
print('\nDay 3:')
print('Min Temp: ' +str(round((w[3]['main']['temp_min'] - 273.13) * (9/5) + 32, 2))+ ' Max Temp: ' +str(round((w[3]['main']['temp_max'] - 273.13) * (9/5) + 32, 2)))
print(w[3]['weather'][0]['main'], '-', w[3]['weather'][0]['description'])
print('\nDay 4:')
print('Min Temp: ' +str(round((w[4]['main']['temp_min'] - 273.13) * (9/5) + 32, 2))+ ' Max Temp: ' +str(round((w[4]['main']['temp_max'] - 273.13) * (9/5) + 32, 2)))
print(w[4]['weather'][0]['main'], '-', w[4]['weather'][0]['description'])
print('\nDay 5:')
print('Min Temp: ' +str(round((w[5]['main']['temp_min'] - 273.13) * (9/5) + 32, 2))+ ' Max Temp: ' +str(round((w[5]['main']['temp_max'] - 273.13) * (9/5) + 32, 2)))
print(w[5]['weather'][0]['main'], '-', w[5]['weather'][0]['description'])

