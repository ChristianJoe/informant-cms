import json
import os
from enum import Enum

import requests

from ..models.genre import Genre

TOKEN = os.environ.get('DIALOGFLOW_DEV_TOKEN')

GET, POST, PUT, DELETE = range(4)


class Entity(Enum):
    GENRES = 'genres'
    TAGS = 'tags'


def api_call(endpoint, *, id='', attribute=None, params=None, data=None, method=GET):
    """
    Makes a call to the Dialogflow API
    :param endpoint: API endpoint (eg. 'intents')
    :param id: The UUID of an API object
    :param attribute: The attribute you want to access ('entries' in '/entities/{id}/entries')
    :param params: Additional parameters you want to pass. By default, 'v' and 'lang' are passed.
    :param data: JSON-serializable data to be sent
    :param method: Can be GET (querying objects), POST (adding objects) or PUT (update objects)
    :return:
    """

    if TOKEN is None:
        raise Exception(f'DIALOGFLOW_DEV_TOKEN is not set in environment.')

    if not params:
        params = {}

    params['v'] = '20150910'
    params['lang'] = 'de'

    params_url = '&'.join(f'{k}={v}' for k, v in params.items())
    url = f'https://api.dialogflow.com/v1/{endpoint}'

    if id:
        url += f'/{id}'

    if attribute:
        url += f'/{attribute}'

    url += f'?{params_url}'

    headers = {
        'Authorization': f'Bearer {TOKEN}',
        'Content-Type': 'application/json',
    }

    methods = {
        GET: requests.get,
        POST: requests.post,
        PUT: requests.put,
        DELETE: requests.delete,
    }

    the_method = methods[method]

    if data is not None:
        data = json.dumps(data)

    r = the_method(url, headers=headers, data=data)

    if r.status_code == 200:
        return r.json()

    else:
        raise ValueError(f'Loading URL {url} failed with code {r.status_code}')


def get_entity_uuid(entity: Entity):
    entities = api_call('entities')

    for e in entities:
        if e['name'] == entity.value:
            return e['id']


def add_entry(entry, entity, optional=False):
    if TOKEN is None and optional:
        return

    uuid = get_entity_uuid(entity)
    data = [
        {
            "synonyms": [
                entry,
            ],
            "value": entry,
        },
    ]

    return api_call('entities', id=uuid, attribute='entries', data=data, method=POST)


def delete_entry(entry, entity, optional=False):
    if TOKEN is None and optional:
        return

    uuid = get_entity_uuid(entity)
    data = [
      entry
    ]

    return api_call('entities', id=uuid, attribute='entries', data=data, method=DELETE)


def update_tags():
    from ..models.tag import ReportTag
    tags = ReportTag.objects.all()
    tag_uuid = get_entity_uuid(Entity.TAGS)
    existing_tags = [
        entry['value']
        for entry in
        api_call('entities', id=tag_uuid)['entries']
    ]

    data = []
    for tag in tags:
        if not tag.name in existing_tags:
            data.append({"value": tag.name})
        
    return api_call('entities', id=tag_uuid, attribute='entries', data=data, method=POST)


def update_genres():
    genres = Genre.objects.all()
    gerne_uuid = get_entity_uuid(Entity.GENRES)
    existing_genres = [
        entry['value']
        for entry in
        api_call('entities', id=gerne_uuid)['entries']
    ]

    data = []
    for genre in genres:
        if not genre.name in existing_genres:
            data.append({"value": genre.name})

    return api_call('entities', id=gerne_uuid, attribute='entries', data=data, method=POST)
