import os
from dotenv import load_dotenv
import dearpygui.dearpygui as dpg
import requests

load_dotenv()

TOKEN = os.getenv("TOKEN")

def searchSong():
    searchQuery = dpg.get_value("search_box")
    base_url = "https://api.genius.com"
    headers = {'Authorization': 'Bearer ' + TOKEN}
    search_url = base_url + "/search"
    data = {'q': searchQuery}
    response = requests.get(search_url, data=data, headers=headers)
    json = response.json()

    print(f'json response: {json}')

def main():
    dpg.create_context()
    dpg.create_viewport(height=800, width=600)
    dpg.setup_dearpygui()

    with dpg.window(tag="Lyrical"):
        dpg.add_text("Hello, lyrical")
        dpg.add_text("Search for a song")
        # dpg.add_button(label="Save", callback=save_callback)
        dpg.add_input_text(tag="search_box")
        # dpg.add_slider_float(label="Float")
        dpg.add_button(label="Search", tag="search-btn", callback=searchSong)

    dpg.show_viewport()
    dpg.set_primary_window("Lyrical", True)
    dpg.start_dearpygui()
    dpg.destroy_context()

if __name__ == "__main__":
    main()