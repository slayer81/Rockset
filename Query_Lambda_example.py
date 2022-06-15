from rockset import Client, ParamDict

# import os
# apiKey = os.environ.get('ROCKSET_APIKEY') # Needs reboot to activate
# apiKey = 'Avv93keLLBd2yQgDNShaVnJNPbZO4xhSDDvLQNojCvwIh2a9KXrwG88WplpNHSNO'
# rs = Client(api_key=apiKey, api_server='https://api.euc1a1.rockset.com')

# Below is the example code provided via the Quickstart Guide
# The reference to the api_key seems to be a Rockset-specific function
# ie: calling '$ENV_REF'
rs = Client(api_key='$ROCKSET_APIKEY',
          api_server='https://api.euc1a1.rockset.com')

# retrieve Query Lambda
qlambda = rs.QueryLambda.retrieve(
    'getRecommendedMovies',
    version='1f9ffc091014b427',
    workspace='commons')

params = ParamDict()
params['genre'] = "Action"
params['userId'] = "100"
results = qlambda.execute(parameters=params)
print(results)

