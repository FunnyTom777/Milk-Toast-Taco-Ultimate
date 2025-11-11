import dearpygui.dearpygui as dpg # type: ignore

money = 500
strmoney = f"${money}"
manualopen = False

def on_key_press(sender, app_data):
    # app_data gives you the key code number
    if app_data == dpg.mvKey_F10:
        global manualopen
        if manualopen == True:
            manualopen = False
        elif manualopen == False:
            manualopen = True
        else:
            print("Error")
        print("Manual Toggled!! :D")

def openmanual():
    with dpg.window(label="MTT Manual"):
        dpg.add_text("Welcome to the MTT manual! where you can get a small idea of whats going on in MTT!")
        dpg.add_text(":D")


dpg.create_context()
dpg.create_viewport(title='Milk Toast Taco', width=600, height=300)

with dpg.window(label="Welcome To Milk Toast Taco!"):
    dpg.add_text("Heres how much Money You have: " + strmoney)
    dpg.add_text("Good luck with the chaos! (Tip: you can press F10 to open the manual at any time :D)")

# Add a key handler for F10
with dpg.handler_registry():
    dpg.add_key_press_handler(callback=on_key_press)

dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()
