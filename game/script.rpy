transform goaway_left:
    on show:
        alpha 1.0
    on hide:
        linear 0.2 alpha 0.0
        linear 0.2 xoffset -20
        linear 0.1 alpha 0.0

transform floating:
    easein 0.1 yoffset -15
    easein 0.1 yoffset 15

init python :
    def eyewarp(x) :
        return x**1.33
    eye_open = ImageDissolve("eye.png", .5, ramplen=128, reverse=False, time_warp=eyewarp)
    eye_shut = ImageDissolve("eye.png", .5, ramplen=128, reverse=True, time_warp=eyewarp)

define cutin = CropMove(0.15, "wiperight")

#define wipe_normal = ImageDissolve("normal_wipe", 0.5) #custom soft-edge wipe
define wipe_normal = ImageDissolve("test_wipe_1", 0.3) #custom soft-edge wipe 2 for right to left
#define default way of showing a character
transform enter_from_right_hide:
    xoffset 50
transform enter_from_left_hide:
    xoffset -50
transform exit_left:
    linear 0.2 xoffset -50 alpha 0.0
transform exit_right:
    linear 0.2 xoffset 50 alpha 0.0
transform exit_none:
    linear 0.2 alpha 0.0
transform transparent:
    alpha 0.0
transform seen:
    linear 0.2 alpha 1.0 xoffset 0.0
transform showoffset:
    yoffset 100

transform alignx(value):
    xalign value

transform hikari_shock_offset:
    yoffset -880
    xoffset -10

init python:
    def show_default(character_name, xalign_num, enter):
        renpy.show(character_name)   
        renpy.show(character_name,at_list=[showoffset])
        renpy.show(character_name,at_list=[alignx(xalign_num)])
        renpy.show(character_name,at_list=[transparent])
        if enter == "L":
            renpy.show(character_name,at_list=[enter_from_left_hide])
        elif enter == "R":
            renpy.show(character_name,at_list=[enter_from_right_hide])
        renpy.show(character_name,at_list=[seen])
    def hide_default(character_name, exit_dir):
        if exit_dir == "L":
            renpy.show(character_name,at_list=[exit_left])
        elif exit_dir == "R":
            renpy.show(character_name,at_list=[exit_right])
        else:
            renpy.show(character_name,at_list=[exit_none])
    def show_shock(character):
        renpy.show("shock_animation",zorder=10)
        if character == "hk":
            renpy.show("shock_animation",at_list=[hikari_shock_offset])

transform VHS:
    shader "MakeVisualNovels.VHS"
    #Color applies a shift in color.
    #Remember R G B A.  Values are expressed between 0.0 and 1.0
    #See the bottom  of this document for a cheat sheet.
    #Use White vec4(1.0, 1.0, 1.0, 1.0) to disable this effect.
    #Pure black turns the entire image black.
    #u_color (0.5, 0.5, 0.5, 1.0)
    u_color (0.52, 0.39, 0.28, 1.0)

image shock_animation:
    "shock_effect"
    pause 0.3
    "shock_effect_1"
    pause 0.3
    repeat    
        

image speed:
    "comic speed1"
    pause 0.1
    "comic speed2"
    pause 0.1
    "comic speed3"
    pause 0.1
    "comic speed4"
    pause 0.1
    repeat

image battle:
    "battle1" with dissolve
    pause 2.0
    "battle2" with dissolve
    pause 2.0
    "battle3" with dissolve

image ending :
    "end" with dissolve
    pause 24.0
    "end1" with dissolve
    pause 2.0
    "end2" with dissolve
    pause 2.0
    "end3" with dissolve
    pause 16.0
    "end4" with dissolve
    pause 2.0
    "end5" with dissolve
    pause 2.0
    "end" with dissolve
    pause 2.0
    "end6" with dissolve
    pause 2.0
    "end7" with dissolve
    pause 18.0
    "end6" with dissolve
    pause 2.0
    "end" with dissolve
    pause 4.0
    "end8" with dissolve
    pause 2.0
    "end9" with dissolve
    pause 18.0
    "end8" with dissolve
    pause 2.0
    "end" with dissolve

image cg03_special :
    "cg03" with dissolve
    pause 5.0
    "cg03_3" with dissolve
    pause 5.0
    "cg03_4" with dissolve
    pause 5.0
    "cg03_5" with dissolve
    pause 5.0
    repeat

image cg02 :
    "cg02_1" with dissolve
    pause 5.0
    "cg02_2" with dissolve
    pause 5.0
    repeat

define hk_pts = 0
define s_pts = 0
define h_pts = 0

define h = Character('遙', color="#FFFFFF")
define k = Character('界', color="#FFFFFF")
define t = Character('司', color="#FFFFFF")
define kz = Character('和', color="#FFFFFF")
define hk = Character('光', color="#FFFFFF")
define s = Character('幸', color="#FFFFFF")

# 遊戲從這裡開始。
label start:
    stop music fadeout 1.0
    scene black
    with dissolve
    "有誰會想到命運會突然改變，令我在一瞬之間失去所有？{p}看似平凡的一天，其實並不是必然。"
    "我記得，那一天是我們一家人去海灘的日子。"
    show childhood1 at VHS
    with dissolve
    "爸爸媽媽在車頭駕著車，而我和妹妹就在後排並肩而坐。"
    "窗外的景色全是沿着山路便能看見的樹與海景。"
    "對於我們土生土長的人來說，並非新鮮的事物，因此亦沒有特別興奮。"
    "但是，能和家人一起去遊山玩水，也算是愉快的事。"
    "畢竟平日就只有我和遙在一起，父母兩人都要出去公幹。"
    "媽媽說，我們今天要去的地方是石澳沙灘，在我們的這區算是挺有名的景點。"
    "車內的空調吹著一縷縷涼快的風，與烈日當空的室外大相逕庭。"
    "不過，就這樣呆坐著有什麼好處呢？"
    "這種時候，當然要玩一下我們小學生的玩意了。"
    "想到這邊，我馬上轉身，目光尋找著妹妹的身影。"
    show childhood2_1 at VHS
    show childhood2_1:
        yoffset -75
    with dissolve
    hide childhood1
    "旁邊的妹妹安靜地坐於座位上，也會不時望向我。"
    k "「遙，要不要來玩遊戲呀？」"
    h "「嗯，是什麼遊戲呀？」"
    k "「哼 讓我想想。{p}\ \ \ 啊，有了。你猜猜看？」"
    h "「哥哥你別買關子啦！」"
    k "「哈哈，好吧。是小學的《麻芝菇》。」"
    h "「啊，我有跟司玩過！」"
    h "「他說讓我快點學玩，不然哥哥會拿來欺負我。」"
    k "「哈？司那傢伙，還真夠膽說我。{p}\ \ \ 明明自己對我也是那麼高傲的態度。」"
    h "「司對女生那麼溫柔，可能下輩子哥哥當女生就可以體會了吧～」"
    k "「哼，我當女生的話才不要司呢。{p}\ \ \ 這麼多話說，快點開始啦。」"
    h "「嗯，好呀。。。麻芝！」"
    k "「哦哦！我閃！{w}芝姑！」"
    h "「哈！沒事！{w}麻姑！」"
    "如是者，我與遙切磋了十餘回合。"
    "{color=#FFFFFF}媽媽{/color}" "「界，遙，我們還有15分鐘就到了。」"
    "{color=#FFFFFF}爸爸{/color}" "「哎，就讓孩子們好好玩耍吧～今天時間多的是呢。」"
    "坐在後排的我隱約看見，"
    "爸爸媽媽溫柔地笑了。"
    "那大概是我所見到，父母親最後的笑容。"
    k "「......啊，」"
    play sound "crash.mp3"
    show childhood2_1 :
        linear 0.2 yoffset 0
        linear 0.2 yoffset -150
        linear 0.1 yoffset 0
        linear 0.1 yoffset -150
        linear 0.1 yoffset 0
        linear 0.1 yoffset -150
        linear 0.1 yoffset -75
    pause 1.0
    hide childhood2_1
    stop sound fadeout 1.0
    k "「哇啊啊！！！」"
    hide childhood2_1
    show black
    "突然，我們的車受到巨大的震盪。我們遇上了車禍。"
    "「遙！！！」"
    show childhood3_1 at VHS
    show childhood3_1 :
        linear 5.0 xoffset -780
    with eye_open
    "睜開眼的時候，便發現自己已身處於綠色草叢中。{p}\ \ \ 鼻子嗅到了，是刺鼻的機油味。"
    "在眼前，我只能看到頭破血流的妹妹，還有壓在她之上的汽車殘骸。"
    show childhood3 at VHS
    with dissolve
    hide childhood3_1
    k "「遙...你等我。{w}很快來救妳......」"
    "遙也正向我伸出手，儘管身上佈滿血跡。"
    h "「哥哥...」"
    play sound "heartbeat.mp3"
    show childhood3_2 at VHS
    show childhood3_2 :
        linear 1.0 alpha 0.0 truecenter zoom 1.25
    "我無論如何也要救她。"
    "即使只能止血也好，我怎麼會讓遙在我面前死去？"
    "「遙......我很快...」"
    show childhood3_3 at VHS
    show childhood3_3 :
        alpha 0.0
        linear 2.0 alpha 1.0
    "不行，身體太重了，視界亦越發模糊。"
    hide childhood3
    hide childhood3_3
    with eye_shut
    hide childhood3_2
    show childhood3_3 at VHS
    show eye1
    show end:
        alpha 1.0
    show end:
        linear 1.0 alpha 0.0
        linear 1.0 alpha 1.0
        linear 1.0 alpha 0.0
        pause 1.0
        linear 1.0 alpha 1.0
    "但，她是我唯一的妹妹。"
    "「遙...！{w}妳等我...」"
    "我用盡身體的力氣，向前伸出手。"
    "向前。"
    "向前爬也要靠近遙。"
    hide childhood3_3
    hide end
    hide eye1
    "如果這個世界有神，祂見到這一刻盡力的我，{p}又會怎麼想呢？"
    play sound "heartbeat.mp3"
    "我們要活下去......{w}不是，就算我死了，遙也絕對要活下去。{p}絕對{cps=10}......{/cps}"
    show white
    with dissolve
    "{color=#FFFFFF}少女{/color}""「不用擔心，」"
    "{color=#FFFFFF}少女{/color}""「我會一直保護你。」"
    "嗯。這樣我就......"
    $ quick_menu = False
    window hide dissolve
    hide white
    with dissolve
    pause 2.0
    show khome
    with dissolve
    window show dissolve
    $ quick_menu = True
    k "「那我出門啦～」"
    show haruka_s
    with dissolve
    h "「嗯！爸爸媽媽，我們出去啦！」"
    "我們看著玄關旁的相框，然後道別，前往學校。"
    hide haruka_s
    with dissolve
    hide khome
    with dissolve
    show home_k_d
    with dissolve
    k "「司，真早呀！」"
    show tsukasa
    with dissolve
    t "「什麼啦，不是説好早5分鐘在這裏等嗎。」"
    show tsukasa:
        linear 0.3 xalign 0.2
    show haruka_s at right:
        xalign 0.8
    with dissolve
    h "「唉...都怪哥哥啦，又睡過頭！」"
    k "「我也沒辦法啦...」{p}（加上昨晚又是那個夢...）"
    show haruka_su
    show haruka_su at right:
        xalign 0.8
        alpha 0.0
    show haruka_su:
        linear 0.2 alpha 1.0
    h "「嗯？你剛剛說什麼了嗎？」"
    hide haruka_s
    k "「啊、啊啊沒有。我們走吧。」"
    show haruka_l
    show haruka_l at right:
        xalign 0.8
        alpha 0.0
    show haruka_l:
        linear 0.2 alpha 1.0
    h "「那麼我們要走快兩步了～{p}\ \ \ 補回哥哥睡過頭的10分鐘！」"
    hide haruka_su
    show tsukasa:
        linear 0.2 xoffset -50 alpha 0.0
    show haruka_l:
        linear 0.2 xoffset -50 alpha 0.0
    pause 0.2
    show home_t_d:
        xoffset -15
    with dissolve
    hide tsukasa
    hide haruka_l
    hide home_k_d
    show tsukasa
    show tsukasa:
        xalign 0.2
        alpha 0.0
        xoffset 50
    show tsukasa:
        linear 0.2 xoffset 0 alpha 1.0
    show haruka_s
    show haruka_s:
        xalign 0.8
        alpha 0.0
        xoffset 50
    show haruka_s:
        linear 0.2 xoffset 0 alpha 1.0
    t "「如果不是跟你們由細玩到大，我肯定第一時間會丟下界。哼。」"
    k "「呃嘿嘿...謝謝你這麼給面子喔～{w}真的難為你啦。」"
    t "「不過，你們倆在車禍過後大難不死實在是太好啦...{p}\ \ \ 雖然已經不能再見到伯父伯母......」"
    "只有我和遙在那個車禍裡生還了。"
    "詳情我也不太清楚，{w}只知道遙比我早許多出院，{p}期間一直在我身邊等待我醒來。"
    "這些都是後來司告訴我的事。"
    k "「那倒是呢，司沒了我們的話會好寂寞啊～{p}\ \ \ 平常又是自己一個人住。」"
    t "「哼，把自己說得那麼高高在上。」"
    show haruka_l
    show haruka_l:
        xalign 0.8
        alpha 0.0
    show haruka_l:
        linear 0.2 alpha 1.0
    h "「哈哈...日常的鬥嘴又來了～」"
    hide haruka_s
    t "「說起來，你們有聽說嗎？我們學校的能力特殊班竟然只有5個人喔！」"
    k "「那...不就我們三個，還有另外兩個人...{p}\ \ \ 不知道會不會很難相處呢？」"
    show haruka_s
    show haruka_s:
        xalign 0.8
        alpha 0.0
    show haruka_s:
        linear 0.2 alpha 1.0
    h "「反正我們三個從小認識，{p}\ \ \ 到時候把他們兩個人也拉進來一起玩不就好了嗎？」"
    hide haruka_l
    t "「還有聽說這年沒有考試喔！」"
    k "「喔喔喔喔！！特殊班太讚了吧！」"
    show haruka_e2
    show haruka_e2:
        xalign 0.8
        alpha 0.0
    show haruka_e2:
        linear 0.2 alpha 1.0
    h "「哎，看哥哥現在多精神...{p}\ \ \ 早知道剛才用這句叫醒你好了...」"
    hide haruka_s
    t "「哈哈哈！這提案挺有用吧？」"
    show haruka_e3
    show haruka_e3:
        xalign 0.8
        alpha 0.0
    show haruka_e3:
        linear 0.2 alpha 1.0
    h "「乾脆讓司來我們家住好了，多一個人照顧這哥哥～」"
    hide haruka_e2
    k "「等等，說得會不會過分了點？」"
    t "「嘛，反正在我眼內，基本上都是遙照顧你呢～{p}\ \ \ 真羨慕有妹妹的人！」"
    k "「那你把遙娶了不就變成我們的家人了嗎？」"
    show haruka_a3
    show haruka_a3:
        xalign 0.8
        alpha 0.0
    show haruka_a3:
        linear 0.2 alpha 1.0
    h "「別這樣...」"
    hide haruka_e3
    t "「界說話真的不經大腦呀，哈哈哈～！？」"
    play sound "explo.mp3"
    show haruka_su
    show haruka_su:
        xalign 0.8
        alpha 0.0
    show haruka_su:
        linear 0.2 alpha 1.0
    show home_t_d:
        linear 0.05 xoffset 0
        linear 0.05 xoffset -30
        linear 0.05 xoffset 0
        linear 0.05 xoffset -30
        linear 0.05 xoffset 0
        linear 0.05 xoffset -30
        linear 0.05 xoffset 0
        linear 0.05 xoffset -30
        linear 0.1 xoffset -15
    "路上的一輛車著火爆炸了。"
    hide haruka_a3
    stop sound fadeout 1.0
    hide haruka_su
    with dissolve
    hide tsukasa
    with dissolve
    hide home_t_d
    with dissolve
    show leak
    with dissolve
    show haruka_ysd
    show haruka_ysd:
        xalign 0.2
    with dissolve
    show tsukasa
    show tsukasa:
        xalign 0.8
    with dissolve
    k "「不是吧？能力暴走？」"
    t "「切，偏偏要在中七第一天發生這些事！」"
    show haruka_s
    show haruka_s:
        xalign 0.2
        alpha 0.0
    show haruka_s:
        linear 0.2 alpha 1.0
    h "「雖然未開學，不過我們三個姑且算是超能力班！{p}\ \ \ 先把書包放在這裏～」"
    hide haruka_ysd
    "果然臨危不亂才是遙呢～"
    "目光回到事發現場，車旁有一位正在咆哮的大叔。"
    "他的雙手不停噴火，情況已經控制不住。"
    t "「看來是精神錯亂令他胡亂思考，{p}\ \ \ 喚醒了他過去的能力。」"
    k "「我們兩個去制服他！」"
    t "「好！」"
    show tsukasa:
        linear 0.2 xoffset -50 alpha 0.0
    pause 0.2
    hide tsukasa
    hide haruka_s
    with dissolve
    hide tsukasa
    "這時，大叔撲倒路邊的初中生。"
    "{color=#FFFFFF}初中生{/color}" "「大哥哥，救我呀！」"
    "快要被襲擊的他正在呼喚我們。"
    "司馬上向我打了個眼色，看來他要先去把初中生營救出來。"
    show tsukasa
    with dissolve
    t "「喝！」"
    show tsukasa:
        linear 0.1 xoffset -100
        linear 0.1 xoffset 0
    "司一腳踢走大叔。"
    k "「果然的身手不凡！{w}你平時肯定又在偷練了！」"
    t "「真多話說，你顧得到自己那邊嗎？」"
    "車輛上的火焰越燒越旺，像是有了意志一樣，\n\ \ \ 開始伸向路上的人們。"
    "但我也不甘示弱。"
    "將「意志力」纏繞住拳頭，"
    "然後一個拳風吹熄路邊嘅火種。"
    k "「——哈！」"
    show tsukasa:
        linear 0.3 xalign 0.2
    show haruka_s
    show haruka_s:
        alpha 0.0
        xalign 0.8
        xoffset 50
    show haruka_s:
        linear 0.2 xoffset 0 alpha 1.0
    pause 0.2
    h "「哥哥、司！我這邊的人已經安全了！」"
    "{color=#FFFFFF}路邊眾人{/color}""「哇，謝謝你們啊！」\n「難道他們是特殊班的學生？」\n「那個男生的踢腿真的帥！」"
    show haruka_lb
    show haruka_lb:
        xalign 0.8
        alpha 0.0
    show haruka_lb:
        linear 0.2 alpha 1.0
    h "「剩下的就交給你們聯絡警察啦！{p}\ \ \ 我們先上學～拜託大家啦！」"
    hide haruka_s
    show haruka_big_a3_s
    show haruka_big_a3_s:
        alpha 0.0
    show haruka_big_a3_s:
        linear 0.2 alpha 1.0
    show haruka_lb:
        linear 0.2 alpha 0.0
    show tsukasa:
        linear 0.2 alpha 0.0
    "妹妹向街坊揮手後，又轉過身盯緊我們。"
    hide haruka_lb
    "「妹妹大人」的壓迫感... 真的好可怕......"
    show haruka_big_a4
    show haruka_big_a4:
        alpha 0.0
    show haruka_big_a4:
        linear 0.2 alpha 1.0
    h "「你們兩個！！知不知道我們已經遲到啦！？」"
    hide haruka_big_a3_s
    k "「額...難道要由得他暴走嘛...？」"
    show haruka_big_a1
    show haruka_big_a1:
        alpha 0.0
    show haruka_big_a1:
        linear 0.2 alpha 1.0
    h "「哼！總之下次哥哥早點出門不就好了！」"
    hide haruka_big_a4
    "站在一旁的司也滴著冷汗，不發一語。"
    show tsukasa:
        linear 0.2 alpha 1.0
    show haruka_a3
    show haruka_a3:
        alpha 0.0
        xalign 0.8
    show haruka_a3:
        linear 0.2 alpha 1.0
    show haruka_big_a1:
        linear 0.2 alpha 0.0
    h "「還有司！剛才你有空耍帥的話就趕緊過去幫哥哥啦！{p}\ \ \ 還有空陶醉在街坊的讚美當中嗎？！」"
    hide haruka_big_a1
    t "「呃... 下次會的了...」"
    "司尷尬的強顏歡笑了，然後好像想到什麼的樣子，\n又變回那幅淘氣的樣子。"
    t "「既然都到這地步了，那麼我們就來比誰最快跑回校吧！{p}\ \ \ 幸好平日我有鍛鍊身體呢～」"
    show tsukasa:
        linear 0.2 xoffset -50 alpha 0.0
    "司健步如飛，馬上就跑到九霄雲外了。"
    hide tsukasa
    show haruka_s
    show haruka_s:
        xalign 0.8
        alpha 0.0
    show haruka_s:
        linear 0.2 alpha 1.0
    h "「哈哈～我倒沒有司考到入學試全級第二的基礎值那般厲害啦，{p}\ \ \ 不過好在我的技能也幫到忙！」"
    hide haruka_a3
    h "「『浮游』!」"
    show haruka_s:
        linear 0.2 yoffset -50 alpha 0.0
    "遙把自己浮起，直接飛往學校。司就靠驚人的運動量跑去。"
    hide haruka_s
    "至於我嘛..."
    "姑且也有一招。"
    "——『想像』！"
    "跟判定出來的名字沒有太大關係的技能——想像，{p}可以用想像力小幅度強化自己身體，這招便是我的特技。"
    "開學第一天就面臨遲到的壓迫，\n當個中七學生也真的不容易呢～"
    hide leak
    with dissolve
    show sd
    with dissolve
    play sound "chime.mp3"
    "幹，真的遲到了。"
    "...但司跟遙已經安全到步了！"
    "啊啊啊啊，怎麼會這樣呀！！"
    show schoolcoora
    with dissolve
    hide sd
    "看看可不可以偷偷的...爬進去課室裡面......"
    show classroom :
        xoffset -150
        yoffset -15
    with dissolve
    pause 0.5
    show classroom :
        linear 0.5 xoffset -100
        pause 0.5
        linear 0.5 xoffset -50
        pause 0.5
        linear 0.5 xoffset 0
        linear 0.1 yoffset 0
        linear 0.1 yoffset -30
        linear 0.1 yoffset -15
    pause 2.5
    hide schoolcoora
    "咚！"
    show classroom1
    hide classroom
    k "「好痛！」"
    show classroom:
        xoffset 0
        yoffset -15
    "{color=#FFFFFF}老師{/color}" "「這位同學，開學第一天就遲到，還想裝作若無其事，也挺過分的喔。」"
    hide classroom1
    "開學第一天就被老師用名冊敲頭。{p}我只好乖乖認命啦...唉，真倒楣。"
    "不好意思之下，視線稍微移往同學們..."
    "原來，今年同班的兩位都是女同學。"
    show classroom:
        linear 0.2 xoffset -100
    show hikari_s
    show hikari_s:
        alpha 0.0
        xoffset 50
    show hikari_s:
        linear 0.2 alpha 1.0 xoffset 0
    "一位栗色短髮的女生，看上去挺活潑的感覺。"
    show classroom:
        linear 0.2 xoffset 0
    show hikari_s:
        linear 0.2 xoffset 50 alpha 0.0
    show sachi_n
    show sachi_n:
        alpha 0.0
        xoffset -50
    show sachi_n:
        linear 0.2 alpha 1.0 xoffset 0
    "還有另一位黑色馬尾的女生，給人的感覺比一般人成熟，也更陰沈。"
    hide hikari_s
    show classroom:
        linear 0.2 xoffset -50
    show sachi_n:
        linear 0.2 xoffset -50 alpha 0.0
    show tsukasa
    show tsukasa:
        alpha 0.0
        xalign 0.4
        xoffset 50
    show tsukasa:
        linear 0.2 alpha 1.0 xoffset 0
    show haruka_s
    show haruka_s:
        alpha 0.0
        xalign 0.6
        xoffset 50
    show haruka_s:
        linear 0.2 alpha 1.0 xoffset 0
    "然後還有司和遙。"
    hide sachi_n
    show tsukasa:
        linear 0.2 alpha 0.0
    show haruka_s:
        linear 0.2 alpha 0.0
    "這就是我們今年的同學了。"
    hide tsukasa
    hide haruka_s
    k "「啊哈哈...不好意思，我遲到了...{p}\ \ \ 我是特殊班的同學，大家叫我界就可以啦。」"
    "老師見了便和藹地笑了笑。"
    show kazu
    with dissolve
    kz "「噢～你就是界。」"
    kz "「詳細的事兩位同學都跟我交代了啦，你在那裏先找個位置坐下吧。」"
    hide kazu
    with dissolve
    show kazu_small
    with dissolve
    show hikari_s
    show hikari_s:
        xalign 0.8
    with dissolve
    show sachi_n
    show sachi_n:
        xalign 0.2
    with dissolve
    hk "「啊，你就是那個負責撲熄火種的人！"
    show hikari_l1_s
    show hikari_l1_s:
        xalign 0.8
        alpha 0.0
    show hikari_l1_s:
        linear 0.2 alpha 1.0
    extend "有點東西額你～」"
    hide hikari_s
    s "「喔... 真是熱心。剛才沒弄傷吧？」"
    k "「啊，沒問題～{w}只是趕不上那邊兩位的步伐而已。」"
    "說著話也感受到自己冒出冷汗了。"
    kz "「既然大家是第一次見面，不如從自我介紹開始吧！{p}\ \ \ 我是和，你們的班主任兼體育老師，{p}\ \ \ 平時最重要的戰鬥訓練就是由我負責領隊的。」"
    show kazu_small:
        linear 0.2 alpha 0.0
    show hikari_l1_s:
        linear 0.2 alpha 0.0
    show hikari_big_a zorder 100
    show hikari_big_a
    show hikari_big_a:
        alpha 0.0
    show hikari_big_a:
        linear 0.2 alpha 1.0
    show sachi_n:
        linear 0.2 alpha 0.0
    hk "「吾乃照耀一切之光！帶領眾人之光！開拓命運之光是也！"
    hide sachi_n
    hide hikari_li_s
    show hikari_big_p1 zorder 101
    show hikari_big_p1:
        alpha 0.0
    show hikari_big_p1:
        linear 0.2 alpha 1.0
    extend "\n\ \ \ 是此城絕無僅有，擁有領袖氣質的“特殊能力者”！{p}\ \ \ 你們知道嗎？吾之臣下啊，這一年的戰鬥，{p}\ \ \ 吾等定要取得勝利，方能引領凡夫們前往更繁榮的未來。」"
    hk "「降伏吧眾人，我們今天結下互助之盟約，開創光明未來！」"
    hide hikari_big_a
    "她...到底在幹嘛..."
    "別這樣了...好尷尬..."
    "誰可以幫忙解圍呀？拜託了？"
    show haruka_s
    show haruka_s:
        xalign 0.2
        xoffset -50
        alpha 0.0
    show haruka_s:
        linear 0.2 xoffset 0 alpha 1.0
    h "「我是遙，是界的妹妹。請大家多多指教！」"
    "遙完全無視了剛才的中二病開場白..."
    "做得非常好呀！我的妹妹！"
    show tsukasa
    show tsukasa:
        alpha 0.0
        xalign 0.2
        xoffset -100
    show tsukasa:
        linear 0.2 xoffset -50 alpha 1.0
    show haruka_s:
        linear 0.2 xalign 0.4 alpha 0
    t "「我叫司。大家既然是同學一場，有什麼煩惱都可以找我幫忙，不用客氣喔！」"
    hide haruka_s
    k "「我是界，跟遙和司是從小就認識，也希望可以跟大家做朋友。」"
    show sachi_n
    show sachi_n:
        alpha 0.0
        xalign 0.8
        xoffset 50
    show sachi_n:
        linear 0.2 xoffset 0 alpha 1.0
    s "「叫我幸就可以...還有，我是重讀生...」"
    show tsukasa:
        linear 0.2 alpha 0.0
    show hikari_big_p1:
        linear 0.2 alpha 0.0
    show kazu_small
    show kazu_small:
        alpha 0.0
        xalign 0.2
        xoffset -50
    show kazu_small:
        linear 0.2 xoffset 0 alpha 1.0
    kz "「幸雖然是留級生，但都是一個好有經驗的戰鬥員的哦，{p}\ \ \ 你們要好好相處喔!」"
    hide hikari_big_p1
    hide sachi_n
    with dissolve
    hide kazu_small
    with dissolve
    hide tsukasa
    hide haruka
    "大家的樣子看起來都很高興。{p}雖然儘是奇怪的人，但這年應該會過得挺開心。"
    show kazu
    show kazu:
        xalign 0.5
    with dissolve
    kz "「嗯！那就好了，我們開始上課吧。{p}\ \ \ 今年雖然只有5個同學，但係看來也是熱鬧的一屆！」"
    hide kazu
    with dissolve
    hide classroom
    with dissolve
    show island:
        subpixel True
        parallel:
            linear 20 zoom 1.25
        parallel:
            linear 20 xalign 0.5
        parallel:
            linear 20 yalign 0.5
    with dissolve
    "2001年，東亞的這個城市突然出現一個結界。{p}所有能力只能在這個結界中使用。{p}年青人因為他們有一定自我意識、與身體機能健全，{p}而且又未受社會影響，所以能發揮出最大效用的超能力。"
    show machi
    with dissolve
    hide island
    show machi:
        linear 15 xoffset -580
    "我們的理想就是建立帕拉圖式的世界，通過能力理解自身的強處和天資所在，{p}錘鍊身心，繼而尋覓適合自己的社會定位和工作，{p}活得開心，再無憂慮，大同小康，豈不快哉。"
    show battle
    with dissolve
    hide machi
    "這個結界既然可以將我們的人格及信仰具現化，{p}學生自然可以更加認識自己內心的想法，{p}而我們嘅日常課業——戰鬥，亦是最能夠反映人類的真面目，{p}從而認識真正的自我。"
    "所以從教育上看，超能力戰鬥可以令學生理解自己，{p}也可明白人的意志力可以改變事物，學會人定勝天的道理。{p}從而，這個計劃能培養未來的領袖人才，{p}傑出學生將來會就職於大公司之中。"
    show central
    with dissolve
    hide battle
    "這城市亦成為了旅遊勝地，而教育家亦使用這個島作為教育部設施，{p}因此在城市建立了無數座學校。{p}標榜運用超能力的經歷能令學生做好生涯規劃，{p}讓世界各地的家長趨之若鶩，而不同學校的精英亦會轉校入讀。"
    "新時代下的學校，成為一個可以將心靈和物質結合的空間，{p}因此受到無數國際菁英的青睞。"
    hide central
    with dissolve
    show classroom:
        yoffset -15
        xoffset -100
    with dissolve
    show kazu
    with dissolve
    kz "「透過意志力，將自己想像的概念化為現實，{p}\ \ \ 但前提是你們要相信這些概念，或者對其有真切了解。」"
    show kazu_small
    show kazu_small:
        alpha 0.0
        xalign 0.2
        linear 0.2 alpha 1.0
    show haruka_e1
    show haruka_e1:
        xalign 0.8
        alpha 0.0
    show haruka_e1:
        linear 0.2 alpha 1.0
    h "「那是不是等於，例如你係一個超級金庸迷，經過鍛鍊，{p}\ \ \ 可以令你真切相信自己可以使出小說裡面嘅神掌，{p}\ \ \ 武功招式就會化成現實？」"
    kz "「沒有錯。」"
    kz "「每個人的能力會根據自己的信仰和人格而有所不同，亦會有所改變。」"
    show tsukasa
    show tsukasa:
        xalign 0.6
        alpha 0.0
        xoffset -50
    show tsukasa:
        linear 0.2 xoffset 0 alpha 1.0
    show haruka_e1:
        linear 0.2 xoffset 50
    t "「反過來說，當你信仰崩壞的時候，{p}\ \ \ 你也不能使出相應的能力，除非你能重建自己的信念。」"
    show haruka_e1:
        linear 0.2 xoffset 100 alpha 0.0
    show tsukasa:
        linear 0.2 xoffset 50 alpha 0.0
    show classroom:
        linear 0.2 xoffset 0
    show hikari
    show hikari:
        xalign 0.2
        alpha 0.0
        xoffset -50
    show hikari:
        linear 0.2 xoffset 0 alpha 1.0
    show kazu_small:
        linear 0.2 xalign 0.8
    hk "「哪如果上面的金庸迷被敵對流派的劍法一劍打跨，{p}\ \ \ 如果他失去自信，就再無法使出能力？」"
    hide haruka_e1
    hide tsukasa
    kz "「嗯，就是這樣。」"
    kz "「除了意志力，人格也是非常重要的喔。{p}\ \ \ 人格可以延伸理解為性格，與意志不同，是每個人最擅長的屬性，{p}\ \ \ 像是固有技能一般，比較難以改變。」"
    show sachi_n
    show sachi_n:
        xalign 0.4
        alpha 0.0
        xoffset 50
    show sachi_n:
        linear 0.2 xoffset 0 alpha 1.0
    show hikari:
        linear 0.2 xoffset -50
    s "「從此也能推論，單純或蠢的人雖然可以掌握的技能會較少，{p}\ \ \ 相對擁有的強度也會更高。」"
    kz "「正是，而且大部分學生都只會在這個城市逗留一年，{p}\ \ \ 在那一年中，他們可以選擇參加校際戰鬥，{p}\ \ \ 也可以自由運用能力度過那一年，比如說今年電影班很受歡迎。"
    kz "「如果校方發現學生有問題，{p}\ \ \ 可以要求學生留級，令學校有少數的留級生存在。」"
    s "「校際戰鬥的勝利者可以挑戰最終boss，它的形態按挑戰者而定，{p}\ \ \ 但甚少有挑戰者成功。」"
    show sachi_n:
        linear 0.2 xoffset -50 alpha 0.0
    show hikari:
        linear 0.2 xoffset -100 alpha 0.0
    show classroom:
        linear 0.2 xoffset -50
    show kazu
    with dissolve
    kz "「老師的職責是幫學生開導能力，以及在人生路上啟發學生。{p}\ \ \ 與學生在難忘的關卡上共同經歷，提升羈絆，亦會一同研發新的能力，{p}\ \ \ 就像舊時代的高中視覺藝術班一樣。」"
    hide sachi_n
    hide hikari
    "因此，現今教師變成了上流職業。亦有時要配合學校方針，{p}也會「處理」有問題的學生。"
    kz "「好啦，那麼大家好有什麼問題呢？」"
    show hikari
    show hikari:
        alpha 0.0
        xalign 0.2
        xoffset -50
    show hikari:
        linear 0.2 xoffset 0 alpha 1.0
    hk "「老師！那為什麼不同國家不派人來這裡打仗呢？{p}\ \ \ 既然這裡能用超能力的話。」"
    kz "「那是因為，能力就算再強也好，最終只會存在於這個城市裡，{p}\ \ \ 一旦出去了就會消失。」"
    show hikari:
        linear 0.2 xoffset 50 alpha 0.0
    show kazu:
        linear 0.2 xoffset 50 alpha 0.0
    "唉，聽課真的悶死我了..."
    hide hikari
    hide kazu
    hide haruka_s
    "哈啊～我都不自覺打了個呵欠。"
    kz "「那麼今天要講的就差不多啦～{p}\ \ \ 接下來的時間便是大家最期待的...」"
    "喔喔！撤回前言。"
    "我果然沒有進錯學校！"
    show sachi_n
    show sachi_n:
        xalign 0.2
        xoffset -100
        alpha 0.0
    show sachi_n:
        linear 0.2 xoffset -50 alpha 1.0
    show hikari_l1_b
    show hikari_l1_b:
        xalign 0.4
        xoffset -50
        alpha 0.0
    show hikari_l1_b:
        linear 0.2 xoffset 0 alpha 1.0
    show haruka_s
    show haruka_s:
        xalign 0.6
        xoffset 50
        alpha 0.0
    show haruka_s:
        linear 0.2 xoffset 0 alpha 1.0
    show tsukasa
    show tsukasa:
        xalign 0.8
        xoffset 100
        alpha 0.0
    show tsukasa:
        linear 0.2 xoffset 50 alpha 1.0
    "{color=#FFFFFF}眾人{/color}" "{size=+40}「——戰鬥訓練！」{/size}"
    show sachi_n:
        linear 0.2 alpha 0.0
    show hikari_l1_b:
        linear 0.2 alpha 0.0
    show haruka_s:
        linear 0.2 alpha 0.0
    show tsukasa:
        linear 0.2 alpha 0.0
    $ quick_menu = False
    window hide dissolve
    hide classroom
    with dissolve
    hide sachi_n
    hide hikari_l1_b
    hide haruka_s
    hide tsukasa
    pause 1.0
    show waterf:
        zoom 1.0
    with dissolve
    window show dissolve
    $ quick_menu = True
    k "「哇，想不到這處竟然有瀑布喔！」"
    show haruka_l
    with dissolve
    h "「畢竟這是香港仔的特色嘛！」"
    show kazu_small
    show kazu_small:
        xalign 0.8
        alpha 0.0
        xoffset 50
    show kazu_small:
        linear 0.2 xoffset 0 alpha 1.0
    kz "「好啦，我們第一次的訓練，就來玩簡單的模擬戰吧。{p}\ \ \ 嗯...分組方面就遙和界對司、光、幸啦。」"
    show kazu_small:
        linear 0.2 alpha 0.0
    k "「啊，我對戰鬥沒什麼認識...{p}\ \ \ 遙，你知不知道要怎樣做嗎？」"
    hide kazu_small
    "遙準備好她的騎士槍，已經在注入所需的意志力進去。"
    h "「哥哥，戰鬥裡面我們會受到一連串的攻擊，{p}\ \ \ 所以要用返我們有的招式擋回去，甚至還擊！」"
    k "「喔、喔喔。」"
    $ quick_menu = False
    window hide dissolve
    show white zorder 1000
    with dissolve
    show action movement zorder 100:
        zoom 1.0
        linear 4.0 xoffset -10400
    show hikari-action1:
        zoom 1.0
        easein 3.0 xoffset -150
    hide white
    with dissolve
    pause 3.0
    show end
    with dissolve
    hide action movement
    hide hikari-action1
    show whiteline:
        yalign 0.5
        xoffset -1920
    show whiteline:
        linear 0.1 xoffset 0
    pause 0.1
    show whiteline:
        linear 0.1 yzoom 54.0
    pause 0.1
    show hikari-action2_1:
        yalign 0.5
    hide whiteline
    pause 1.5
    show hikari-action3:
        truecenter zoom 1.50
    hide hikari-action2_1
    hide end
    show speed zorder 100 :
        alpha 0.5
    show hikari-action3:
        linear 1.5 truecenter zoom 1.45
    pause 1.0
    show hikari-action3:
        linear 0.1 truecenter zoom 1.0
    pause 0.1
    hide speed
    pause 1.0
    show white zorder 1000
    with dissolve
    hide hikari-action3
    pause 1.0
    hide white
    with dissolve
    $ quick_menu = True
    window show dissolve
    show haruka_s
    show haruka_s:
        alpha 0.0
    show haruka_s:
        linear 0.2 alpha 1.0
    h "「看，剛才光作出了行動，{p}『領袖氣質』是讓隊友強化的技能，所以這次不會受到攻擊——{p}\ \ \ 好，輪到我地進攻的時候了！」"
    hide haruka_l
    menu :
        "界—>遙" :
            jump battle1_1
        "遙—>界" :
            jump battle1_2

label battle1_1:
    $ quick_menu = False
    window hide dissolve
    show white zorder 1000
    with dissolve
    hide haruka_s
    show action movement zorder 100:
        linear 4.0 xoffset -10400
    show kai-action1:
        zoom 1.0
        alpha 1.0
    show kai-action1:
        zoom 1.0
        easein 3.0 xoffset -150
    hide white
    with dissolve
    pause 3.0
    show end
    with dissolve
    hide action movement
    hide kai-action1
    show whiteline:
        yalign 0.5
        xoffset -1920
    show whiteline:
        linear 0.1 xoffset 0
    pause 0.1
    show whiteline:
        linear 0.1 yzoom 54.0
    pause 0.1
    show kai-action2_1:
        yalign 0.5
    hide whiteline
    pause 1.5
    show kai-action3:
        truecenter zoom 1.50
    hide kai-action2_1
    hide end
    show speed zorder 100 :
        alpha 0.5
    show kai-action3:
        linear 1.5 truecenter zoom 1.45
    pause 1.0
    show kai-action3:
        linear 0.1 truecenter zoom 1.0
    pause 0.1
    hide speed
    pause 1.0
    show white zorder 1000
    with dissolve
    hide kai-action3



    show action movement zorder 100:
        linear 4.0 xoffset -10400
    show haruka-action1:
        zoom 1.0
        alpha 1.0
    show haruka-action1:
        zoom 1.0
        easein 3.0 xoffset -150
    hide white
    with dissolve
    pause 3.0
    show end
    with dissolve
    hide action movement
    hide haruka-action1
    show whiteline:
        yalign 0.5
        xoffset -1920
    show whiteline:
        linear 0.1 xoffset 0
    pause 0.1
    show whiteline:
        linear 0.1 yzoom 54.0
    pause 0.1
    show haruka-action2_1:
        yalign 0.5
    hide whiteline
    pause 1.5
    show haruka-action3:
        truecenter zoom 1.50
        yalign 1.0
        xoffset -300
    show haruka-action3:
        easein 2.0 xoffset -480
    pause 2.0
    show haruka-action3:
        truecenter zoom 1.50
        yalign 0.0
        xoffset 300
    show haruka-action3:
        easein 2.0 xoffset 480
    pause 2.0
    show haruka-action3:
        truecenter zoom 1.50
        yalign 0.5
        xoffset 300
    show haruka-action3:
        easein 2.0 xoffset 0
    pause 2.0
    hide haruka-action2_1
    hide end
    show speed zorder 100 :
        alpha 0.5
    show haruka-action3:
        linear 0.1 zoom 1.0 xoffset 0
    pause 0.1
    hide speed
    pause 1.0
    show white zorder 1000
    with dissolve
    hide haruka-action3
    pause 1.0
    hide white
    with dissolve
    jump afterbattle0

label battle1_2:
    $ quick_menu = False
    window hide dissolve
    show action movement zorder 100:
        linear 4.0 xoffset -10400
    show haruka-action1:
        zoom 1.0
        alpha 1.0
    show haruka-action1:
        zoom 1.0
        easein 3.0 xoffset -150
    hide white
    with dissolve
    hide haruka_s
    pause 3.0
    show end
    with dissolve
    hide action movement
    hide haruka-action1
    show whiteline:
        yalign 0.5
        xoffset -1920
    show whiteline:
        linear 0.1 xoffset 0
    pause 0.1
    show whiteline:
        linear 0.1 yzoom 54.0
    pause 0.1
    show haruka-action2_1:
        yalign 0.5
    hide whiteline
    pause 1.5
    show haruka-action3:
        truecenter zoom 1.50
        yalign 1.0
        xoffset -300
    show haruka-action3:
        easein 2.0 xoffset -480
    pause 2.0
    show haruka-action3:
        truecenter zoom 1.50
        yalign 0.0
        xoffset 300
    show haruka-action3:
        easein 2.0 xoffset 480
    pause 2.0
    show haruka-action3:
        truecenter zoom 1.50
        yalign 0.5
        xoffset 300
    show haruka-action3:
        easein 2.0 xoffset 0
    pause 2.0
    hide haruka-action2_1
    hide end
    show speed zorder 100 :
        alpha 0.5
    show haruka-action3:
        linear 0.1 zoom 1.0 xoffset 0
    pause 0.1
    hide speed
    pause 1.0
    show white zorder 1000
    with dissolve
    hide haruka-action3

    show white zorder 1000
    with dissolve
    show action movement zorder 100:
        linear 4.0 xoffset -10400
    show kai-action1:
        zoom 1.0
        alpha 1.0
    show kai-action1:
        zoom 1.0
        easein 3.0 xoffset -150
    hide white
    with dissolve
    pause 3.0
    show end
    with dissolve
    hide action movement
    hide kai-action1
    show whiteline:
        yalign 0.5
        xoffset -1920
    show whiteline:
        linear 0.1 xoffset 0
    pause 0.1
    show whiteline:
        linear 0.1 yzoom 54.0
    pause 0.1
    show kai-action2_1:
        yalign 0.5
    hide whiteline
    pause 1.5
    show kai-action3:
        truecenter zoom 1.50
    hide kai-action2_1
    hide end
    show speed zorder 100 :
        alpha 0.5
    show kai-action3:
        linear 1.5 truecenter zoom 1.45
    pause 1.0
    show kai-action3:
        linear 0.1 truecenter zoom 1.0
    pause 0.1
    hide speed
    pause 1.0
    show white zorder 1000
    with dissolve
    hide kai-action3
    pause 1.0
    hide white
    with dissolve
    jump afterbattle0



label afterbattle0:
    show haruka_l
    show haruka_l:
        alpha 0.0
    show haruka_l:
        linear 0.2 alpha 1.0
    $ quick_menu = True
    window show dissolve
    h "「沒錯啦！不過哥哥你以後都要根據戰況，{p}\ \ \ 做出攻擊次序的判斷，不可以只靠我和司喔！」"
    k "「說得也有道理。」"
    # show hikari small
    # show hikari small:
    #   xalign 0.2
    #   alpha 0.0
    #   xoffset 50
    # show hikari small:
    #    linear 0.2 xoffset 0 alpha 1.0
    hk "「2對3，你們都敢這麼輕敵？」"
    # show tsukasa small
    # show tsukasa small:
    #   xalign 0.2
    #   alpha 0.0
    #   xoffset 50
    # show tsukasa small:
    #    linear 0.2 xoffset 0 alpha 1.0
    # show hikari small:
    #    linear 0.2 xalign 0.4
    t "「接招！」"
    s "「...！」"
    show haruka_a4
    show haruka_a4:
        alpha 0.0
    show haruka_a4:
        linear 0.2 alpha 1.0
    h "「對面的攻擊要來了！觀察他們的攻擊次序之後，{p}\ \ \ 就要想一下如何用返相剋的成員去抵擋敵方的攻擊，{p}\ \ \ 才有機會繼續戰鬥下去！」"
    hide haruka_l
    $ quick_menu = False
    window hide dissolve
    show white zorder 1000
    with dissolve
    show action movement zorder 100:
        zoom 1.0
        linear 4.0 xoffset -10400
    show hikari-action1:
        zoom 1.0
        easein 3.0 xoffset -150
    hide white
    with dissolve
    pause 3.0
    show end
    with dissolve
    hide action movement
    hide hikari-action1
    show whiteline:
        yalign 0.5
        xoffset -1920
    show whiteline:
        linear 0.1 xoffset 0
    pause 0.1
    show whiteline:
        linear 0.1 yzoom 54.0
    pause 0.1
    show hikari-action2_1:
        yalign 0.5
    hide whiteline
    pause 1.5
    show hikari-action3:
        truecenter zoom 1.50
    hide hikari-action2_1
    hide end
    show speed zorder 100 :
        alpha 0.5
    show hikari-action3:
        linear 1.5 truecenter zoom 1.45
    pause 1.0
    show hikari-action3:
        linear 0.1 truecenter zoom 1.0
    pause 0.1
    hide speed
    pause 1.0
    show white zorder 1000
    with dissolve
    hide hikari-action3



    show action movement zorder 100:
        linear 4.0 xoffset -10400
    show tsukasa-action1:
        zoom 1.0
        alpha 1.0
    show tsukasa-action1:
        zoom 1.0
        easein 3.0 xoffset -150
    hide white
    with dissolve
    pause 3.0
    show end
    with dissolve
    hide action movement
    hide tsukasa-action1
    show whiteline:
        yalign 0.5
        xoffset -1920
    show whiteline:
        linear 0.1 xoffset 0
    pause 0.1
    show whiteline:
        linear 0.1 yzoom 54.0
    pause 0.1
    show tsukasa-action2:
        yalign 0.5
    hide whiteline
    pause 1.5
    show tsukasa-action3:
        truecenter zoom 1.50
    hide tsukasa-action2
    hide end
    show speed zorder 100 :
        alpha 0.5
    show tsukasa-action3:
        linear 1.5 truecenter zoom 1.45
    pause 1.0
    show tsukasa-action3:
        linear 0.1 truecenter zoom 1.0
    pause 0.1
    hide speed
    pause 1.0
    show white zorder 1000
    with dissolve
    hide tsukasa-action3



    show action movement zorder 100:
        linear 4.0 xoffset -10400
    show sachi-action1:
        zoom 1.0
        alpha 1.0
    show sachi-action1:
        zoom 1.0
        easein 3.0 xoffset -150
    hide white
    with dissolve
    pause 3.0
    show end
    with dissolve
    hide action movement
    hide sachi-action1
    show whiteline:
        yalign 0.5
        xoffset -1920
    show whiteline:
        linear 0.1 xoffset 0
    pause 0.1
    show whiteline:
        linear 0.1 yzoom 54.0
    pause 0.1
    show sachi-action2_1:
        yalign 0.5
    hide whiteline
    pause 1.5
    show sachi-action3:
        truecenter zoom 1.50
        yalign 1.0
        xoffset -300
    show sachi-action3:
        easein 2.0 xoffset -480
    pause 2.0
    show sachi-action3:
        truecenter zoom 1.50
        yalign 0.0
        xoffset 300
    show sachi-action3:
        easein 2.0 xoffset 480
    pause 2.0
    hide sachi-action2_1
    hide end
    show speed zorder 100 :
        alpha 0.5
    show sachi-action3:
        linear 0.1 zoom 1.0 xoffset 0
    pause 0.1
    hide speed
    pause 1.0
    show white zorder 1000
    with dissolve
    hide sachi-action3
    pause 1.0
    hide white
    with dissolve
    window show dissolve
    $ quick_menu = True
    show haruka_s
    show haruka_s:
        alpha 0.0
    show haruka_s:
        linear 0.2 alpha 1.0
    h "「留意他們平日有什麼弱點，再派對方的剋星出來就可以啦。{p}\ \ \ 這次我覺得，先用哥哥的『想像』擋住高基礎值的司，{p}\ \ \ 然後我再用『浮游』抵擋幸的飛鏢攻擊！」"
    hide haruka_a4
    menu :
        "界—>遙" :
            jump battle2

label battle2:
    $ quick_menu = False
    window hide dissolve
    show white zorder 1000
    with dissolve
    show action movement zorder 100:
        linear 4.0 xoffset -10400
    show kai-action1:
        zoom 1.0
        alpha 1.0
    show kai-action1:
        zoom 1.0
        easein 3.0 xoffset -150
    hide white
    with dissolve
    pause 3.0
    show end
    with dissolve
    hide action movement
    hide kai-action1
    show whiteline:
        yalign 0.5
        xoffset -1920
    show whiteline:
        linear 0.1 xoffset 0
    pause 0.1
    show whiteline:
        linear 0.1 yzoom 54.0
    pause 0.1
    show kai-action2_1:
        yalign 0.5
    hide whiteline
    pause 1.5
    show kai-action3:
        truecenter zoom 1.50
    hide kai-action2_1
    hide end
    show speed zorder 100 :
        alpha 0.5
    show kai-action3:
        linear 1.5 truecenter zoom 1.45
    pause 1.0
    show kai-action3:
        linear 0.1 truecenter zoom 1.0
    pause 0.1
    hide speed
    pause 1.0
    show white zorder 1000
    with dissolve
    hide kai-action3



    show action movement zorder 100:
        linear 4.0 xoffset -10400
    show haruka-action1:
        zoom 1.0
        alpha 1.0
    show haruka-action1:
        zoom 1.0
        easein 3.0 xoffset -150
    hide white
    with dissolve
    pause 3.0
    show end
    with dissolve
    hide action movement
    hide haruka-action1
    show whiteline:
        yalign 0.5
        xoffset -1920
    show whiteline:
        linear 0.1 xoffset 0
    pause 0.1
    show whiteline:
        linear 0.1 yzoom 54.0
    pause 0.1
    show haruka-action2_1:
        yalign 0.5
    hide whiteline
    pause 1.5
    show haruka-action3:
        truecenter zoom 1.50
        yalign 1.0
        xoffset -300
    show haruka-action3:
        easein 2.0 xoffset -480
    pause 2.0
    show haruka-action3:
        truecenter zoom 1.50
        yalign 0.0
        xoffset 300
    show haruka-action3:
        easein 2.0 xoffset 480
    pause 2.0
    show haruka-action3:
        truecenter zoom 1.50
        yalign 0.5
        xoffset 300
    show haruka-action3:
        easein 2.0 xoffset 0
    pause 2.0
    hide haruka-action2_1
    hide end
    show speed zorder 100 :
        alpha 0.5
    show haruka-action3:
        linear 0.1 zoom 1.0 xoffset 0
    pause 0.1
    hide speed
    pause 1.0
    show white zorder 1000
    with dissolve
    hide haruka-action3
    pause 1.0
    hide white
    with dissolve
    show haruka
    with dissolve
    $ quick_menu = True
    window show dissolve
    show haruka_l
    show haruka_l:
        alpha 0.0
    show haruka_l:
        linear 0.2 alpha 1.0
    h "「嗯！就是這樣！小心還有最後一次攻擊喔！{p}\ \ \ 這次指揮就交給哥哥了！我相信你。」"
    hide haruka_s
    $ quick_menu = False
    window hide dissolve
    show white zorder 1000
    with dissolve
    show action movement zorder 100:
        zoom 1.0
        linear 4.0 xoffset -10400
    show hikari-action1:
        zoom 1.0
        easein 3.0 xoffset -150
    hide white
    with dissolve
    pause 3.0
    show end
    with dissolve
    hide action movement
    hide hikari-action1
    show whiteline:
        yalign 0.5
        xoffset -1920
    show whiteline:
        linear 0.1 xoffset 0
    pause 0.1
    show whiteline:
        linear 0.1 yzoom 54.0
    pause 0.1
    show hikari-action2_1:
        yalign 0.5
    hide whiteline
    pause 1.5
    show hikari-action3:
        truecenter zoom 1.50
    hide hikari-action2_1
    hide end
    show speed zorder 100 :
        alpha 0.5
    show hikari-action3:
        linear 1.5 truecenter zoom 1.45
    pause 1.0
    show hikari-action3:
        linear 0.1 truecenter zoom 1.0
    pause 0.1
    hide speed
    pause 1.0
    show white zorder 1000
    with dissolve
    hide hikari-action3

    show action movement zorder 100:
        linear 4.0 xoffset -10400
    show sachi-action1:
        zoom 1.0
        alpha 1.0
    show sachi-action1:
        zoom 1.0
        easein 3.0 xoffset -150
    hide white
    with dissolve
    pause 3.0
    show end
    with dissolve
    hide action movement
    hide sachi-action1
    show whiteline:
        yalign 0.5
        xoffset -1920
    show whiteline:
        linear 0.1 xoffset 0
    pause 0.1
    show whiteline:
        linear 0.1 yzoom 54.0
    pause 0.1
    show sachi-action2_1:
        yalign 0.5
    hide whiteline
    pause 1.5
    show sachi-action3:
        truecenter zoom 1.50
        yalign 1.0
        xoffset -300
    show sachi-action3:
        easein 2.0 xoffset -480
    pause 2.0
    show sachi-action3:
        truecenter zoom 1.50
        yalign 0.0
        xoffset 300
    show sachi-action3:
        easein 2.0 xoffset 480
    pause 2.0
    hide sachi-action2_1
    hide end
    show speed zorder 100 :
        alpha 0.5
    show sachi-action3:
        linear 0.1 zoom 1.0 xoffset 0
    pause 0.1
    hide speed
    pause 1.0
    show white zorder 1000
    with dissolve
    hide sachi-action3

    show action movement zorder 100:
        linear 4.0 xoffset -10400
    show tsukasa-action1:
        zoom 1.0
        alpha 1.0
    show tsukasa-action1:
        zoom 1.0
        easein 3.0 xoffset -150
    hide white
    with dissolve
    pause 3.0
    show end
    with dissolve
    hide action movement
    hide tsukasa-action1
    show whiteline:
        yalign 0.5
        xoffset -1920
    show whiteline:
        linear 0.1 xoffset 0
    pause 0.1
    show whiteline:
        linear 0.1 yzoom 54.0
    pause 0.1
    show tsukasa-action2:
        yalign 0.5
    hide whiteline
    pause 1.5
    show tsukasa-action3:
        truecenter zoom 1.50
    hide tsukasa-action2
    hide end
    show speed zorder 100 :
        alpha 0.5
    show tsukasa-action3:
        linear 1.5 truecenter zoom 1.45
    pause 1.0
    show tsukasa-action3:
        linear 0.1 truecenter zoom 1.0
    pause 0.1
    hide speed
    pause 1.0
    show white zorder 1000
    with dissolve
    hide tsukasa-action3

    show action movement zorder 100:
        linear 4.0 xoffset -10400
    show sachi-action1:
        zoom 1.0
        alpha 1.0
    show sachi-action1:
        zoom 1.0
        easein 3.0 xoffset -150
    hide white
    with dissolve
    pause 3.0
    show end
    with dissolve
    hide action movement
    hide sachi-action1
    show whiteline:
        yalign 0.5
        xoffset -1920
    show whiteline:
        linear 0.1 xoffset 0
    pause 0.1
    show whiteline:
        linear 0.1 yzoom 54.0
    pause 0.1
    show sachi-action2_1:
        yalign 0.5
    hide whiteline
    pause 1.5
    show sachi-action3:
        truecenter zoom 1.50
        yalign 1.0
        xoffset -300
    show sachi-action3:
        easein 2.0 xoffset -480
    pause 2.0
    show sachi-action3:
        truecenter zoom 1.50
        yalign 0.0
        xoffset 300
    show sachi-action3:
        easein 2.0 xoffset 480
    pause 2.0
    hide sachi-action2_1
    hide end
    show speed zorder 100 :
        alpha 0.5
    show sachi-action3:
        linear 0.1 zoom 1.0 xoffset 0
    pause 0.1
    hide speed
    pause 1.0
    show white zorder 1000
    with dissolve
    hide sachi-action3

    pause 1.0
    hide white
    with dissolve
    window show dissolve
    $ quick_menu = True
    menu :
        "遙—>界—>遙" :
            jump battle3w
        "遙—>界—>界" :
            jump battle3l
        "界—>遙—>界" :
            jump battle3l

label battle3w:
    $ quick_menu = False
    window hide dissolve
    show white zorder 1000
    with dissolve
    hide haruka_s
    show action movement zorder 100:
        linear 4.0 xoffset -10400
    show haruka-action1:
        zoom 1.0
        alpha 1.0
    show haruka-action1:
        zoom 1.0
        easein 3.0 xoffset -150
    hide white
    with dissolve
    pause 3.0
    show end
    with dissolve
    hide action movement
    hide haruka-action1
    show whiteline:
        yalign 0.5
        xoffset -1920
    show whiteline:
        linear 0.1 xoffset 0
    pause 0.1
    show whiteline:
        linear 0.1 yzoom 54.0
    pause 0.1
    show haruka-action2_1:
        yalign 0.5
    hide whiteline
    pause 1.5
    show haruka-action3:
        truecenter zoom 1.50
        yalign 1.0
        xoffset -300
    show haruka-action3:
        easein 2.0 xoffset -480
    pause 2.0
    show haruka-action3:
        truecenter zoom 1.50
        yalign 0.0
        xoffset 300
    show haruka-action3:
        easein 2.0 xoffset 480
    pause 2.0
    show haruka-action3:
        truecenter zoom 1.50
        yalign 0.5
        xoffset 300
    show haruka-action3:
        easein 2.0 xoffset 0
    pause 2.0
    hide haruka-action2_1
    hide end
    show speed zorder 100 :
        alpha 0.5
    show haruka-action3:
        linear 0.1 zoom 1.0 xoffset 0
    pause 0.1
    hide speed
    pause 1.0
    show white zorder 1000
    with dissolve
    hide haruka-action3

    show white zorder 1000
    with dissolve
    show action movement zorder 100:
        linear 4.0 xoffset -10400
    show kai-action1:
        zoom 1.0
        alpha 1.0
    show kai-action1:
        zoom 1.0
        easein 3.0 xoffset -150
    hide white
    with dissolve
    pause 3.0
    show end
    with dissolve
    hide action movement
    hide kai-action1
    show whiteline:
        yalign 0.5
        xoffset -1920
    show whiteline:
        linear 0.1 xoffset 0
    pause 0.1
    show whiteline:
        linear 0.1 yzoom 54.0
    pause 0.1
    show kai-action2_1:
        yalign 0.5
    hide whiteline
    pause 1.5
    show kai-action3:
        truecenter zoom 1.50
    hide kai-action2_1
    hide end
    show speed zorder 100 :
        alpha 0.5
    show kai-action3:
        linear 1.5 truecenter zoom 1.45
    pause 1.0
    show kai-action3:
        linear 0.1 truecenter zoom 1.0
    pause 0.1
    hide speed
    pause 1.0
    show white zorder 1000
    with dissolve
    hide kai-action3

    show white zorder 1000
    with dissolve
    show action movement zorder 100:
        linear 4.0 xoffset -10400
    show haruka-action1:
        zoom 1.0
        alpha 1.0
    show haruka-action1:
        zoom 1.0
        easein 3.0 xoffset -150
    hide white
    with dissolve
    pause 3.0
    show end
    with dissolve
    hide action movement
    hide haruka-action1
    show whiteline:
        yalign 0.5
        xoffset -1920
    show whiteline:
        linear 0.1 xoffset 0
    pause 0.1
    show whiteline:
        linear 0.1 yzoom 54.0
    pause 0.1
    show haruka-action2_1:
        yalign 0.5
    hide whiteline
    pause 1.5
    show haruka-action3:
        truecenter zoom 1.50
        yalign 1.0
        xoffset -300
    show haruka-action3:
        easein 2.0 xoffset -480
    pause 2.0
    show haruka-action3:
        truecenter zoom 1.50
        yalign 0.0
        xoffset 300
    show haruka-action3:
        easein 2.0 xoffset 480
    pause 2.0
    show haruka-action3:
        truecenter zoom 1.50
        yalign 0.5
        xoffset 300
    show haruka-action3:
        easein 2.0 xoffset 0
    pause 2.0
    hide haruka-action2_1
    hide end
    show speed zorder 100 :
        alpha 0.5
    show haruka-action3:
        linear 0.1 zoom 1.0 xoffset 0
    pause 0.1
    hide speed
    pause 1.0
    show white zorder 1000
    with dissolve
    hide haruka-action3

    pause 1.0
    hide white
    with dissolve
    $ quick_menu = True
    window show dissolve
    h "「太好啦，哥哥！果然我們兩個的默契是無人能敵的～嘻嘻！」"
    k "「哈～ 我們竟然這都能贏了！」"
    jump afterbattle1

label battle3l:
    show white zorder 1000
    with dissolve
    pause 1.0
    hide white
    with dissolve
    $ quick_menu = True
    window show dissolve
    k "「啊...我的指示下得不好。對不起了，遙。」"
    show haruka_ysd
    show haruka_ysd:
        alpha 0.0
    show haruka_ysd:
        linear 0.2 alpha 1.0
    h "「哎～別這樣說，哥哥這次第一次給指示嘛～"
    hide haruka_l
    show haruka_l
    show haruka_l:
        alpha 0.0
    show haruka_l:
        linear 0.2 alpha 1.0
    extend "\n \ \ \ 來日方長，到時再一起奪得勝利吧！」"
    hide haruka_ysd
    jump afterbattle1

label afterbattle1:
    hide haruka
    hide haruka_s
    show waterf:
        linear 0.2 xoffset -49
    show haruka_l:
        linear 0.2 xoffset -50 alpha 0.0
    show tsukasa
    show tsukasa:
        xalign 0.2
        xoffset 50
        alpha 0.0
    show tsukasa:
        linear 0.2 xoffset 0 alpha 1.0
    show sachi_n
    show sachi_n:
        xalign 0.8
        xoffset 50
        alpha 0.0
    show sachi_n:
        linear 0.2 xoffset 0 alpha 1.0
    t "「果然每次見到都覺得好厲害。」"
    hide haruka_l
    s "「你指的是。」"
    t "「你的『複製』，不覺得好bug的嗎，{p}\ \ \ 無論怎麼練也沒辦法學到。」"
    s "「我也只可以複製一次，{p}\ \ \ 不然就要再觸碰一次物件才行。」"
    "司用意志力整了一個有型無實的氣泡。"
    t "「我最多也只可以做到這樣。{p}\ \ \ 再大一點已經製造不了，更別說要複製物件。」"
    show tsukasa:
        linear 0.2 xalign 0.5
    show hikari
    show hikari:
        xalign 0.2
        xoffset -50
        alpha 0.0
    show hikari:
        linear 0.2 xoffset 0 alpha 1.0
    hk "「的確是蠻強的！不過還是遠不及我的能力，哇哈哈哈哈哈!」"
    show waterf:
        linear 0.2 xoffset 0
    show tsukasa:
        linear 0.2 xoffset 50 alpha 0.0
    show hikari:
        linear 0.2 xoffset 50 alpha 0.0
    show sachi_n:
        linear 0.2 xoffset 50 alpha 0.0
    show haruka_s
    show haruka_s:
        alpha 0.0
        xalign 0.5
        xoffset -50
    show haruka_s:
        linear 0.2 xoffset 0 alpha 1.0
    k "「模擬戰，其實挺刺激的啊。」"
    hide tsukasa
    hide hikari
    hide sachi_n
    show haruka_big_lb
    show haruka_big_lb:
        alpha 0.0
    show haruka_big_lb:
        linear 0.2 alpha 1.0
    show haruka_s:
        linear 0.2 alpha 0.0
    h "「對呀! 尤其可以跟哥哥一組～」"
    hide haruka_s
    "遙走上前，點了點我的鼻子，莞爾一笑。"
    k "「啊啊、這個嘛...」"
    show haruka_s
    show haruka_s:
        alpha 0.0
    show haruka_s:
        linear 0.2 alpha 1.0
    show haruka_big_lb:
        linear 0.2 alpha 0.0
    h "「走吧，大家都準備回去更衣室了～」"
    hide haruka_big_lb
    show haruka_s:
        linear 0.2 alpha 0.0
    hide waterf
    with dissolve
    pause 2.0
    show srth
    with dissolve
    "就這樣，我順利地完成了入學後第一個體育課，{p}也認識了新的同學。"
    hide haruka_s
    "經過這一次，我對接下來的日子抱著期待著刺激的心。{p}我相信，我們的校園生活將會變得越來越精彩。"
    "心中繼續猜想美好嘅將來，我們三人一邊在夕陽下的大道走下去，緩步走回家。"
    "兒時看著這漁港，也沒有特別的感覺，{p}但係這年我想我們應該能在此找到屬於自己的路向。"
    "明年三月——我們絕對要在大賽中勝出，{p}成為這個城市唯一有資格挑戰最終大敵的小隊。"
    hide srth
    with dissolve
    window hide dissolve
    $ quick_menu = False
    pause 1.0
    pause 2.0
    jump ch2
    return
