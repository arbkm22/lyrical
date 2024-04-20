import dearpygui.dearpygui as dpg

def save_callback():
    print("Save clicked")

def main():
    dpg.create_context()
    dpg.create_viewport(height=800, width=600)

    dpg.setup_dearpygui()

    with dpg.window(label="Lyrical"):
        dpg.add_text("Hello, lyrical")
        dpg.add_button(label="Save", callback=save_callback)
        dpg.add_input_text(label="String")
        dpg.add_slider_float(label="Float")

    dpg.show_viewport()
    dpg.start_dearpygui()
    dpg.destroy_context()

if __name__ == "__main__":
    main()