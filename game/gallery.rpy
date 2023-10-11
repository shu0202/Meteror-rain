init python:

    g = Gallery()

    g.button("1")
    g.condition("persistent.unlock_1")
    g.image("cg01")

    g.button("2")
    g.condition("persistent.unlock_2")
    g.image("cg02")

    g.button("3")
    g.condition("persistent.unlock_3")
    g.image("cg03_special")

    g.button("4")
    g.condition("persistent.unlock_4")
    g.image("cg04")



    g.transition = dissolve
screen gallery:

    tag menu

    #use game_menu(_("Extra")):

    hbox :
        spacing 150
        xalign 0.5
        yalign 0.2
        vbox :
            spacing 4.5
            add g.make_button("1","unlock2","locked1.png",hover_border="unlock2_hover",idle_border="unlock2_idle",xalign=0.5,yalign=0.5)
            text "cg01" :
                xalign 0.5
        vbox :
            spacing 5
            add g.make_button("2","unlock1","locked2.png","unlock_hover","unlock_idle",xalign=0.5,yalign=0.5)
            text "cg02" :
                xalign 0.5

    hbox :
        spacing 150
        xalign 0.5
        yalign 0.6
        vbox :
            spacing 4.5
            add g.make_button("3","unlock3","locked3.png","unlock3_hover","unlock3_idle",xalign=0.5,yalign=0.5)
            text "cg03" :
                xalign 0.5

        vbox :
            spacing 4.5
            add g.make_button("4","unlock4","locked4.png","unlock4_hover","unlock4_idle",xalign=0.5,yalign=0.5)
            text "cg04" :
                xalign 0.5
    hbox :
        xalign 0.9
        yalign 0.9
        textbutton _("返回"):
            style "return_button"

            action Return()
