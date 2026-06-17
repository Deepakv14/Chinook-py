from pydantic import BaseModel

class ArtistRevenue(BaseModel):
    artist_name: str
    total_revenue: float

class CountrySales(BaseModel):
    country: str
    total_sales: float    

class CustomerCount(BaseModel):
    country: str
    customer_count: int

class TrackInfo(BaseModel): 
    track_name: str
    album_title: str
    artist_name: str
    unit_price: float
            