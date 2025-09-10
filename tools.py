

from langchain_core.tools import tool
from langchain_community.utilities.wikipedia import WikipediaAPIWrapper
import os
import requests

# Tool to get current weather for a given location using WeatherAPI
@tool
def get_current_weather(location: str) -> str:
    """
    Get the current weather for a specific city.

    Args:
        location (str): The name of the city (e.g., "Karachi", "London", "New York").

    Returns:
        str: A short weather report with temperature (°C), feels-like temperature, and humidity.

    Example:
        "The current temperature in Karachi is 32°C, feels like 35°C, with 60% humidity."
    """
    API_KEY = os.environ["WEATHER_API_KEY"]  # Get API key from environment variable
    if not API_KEY:
        raise ValueError("WEATHER_API_KEY environment variable not set")
    try:
        # Build API request URL
        page = f"https://api.weatherapi.com/v1/current.json?key={API_KEY}&q={location}&aqi=no"
        url = requests.get(page)
        url.raise_for_status()  # Raise error if request failed
        weather_data = url.json()  # Parse JSON response
        # Format and return weather information
        return f"The current temperature in {location} is {weather_data['current']['temp_c']}°C , feelslike {weather_data['current']['feelslike_c']}°C, humidity {weather_data['current']['humidity']}"
    except Exception as e:
        # Return error message if something goes wrong
        return f"Could not retrieve weather data for {location}"                                            

# Tool to get top 3 news headlines for a given region or topic using NewsAPI
@tool
def get_news_headlines(region: str) -> str:
    """
    Fetch the latest news headlines related to a given region or topic.

    Args:
        region (str): The name of the region, city, country, or topic of interest 
                      (e.g., "Pakistan", "technology", "New York").

    Returns:
        str: A formatted string containing the top 3 recent news headlines with their descriptions and source of news.
             Each headline is numbered for readability.

    Example:
        Input: "Pakistan"
        Output:
            1- (BBC) Pakistan announces new economic reforms. The government introduced measures to stabilize inflation.

            2- (Reuters) Cricket team prepares for upcoming series. Players are in training camp ahead of the tournament.

            3- (Al Jazeera) Major tech conference held in Islamabad. Industry leaders discuss AI and digital transformation.
    """
    API_KEY = os.environ["NEWS_API_KEY"]  # Get API key from environment variable
    if not API_KEY:
        raise ValueError("NEWS_API_KEY environment variable not set")
    
    try:
        # Build API request URL
        page = f"https://newsapi.org/v2/everything?q={region}&apiKey={API_KEY}"
        url = requests.get(page)
        url.raise_for_status()  # Raise error if request failed
        news_data = url.json()  # Parse JSON response
        articles = news_data.get("articles", [])[:3]  # Get top 3 articles
        if not articles:
            return f"No news articles found for region: {region}"
        headlines = []
        # Format each article's headline, description, and source
        for idx, article in enumerate(articles, 1):
            source = article['source']['name']
            title = article['title']
            desc = article.get('description', "")
            headlines.append(f"{idx}- ({source}) {title}. {desc}")

        return "\n\n".join(headlines)
    except Exception as e:
        # Return error message if something goes wrong
        return f"Could not retrieve news for topic: {region}"

# Tool to get a summary of a topic from Wikipedia
@tool
def get_info_from_wikipedia(info: str) -> str:
    """Get information on a given topic from wikipedia"""
    try:
        wiki = WikipediaAPIWrapper(top_k_results=1)   # Create Wikipedia API wrapper
        result = wiki.run(info)  # Query Wikipedia for the topic
        return f"Here is some information from wikipedia on {info}: {result}"
    except Exception as e:
        # Return error message if something goes wrong
        return f"Could not retrieve information on {info}. Error: {e}"