import pytest
from fixture.application import Application


<<<<<<< HEAD:conftest.py
@pytest.fixture(scope='session')
=======
@pytest.fixture
>>>>>>> parent of e886393... Тесты на создание, модификацию и удаление групп и контактов:tests/conftest.py
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture
