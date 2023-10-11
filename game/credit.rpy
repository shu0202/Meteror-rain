label credits:
    play music "cminor.mp3" loop
    $ renpy.block_rollback()
    $ credits_speed = 100 #scrolling speed in seconds
    scene black #replace this with a fancy background
    show ending
    show text "{color=#ffffff}{size=40}企劃" :
        xalign 0.5
        yalign 0.2
    with dissolve
    show cohere_w :
        xalign 0.52
        yalign 0.5
    with dissolve
    pause 3.0
    hide cohere_w
    with dissolve
    hide text
    with dissolve
    pause 0.5
    show cred at Move((0.5, 1.0), (0.5, -6.0), credits_speed, repeat=False, bounce=False, xanchor=0.5, yanchor=0)
    with Pause(credits_speed+2)
    stop music fadeout 1.0
    show thanks:
        yanchor 0.5 ypos 0.5
        xanchor 0.5 xpos 0.5
    with dissolve
    with Pause(3)
    hide thanks
    return

init python:
    credits = ('{color=#ffffff}監督', '{color=#ffffff}楊修\nRayMond'), ('{color=#ffffff}劇本監督', '{color=#ffffff}Taku\nJay Chow\n賢王'), ('{color=#ffffff}劇本修正', '{color=#ffffff}Fox\n楊修\nRayMond\nWang'), ('{color=#ffffff}人物設計', '{color=#ffffff}RayMond'), ('{color=#ffffff}作畫', '{color=#ffffff}RayMond'), ('{color=#ffffff}背景', '{color=#ffffff}楊修\nRayMond\nTaku\n賢王'), ('{color=#ffffff}程式設計', '{color=#ffffff}楊修\nFox\nTaku'), ('{color=#ffffff}音樂總監', '{color=#ffffff}Wang') ,( '{color=#ffffff}背景音樂', '{color=#ffffff}YouTube音效庫') , ('{color=#ffffff}圖像處理', '{color=#ffffff}RayMond\n楊修') , ('{color=#ffffff}混音', '{color=#ffffff}楊修\nWang') , ('{color=#ffffff}背景處理', '{color=#ffffff}楊修') , ('{color=#ffffff}演出總監', '{color=#ffffff}楊修') , ('{color=#ffffff}演出修正', '{color=#ffffff}RayMond') , ('{color=#ffffff}攝影', '{color=#ffffff}RayMond\n賢王\nTaku') , ('{color=#ffffff}作畫監督', '{color=#ffffff}RayMond') , ('{color=#ffffff}美術', '{color=#ffffff}RayMond') , ('{color=#ffffff}人物設定', '{color=#ffffff}Jay Chow\nTaku\n賢王') , ('{color=#ffffff}團隊召集', '{color=#ffffff}Taku\nFox\n楊修')
    credits_s = "{size=50}{color=#ffffff}Cast\n\n"
    c1 = ''
    for c in credits:
        if not c1==c[0]:
            credits_s += "\n{size=40}" + c[0] + "\n"
        credits_s += "{size=30}" + c[1] + "\n"
        c1=c[0]
    credits_s += "\n{size=40}{color=#ffffff}Engine\n{size=30}{color=#ffffff}Ren'py\n7.3.0.271" #Don't forget to set this to your Ren'py version

init:
    image cred = Text(credits_s, text_align=0.5)
    image thanks = Text("{size=80}{color=#ffffff}Thanks for Playing!", text_align=0.5)
