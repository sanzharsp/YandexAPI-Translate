import requests
from dataclasses import dataclass
import os
import json
from os.path import join, dirname
from dotenv import load_dotenv
dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)



@dataclass
class Translate:
    url: str
    sourceLanguageCode: str
    targetLanguageCode: str
    texts: str or None
    headers: dict
    folderID: str


def post(translated_data: Translate) -> str:

    datas = {
        'sourceLanguageCode': translated_data.sourceLanguageCode,
        'targetLanguageCode': translated_data.targetLanguageCode,
        'texts': translated_data.texts,
        'folderId': translated_data.folderID
    }

    try:
        response = requests.post(translated_data.url, json=datas, headers=translated_data.headers)
    except Exception as e:
        return e
    return response.text



texts = """Данные не были переданы корректно"""

sourceLanguageCode = 'ru'
targetLanguageCode = 'kk'
headers = {'Authorization': 'Bearer {}'.format(os.environ.get('TOKEN'))}
data = Translate(os.environ.get('URLS'), sourceLanguageCode, targetLanguageCode, texts, headers, os.environ.get('FOLDERID'))


json_convert = json.loads(post(data))
print(json_convert['translations'][0]['text'])
