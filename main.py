import dearpygui.dearpygui as dpg

dpg.create_context()


def init(sender, app_data, user_data):
    what = dpg.get_value(user_data[0])
    where = dpg.get_value(user_data[1])
    print(what, '/', where)


with dpg.window(tag="root"):
    
    what = dpg.add_input_text(default_value="What?")
    dpg.add_button(label="Set What", callback=lambda: dpg.show_item("file_dialog_id"))
    where = dpg.add_input_text(default_value="Where?")
    dpg.add_button(label="Set Where", callback=lambda: dpg.show_item("file_dialog_id"))
    dpg.add_button(label="Init", callback=init, user_data=[what, where])
    

dpg.create_viewport(title='sdjfldsf', width=600, height=800)
dpg.setup_dearpygui()
dpg.show_viewport()
dpg.set_primary_window("root", True)


dpg.start_dearpygui()

dpg.destroy_context()