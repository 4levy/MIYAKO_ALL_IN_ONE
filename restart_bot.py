import os
import sys
import asyncio

async def restart_bot():
    print("Restarting bot...")
    os.execv(sys.executable, [sys.executable, "main.py"])

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(restart_bot())