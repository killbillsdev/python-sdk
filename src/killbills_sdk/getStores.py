import requests

def get_stores(env, api_key):
    
    if not env or env == '' or env is None:
        raise ValueError('No environment specified')
    if not api_key:
        raise ValueError('No API key provided')

    base_url = f'https://w.{"killbills.co" if env == "prod" else f"{env}.killbills.dev"}/stores'
    headers = {'Authorization': api_key}

    response = requests.get(base_url, headers=headers)
    if 'error' in response.json() :
        raise ValueError(f'Error: {response.status_code} - {response.text}')
    return response.json().get('items')

