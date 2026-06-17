import sqlite3
from queries import (get_top_artists, get_sales_by_country, get_customers_by_country, get_top_expensive_tracks)
import asyncio
from providers.factory import LLMFactory
from dotenv import load_dotenv


import os

load_dotenv()

gemini_api_key = os.getenv("GEMINI_API_KEY")

if gemini_api_key is None:
    raise ValueError("GEMINI_API_KEY not found")


DB_PATH = "Chinook.db"
async def async_top_artists():
    return await asyncio.to_thread(
        get_top_artists,
        DB_PATH,
    )


async def async_country_sales():
    return await asyncio.to_thread(
        get_sales_by_country,
        DB_PATH,
    )

    
async def async_customers_by_country():
    return await asyncio.to_thread(
        get_customers_by_country,
        DB_PATH,
        "USA",
    )    

async def async_top_expensive_tracks():
    return await asyncio.to_thread(
        get_top_expensive_tracks,
        DB_PATH,
    )    

    
llm = LLMFactory.create(
    provider="google-studio",
    api_key=gemini_api_key,
    model="gemini-2.5-flash"
)    

# response = llm.generate_text("Who won FIFA last edition?? ")
response = llm.generate_text("Coffe Shops near me")
print(response)