from fastapi import FastAPI,Request
import httpx
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
import os
from dotenv import load_dotenv
from cachetools import TTLCache
load_dotenv()
api_key = os.getenv('API_KEY')
app =FastAPI()
cache = TTLCache(maxsize=100, ttl=100)
templates = Jinja2Templates(directory="templates")
@app.get("/")
async def news_api(request: Request):
    cache_key = "news_articles"
    if cache_key in cache:
            articles = cache[cache_key]
    else:
        async with httpx.AsyncClient() as client:
            
            response = await client.get(f"https://newsapi.org/v2/everything?q=keyword&apiKey={api_key}")
            response.raise_for_status()
            data = response.json()
            articles = data.get("articles", [])
            cache[cache_key] = articles
    return templates.TemplateResponse("index.html", {
        "request": request,
        "title": "Latest News",
        "articles": articles
    })
