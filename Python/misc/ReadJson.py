import json
from pprint import pprint
from pandas.io.json import json_normalize


with open('TS20180419-205152') as json_data:
    data = json.load(json_data)
    sessions = json_normalize(json_data.json(), record_path='sessions')

# result = json_normalize(data, 'sessions', ['sessions', 'notes',
# ...                                           ['shots', 'x']])

sessions = json_normalize(data.json(), record_path='sessions')
sessions.head()

# print(result)



# df = pd.DataFrame(data['TS20180419-205152'])

# View the first ten rows
# df.head(10)