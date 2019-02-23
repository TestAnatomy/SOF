import PySimpleGUI as Sg
import pyautogui



screenshot_layout = [[Sg.ReadButton("", key="grab_image_in")],
                                 [Sg.Graph(canvas_size=(50, 50), key ="ss",
                                           drag_submits=True,
                                           background_color=None,
                                           graph_top_right=(50, 50),
                                           graph_bottom_left=(0, 0))
                                    ]]

screenshotWindow = Sg.Window('Test Anatomy - Build',
                                         background_color=None,
                                no_titlebar=True, grab_anywhere=True,
                                         resizable=True,
                                auto_size_text=True, alpha_channel=0.1,
                                         return_keyboard_events=True,
                                         size=(70, 70),
                                         keep_on_top=True).Layout(
                                            screenshot_layout).Finalize()
while True:
    b_screenshot_window, values_screenshot_window = screenshotWindow.Read(timeout=0)

    if b_screenshot_window == 'Exit' or b_screenshot_window is None:
        screenshotWindow_active = False
        screenshotWindow.Close()

    if b_screenshot_window != Sg.TIMEOUT_KEY:
        #  print("Screenshot Capture Position: ", b_screenshot_window,
        # values_screenshot_window)
        saveXY = values_screenshot_window
        print(saveXY["ss"][0], saveXY["ss"][1])
        print(screenshotWindow.CurrentLocation())
        ss_win_loc = screenshotWindow.CurrentLocation()

    if b_screenshot_window == "s":
        ss_name = Sg.PopupGetText("Name your screenshot element: ")
        ss_take = pyautogui.screenshot("{}.png".format(ss_name),
                                               region=(ss_win_loc[0] + 20,
                                                       ss_win_loc[1] + 20,
                                                       50, 50))
