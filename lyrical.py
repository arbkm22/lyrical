import os
from dotenv import load_dotenv
import dearpygui.dearpygui as dpg
import requests
import aiohttp
import asyncio
import threading

load_dotenv()

TOKEN = os.getenv("TOKEN")

async def searchSong():
    search_query = dpg.get_value("search_box")
    print('searchQuery: ', search_query)
    base_url = "https://api.genius.com"
    headers = {'Authorization': 'Bearer ' + TOKEN}
    search_url = base_url + "/search"
    data = {'q': search_query}
    async with aiohttp.ClientSession() as session:
        async with session.get(search_url) as resp:
            search_result = await resp.json()
            print(search_result)
    
    # response = requests.get(search_url, data=data, headers=headers)
    # json = response.json()
    # print(f'json response: {json}')
    


def main():
    dpg.create_context()
    dpg.create_viewport(height=800, width=600)
    dpg.setup_dearpygui()

    with dpg.font_registry():
        josefine_font = dpg.add_font("./resources/fonts/JosefinSans.ttf", 20)

    with dpg.window(tag="Lyrical"):
        dpg.bind_font(josefine_font)
        dpg.add_text("Hello, lyrical")
        dpg.add_text("Search for a song")
        dpg.add_input_text(tag="search_box")
        dpg.add_button(label="Search", tag="search-btn", callback=searchSong)


    dpg.show_viewport()
    dpg.set_primary_window("Lyrical", True)
    dpg.start_dearpygui()
    dpg.destroy_context()

    asyncio.run(searchSong)

if __name__ == "__main__":
    main()