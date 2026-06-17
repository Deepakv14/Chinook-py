import sqlite3
from queries import (get_top_artists, get_sales_by_country, get_customers_by_country, get_top_expensive_tracks)
import asyncio

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