import PySimpleGUI as Sg
import pyautogui

ss_window_x = 70
ss_window_y = 70

screenshotWindow_active = False

main_layout = [[Sg.Button("Screenshot Go", key="grab_image")]]
main_window = Sg.Window("Screenshot Tool").Layout(main_layout).Finalize()

while True:
    b, v = main_window.Read(timeout=0)

    if b == "grab_image":
        screenshot_layout = [[  # Sg.ReadButton("",
            #       image_data=TestAnatomy_images.camera,
            #       key="grab_image_in")],
            Sg.Graph(canvas_size=(50, 50), key="ss",
                     drag_submits=True,
                     background_color="blue",
                     graph_top_right=(ss_window_x - 20,
                                      ss_window_y - 20),
                     graph_bottom_left=(0, 0))
        ]]

        screenshotWindow = Sg.Window('Test Anatomy - Build',
                                     background_color="blue",
                                     no_titlebar=False, grab_anywhere=True,
                                     resizable=True,
                                     auto_size_text=True, alpha_channel=0.1,
                                     return_keyboard_events=True,
                                     size=(ss_window_x, ss_window_y),
                                     keep_on_top=True).Layout(
                screenshot_layout).Finalize()

        print(screenshotWindow.Size)

        screenshotWindow_active = True

    if screenshotWindow_active:
        b_screenshot_window, values_screenshot_window = screenshotWindow.Read(
            timeout=0)

        if b_screenshot_window == 'Exit' or b_screenshot_window is None:
            screenshotWindow_active = False
            screenshotWindow.Close()

        if b_screenshot_window != Sg.TIMEOUT_KEY and screenshotWindow_active:
            #  print("Screenshot Capture Position: ", b_screenshot_window,
            # values_screenshot_window)
            saveXY = values_screenshot_window
            print(saveXY["ss"][0], saveXY["ss"][1])
            print(screenshotWindow.CurrentLocation())
            ss_win_loc = screenshotWindow.CurrentLocation()
            # print(screenshotWindow.Size()[0])

        if b_screenshot_window == "e":
            ss_name = Sg.PopupGetText("Name your screenshot element: ")
            screenshotWindow.Hide()
            ss_take = pyautogui.screenshot("{}.png".format(ss_name),
                                           region=(ss_win_loc[0] + 5,
                                                   ss_win_loc[1] - 10,
                                                   screenshotWindow.Size[0],
                                                   screenshotWindow.Size[1]))
            screenshotWindow.Close()
            screenshotWindow_active = False

    if b is None:
        break

    else:
        pass
