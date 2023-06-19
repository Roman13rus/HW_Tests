from yandex_disk import LoaderYD
import pytest
import os
import requests
from dotenv import load_dotenv


class TestYDFolders:
    put_folder = LoaderYD(os.getenv('TOKEN'))
    def test_put_folder_response(self): 
        """тест проверки работы функции  в момент создания папки. 
        """
        load_dotenv()
        exp_response_code = [201, 409]
        put_folder = LoaderYD(os.getenv('TOKEN'))
        real_response_code = put_folder.put_upload_field('My_tests_folder').status_code
        assert real_response_code in exp_response_code
        
    def test_field_in_YD(self):
        """тест проверки наличия папки на яндекс диске 
        """
        exp_response_code = 200
        load_dotenv()
        get_folders = LoaderYD(os.getenv('TOKEN'))
        result_code = get_folders.get_objects_in_YD('My_tests_folder').status_code
        assert result_code == exp_response_code
      

if __name__ == "__main__":
    pytest.main()