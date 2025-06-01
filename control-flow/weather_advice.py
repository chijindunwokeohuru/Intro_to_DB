#!/usr/bin/env python3
"""
Weather Recommendation Program
This script provides clothing recommendations based on current weather conditions.
"""

def get_weather_recommendation():
    # Prompt user for weather input
    weather = input("What's the weather like today? (sunny/rainy/cold): ").lower()

    # Provide recommendations based on weather condition
    if weather == "sunny":
        print("Wear a t-shirt and sunglasses.")
    elif weather == "rainy":
        print("Don't forget your umbrella and a raincoat.")
    elif weather == "cold":
        print("Make sure to wear a warm coat and a scarf.")
    else:
        print("Sorry, I don't have recommendations for this weather.")
        
get_weather_recommendation()