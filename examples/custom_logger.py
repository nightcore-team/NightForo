import asyncio
import json
import logging
import os
from datetime import datetime

from nightforo import Client, LoggerData


class JSONFormatter(logging.Formatter):
    def format(self, record: logging.LogRecord) -> str:

        log_entry = {
            "timestamp": datetime.now().isoformat(),
            "level": record.levelname,
            "logger": record.name,
            "message": record.getMessage(),
            "module": record.module,
            "function": record.funcName,
            "line": record.lineno,
        }
        if record.exc_info:
            log_entry["exception"] = self.formatException(record.exc_info)
        return json.dumps(log_entry, ensure_ascii=False)


async def main():
    token = os.getenv("API_KEY")
    if token is None:
        raise Exception("No api key found")

    data = LoggerData(
        level=logging.DEBUG, root=True, formatter=JSONFormatter()
    )

    Client(token, logger_data=data)


if __name__ == "__main__":
    asyncio.create_task(main())
