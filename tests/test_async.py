import pytest_asyncio


@pytest_asyncio.fixture
async def async_example_fixture():
    await pytest_asyncio.sleep(1)
    yield


@pytest_asyncio.fixture
async def test_async_example(async_example_fixture):
    pass
