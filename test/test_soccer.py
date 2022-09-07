import pytest
# import testapp as app


@pytest.fixture(params=['nodict', 'dict'])
def generate_initial_transform_parameters(request):
    pass
