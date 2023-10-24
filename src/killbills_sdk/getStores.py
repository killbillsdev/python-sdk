import requests

def get_stores(env, api_key, limit=100, offset=0):
    
    if not env or env == '' or env is None:
        raise ValueError('No environment specified')
    if not api_key:
        raise ValueError('No API key provided')

    base_url = f'https://w.{"killbills.co" if env == "prod" else f"{env}.killbills.dev"}/stores'
    headers = {'Authorization': api_key}
    params = {
        'limit': limit,
        'offset': offset
    }
    response = requests.get(base_url, headers=headers, params=params)
    if response.status_code != 200:
        raise ValueError(f'Error: {response.status_code} - {response.text}')
    return response.json()

