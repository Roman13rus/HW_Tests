import requests
import os
from dotenv import load_dotenv
import json


class LoaderYD:  #Класс для загрузки фото на яндекс диск
    def __init__(self, token_YD):
        self.token_YD = token_YD
    
    def get_headers(self): # метод получения headers для запросов к api яндекс
        return {
            'Content-Type': 'application/json',
            'Authorization': 'OAuth {}'.format(self.token_YD)
        }
    
    def put_upload_field(self, name_field):  #метод создания папки для закладки фото на Яндекс Диске
        upload_url = "https://cloud-api.yandex.net/v1/disk/resources"
        headers = self.get_headers()
        params = {"path": name_field, "fields":name_field}
        response = requests.put(upload_url, headers=headers, params=params)
        return response
    def get_objects_in_YD(self, path):
        upload_url = "https://cloud-api.yandex.net/v1/disk/resources"
        headers = self.get_headers()
        params = {"path": path}
        response = requests.get(upload_url, headers=headers, params=params)
        return response
    
# if __name__ == "__main__":
#     load_dotenv()
#     put_folder = LoaderYD(os.getenv('TOKEN'))
#     put_folder._put_upload_field('My_tests_folder').status_code
#     put_folder.get_objects_in_YD('My_tests_folder').status_code


    