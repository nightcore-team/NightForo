import asyncio
import os

from nightforo import ArzGuardGroupsIdsEnum, Client


async def main():
    token = os.getenv("API_KEY")
    if token is None:
        raise Exception("No api key found")

    client = Client(token)

    user_id = -1

    response = await client.promote_user(
        user_id, ArzGuardGroupsIdsEnum.MODERATORS
    )

    print(response.success)


if __name__ == "__main__":
    asyncio.create_task(main())
