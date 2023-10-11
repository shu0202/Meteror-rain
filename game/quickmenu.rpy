screen rightmenu :
    modal True
    add "gui/overlay/confirm.png"
    vbox :
        style_prefix "right"
        xcenter 0.93
        yalign 0.3
        imagebutton auto "blue_%s.png" action ShowMenu('history')
        imagebutton auto "red_%s.png" action ShowMenu('save')
        imagebutton auto "nblue_%s.png" action ShowMenu("load")
        imagebutton auto "green_%s.png" action QuickSave()
        imagebutton auto "purple_%s.png" action QuickLoad()
        imagebutton auto "brown_%s.png" action ShowMenu('preferences')
        imagebutton auto "pink_%s.png" action MainMenu(confirm=True)
        imagebutton auto "black_%s.png" action Hide('rightmenu',dissolve)
