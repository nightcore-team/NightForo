import asyncio
import os

from nightforo import Client, ThreadGetParams


async def main():
    token = os.getenv("API_KEY")
    if token is None:
        raise Exception("No api key found")

    client = Client(token)

    example_thread_id = 123

    params = ThreadGetParams(with_posts=True)
    await client.get_thread(example_thread_id, params)


if __name__ == "__main__":
    asyncio.create_task(main())
