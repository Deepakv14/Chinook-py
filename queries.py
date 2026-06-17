import sqlite3
from models import ArtistRevenue, CountrySales, CustomerCount, TrackInfo

# Find the top 5 artists by total revenue
def get_top_artists(db_path:str, limit:int=5) -> list[ArtistRevenue]:
    
    with sqlite3.connect(db_path) as conn:
        cursor = conn.cursor()
        
        query = """
        SELECT Artist.Name, SUM(Invoice.Total) AS TotalRevenue
        FROM Artist
        JOIN Album ON Artist.ArtistId = Album.ArtistId
        JOIN Track ON Album.AlbumId = Track.AlbumId
        JOIN InvoiceLine ON Track.TrackId = InvoiceLine.TrackId
        JOIN Invoice ON InvoiceLine.InvoiceId = Invoice.InvoiceId
        GROUP BY Artist.ArtistId
        ORDER BY TotalRevenue DESC
        LIMIT ?;
        """
        
        results = cursor.execute(query, (limit,)).fetchall()
        
        return [ArtistRevenue(artist_name=row[0], total_revenue=row[1]) for row in results]

# Find total sales by country
def get_sales_by_country(db_path:str) -> list[CountrySales]:
    with sqlite3.connect(db_path) as conn:
        cursor = conn.cursor()
        
        query = """
        SELECT Customer.Country, SUM(Invoice.Total) AS TotalSales
        FROM Customer
        JOIN Invoice ON Customer.CustomerId = Invoice.CustomerId
        GROUP BY Customer.Country
        ORDER BY TotalSales DESC;
        """
        
        results = cursor.execute(query).fetchall()
        
        return [CountrySales(country=row[0], total_sales=row[1]) for row in results]


# Find the number of customers in each country
def get_customers_by_country(db_path: str, country: str) -> CustomerCount:
    with sqlite3.connect(db_path) as conn:
        cursor = conn.cursor()

        query = """
        SELECT Country, COUNT(*) AS CustomerCount
        FROM Customer
        WHERE Country = ?
        GROUP BY Country;"""

        row = cursor.execute(query, (country,)).fetchone()

        if row is None:
            return CustomerCount(country=country, customer_count=0)
        return CustomerCount(country=row[0], customer_count=row[1])


# Find the top 10 most expensive tracks
def get_top_expensive_tracks(db_path:str, limit:int=10) -> list[TrackInfo]:
    with sqlite3.connect(db_path) as conn:
        cursor = conn.cursor()

        query="""
        SELECT Track.Name, Album.Title, Artist.Name, Track.UnitPrice 
        FROM Track
        JOIN Album ON Track.AlbumId = Album.AlbumId
        JOIN Artist ON Album.ArtistId = Artist.ArtistId
        ORDER BY Track.UnitPrice DESC
        LIMIT ?;
        """

        results = cursor.execute(query, (limit,)).fetchall()

        return [TrackInfo(track_name=row[0], album_title=row[1], artist_name=row[2], unit_price=row[3]) for row in results]