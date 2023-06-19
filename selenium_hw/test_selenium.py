from main import autorization_in_yandex
import pytest
class TestAutorization:
    def test_yandex_autorization(self):
        expection_result = "Яндекс ID"
        assert autorization_in_yandex() == expection_result
if __name__ == "__main__":
    pytest.main()