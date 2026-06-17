import asyncio
from module1 import async_top_artists, async_country_sales, async_customers_by_country, async_top_expensive_tracks

async def main():
    artits, country_sales, customers_by_country, top_expensive_tracks = await asyncio.gather(
        async_top_artists(),
        async_country_sales(),  
        async_customers_by_country(),
        async_top_expensive_tracks()
    )

    # print("\nTop 5 Artists by Revenue:")   
    # for artist in artits:
    #     print(f"{artist.artist_name}: ${artist.total_revenue:.2f}")

    # print("\nSales by Country:")
    # for country in country_sales:   
    #     print(f"{country.country}: ${country.total_sales:.2f}")

    # print("\nCustomers by Country:")
    # customer_count = customers_by_country
    # print(f"{customer_count.country}: {customer_count.customer_count} customers")

    print("\nTop Expensive Tracks:")
    for track in top_expensive_tracks:
        print(f"{track.track_name} - {track.album_title} by {track.artist_name}: ${track.unit_price:.2f}")

if __name__ == "__main__":
    asyncio.run(main())
