import requests
import datetime

today = datetime.datetime.now()
today_format = today.strftime('%Y%m%d')

USERNAME = "j-agbaje"
TOKEN = "kdjbdhdhdbsndnsdnndk"
GRAPH_ID = 'graph1'
pixela_url = 'https://pixe.la/v1/users'

user_params = {
    'token': TOKEN,
    'username': USERNAME,
    'agreeTermsOfService': 'yes',
    'notMinor': 'yes',
}

# response = requests.post(pixela_url, json=user_params)
# print(response.text)

graph_url = f"{pixela_url}/{USERNAME}/graphs"

graph_params = {
    'id': GRAPH_ID,
    'name': 'Bible Study Graph',
    'unit': 'chapter',
    'type': 'int',
    'color': 'ajisai',
}

headers = {
    'X-USER-TOKEN': TOKEN
}

# response = requests.post(graph_url, json=graph_params, headers=headers)
# print(response.text)

post_pixel_url = f'{pixela_url}/{USERNAME}/graphs/{GRAPH_ID}'

post_params = {
    'date': today_format,
    'quantity': input('How many chapters did you read today?: '),
}

response = requests.post(post_pixel_url, json=post_params, headers=headers)
print(response.text)

update_pixel_url = f'{pixela_url}/{USERNAME}/graphs/{GRAPH_ID}/{today_format}'

update_params = {
    'quantity': input('How many chapters did you actually read today?: '),
}

response = requests.put(update_pixel_url, json=update_params, headers=headers)
print(response.text)

delete_pixel_url = f'{pixela_url}/{USERNAME}/graphs/{GRAPH_ID}/{today_format}'

# response = requests.delete(delete_pixel_url, headers=headers)
# print(response.text)
