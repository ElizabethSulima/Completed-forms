from typing import AsyncIterator

import pytest
from fastapi import status
from httpx import ASGITransport, AsyncClient

import api


pytestmark = pytest.mark.anyio


@pytest.fixture(scope="package")
def anyio_backend():
    return "asyncio"


@pytest.fixture(name="client")
async def client_fixture() -> AsyncIterator[AsyncClient]:
    """
    TestClient for FastAPI
    """
    # pylint: disable=C0301

    async with AsyncClient(
        transport=ASGITransport(app=api.apps), base_url="http://test"  # type: ignore
    ) as ac:
        yield ac


@pytest.mark.parametrize(
    "data, status_code, response_text",
    (
        (
            {
                "date": "2024-08-12",
                "phone": "+7 455 714 77 11",
                "text": "Любой текст",
            },
            status.HTTP_200_OK,
            "name 3",
        ),
        (
            {
                "date": "202408-12",
                "phone": "+7 455 714 77 11",
                "text": "Любой текст",
            },
            status.HTTP_404_NOT_FOUND,
            {
                "date": "202408-12",
                "phone": "+7 455 714 77 11",
                "text": "Любой текст",
            },
        ),
    ),
)
async def test_form_templates(
    client: AsyncClient, data, status_code, response_text
):
    response = await client.post("/get_form/", json=data)
    assert response.status_code == status_code
    assert response.json()["template"] == response_text
