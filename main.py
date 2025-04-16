# main.py
import asyncio
from bot import send_signal
from signal_generator import generate_signal

async def main():
    pair = 'EURUSD=X'  # EUR/USD pair
    signal = generate_signal(pair)
    await send_signal(signal)

# কল করো asyncio
import nest_asyncio
nest_asyncio.apply()

asyncio.run(main())
