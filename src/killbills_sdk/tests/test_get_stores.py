import pytest
import os,time
from dotenv import load_dotenv
load_dotenv()

from getStores import get_stores

def test_get_stores_returns_list_of_dicts():
    env = 'dev'
    api_key = os.environ.get("TEST_API_KEY")
    result = get_stores(env, api_key)
    assert isinstance(result, list)
    for item in result:
        assert isinstance(item, dict)

def test_get_stores_returns_empty_when_nokey():
    env = 'dev'
    with pytest.raises(ValueError) as exc_info:
        print(get_stores(env, None))
    assert str(exc_info.value) == 'No API key provided'

def test_get_stores_returns_empty_when_noenv():
    api_key = "TEST_API_KEY"
    with pytest.raises(ValueError) as exc_info:
        print(get_stores(None, api_key))
    assert str(exc_info.value) == 'No environment specified'

def test_get_stores_returns_empty_when_wrongkey():
    env = 'dev'
    api_key = "TEST_API_KEY"
    with pytest.raises(ValueError) as exc_info:
        print(get_stores(env, api_key))
    assert str(exc_info.value) == 'Error: 200 - {"error":"Invalid authorization header","e":{}}'