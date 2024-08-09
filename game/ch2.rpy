label ch2:
    show sd
    with dissolve
    window show dissolve
    $ quick_menu = True
    "踏入校門，今天又是新的上課天。"
    "對於我們來說，更是各自強化日。"
    "根據昨天的模擬戰所測出的結果，和老師把我們的戰果分析了一遍，{p}並會在今天與我們逐一檢討，務求讓我們改善不足之處。"
    show schoolcoora
    with dissolve
    hide sd
    k "「哈～要是在中六就肯定不會有這種課堂了～{p}\ \ \ 一整天只進行檢討還有自主訓練什麼的，{p}\ \ \ 換作他們就絕對會認為是浪費時間！」"
    show tsukasa
    show tsukasa:
        alpha 0.0
    show tsukasa:
        linear 0.2 alpha 1.0
    t "「這你就要感謝我們城的這個結界了啦！{p}\ \ \ 沒了它，其實我們跟中二病患者沒分別呢～哈哈！」"
    show haruka_s
    show haruka_s:
        xalign 0.8
        alpha 0.0
    show haruka_s:
        linear 0.2 alpha 1.0
    show tsukasa:
        linear 0.2 xalign 0.2
    h "「別這樣說，反正我們也是有好好用功唸書的。{p}\ \ \ 你看，這是我昨晚做的資料搜集，{p}\ \ \ 是為了開發新的技能喔！」"
    t "「呵，不愧是乖學生啊，遙。」"
    show haruka_n
    show haruka_n:
        xalign 0.8
        alpha 0.0
    show haruka_n:
        linear 0.2 alpha 1.0
    h "「你才是，剛才你不也在樓下公園鍛鍊身體嗎？"
    hide haruka_s
    show haruka_l
    show haruka_l:
        xalign 0.8
        alpha 0.0
    show haruka_l:
        linear 0.2 alpha 1.0
    extend "\n \ \ \ 嘛，不過也總比我家的懶睡豬來的好，嘿嘿～～」"
    hide haruka_n
    k "「我、我也是有進步的喔！{p}\ \ \ 你看，今天我們不是早到學校了嘛？ 我也是有努力起床的喔！」"
    t "「好的好的，真厲害呢！」"
    h "「做得好！」"
    "大家在一番嘲諷過後，便同時忍不住聲音大笑了出來。"
    show haruka_l:
        linear 0.2 alpha 0.0
    show tsukasa:
        linear 0.2 alpha 0.0
    show classroom:
        yoffset -15
        xoffset -50
    with dissolve
    hide tsukasa
    hide haruka_l
    hide sd
    show hikari
    show hikari:
        alpha 0.0
    show hikari:
        linear 0.2 alpha 1.0
    hk "「早啊，青梅竹馬三人組～」"
    show sachi_n
    show sachi_n:
        xalign 0.8
        alpha 0.0
    show sachi_n:
        linear 0.2 alpha 1.0
    show hikari:
        linear 0.2 xalign 0.2
    s "「各位早安。」"
    hk "「呐呐，看看這個！！{p}\ \ \ 是我昨天回家找到的機械人喔！」"
    show hikari:
        linear 0.2 xoffset -50
    show sachi_n:
        linear 0.2 xalign 0.4
    show tsukasa
    show tsukasa:
        xalign 0.8
        alpha 0.0
    show tsukasa:
        linear 0.2 alpha 1.0
    t "「都幾歲人了還玩這些～ 而且還帶回校是怎樣」"
    k "「喔喔！這部《鏡光神》我小時候也很喜歡看！」"
    hk "「原來你也是同好嗎？！那部戰機你有買嗎？」"
    k "「當然有！男主角的覺醒畫面真的太熱血了！！」"
    hk "「對啊！那時候幸好有爺爺讓陪我一起看，{p}\ \ \ 每天放學後4:30pm坐在電視前等著播《放學穿梭機》！」"
    k "「啊啊，你真好呀！我那時只有做完功課才準看電視的...」"
    show tsukasa:
        linear 0.2 xalign 0.6
    show haruka_l
    show haruka_l:
        xalign 0.8
        alpha 0.0
    show haruka_l:
        xoffset 50
    show haruka_l:
        linear 0.2 alpha 1.0 xoffset 0
    show sachi_n:
        linear 0.2 alpha 0.0
    show tsukasa:
        linear 0.2 alpha 0.0
    h "「哈哈，結果不也是我跟你一起把功課做完了嘛？{p}\ \ \ 那部的確挺好看的～」"
    hide sachi_n
    hide tsukasa
    k "「Yeah！結果我就把整部都看完了！」"
    hk "「那時候我和爺爺也買了整盒DVD看呢！」"
    k "「喔喔喔！這現在還有得賣嗎—— {p}\ \ \ 啊，和老師來了。」"
    show haruka_l:
        linear 0.2 alpha 0.0
    show hikari:
        linear 0.2 alpha 0.0
    "大家馬上回到自己的座位。"
    hide haruka_l
    hide hikari
    "一想到今天的課題，心裏就緊張起來了。{p}畢竟是跟老師一對一的檢討環節呢。"
    show classroom:
        easein 0.5 xoffset -100
        pause 0.7
        easein 0.5 xoffset 0
        pause 0.7
        easein 0.5 xoffset -50
    pause 3.0
    "怎麼辦呢... 感覺上班上大家都有自己的專長，只有我比較普通。"
    show hikari
    show hikari:
        alpha 0.0
        xoffset 50
    show classroom:
        linear 0.2 xoffset -100
    show hikari:
        linear 0.2 xoffset 0 alpha 1.0
    "光即使不能戰鬥，但她是特殊能力者，{p}『領袖魅力』這種全體加攻擊力的技能可是非常稀有。"
    show sachi_n
    show sachi_n:
        alpha 0.0
        xoffset -50
    show classroom:
        linear 0.2 xoffset -67
    show hikari:
        linear 0.2 alpha 0.0
    show sachi_n:
        linear 0.2 alpha 1.0 xoffset 0
    "幸雖然只有『複製』物件的技能，但憑著沈著冷靜和敏捷的戰鬥風格，{p}她的定位便很明確了——能讓人聯想到忍者的形象。"
    hide hikari
    show tsukasa
    show tsukasa:
        alpha 0.0
        xoffset -50
    show classroom:
        linear 0.2 xoffset -33
    show sachi_n:
        linear 0.2 alpha 0.0
    show tsukasa:
        linear 0.2 alpha 1.0 xoffset 0
    "司的能力是可以看到對方基礎值的『觀測』，{p}透過這種技能，他每天鞭策自己的基礎值，刻苦地進行秘密訓練。{p}但是這點事情，我作為他的死黨當然是知道的。"
    hide sachi_n
    show haruka_s
    show haruka_s:
        alpha 0.0
        xoffset -50
    show classroom:
        linear 0.2 xoffset 0
    show tsukasa:
        linear 0.2 alpha 0.0
    show haruka_s:
        linear 0.2 alpha 1.0 xoffset 0
    "遙的『浮游』加上她的騎士槍，可謂絕配。{p}雖然她天生身體質素沒有特別好，{p}但用『浮游』為敵人加上debuff後便可以令她處於優勢。"
    hide tsukasa
    show classroom:
        linear 0.2 xoffset -50
    show haruka_s:
        linear 0.2 alpha 0.0
    "說到底，像我這種普通的身體強化，算是通街都有的技能到底是要如何進步啊...... 這下真的傷腦筋了。"
    hide haruka_s
    "在思索的途中，和老師的點名把思緒打斷了。"
    kz "「遙同學！」"
    h "「在！」"
    "遙拿著筆記本和鉛筆急忙走出去教師桌。{p}只見遙驚訝的樣子，在不久後又認真地記著筆記。{p}片刻之後，又回到座位上。"
    "同樣的流程也發生在幸的身上。{p}至於司，原來他一早就消失了。"
    k "「遙，你剛才有見過司嗎？」"
    show haruka_su
    show haruka_su:
        alpha 0.0
    show haruka_su:
        linear 0.2 alpha 1.0
    h "「啊，他是第一個去檢討的。之後馬上就離開教室了。」"
    show hikari
    show hikari:
        xalign 0.8
        alpha 0.0
    show hikari:
        xoffset 50
    show hikari:
        linear 0.2 alpha 1.0 xoffset 0
    show haruka_su:
        linear 0.2 xalign 0.2
    hk "「啊啊，他的話剛才好像說要去瀑布修行喔。」"
    k "「欸，真的假的。一大清早就這麼拼命嗎？」"
    show sachi_n
    show sachi_n:
        xalign 0.8
        alpha 0.0
    show sachi_n:
        xoffset 50
    show sachi_n:
        linear 0.2 xoffset 0 alpha 1.0
    show hikari:
        linear 0.2 xalign 0.6
    s "「也不難理解的吧。畢竟只有一年的時間。」"
    hk "「對，在這一年修行好，便可以做到想做的事了。{p}\ \ \ 界，你有什麼想用這種力量做的事嗎？」"
    menu:
        "我也不太清楚" :
            jump ch2_h1
        "我想品嚐一下成為強者的滋味" :
            jump ch2_hk1
        "我純粹想畢業，然後進大公司而已" :
            jump ch2_s1

label ch2_h1:
    $h_pts += 1
    hk "「嗯～ 那麼今年就好好努力尋找自我吧！{p}\ \ \ 也算是人生的一個突破喔！」"
    s "「可能答案意外地簡單...也說不定呢。{p}\ \ \ 總之，先努力找吧。」"
    #"[h_pts] [hk_pts] [s_pts]"
    jump ch2_1

label ch2_hk1:
    $hk_pts += 1
    hk "「喔喔！果然界也是渴望力量之人！{p}\ \ \ 來跟我混，讓吾賜給你力量吧、呵呵呵！！！」"
    s "「你那種力量，誰會想要...」"
    #"[h_pts] [hk_pts] [s_pts]"
    jump ch2_1

label ch2_s1:
    $s_pts += 1
    hk "「呃，這話題有那麼現實嗎？」"
    s "「這不就挺好的嘛。算是個腳踏實地的理想。」"
    jump ch2_1

label ch2_1:
    show haruka_su:
        linear 0.2 alpha 0.0
    show hikari:
        linear 0.2 alpha 0.0
    show sachi_n:
        linear 0.2 alpha 0.0
    hide classroom
    with dissolve
    pause 0.5
    show classroom:
        yoffset -15
        xoffset -50
    with dissolve
    show kazu
    show kazu:
        alpha 0.0
    show kazu:
        linear 0.2 alpha 1.0
    kz "「界同學，輪到你了。」"
    hide haruka_su
    hide hikari
    hide sachi_n
    k "「啊啊，好的！」"
    kz "「那麼，開始之前有一道問題想要問問你。{p}\ \ \ 你覺得自己目前有什麼要提升的嗎？」"
    k "「呃...這樣問我也...」"
    kz "「沒錯，『想像』這種技能其實顧名思義，便是最依賴使用者對世界的想像力。{p}\ \ \ 你希望世界會怎樣，或者希望未來會怎樣，其實也會直接反映到能力上面去。」"
    k "「原來如此... 怪不得以前能力檢查的時候判定的名字這麼奇怪...」"
    kz "「所以，換句問題就是——界，你希望成為一個怎樣的人？{p}\ \ \ 若回答不了這道問題，是不能直接有成長的。」"
    k "「嗯... 目前來說，我大概想成為一個足夠強大保護家人朋友的能力者吧。」"
    kz "「那麼，你個人的願望呢？」"
    k "「我......」"
    show kazu:
        linear 0.2 alpha 0.0
    show randomsky:
        xoffset -580
    with dissolve
    show randomsky:
        linear 40 xoffset 0
    "和老師一語中的。"
    "果然在特殊能力班的老師面前是遮掩不了。"
    "——遮掩不了我空虛的心。"
    "那次山泥傾瀉的車禍後醒來，我一直很恍惚，也有時候會突然抱緊遙。{p}因為我已經不能再失去了。"
    "只是保護著我所擁有的，已經足夠艱難了。{p}難道我還能進一步追求什麼嗎？{p}我有這個資格去找尋嗎？"
    "至少，我現在還有遙、還有司。{p}我至少不是一無所有。"
    "失去雙親的我們猶如沒能泊岸的孤舟。{p}在這怒海之中不斷漂泊流浪，{p}靠著父母剩下的錢，我和遙在這城市中相依為命。"
    "遙好像也是裝作堅強一般，展露溫暖的笑容。{p}她顧好了生活的起居飲食，做飯、洗衣都是她一手搞定，{p}而其他粗重家務就由我負責。"
    "此外，我心中還有一個重任，{p}就是絕對要保護好家人朋友。"
    "這是那次意外後，我在心中暗自許下的約定。{p}但此外的我，並不覺得自己有向前邁進過。"
    "身體長大了，思想也成為高中生了，{p}但心裡的意志還是那時候的我。"
    "仍然空洞。"
    "...界......"
    "......界..."
    hide randomsky
    with dissolve
    show kazu:
        linear 0.2 alpha 1.0
    kz "「...界？」"
    "啊，我剛才還在上課啊。"
    kz "「界，你沒事吧？」"
    k "「我沒事，不用擔心。只是對於自己的路向沒有太明確」"
    kz "「那麼，先透過練習提高跟隊友的默契吧。」"
    k "「欸？這就可以了嗎？」"
    kz "「嗯，我覺得你可以先跟最熟悉的遙一起練習，也許試試練出合作技也不錯呢！」"
    k "「嗯。好吧！」"
    kz "「那麼，加油吧。界，你可以的。」"
    show haruka_s
    show haruka_s:
        alpha 0.0
        xalign 0.8
    show haruka_s:
        xoffset 50
    show haruka_s:
        linear 0.2 xoffset 0 alpha 1.0
    show kazu:
        linear 0.2 xalign 0.2
    show classroom:
        linear 0.2 xoffset -100
    k "「遙！一起出去練習吧！」"
    kz "「嗯。慢慢走吧～」"
    show kazu:
        linear 0.2 alpha 0.0
    show haruka_s:
        linear 0.2 alpha 0.0
    hide classroom
    with dissolve
    pause 0.5
    hide haruka_s
    hide kazu
    show gym_a_o
    with dissolve
    show haruka_lb
    show haruka_lb:
        alpha 0.0
    show haruka_lb:
        linear 0.2 alpha 1.0
    h "「呵呵呵！」"
    k "「...遙？你怎麼了？」"
    show haruka_s
    show haruka_s:
        alpha 0.0
    show haruka_s:
        linear 0.2 alpha 1.0
    h "「——這下終於沒人了。」"
    hide haruka_lb
    show gym_a_o:
        linear 0.4 alpha 0
    show haruka_s:
        linear 0.4 alpha 0
    pause 0.7
    show cg_gym zorder 100
    with dissolve
    h "「哥哥，我終於可以和你一起鑽研這份精華筆記了呢！」"
    hide haruka_s
    h "「由昨晚開始研讀關於意志力戰鬥的事的時候便越讀越覺得有興趣，{p}\ \ \ 不，意志力已經成為我的一部分了！」"
    show gym_a_o
    h "「看好這份筆記的這頁了！{p}\ \ \ 你準備和我一起組出最完美的合作技吧！」"
    k "「呃... 那麼遙師傅，請問我們應該開發哪招合作技呢？」"
    show gym_a_o:
        alpha 1.0
    h "「嗯！從客觀看，我覺得哥哥有著身體強化技能的優勢，{p}\ \ \ 卻沒有像司那種野獸派的戰鬥風格。那麼，應該從一些溫柔一點...」"
    "遙面上泛起了尷尬的紅暈，說實話挺可愛的。{p}不愧是我的妹妹。"
    h "「咳咳，技術成分多一點的路線入手！」"
    "不過溫柔一點...{p}我又不是要把對手吃掉了......"
    h "「所以這招！參考了太極拳法而制定的合作技應該很適合我們！」"
    k "「呃...但，我沒打過功夫喔。」"
    h "「不試試怎麼知道呢～ 來吧，坐言起行才是最實際的喔」"
    hide cg_gym
    with dissolve
    show haruka_s
    show haruka_s:
        alpha 0.0
    show haruka_s:
        linear 0.2 alpha 1.0
    hide cg_gym
    h "「首先，意志力在我們的世界裡是最重要的吧？"
    show haruka_l
    show haruka_l:
        alpha 0.0
    show haruka_l:
        linear 0.2 alpha 1.0
    extend "\n \ \ \ 那麼，就要讓自己投入於角色之中。」"
    hide haruka_s
    show haruka_su
    show haruka_su:
        alpha 0.0
    show haruka_su:
        linear 0.2 alpha 1.0
    h "「——哥哥，跟著我喊一聲。」"
    "嗯？"
    "遙擺起了一雙拳頭，架勢還模仿得不錯。"
    hide haruka_l
    show haruka_a1
    show haruka_a1:
        alpha 0.0
    show haruka_a1:
        linear 0.2 alpha 1.0
    h "「太極拳、遙！！」"
    k "「什麼？你要打十個嗎！！？」"
    hide haruka_su
    show haruka_e3
    show haruka_e3:
        alpha 0.0
    show haruka_e3:
        linear 0.2 alpha 1.0
    h "「呃？但說起太極拳法，最有名的不就是武禹襄嗎？{p}\ \ \ 還有套電影叫武太極門什麼的！」"
    k "「好了好了，那麼我要怎麼配合你？」"
    hide haruka_a1
    show haruka_e1
    show haruka_e1:
        alpha 0.0
    show haruka_e1:
        linear 0.2 alpha 1.0
    h "「哼... 你要在我對面，當我的敵人。{p}\ \ \ 你要給我好好擋住，然後我會把你的力分散出去。」"
    k "「進攻了喔—— 哈！」"
    show gym_a_o:
        linear 0.1 truecenter zoom 1.05
    show speed:
        alpha 0.3
    show haruka_a3
    show haruka_a3:
        alpha 0.0
    show haruka_a3:
        linear 0.2 alpha 1.0
    h "「哼！赫！呀啊啊！」"
    hide haruka_e1
    show gym_a_o:
        linear 0.1 truecenter zoom 1.0
    hide speed
    show orb_b zorder 100
    show orb_b:
        xalign 0.5
        yalign 0.5
        alpha 0.0
    show orb_b:
        xoffset 150
        yoffset -100
    show orb_b:
        easein 2.0 yoffset -105
        easein 2.0 yoffset -95
        repeat

    show orb zorder 1000
    show orb:
        xalign 0.5
        yalign 0.5
        alpha 0.0
    show orb:
        xoffset 150
        yoffset -100
    show orb:
        linear 0.2 alpha 1.0
    pause 0.2
    show orb:
        easein 2.0 yoffset -105
        easein 2.0 yoffset -95
        repeat
    show orb_b:
        alpha 1.0
    "微小的粒子發著光，從我的手臂流到遙的那邊，再聚集成一個圓點。"
    show haruka_a4
    show haruka_a4:
        alpha 0.0
    show haruka_a4:
        linear 0.2 alpha 1.0
    h "「呀，哈、再來！！」"
    hide haruka_a3
    k "「——！！、！、！」"
    show orb:
        linear 0.2 truecenter zoom 2
    show orb_b:
        linear 0.2 truecenter zoom 2
    pause 0.2
    show orb:
        easein 2.0 yoffset -105
        easein 2.0 yoffset -95
        repeat
    show orb_b:
        easein 2.0 yoffset -105
        easein 2.0 yoffset -95
        repeat
    show haruka_s
    show haruka_s:
        alpha 0.0
    show haruka_s:
        linear 0.2 alpha 1.0
    h "「看到了嗎，這些能量正在被我儲起來。」"
    hide haruka_a4
    "圓點慢慢變厚，變得越來越大顆。{p}感覺有點像以前看的格鬥漫畫的一個集氣絕招。"
    "不過遙的身手那麼敏捷，要擋著並卸走對手的格鬥術也不是沒可能的事。"
    show haruka_a4
    show haruka_a4:
        alpha 0.0
    show haruka_a4:
        linear 0.2 alpha 1.0
    h "「再多一點，別留情、{p}\ \ \ 呀啊啊啊啊啊！」"
    hide haruka_s
    "隨著我的加速，遙也跟著以更快的步伐擋住攻擊，並儲起我攻擊時的意志力。"
    show haruka_a3
    show haruka_a3:
        alpha 0.0
    show haruka_a3:
        linear 0.2 alpha 1.0
    h "「這下子總能、球體形成，能力注入，『浮游』！"
    show haruka_a4 zorder 10
    show haruka_a4:
        alpha 0.0
    show haruka_a4:
        linear 0.2 alpha 1.0
    extend "\n\ \ \ 啊啊啊啊啊！」"
    hide haruka_a3
    show orb:
        linear 0.2 truecenter zoom 0.1
    show orb_b:
        linear 0.3 truecenter zoom 0.1
    pause 0.2
    hide orb
    show orb_b:
        linear 0.3 truecenter zoom 100
    pause 1.0
    show orb_b:
        linear 0.3 alpha 0.0
    "想不到那個球體意外地脆弱，只要稍微注入自己的意志力便會爆破。"
    hide orb_b
    "幸好遙的反應速度夠快，馬上往後跳了兩米。"
    "要是我的話應該趕不及加速了吧。"
    k "「別介意，我們再來一次吧！」"
    show haruka_a4 zorder 0
    show haruka_s
    show haruka_s:
        alpha 0.0
    show haruka_s:
        linear 0.2 alpha 1.0
    h "「你站這麼遠怎麼行，過來這邊近一點——」"
    hide haruka_a4
    "不知是否因為剛才的爆炸，遙還沒來得及冷靜下來，差點在我面前摔倒。"
    k "「小心呀！」"
    "我奮不顧身向前一撲，遙捉著我的衣袖，一下子拉近我們兩個人的距離。"
    show haruka_big_s
    show haruka_big_s:
        alpha 0.0
    show haruka_big_s:
        linear 0.2 alpha 1.0
    show haruka_s:
        linear 0.2 alpha 0.0
    k "「——。」"
    hide haruka_s
    "我跟遙面對面，凝視著對方深邃的眼眸。"
    show haruka_big_nb
    show haruka_big_nb:
        alpha 0.0
    show haruka_big_nb:
        linear 0.2 alpha 1.0
    extend "\n瞬間，遙的臉上泛起了紅暈。"
    hide haruka_big_s
    show haruka_big_a2_bl
    show haruka_big_a2_bl:
        alpha 0.0
    show haruka_big_a2_bl:
        linear 0.2 alpha 1.0
    h "「——啊...啊啊啊！好近好近！哥哥你是想對我這個無防備的妹妹做什麼啦！」"
    hide haruka_big_nb
    hide haruka_e3
    k "「不是你把我拉近來的嗎！？」"
    show haruka_a2_bl
    show haruka_a2_bl:
        alpha 0.0
    show haruka_a2_bl:
        linear 0.2 alpha 1.0
    show haruka_big_a2_bl:
        linear 0.2 alpha 0.0
    h "「太狡猾了！！罰你自己練習10次！」"
    hide haruka_big_a2_bl
    show haruka_a2_bl:
        linear 0.2 alpha 0.0
    hide gym_a_o
    with dissolve
    pause 0.5
    hide haruka_a2_bl
    show gym_a:
        yoffset -60
    with dissolve
    show haruka_s
    show haruka_s:
        alpha 0.0
    show haruka_s:
        linear 0.2 alpha 1.0
    show orb_b zorder 99
    show orb_b:
        xalign 0.5
        yalign 0.5
        alpha 0.0
        truecenter zoom 2
    show orb_b:
        xoffset 150
        yoffset -100
    show orb_b:
        easein 2.0 yoffset -105
        easein 2.0 yoffset -95
        repeat
    show orb zorder 100
    show orb:
        xalign 0.5
        yalign 0.5
        alpha 0.0
        truecenter zoom 2
    show orb:
        xoffset 150
        yoffset -100
    show orb:
        linear 0.2 alpha 1.0
    pause 0.2
    show orb:
        easein 2.0 yoffset -105
        easein 2.0 yoffset -95
        repeat
    show orb_b:
        alpha 1.0
    k "「哈啊...10次了。那麼，遙師傅，下一步要怎麼做呢？」"
    show haruka_su
    show haruka_su:
        alpha 0.0
    show haruka_su:
        linear 0.2 alpha 1.0
    h "「咳哼。下一步呢，就是我把卸走的力像這樣轉換為我們的力，{p}\ \ \ 再把它像球一樣傳送給你，過程裡面我們互相傳送，"
    hide haruka_s
    show haruka_lb
    show haruka_lb:
        alpha 0.0
    show haruka_lb:
        linear 0.2 alpha 1.0
    extend "\n\ \ \ 像俗語所說的「辦公耍太極」一樣，{p}\ \ \ 就是把「責任」互相推來推去的感覺。」"
    hide haruka_su
    show haruka_s
    show haruka_s:
        alpha 0.0
    show haruka_s:
        linear 0.2 alpha 1.0
    h "「球裡面有著我的人格能力在裡面，{p}\ \ \ 所以獲得它以後哥哥也可以有暫時減輕重量的效果{p}\ \ \ ——簡單來說就是模擬光一樣的能力啦！」"
    k "「喔喔！想不到這樣也行得通欸！{p}\ \ \ 那傢伙每天強調自己是什麼特殊能力者，這下子她就無話可說了吧！」"
    hide haruka_lb
    show haruka_l
    show haruka_l:
        alpha 0.0
    show haruka_l:
        linear 0.2 alpha 1.0
    h "「那麼在用完整顆力量之前我們就進行交替攻擊，一人一下強力攻擊。{p}\ \ \ 你記得在球裡加入『想像』喔！」"
    k "「嗯，那就開始練習吧！」"
    hide haruka_s
    show haruka_a3
    show haruka_a3:
        alpha 0.0
    show haruka_a3:
        linear 0.2 alpha 1.0
    h "「球體形成，能力注入，『浮游』！"
    hide haruka_l
    show haruka_a2_woa
    show haruka_a2_woa:
        alpha 0.0
    show haruka_a2_woa:
        linear 0.2 alpha 1.0
    extend "\n\ \ \ 哥哥！接著！」"
    hide haruka_a3
    show orb_b:
        linear 0.2 xoffset 250 yoffset -185 truecenter zoom 0.5
    show orb:
        linear 0.2 xoffset 250 yoffset -185 truecenter zoom 0.5
    pause 0.2
    show orb_b:
        linear 0.03 xoffset 200 yoffset -105 truecenter zoom 0.7
    show orb:
        linear 0.03 xoffset 200 yoffset -105 truecenter zoom 0.7
    pause 0.03
    show orb_b:
        linear 0.03 xoffset 150 yoffset -55 truecenter zoom 2
    show orb:
        linear 0.03 xoffset 150 yoffset -55 truecenter zoom 2
    pause 0.03
    show orb_b:
        linear 0.03 xoffset 0 yoffset 0 truecenter zoom 5
    show orb:
        linear 0.03 xoffset 0 yoffset 0 truecenter zoom 5
    pause 0.03
    show orb:
        linear 0.1 xoffset 30
        linear 0.1 xoffset -30
        linear 0.1 xoffset 30
        linear 0.1 xoffset -30
        linear 0.1 xoffset 30
        linear 0.1 xoffset -30
    show orb_b:
        linear 0.1 xoffset 30
        linear 0.1 xoffset -30
        linear 0.1 xoffset 30
        linear 0.1 xoffset -30
        linear 0.1 xoffset 30
        linear 0.1 xoffset -30
    pause 0.6
    show orb:
        linear 0.05 xoffset 30
        linear 0.05 xoffset -30
        repeat
    show orb_b:
        linear 0.05 xoffset 30
        linear 0.05 xoffset -30
        repeat
    k "「可惡...在我手中停下來呀...」"
    show orb:
        linear 0.1 truecenter zoom 0.1
    show orb_b:
        linear 0.2 truecenter zoom 0.1
    pause 0.1
    hide orb
    show orb_b:
        linear 0.3 truecenter zoom 100
    pause 1.0
    show orb_b:
        linear 0.3 alpha 0.0
    "本以為會停在手心裡的能量球突然爆開。"
    hide orb_b
    k "「啊啊啊！」"
    show haruka_n
    show haruka_n:
        alpha 0.0
    show haruka_n:
        linear 0.2 alpha 1.0
    h "「哥哥！沒事嗎？」"
    hide haruka_a2_woa
    k "「...咳... 沒事，再來一次吧！」"
    show haruka_a3
    show haruka_a3:
        alpha 0.0
    show haruka_a3:
        linear 0.2 alpha 1.0
    h "「嗯。"
    hide haruka_n
    show haruka_a2_woa
    show haruka_a2_woa:
        alpha 0.0
    show haruka_a2_woa:
        linear 0.2 alpha 1.0
    extend "——傳球！哥哥，交給你了！」"
    hide haruka_a3
    k "「這次一定要——！！」"
    show orb_b zorder 99
    show orb_b:
        xalign 0.5
        yalign 0.5
        truecenter zoom 5
    show orb zorder 100
    show orb:
        xalign 0.5
        yalign 0.5
        truecenter zoom 5
    show orb:
        linear 0.2 xoffset 30
        linear 0.2 xoffset -30
        repeat
    show orb_b:
        linear 0.2 xoffset 30
        linear 0.2 xoffset -30
        repeat
    "球的旋轉速度的確減慢了。"
    show orb:
        linear 0.1 xoffset 30
        linear 0.1 xoffset -30
        repeat
    show orb_b:
        linear 0.1 xoffset 30
        linear 0.1 xoffset -30
        repeat
    "再用力壓住它，應該可以..."
    show orb:
        linear 0.1 truecenter zoom 0.1
    show orb_b:
        linear 0.2 truecenter zoom 0.1
    pause 0.1
    hide orb
    show orb_b:
        linear 0.3 truecenter zoom 100
    pause 1.0
    show orb_b:
        linear 0.3 alpha 0.0
    "球發出青藍色的光爆炸了。"
    k "「啊、啊啊！！」"
    "在那之後，我和遙訓練了好一會兒。"
    show haruka_a1
    show haruka_a1:
        alpha 0.0
    show haruka_a1:
        linear 0.2 alpha 1.0
    h "「——哥哥！接著！」"
    hide haruka_a2_woa
    k "「來吧——啊啊啊！」"
    show haruka_a2_woa
    show haruka_a2_woa:
        alpha 0.0
    show haruka_a2_woa:
        linear 0.2 alpha 1.0
    h "「哥哥！」"
    hide haruka_a1
    "那個裝著意志力的球在手中一滑，瞬間便讓我接不住了。"
    "一道強烈的電光在我身上炸開。"
    show gym_a:
        easein 0.5 yoffset 0
    show haruka_a2_woa:
        easein 0.5 yoffset 60 alpha 0.0
    k "「呃...」"
    hide haruka_a2_woa
    h "「哥哥，你沒事吧？是不是我每次傳送的時候太用力了？」"
    k "「嗯嗯，沒有啊。是我接不好而已。{p}\ \ \ 看來我們今天最多只能做到連續兩次交替攻擊...」"
    show gym_a:
        easein 0.5 yoffset -60
    show haruka_ysm
    show haruka_ysm:
        alpha 0.0
        yoffset 60
    show haruka_ysm:
        easein 0.5 yoffset 0 alpha 1.0
    h "「嗯，感覺很不服氣呢...」"
    k "「今天就回去休息吧。這樣下去只會無謂的消耗體力而已...{p}\ \ \ 或者轉移一下注意力也可以。{p}\ \ \ 遙，你有什麼提議嗎？」"
    show haruka_s
    show haruka_s:
        alpha 0.0
    show haruka_s:
        linear 0.2 alpha 1.0
    h "「時間還早，不如我們等下放學後一起出去外面繞個圈？」"
    hide haruka_ysm
    k "「嗯，好呀。你想去哪裡？」"
    show haruka_lb
    show haruka_lb:
        alpha 0.0
    show haruka_lb:
        linear 0.2 alpha 1.0
    h "「那當然是旺角了。」"
    hide haruka_s
    hide schoolcoora
    show haruka_lb:
        linear 0.2 alpha 0.0
    hide gym_a
    with dissolve
    pause 1.0
    show mk
    with dissolve
    hide haruka_lb
    "城市中聚集各大唱片店的地區。{p}旺角。"
    "處於我們對面海，九龍尖沙嘴以北的一帶。{p}因當區的旅遊和購物中心而聞名。"
    "人們在擠擁的街頭上喘不過氣的時候，其中一大聚腳點便是這個信和中心。{p}時至今日仍是潮人的聖地。"
    #show cg_disco
    #with dissolve
    h "「哥哥，快點來這邊！！哥哥的碟今天開售了！」"
    k "「欸？我什麼時候出碟了？」"
    h "「不是哥哥，是哥哥啦！」"
    k "「你什麼時候跟別的男生結契了？！」"
    h "「你活在什麼時代呀！明明已經2019年了你還不認識他？{p}\ \ \ 『哥哥』Wing是現在最流行的本地歌手喔！啊啊，我太幸運了，{p}\ \ \ 今天連這隻Fong姐的碟也搶得到！」"
    k "「欸，Fong姐...？」"
    h "「你看！這隻唱片！！是Fong剛出便賣斷貨的新碟喔！！」"
    "對喔... 差點忘記了遙本來就是個不折不扣的年輕人。{p}尤其對這些本地電影和音樂，都沒有免疫力。{p}有時候在房間關著門也會聽到她的哼歌聲。"
    k "「那個，遙小姐......」"
    h "「怎麼了？」"
    k "「我們...不是說好放學後去練習的嗎...？」"
    h "「哥哥，你太天真了！{p}\ \ \ 這其實也是鍛鍊的一環！！」"
    k "「...怎麼說？難道光她把中二病傳染給你了嗎？{p}\ \ \ 明天要回學校痛扁她一頓才行——」"
    h "「不是啦！繼續下去我要生氣了喔！！{p}\ \ \ 再說，我們現在要修行的不就是意志力跟信念嗎？{p}\ \ \ 文化上的修行也是很重要的喔。{p}\ \ \ 所以要看電影、還有聽音樂，吸收一下裡面的內涵才能有所成長呀！」"
    k "「原來如此，的確有道理。」"
    h "「所以，哥哥今晚的功課就是這個—— 拿著去那邊租了吧。」"
    "遙遞給我的是她剛才訓練時說的電影《武太極門》。"
    "而她則是抱著另一部電影在胸前，陶醉在自己的世界之中。"
    #hide cg_disco
    #with dissolve
    k "「不好意思，請讓我租一下這個。」"
    "{color=#FFFFFF}？？？{/color}" "「嗯，可以喔。退還的日期已經寫再收據上了。」"
    "店員先生不但有禮貌的笑容，還幫我把電影裝進袋子裡面，{p}然後雙手拿著袋子交到我手裡。"
    k "「喔喔，謝謝。」"
    "{color=#FFFFFF}？？？{/color}" "「嗯！下次再見。薄扶林能力特殊科的同學。」"
    k "「欸？你認識我們嗎？」"
    "{color=#FFFFFF}？？？{/color}" "「嗯，當然認識了。因為是我們的好對手。」"
    "這時我轉頭才發現，遙的雙眼發出的已經不止是普通的金光了。{p}嗯，兩眼發青光的程度也到了。"
    #show cg_disco_wing
    #with dissolve
    h "「哥哥！！！怎麼會在這裡！！！！！{p}\ \ \ 可以給我簽個名嗎？？？」"
    "——欸？！"
    "所以，這就是哥哥嗎？！"
    "喔喔，這麼看上去，他的確眉目清秀，待人有禮，而且真情流露，{p}出道以來，後輩對他的評價也非常不錯。"
    "而且對粉絲也是非常寵愛，這一點對於遙來說應該特別重要吧。{p}感覺上就連男生也會被他的氣質迷倒吧。"
    "{color=#FFFFFF}Wing{/color}" "「噓... 我今天是來代替我校的朋友的更...他病倒了所以沒人看店。」"
    "Wing接過唱片盒子，簽了名。"
    h "「...欸～ 原來哥哥還在讀書嗎？」"
    "{color=#FFFFFF}Wing{/color}" "「嗯，是的。今年就最後一年了，我跟阿Fong也是呢。」"
    h "「——欸～～原來Fong姐也是嗎！」"
    "{color=#FFFFFF}Wing{/color}" "「我們兩個也是旺角彌敦中學的代表。{p}\ \ \ 要是你們的目標也是校際大賽的話，我們就早晚會遇見呢。」"
    k "「嗯，我們班也會向校際大賽的目標進發。」"
    h "「啊啊啊啊啊！早知道入旺角彌敦中學啦！！！{p}\ \ \ 失算了！！！！」"
    "遙壓低聲線呼喊著心中巨大的遺憾，而Wing見狀也瞇著眼睛地笑了。"
    "{color=#FFFFFF}Wing{/color}" "「哈哈哈，那麼遙小姐，下次見面的時候，或許就是敵人了喔。」"
    h "「那麼要是我們贏了，那時候可以跟你合照嗎？？」"
    "{color=#FFFFFF}Wing{/color}" "「嗯！那到時再聊吧。{p}\ \ \ 人開始多，我也差不多要戴口罩遮著臉了。」"
    k "「啊哈哈，當歌手真辛苦呢。」"
    h "「我們也差不多回去了，哥哥，下次見！」"
    #hide cg_disco_wing
    #with dissolve
    "跟Wing先生道別後，我們便踏出了信和中心。"
    "遙的臉上還是一副陶醉的樣子，{p}果然她一說到自己喜歡的東西時就會完全失去冷靜呢。"
    "不過感覺真奇妙，遙叫其他人做哥哥的時候，有一種奇怪的感覺。{p}不管了，眼前最需要集中精神的，應該是我們的合作技能。"
    "今晚回去後把電影看了，再試著腦內模擬一下今天的練習吧。"
    hide mk
    with dissolve
    pause 1.0
    show home_t_n:
        xoffset -15
    with dissolve
    "今天我們照舊先到司的家吃飯，之後才回家睡覺。"
    show thome
    with dissolve
    k "「我們回來了～司，在嗎～」"
    hide home_t_n
    show tsukasa
    show tsukasa:
        alpha 0.0
    show tsukasa:
        linear 0.2 alpha 1.0
    t "「喔喔！等你們好久了！{p}\ \ \ 剛剛去幹嘛了？呵呵～兩兄妹私下的約會嗎？」"
    show haruka_e3
    show haruka_e3:
        alpha 0.0
        xalign 0.8
    show haruka_e3:
        xoffset 50
    show haruka_e3:
        linear 0.2 xoffset 0 alpha 1.0
    show tsukasa:
        linear 0.2 xalign 0.2
    h "「才不是了～ 我們剛剛修行後，去了旺角的唱片店。」"
    k "「嗯，然後遇上了我們未來的對手。」"
    show haruka_e3:
        linear 0.2 alpha 0.0
    show tsukasa:
        linear 0.2 alpha 0.0
    hide thome
    with dissolve
    pause 1.0
    show thome
    with dissolve
    hide haruka_e3
    show haruka_s
    show haruka_s:
        xalign 0.8
        alpha 0.0
    show tsukasa zorder 100
    show haruka_s:
        linear 0.2 alpha 1.0
    show tsukasa:
        linear 0.2 alpha 1.0
    t "「欸～ 旺角彌敦中學啊...{p}\ \ \ 聽上去挺厲害呢，畢竟他們那邊有不同的文化和文化載體...{p}\ \ \ 每天接觸著，搞不好到大賽時會比我們有更強的意志力呢！」"
    show haruka_l
    show haruka_l:
        xalign 0.8
        alpha 0.0
    show haruka_l:
        linear 0.2 alpha 1.0
    h "「司每次說到意志力和武功這些話題就會緊張起來，這點也是多年不變呢～」"
    hide haruka_s
    k "「說起來，司你今天打算做什麼飯？」"
    t "「界，你問了一個非常有焦點的問題——今天吃什麼？就讓你們猜一下吧。」"
    k "「日本菜？泰國菜？」"
    t "「真是膚淺。」"
    t "「...今天，我們缺乏了浪漫。{p}\ \ \ 缺乏了男人的浪漫！！{p}\ \ \ 所以今天吃豆腐火腩飯！！！」"
    show haruka_e3
    show haruka_e3:
        xalign 0.8
        alpha 0.0
    show haruka_e3:
        linear 0.2 alpha 1.0
    "{color=#FFFFFF}界、遙{/color}" "「呃......」"
    hide haruka_l
    show haruka_s
    show haruka_s:
        xalign 0.8
        alpha 0.0
    show haruka_s:
        linear 0.2 alpha 1.0
    h "「難道，司今天修行得挺順利嗎？」"
    hide haruka_e3
    "司聽到便更高興哋翻兜著熱鍋裡面的燒肉。"
    t "「對呢... 成熟的能力者跟這裡每一塊火腩一樣，{p}\ \ \ 是要經過鴻鴻烈火、經過百度高溫。我們需要經過歷練和試煉。」"
    show haruka_su
    show haruka_su:
        xalign 0.8
        alpha 0.0
    show haruka_su:
        linear 0.2 alpha 1.0
    h "「但司你今天不是在薄扶林瀑布練功來著嗎？」"
    hide haruka_s
    t "「沒錯。在一整個下午的修行裡面，我終於明白了...」"
    k "「明白你個頭！你又自己一個出去偷練了嗎？」"
    "我敲了敲司的頭。"
    t "「咕呃...{w}喂，你怎麼能敲大廚的頭！廚房很危險的喔！」"
    k "「怎麼只有上學期間總是找不到你呀...{p}\ \ \ 所以呢？你現在的基礎值又變高多少了？」"
    t "「哼！為自己有這麼上進的朋友感到自豪吧，{p}\ \ \ 我的基礎值現在可是4000了喔！力量更是有1200的高數值！」"
    k "「哇... 果然是偷練專家...我強化後才只有1350而已。」"
    show haruka_l
    show haruka_l:
        xalign 0.8
        alpha 0.0
    show haruka_l:
        linear 0.2 alpha 1.0
    h "「司這就對了，多灌輸這種價值觀給哥哥吧，{p}\ \ \ 不然畢業後都不知能不能被聘請呢～」"
    hide haruka_su
    t "「這種價值觀才不是灌輸的呢！是要尋找目標！知道了嗎——{w}喔。」"
    "叮咚～"
    "門鈴在這種時間響起來了，是有誰來了嗎？"
    t "「啊啊，來了來了～"
    show haruka_l:
        linear 0.2 alpha 0.0
    show tsukasa:
        linear 0.2 alpha 0.0
    hide thome
    with dissolve
    #show cg_wholefamily_wo_t
    #with dissolve
    hide haruka_l
    hide tsukasa
    t "光、幸！歡迎歡迎～ 今天真是辛苦了～」"
    h "「喔喔！竟然是放學後同學會？！」"
    hk "「哈囉～ 各位臣下，還有力氣high下去嗎～」"
    s "「我們買了雪糕和糖水來喔。而且是西灣河直送、日月記糖水。」"
    k "「哇啊！太幸福了！你們今天去西灣河了嗎？」"
    hk "「沒錯！我和這位臣下一起到東區訓練了～不過這傢伙不喜歡晒太陽呢～{p}\ \ \ 天氣這麼熱，讓她脫下校服居然也不肯。」"
    s "「很熱的好不好。何況我已經跟著你搭電車把整個港島都經過了一遍了，{p}\ \ \ 就不能欣賞一下我的耐性嗎？」"
    hk "「哈哈，為了吾等的宏大計畫而犧牲，這也是你的榮耀！」"
    s "「...你這傢伙～」"
    h "「好啦～不如我們先來鋪一下桌面吧～光你拿一些筷子來可以嗎？{p}\ \ \ 幸就跟我一起把餸菜捧出來～哥哥你來裝飯吧！」"
    "{color=#FFFFFF}光、幸、界{/color}" "「好的！」"
    "這麼開心熱鬧的吃飯時間，我們到底有多久沒經歷過呢？"
    "回想起來，司因為是留學生，沒有父母在家，由小學開始便過著獨自生活的日子。{p}那時在公園偶然遇上我們，才開始每日來往。"
    "有時候我們一家人會邀請司來家中吃飯，{p}不過車禍之後，大多也是司邀請我們來他家一起做飯，然後才會回家。"
    "其實，司應該是討厭獨自歸家時的寂寞吧。"
    "不過幸好今年開始又多了兩個成員，吃飯團隊的人數由三人增加到現在的五人，{p}說實話我也非常高興。"
    "吃飯當然是越多人越好的嘛。"
    #show cg_wholefamily
    #with dissolve
    #hide cg_wholefamily_wo_t
    t "「這樣，最後一道菜就做好了。」"
    "司拿著最後一碟菜，擺上桌面，讓大家眼前一亮。"
    hk "「哇！司你做飯那麼厲害的嗎？！{p}\ \ \ 感覺每一道菜都很專業。」"
    s "「而且香氣撲鼻，色澤也很豐富。」"
    t "「嘿嘿，我只不過是買了漂亮的碗碟來盛著飯罷了～{p}\ \ \ 不信我明天全用電飯煲一次煮熟，攪拌好再用碗蓋一個形狀，最後盛到碟上，{p}\ \ \ 不也跟外面餐廳看起來一樣嘛～」"
    k "「聽著已經覺得很複雜了...」"
    t "「欸，別腦死啦。現在開飯吧！大家趁熱吃喔！」"
    "{color=#FFFFFF}眾人{/color}" "「我不客氣了～ 哈嗯」"
    "看著光跟幸把飯送進嘴裡。我們三個已經準備好看她們的反應了。"
    "{color=#FFFFFF}光、幸{/color}" "「啊！好好吃喔！！」"
    h "「別看司這樣，他自己住了這麼多年，還是有點技術的。」"
    s "「...搞不好比我廚藝還好呢。」"
    "這樣一起坐著吃飯的風景真叫人享受。"
    "想到從明天開始，我們每天都會一起吃飯，便有一種莫名的雀躍。"
    hk "「對喔，幸你上年也是特殊能力班的吧？」"
    s "「誒，嗯。是這樣。」"
    hk "「其實這個校際大賽的規模有多大？」"
    s "「全城有18間學校，其中有四間最強名校。{p}\ \ \ 我們要在淘汰賽勝出，最後挑戰被坊間譽為「四聖獸」的學校。」"
    h "「四聖獸是哪四間？他們很強嗎？」"
    t "「這個我反而有一點見聞。{p}\ \ \ 前幾天上網查有關練功的資料的時候，剛好看到了。{p}\ \ \ 『四聖獸』，只要有心挑戰大賽的話，肯定要面對的強敵。」"
    t "「其中以『白虎』為首，真身是中環的聖保羅聯合中學。{p}\ \ \ 因其騎士道的高潔精神和其強大而聞名全城。」"
    t "「接著排名第二的『青龍』是城中惡霸——九龍城寨中學。{p}\ \ \ 裡面的學生主要是不良學生、古惑仔、超級校園霸王之類。」"
    t "「擁有『朱雀』的芳名的啟德中學，裡面的學生大多都能好好掌握飛行系技能，{p}\ \ \ 因此在自由的戰鬥裡面佔有很大的優勢。」"
    t "「隱藏於大西北的深山之中的『玄武』——天水門中學，{p}\ \ \ 是位於新界西北部的一個師門，裡面的人打的功夫非常著重防禦。」"
    t "「至於這個都市的最終boss，就無從知曉了。{p}\ \ \ 但是好像挑戰過的人都會被全世界的大企業所爭奪，{p}\ \ \ 畢業後入職完全沒有難度。」"
    hk "「到大公司就職還不如當我的臣下呢～{p}\ \ \ 不過真有這麼好的待遇，怪不得世界各地那麼多人慕名而來。」"
    s "「那種東西見仁見智吧。{p}\ \ \ ——啊，光你幹嘛搶了我的燒肉！」"
    hk "「嘿嘿，沒所謂啦～我跟妳也是拍檔一場～{p}\ \ \ 要不我把豆腐給妳吧、啊啊～嗯！」"
    h "「吃飯要有規有矩啊，別搶來搶去！」"
    "{color=#FFFFFF}司、界{/color}" "「男人的浪漫當然不能揀擇，全吃掉才是王道。」"
    "{color=#FFFFFF}光、遙、幸{/color}" "「男生果然要在這種場合才能團結...」"
    t "「啊哈哈，就是這種場合才需要團結嘛，對吧！界！」"
    k "「司，說得好！」"
    "就是這樣，我們的晚飯時間在歡樂之中度過。"
    "夜晚8點，我們便各自回家。{p}想必司也會為今天感到很高興吧。"
    #hide cg_wholefamily_wo_t
    #with dissolve
    pause 1.0
    #show nrth
    #with dissolve
    "月光伴著天上的星空，在為我跟遙引著路。"
    "海邊的晚風今天也輕輕吹拂著。"
    "在我身旁的遙，高興的踏著步，嘴邊哼起她喜歡的歌。"
    show haruka_s
    show haruka_s:
        alpha 0.0
    show haruka_s:
        linear 0.2 alpha 1.0
    k "「我們五個人，感覺也相處得挺自在的呢。」"
    show haruka_lb
    show haruka_lb:
        alpha 0.0
    show haruka_lb:
        linear 0.2 alpha 1.0
    h "「嗯？是呀。」"
    hide haruka_s
    k "「感覺有點懷念以前的日子了。{p}\ \ \ 那時我們每天也是這麼傻氣地鬧著玩，不知不覺又過了一天。」"
    h "「不過長大後就收斂了呢～ 哥哥和司也是。"
    show haruka_su
    show haruka_su:
        alpha 0.0
    show haruka_su:
        linear 0.2 alpha 1.0
    extend "\n\ \ \ 你們還記得自己曾經有多淘氣嗎？」"
    hide haruka_lb
    k "「哼... 好像有一次，司拉著我條進海港裡面了，{p}\ \ \ 結果最後被漁船上的伯伯就上來，還大罵了我們一頓呢！」"
    show haruka_lb
    show haruka_lb:
        alpha 0.0
    show haruka_lb:
        linear 0.2 alpha 1.0
    h "「哈哈哈，是呀！那時我去找也找不到你們，怎麼料到你們居然在船上！」"
    hide haruka_su
    k "「還有一次我在公園玩氹氹轉，用盡力氣結果就把司給轉了出去！{p}\ \ \ 那次被他打得真痛呢...」"
    show haruka_e4
    show haruka_e4:
        alpha 0.0
    show haruka_e4:
        linear 0.2 alpha 1.0
    h "「啊！那次他飛出來差點把我撞倒了！你們兩個真的是搗蛋組合呢。」"
    hide haruka_lb
    k "「那時有首歌，你還記得怎麼唱嗎？{p}\ \ \ 氹氹轉、菊花園，炒米餅...」"
    show haruka_l
    show haruka_l:
        alpha 0.0
    show haruka_l:
        linear 0.2 alpha 1.0
    h "「真是的，記這些瑣事就最厲害了，哈哈」"
    hide haruka_e4
    k "「遙不喜歡記瑣碎事的話就我來記唄～」"
    show haruka_l:
        linear 0.2 alpha 0.0
    "只見遙閉起眼，輕輕地把頭靠到我的肩上。"
    h "「嗯。交給哥哥了。」"
    hide haruka_l
    "嘴角流露著淺笑。"
    "我把手心貼到她的頭頂，溫柔的掃了掃。"
    k "「嗯。交給我吧。」"
    "今夜的星空也是如此美麗。"
    "跟舊時一樣美麗。"
    #hide nrth
    #with dissolve
    $ quick_menu = False
    window hide dissolve
    show childhood2_1
    with dissolve
    pause 2.0
    hide childhood2_1
    with dissolve
    show cwb_timesquare:
        xoffset -50
    with dissolve
    $ quick_menu = True
    window show dissolve
    show haruka_s
    show haruka_s:
        alpha 0.0
    show haruka_s:
        linear 0.2 alpha 1.0
    h "「幸～」"
    show sachi_n zorder 100
    show sachi_n:
        alpha 0.0
        xalign 0.6
    show sachi_n:
        xoffset 50
    show sachi_n:
        linear 0.2 xoffset 0 alpha 1.0
    show hikari_su4_sb zorder 98
    show hikari_su4_sb:
        alpha 0.0
        xalign 0.8
    show hikari_su4_sb:
        xoffset 50
    show hikari_su4_sb:
        linear 0.2 xoffset 0 alpha 1.0
    show haruka_s:
        linear 0.2 xalign 0.2
    s "「啊，遙，妳來了嗎。」"
    show hikari_l2_s zorder 101
    show hikari_l2_s:
        alpha 0.0
        xalign 0.8
    show hikari_l2_s:
        linear 0.2 alpha 1.0
    hk "「吾，從背後偷襲！」"
    hide hikari_su4_sb
    show hikari_l2_s:
        linear 0.1 xalign 0.5
    pause 0.1
    show sachi_n:
        linear 0.05 xalign 0.9
    "幸一個華麗轉身，躲開了光的飛撲。"
    show hikari_su3_sf zorder 102
    show hikari_su3_sf:
        alpha 0.0
    show hikari_su3_sf:
        linear 0.2 alpha 1.0
    hk "「哎呀！」"
    hide hikari_l2_s
    show hikari_su3_sf:
        easein 0.2 alpha 0.0 yoffset 50
    "在星期六的銅鑼灣街口，光摔了個大交，四腳朝天。"
    show haruka_n
    show haruka_n:
        alpha 0.0
        xalign 0.2
    show haruka_n:
        linear 0.2 alpha 1.0
    h "「光...妳沒事吧？」"
    hide haruka_s
    show hikari_e2_b2
    show hikari_e2_b2
    show hikari_e2_b2:
        alpha 0
        yoffset 50
    show hikari_e2_b2:
        easein 0.5 alpha 1.0 yoffset 0
    hk "「嗚嗚...遙～～」"
    "遙向光伸出善良的手，而光則是眼淚汪汪地看著她。{p}這光景，怎麼讓我想起了主人跟小狗的相處..."
    show hikari_a
    show hikari_a:
        alpha 0.0
    show hikari_a:
        linear 0.2 alpha 1.0
    hk "「嗚嗚... 我今天一定要大爆買！一報雪恥！！」"
    hide hikari_e2_b2
    show haruka_s
    show haruka_s:
        xalign 0.2
        alpha 0.0
    show haruka_s:
        linear 0.2 alpha 1.0
    h "「啊哈哈... 嘛，我們倒是沒有所謂啦。{p}\ \ \ 那麼，這樣就人齊了嗎？」"
    hide haruka_n
    s "「嗯，出發吧。」"
    show hikari_a:
        linear 0.2 xoffset -50 alpha 0.0
    show haruka_s:
        linear 0.2 xoffset -50 alpha 0.0
    show sachi_n:
        linear 0.2 xoffset -50 alpha 0.0
    "三位女生笑著，向大街邁出了步伐。{p}看著面前的溫馨景象，我們再次提問。"
    hide hikari_a
    hide haruka_s
    hide sachi_n
    show tsukasa
    show tsukasa:
        alpha 0.0
        xoffset 50
    show tsukasa:
        linear 0.2 xoffset 0 alpha 1.0
    show cwb_timesquare:
        linear 0.2 xoffset 0
    t "「所以...」"
    k "「為什麼...」"
    "{color=#FFFFFF}司、界{/color}" "「為什麼我們也要出來逛街啦！！？」"
    hide tsukasa
    with dissolve
    hide cwb_timesquare
    with dissolve
    "兩個小時前。"
    hide haruka_s
    show hroom
    with dissolve
    show haruka_s
    show haruka_s:
        alpha 0.0
    show haruka_s:
        linear 0.2 alpha 1.0
    #play sound "ring.mp3"
    h "「喂，幸～ 早安啊。你怎麼了？」"
    show sroom_half
    show sroom_half:
        xoffset 960
        alpha 0.0
    show sroom_half:
        linear 0.2 xoffset 0.0 alpha 1.0
    show haruka_s:
        linear 0.2 xalign 0.2
    pause 0.2
    show sachi_n
    show sachi_n:
        xalign 0.8
        alpha 0.0
    show sachi_n:
        xoffset 50
    show sachi_n:
        linear 0.2 xoffset 0 alpha 1.0
    s "「遙...等下可以跟我一起逛街嗎？」"
    show haruka_lb
    show haruka_lb:
        alpha 0.0
        xalign 0.2
    show haruka_lb:
        linear 0.2 alpha 1.0
    h "「嗯，那天我剛好沒事做，你有什麼想看的嗎？」"
    hide haruka_s
    show sachi_t
    show sachi_t:
        xalign 0.8
        alpha 0.0
    show sachi_t:
        linear 0.2 alpha 1.0
    s "「有東西要買... "
    hide sachi_n
    show sachi_n
    show sachi_n:
        xalign 0.8
        alpha 0.0
    show sachi_n:
        linear 0.2 alpha 1.0
    extend "下個月的文化祭我可能要看看如何準備。」"
    hide sachi_t
    show haruka_e3
    show haruka_e3:
        xalign 0.2
        alpha 0.0
    show haruka_e3:
        linear 0.2 alpha 1.0
    h "「要是搬東西的話，叫上兩個男生肯定會比較輕鬆呀！"
    hide haruka_lb
    show haruka_su
    show haruka_su:
        alpha 0.0
        xalign 0.2
    show haruka_su:
        linear 0.2 alpha 1.0
    extend"啊，那不如也叫上光吧！」"
    hide haruka_e3
    s "「嗯，這樣更好。」"
    show haruka_l
    show haruka_l:
        alpha 0.0
        xalign 0.2
    show haruka_l:
        linear 0.2 alpha 1.0
    h "「那就等下11點，時代廣場等吧。」"
    hide haruka_su
    s "「好的，到時見。」"
    #play sound "cutline.mp3"
    show sroom_half:
        linear 0.2 xoffset 50 alpha 0.0
    show sachi_n:
        linear 0.2 xoffset 50 alpha 0.0
    pause 0.2
    show haruka_l:
        linear 0.2 xoffset -50 alpha 0.0
    pause 0.2
    show hroom
    with dissolve
    show kliving
    with dissolve
    #play sound "game.mp3"
    # cg?
    k "「左邊！！左邊有敵人！！」"
    hide haruka_l
    hide sachi_n
    show tsukasa
    show tsukasa:
        alpha 0.0
    show tsukasa:
        linear 0.2 alpha 1.0
    t "「別顧著指指點點，快點炸爆你後面那兩個鬼！」"
    k "「幹！射歪了」"
    t "「你怎麼炸到我了？老子半條血被你炸走了欸。」"
    k "「等等，你別過來，左邊！左邊的敵人要衝上來——」"
    t "「界你這混蛋！！！」"
    show tsukasa:
        linear 0.2 alpha 0.0 yoffset 50
    #play sound "fight.mp3"
    k "「啊啊啊啊———！」"
    show haruka_e4
    show haruka_e4:
        alpha 0.0
        xoffset 50
    show haruka_e4:
        linear 0.2 xoffset 0 alpha 1.0
    h "「這些遊戲好玩嗎？看你們玩得那麼氣憤。」"
    show haruka_e4:
        linear 0.2 xalign 0.8
    show tsukasa:
        xalign 0.2
    show tsukasa:
        linear 0.1 yoffset 0 alpha 1.0
        linear 0.05 xoffset 25
        linear 0.05 xoffset -25
        linear 0.05 xoffset 25
        linear 0.05 xoffset -25
        linear 0.05 xoffset 25
        linear 0.05 xoffset 0
    show kliving:
        linear 0.1 truecenter zoom 1.05
        linear 0.05 xoffset 50
        linear 0.05 xoffset -50
        linear 0.05 xoffset 50
        linear 0.05 xoffset -50
        linear 0.05 xoffset 50
        linear 0.05 xoffset 0
        linear 0.1 truecenter zoom 1
    "{color=#FFFFFF}司、界{/color}" "「當然好玩了！」"
    show haruka_ysd
    show haruka_ysd:
        alpha 0.0
        xalign 0.8
    show haruka_ysd:
        linear 0.2 alpha 1.0
    h "「但你們都打起來了。"
    hide haruka_e4
    show haruka_l
    show haruka_l:
        alpha 0.0
        xalign 0.8
    show haruka_l:
        linear 0.2 alpha 1.0
    extend "不如做點和平點的事吧？」"
    hide haruka_ysd
    k "「今天是週末、是自由時間喔...」"
    show haruka_l:
        linear 0.2 alpha 0.0
    show tsukasa:
        linear 0.2 alpha 0.0
    #Q版cg
    #show qcg2
    h "「嘻嘻嘻...」"
    hide kliving
    hide tsukasa
    hide haruka_l
    hide hroom
    "遙的笑容，不管見多少次還是很恐怖..."
    t "「不如不要？」"
    k "「感覺不妙...」"
    "說起來，我家有兩條家規。"
    "那好像是..."
    h "「——今天一起出去逛街吧～ 搬東西就交給你們咯！」"
    "家規① 不可違背遙。"
    "家規② 絕對要遵守家規①"
    h "「快點～ 換衣服去～～」"
    "{color=#FFFFFF}司、界{/color}" "「額欸～～」"
    "就是這樣，我們今天便出來銅鑼灣玩了。"
    #hide qcg2
    #show cg3
    k "「我們今天是來買什麼的呀...」"
    t "「...你確定這種問題問女生會有用嗎？」"
    "放眼銅鑼灣的街道，路上的行人都穿得很四正。"
    "這裡大多是馬路和電車路，而且紅綠燈也較多，\n因此除了廣場外的窄路，都基本上比較多車輛經過。"
    "我們也跟路人一樣，逍遙地逛著這街道。"
    "剛才也逛了幾間飲料店，大家拿著滿手的美食，正吃得津津有味。"
    hk "「嗯、嗯嗯嗯！這杯珍珠奶茶！真好喝！！！」"
    h "「光真是嘴饞呢～ 那麼快便想買東西吃了？」"
    hk "「我要去那邊的小食店買燒賣！」"
    t "「不是說好來看文化祭要用的服裝的嗎？」"
    h "「要不我們等下去U記看看衣服吧？」"
    hk "「U記！那裡有很多港漫合作T恤！！」"
    h "「就決定去那裡吧。\n\ \ \ 來～ 這裡有燒賣哦。」"
    hk "「啊啊！遙真的是天使！\n\ \ \ 啊～唔姆唔姆——喔喔喔！好吃！」"
    "遙用竹籤串著燒賣，小心翼翼地放進光的口裡。"
    s "「光你又吃又喝，小心變胖哦。」"
    "幸手裡也拿著竹蔗茅根的杯子，喝了一口。"
    hk "「明明真正上場打的是你～ 你才要多加注意呢！」"
    "靈機一閃的光又頂了幸的嘴。"
    s "「你再多說一遍...？」"
    "幸也握緊手裡的杯子，數滴水珠從蓋子滴了下來。"
    "街上的行人注視著我們，是我們太吵鬧了吧。"
    h "「你們別這樣... 在這裡打吵起來的話會被錄影放上網啦...」"
    t "「女人真麻煩呢，稍微吃一點就那麼介意了。」"
    "司也拿著熱騰騰的咖哩魚蛋，悠然自得地吃著。"
    k "「啊，最沒說服力的人開金口了。」"
    h "「對呢～ 都不知道是誰把『昨天吃太多，今天馬上去鍛鍊！』\n\ \ \ 這種話掛在嘴邊呢？」"
    k "「對呢～ 平常做飯前總是想著『嗯...這道菜的卡路里是多少呢？會不會太飽呢？』\n\ \ \ 之類的問題～」"
    hk "「哈哈，那高材生還真難當呢！」"
    t "「哼！沒了我做飯時的精打細算，你們就等著變胖子吧！」"
    #show cg3 zorder 100
    #hide cg3
    show cwb_timesquare
    with dissolve
    show hikari_a zorder 1
    show hikari_a:
        alpha 0.0
        xalign 0.2
    show hikari_a:
        linear 0.2 alpha 1.0
    show haruka_a2_b
    show haruka_a2_b:
        alpha 0.0
    show haruka_a2_b:
        linear 0.2 alpha 1.0
    show tsukasa
    show tsukasa:
        alpha 0.0
        xalign 0.8
    show tsukasa:
        linear 0.2 alpha 1.0
    pause 0.2
    show tsukasa:
        easein 0.5 xoffset 100
        pause 0.5
        easein 0.5 xoffset 200
        pause 0.5
        easein 0.5 xoffset 300
        pause 0.5
        easein 0.5 xoffset 400
        pause 0.5
        easein 0.5 xoffset 500
    hk "「司...司...！"
    show hikari_l1 zorder 1
    show hikari_l1:
        alpha 0.0
        xalign 0.2
    show hikari_l1:
        linear 0.2 alpha 1.0
    extend "你要繼續走那邊的話就bye bye啦！」"
    hide hikari_a
    show haruka_l
    show haruka_l:
        alpha 0.0
    show haruka_l:
        linear 0.2 alpha 1.0
    h "「哈哈哈，中途離隊了嗎？」"
    hide haruka_a2_b
    show tsukasa:
        linear 0.2 xoffset 0
    t "「才，才不是！U記就是這邊吧！我可是知道的！」"
    k "「別逞強啦，我們一起進去吧。」"
    show tsukasa:
        linear 0.2 xoffset -50 alpha 0.0
    show haruka_l:
        linear 0.2 xoffset -50 alpha 0.0
    show hikari_l1:
        linear 0.2 xoffset -50 alpha 0.0
    pause 0.2
    hide cwb_timesquare
    with dissolve
    hide haruka_l
    hide hikari_l1
    hide tsukasa
    show cwb_uniqlo:
        xoffset -50
    with dissolve
    show tsukasa
    show tsukasa:
        alpha 0.0
    show tsukasa:
        linear 0.2 alpha 1.0
    t "「喔喔，多久沒來這裡了 ? 裝潢變得漂亮了呢！」"
    k "「的確呢..."
    extend "平時我們那麼少來買衣服。」"
    show tsukasa:
        linear 0.2 xoffset -50 alpha 0.0
    show cwb_uniqlo:
        linear 0.2 xoffset -100
    show hikari_l2
    show hikari_l2:
        alpha 0.0
        xoffset 50
    show hikari_l2:
        linear 0.2 alpha 1.0 xoffset 0
    hk "「你看看這個!是那部 Season of Horoscope 的合作T喔！"
    show hikari_t2_s
    show hikari_t2_s:
        alpha 0.0
    show hikari_t2_s:
        linear 0.2 alpha 1.0
    extend "\n\ \ \ 買哪件好呢 ?"
    hide hikari_l2
    show hikari_l2_s
    show hikari_l2_s:
        alpha 0.0
    show hikari_l2_s:
        linear 0.2 alpha 1.0
    extend " 要不全都買吧！」"
    hide hikari_t2_s 
    show hikari_l2_s:
        linear 0.2 xoffset 50 alpha 0.0
    show cwb_uniqlo:
        linear 0.2 xoffset 0
    show sachi_t
    show sachi_t:
        alpha 0.0
        xoffset -50
    show sachi_t:
        linear 0.2 alpha 1.0 xoffset 0
    s "「......這件連衣裙——"
    hide hikari_l2_s
    show sachi_n
    show sachi_n:
        alpha 0.0
    show sachi_n:
        linear 0.2 alpha 1.0
    extend "不行，現在在辦正經事。」"
    hide sachi_t
    show sachi_n:
        linear 0.2 xalign 0.2
    show haruka_e5
    show haruka_e5:
        xalign 0.8
    show haruka_e5:
        alpha 0.0
        xoffset 50
    show haruka_e5:
        linear 0.2 xoffset 0 alpha 1.0
    h "「啊~ 這件連衣裙好可愛喔。"
    show haruka_l
    show haruka_l:
        xalign 0.8
    show haruka_l:
        alpha 0.0
    show haruka_l:
        linear 0.2 alpha 1.0
    extend "幸，你也喜歡這種的嗎?」"
    hide haruka_e5
    #tag: emotion missing
    #thinking with a little bit embarassed then return back to normal
    s "「嘛... "
    extend "我還是有留意這季的新款式的...」"
    show haruka_e5
    show haruka_e5:
        xalign 0.8
    show haruka_e5:
        alpha 0.0
    show haruka_e5:
        linear 0.2 alpha 1.0
    h "「哇，這件外套也很漂亮喔！很像Fong姐上次演唱會穿的那件！"
    hide haruka_l
    show haruka_e2b
    show haruka_e2b:
        xalign 0.8
    show haruka_e2b:
        alpha 0.0
    show haruka_e2b:
        linear 0.2 alpha 1.0
    extend "\n\ \ \ 啊... 不過這麽華麗的衣服要怎麼穿出街呀... "
    hide haruka_e5
    show haruka_ysd_t
    show haruka_ysd_t:
        xalign 0.8
    show haruka_ysd_t:
        alpha 0.0
    show haruka_ysd_t:
        linear 0.2 alpha 1.0
    extend "嗚......」"
    hide haruka_e2b
    show cwb_uniqlo:
        linear 0.2 xoffset -50
    show haruka_ysd_t:
        linear 0.2 xoffset -50 alpha 0.0
    show sachi_n:
        linear 0.2 xoffset -50 alpha 0.0
    show tsukasa
    show tsukasa:
        alpha 0.0
        xoffset 50
    show tsukasa:
        linear 0.2 xoffset 0 alpha 1.0
    t "「真是有意思。」"
    hide haruka_ysd_t
    hide sachi_n
    k "「什麼有意思呀?」"
    t "「你看看這個 —— 是新款的運動衣!"
    extend "\n\ \ \ 看他這麽薄，在冬天竟然還有意志力保暖功能!"
    extend "\n\ \ \ 這樣冬天練功就更輕鬆了!」"
    k "「哈啊... 又是練功的事嗎...」"
    t "「你沒興趣看這些嗎?」"
    k "「嗯..."
    extend " 我衣服基本上也足夠... "
    extend "而且基本上也是遙幫我挑的。」"
    t "「你這男人真沒用，都19歲還要妹妹幫你挑衣服嗎?」"
    k "「呃哈哈... 那我這次自己挑吧。」"
    show tsukasa:
        linear 0.2 alpha 0.0
    show haruka_big_lb
    show haruka_big_lb:
        alpha 0.0
    show haruka_big_lb:
        linear 0.2 alpha 1.0
    h "「好呀。就這樣吧!」"
    show haruka_big_lb:
        linear 0.2 xalign 0.2
    show hikari_big_p1
    show hikari_big_p1:
        xalign 1.0
    show hikari_big_p1:
        alpha 0.0
        xoffset 200
    show hikari_big_p1:
        linear 0.2 xoffset 150 alpha 1.0
    hk "「嗯！好主意！」"
    hide tsukasa
    camera:
        linear 0.05 xoffset 50
        linear 0.05 xoffset -50
        linear 0.05 xoffset 50
        linear 0.05 xoffset 0
    camera
    k "「哇，你們什麼時候在這裡的?」"
    show haruka_big_lb:
        linear 0.2 alpha 0.0
    show hikari_big_p1:
        linear 0.2 alpha 0.0
    show haruka_lb
    show haruka_lb:
        alpha 0.0
    show haruka_lb:
        xalign 0.2
    show haruka_lb:
        linear 0.2 alpha 1.0
    show hikari_p1
    show hikari_p1:
        alpha 0.0
    show hikari_p1:
        xalign 0.5
    show hikari_p1:
        linear 0.2 alpha 1.0
    show sachi_n
    show sachi_n:
        xalign 0.9
    show sachi_n:
        xoffset 50
        alpha 0.0
    show sachi_n:
        linear 0.2 xoffset 0 alpha 1.0
    #tag: missing emotion
    s "「剛剛看完自己喜歡的，打算來看看你們..."
    hide haruka_big_lb
    hide hikari_big_p1
    extend "\n\ \ \ 嘛... 我是不會對誰幫你選衣服有偏見啦...」"
    k "「啊啊啊啊啊啊別再說!!」"
    "這次，我向遙提出了以後自己選衣服的決定。"
    $show_default("haruka_55_e",0.2, "M")
    h "「那麼作為證明，就必須考考你的眼光了。」"
    hide haruka_lb
    k "「呃 ? 怎麼考...」"
    $hide_default("haruka_55_e","M")
    $hide_default("hikari_p1","M")
    $hide_default("sachi_n","M")
    pause 0.2
    hide cwb_uniqlo
    with dissolve
    hide haruka_e3
    hide hikari_p1
    hide sachi_n
    #tag: missing background
    show cwb_uniqlo_change
    with dissolve
    $renpy.show("hikari_35_l")
    $renpy.show("hikari_35_l",at_list=[alignx(0.2)])
    $renpy.show("hikari_35_l",at_list=[showoffset])
    $renpy.show("hikari_35_l",at_list=[transparent])
    $renpy.show("hikari_35_l",at_list=[seen])
    $show_default("sachi_3_n",0.8,"M")
    pause 0.2
    transform jumping:
        linear 0.05 yoffset 50
        linear 0.05 yoffset 100
        linear 0.05 yoffset 50
        linear 0.05 yoffset 100
    $renpy.show("hikari_35_l",at_list=[jumping])
    pause 0.2
    show hikari_12_l
    show hikari_12_l:
        alpha 0.0
        xalign 0.2
    show hikari_12_l:
        xoffset -75
        yoffset 100
    show hikari_12_l:
        linear 0.1 alpha 1.0
    pause 0.1
    hide hikari_35_l
    hk "「看看我穿這件吧~ 等一下，我很快去換~~」"
    $hide_default("hikari_12_l","R")
    #tag: missing emotion
    $show_default("sachi_1_t",0.8,"M")
    s "「不，痛T怎麼穿都一樣吧...」"
    hide sachi_3_n
    hide hikari_12_l
    hk "「才不是痛T呢!是合作商品!!」"
    hk "「嘿，嗯。完美!"
    #tag: missing sprite hikari_shifuku
    extend " 怎麼樣!好看吧!! {p}\ \ \ 畢竟是我這種特殊能力者，穿起來的氣質也是與別不同!」"
    $show_default("tsukasa",0.1,"L")
    show sachi_1_t:
        linear 0.2 xalign 0.9
    t "「喔喔!挺好看的欸... 不愧是潮童!」"
    k "「好看，很適合你呀。」"
    "潮童... 的確這身打扮會讓人聯想到這個詞語，卻沒有一點貶義在其中。{p}這件T恤配上熱褲，更加凸顯了光自由自在的個性。{p}就連頭上這頂帽子也襯托出了那種輕便、爽快的衣著風格。"
    hk "「嘿嘿~ 對吧對吧?」"
    #tag: missing emotion sachi_timid
    s "「那... 那可以請你幫我看看這款連身裙適合我嗎? 我沒有很大自信...」"
    show tsukasa:
        linear 0.1 yoffset 150
        linear 0.1 yoffset 100
    t "「沒關係，交給我們吧!」(大拇指)"
    $hide_default("sachi_1_t","R")
    s "「......嗯，可以了。"
    hide sachi_1_t
    #tag: missing sachi_shifuku
    extend "這樣... 還可以嗎...?」"
    k "「喔喔，好看。很合身呢。」"
    "這樣一看，幸的確有一種優雅氣質被這連身裙帶了出來。{p}雖然連身裙給人一種舒適寫意的感覺，{p}但幸那種稍微成熟的魅力把兩個風格混和得很好，令人不禁停下來細心欣賞。"
    "穿著這件連身裙，就能感覺到她平時做事有多麼細心。"
    t "「嗯，拿出自信來吧！幸姐！」"
    s "幸「那就好了。"
    extend "這件就買下來吧。」(微笑)"
    #hide sachi_shifuku 幸退場
    show tsukasa:
        linear 0.2 xalign 0.5
    "這樣就兩位，還剩一位。"
    "嗯，好期待呀。"
    t "「盯~~~」"
    k "「啊哈哈哈...」"
    show tsukasa:
        linear 0.2 xalign 0.8
    $show_default("haruka_54_e",0.2,"L")
    h "「看什麼啦，就那麼喜歡看人家試穿嗎...」"
    k "「沒有啊，因為是遙，所以會很期待。」"
    show tsukasa:
        linear 0.1 yoffset 150
        linear 0.1 yoffset 100
    t "「嗯！遙最讚啦！」"
    $show_default("haruka_113_su",0.2,"M")
    h "「什麼?! "
    hide haruka_54_e
    $show_default("haruka_272_s",0.2,"M")
    extend "不敢相信，你們居然這麼敢說喔......」"
    hide haruka_113_su
    t "「難道遙沒有看中的衣服嗎？？」"
    show tsukasa:
        linear 0.2 xalign 0.9
    show haruka_272_s:
        linear 0.2 xalign 0.5
    show haruka_272_s zorder 10
    $show_default("hikari_90_l",0.05,"L")
    hk "「難道你不想哥哥對衣服的眼光有所進步嗎~？？」"
    $show_default("haruka_293_a",0.5,"M")
    show haruka_293_a zorder 11
    h "「啊啊啊，好啦，我也進去換就是了!」"
    hide haruka_272_s
    $hide_default("hikari_90_l","M")
    $hide_default("tsukasa","M")
    $hide_default("haruka_293_a","M")
    hide cwb_uniqlo_change
    with dissolve
    "過了五分鐘..."
    hide haruka_293_a
    hide hikari_90_l
    hide tsukasa
    show cwb_uniqlo_change
    with dissolve
    $show_default("hikari_1_n",0.1,"M")
    $show_default("sachi_1_t",0.9,"M")
    pause 0.2
    $show_default("sachi_3_n",0.9,"M")
    s "「遙？你沒事嗎？」"
    hide sachi_1_t
    h "「呃...沒事......{w}就是有點害羞」"
    $show_default("hikari_267_t",0.1,"M")
    pause 0.2
    hide hikari_1_n
    hk "「有什麼好害羞的呢？！來吧！」"
    show hikari_267_t:
        linear 0.05 xalign 0.03
        pause 0.05
        linear 0.2 xalign 0.5
        pause 0.1
        linear 0.2 xalign 0.1
    $ renpy.pause(0.4, hard=True)
    $show_default("haruka",0.5,"R") #tag: for testing purpose need change to haruka_shifuku
    pause 0.1
    $show_default("hikari_53_l",0.1,"M")
    $show_default("sachi_2_s",0.9,"M") #tag: missing emotion
    "{color=#FFFFFF}眾人{/color}" "「喔、喔喔喔!」"
    hide hikari_267_t
    hide sachi_3_n
    hide haruka #tag: delete later after sprite is ready
    h "「怎樣... 適合嗎?」"
    $hide_default("hikari_53_l","M")
    $hide_default("sachi_2_s","M") #tag: missing emotion
    pause 0.2
    $show_default("tsukasa",0.5,"M")
    t "「果然遙真是最讚了!」" 
    #tag: missing emotion
    $hide_default("tsukasa","M")
    pause 0.2
    $show_default("sachi_2_s",0.9,"M")
    $show_default("hikari_53_l",0.1,"M")
    s "「嗯，非常好看喔。」"
    hide tsukasa
    $show_default("hikari_449_e",0.1,"M")
    hk "「哇，真羨慕呢~"
    hide hikari_53_l
    $show_default("hikari_39_l",0.1,"M")
    extend " 果然反差萌太可愛啦!!」"
    hide hikari_449_e
    $hide_default("hikari_39_l","M")
    $hide_default("sachi_2_s","M")
    "這件毛衣陪上格子裙實在太可愛了。"
    hide hikari_39_l
    hide sachi_2_s
    "看起來有點青春活潑的感覺，但回想起遙的務實態度，又能起一種中和的作用。{p}真是太好了，遙能找到這麼適合她的衣服。"
    k "「嗯，很好看喔。看起來很成熟呢。」"
    k "「遙很久沒買新衣服了吧？{w}不如這次就買下來吧。」"
    #tag: missing sprite haruka_shifuku
    h "「嗯，好吧... "
    extend "既然哥哥也這樣說。那就哥哥陪我一起付錢吧。"
    extend "嘿嘿~」"
    "遙湊了過來，繞著我的手臂，然後把我拖到了收銀台。"
    hide cwb_uniqlo_change
    with dissolve
    pause 0.2
    #show cwb_till #tag: missing background
    #with dissolve #tag: missing background
    show cwb_uniqlo_change
    with dissolve
    $show_default("haruka_141_l",0.5,"M")
    "{color=#FFFFFF}店員{/color}" "「哎呀，真是相親相愛呢~ 來陪女朋友買衣服嗎?」"
    $show_default("haruka_94_e",0.5,"M")
    h "「(欸!?)」"
    hide haruka_141_l
    "遙的用驚恐的眼神看了過來..."
    "我該怎麼辦呀..."
    "不過她也是的，追星時還要現在也是，異常高興的遙總會做些不可理喻的事情。"
    menu :
        "順勢承認" :
            jump ch2_agree
        "堅決否認" :
            jump ch2_disagree
        "含糊帶過" :
            jump ch2_subjective

label ch2_agree:
    $h_pts = h_pts + 1
    #"[h_pts] [hk_pts] [s_pts]"
    k "「對！她就是我女朋友！」"
    "{color=#FFFFFF}店員{/color}" "「噢~ 果然我的眼光很準，你們很匹配喔！有夫妻相！」"
    "「是嗎哈哈哈哈哈」"
    $show_default("haruka_182_y",0.5,"M")
    "遙更加抱緊界的手臂"
    hide haruka_94_e
    $show_default("haruka_137_l",0.5,"M")
    h "「哥哥... 謝謝你幫我解圍。」"
    hide haruka_182_y
    jump ch2_2

label ch2_disagree:
    k "「沒有，我們跟同學一起逛街而已。」"
    "{color=#FFFFFF}店員{/color}" "「喔呵？哼哼~~ {w}好吧，那麼玩得開心點喔~」"
    k "「欸...好的!」"
    $show_default("haruka_137_l",0.5,"M")
    h "「哥哥... 謝謝你幫我解圍。」"
    hide haruka_94_e
    jump ch2_2

label ch2_subjective:
    k "「呃哈哈... 不好意思我們有點趕時間...」"
    "{color=#FFFFFF}店員{/color}" "「啊，抱歉了。那麼謝謝惠顧。」"
    $show_default("haruka_137_l",0.5,"M")
    h "「哥哥... 謝謝你幫我解圍。」"
    hide haruka_94_e
    jump ch2_2

label ch2_2:
    k "「別在意啦，我們回大隊去吧。」"
    $hide_default("haruka_137_l","M")
    hide cwb_uniqlo_change
    with dissolve
    #hide cwb_till #tag: missing background
    #with dissolve #tag: missing background
    pause 0.2
    show cwb_backstreet
    with dissolve
    "各自在櫃檯付了錢後，我們便繼續逛著銅鑼灣的街道。"
    "在琳瑯滿目的櫥窗便四處遊走，感覺是有點眼花撩亂。{p}不過女生倒是看得很高興。"
    "到底我們什麼時候才能回家呢...？{p}心裏思念著今早玩過的遊戲，我一邊這麼祈求著。"
    #show qcg3 #tag: missing cg
    #with dissolve
    s "「啊，找到了。{p}\ \ \ 就是這個。」"
    hide cwb_backstreet
    "幸突然停下腳步，盯著櫥窗裡面一個商品。"
    s "「是這個了。」"
    k "「喔?這個是...」"
    "櫥窗裏的是一個掛頭式耳機。"
    h "「幸也喜歡聽音樂的嗎？你喜歡那個歌手呀？」"
    s "「欸？...啊，不是，我純粹喜歡聽純音樂。」"
    h "「這個耳機~ 也不算太貴，你要買嗎？」"
    s "「嗯...嗯。」"
    t "「那麼我們進店裡去吧。」"
    #hide qcg3 #tag: missing cg
    #with dissolve
    show cwb_logon #tag: missing bg
    with dissolve
    $show_default("haruka_1_n",0.2,"M")
    $show_default("tsukasa",0.8,"M")
    t "「這間雜貨店是什麼呀?居然連腹肌按摩器也有得賣!?」"
    k "「什麼!?這邊竟然有絕版的遊戲——志恆的大冒險??」"
    $show_default("haruka_314_a",0.2,"M")
    h "「呵呵，一開始是誰說不想出來的呀？」"
    hide haruka_1_n
    "{color=#FFFFFF}司&界{/color}""「是誰？誰說了？？給我出來!」"
    $hide_default("haruka_314_a","L")
    $hide_default("tsukasa","L")
    show cwb_logon:
        linear 0.2 xoffset -50
    $show_default("sachi_3_n",0.5,"R")
    "在店的角落，幸自己一個在看著耳機，還有旁邊的——女僕裝？"
    hide haruka_314_
    hide tsukasa
    k "「幸，你喜歡這種的嗎？」"
    #tag: missing emotion
    s "「呃...呃！不是不是。」"
    k "「那為什麼會在看這些呀？」"
    #tag: missing emotion
    s "「只是...有點懷念而已。」"
    "低著頭，幸露出了溫暖的笑容。 "
    "的確，這樣子的幸也挺有魅力。"
    k "「是以前的班級嗎？」"
    #tag: missing emotion
    s "「文化祭很好玩的。那時候跟同學辦冰室，很難忘。」"
    k "「這樣嗎...今年也要辦吧？{p}\ \ \ 你想辦什麼呢？」"
    #tag: missing emotion
    s "「不知道。」"
    k "「到時一起提議辦冰室吧！」"
    #tag: missing emotion
    s "「...欸？真的嗎？」"
    "既然能令幸高興，想必大家也會贊成吧。"
    k "「嗯。大家也會很高興的。」"
    #tag: missing emotion
    s "「嗯。"
    extend "謝謝你。」"
    $hide_default("sachi_3_n","M")
    $show_default("hikari_41_l",0.5,"M")
    pause 0.2
    $renpy.show("hikari_41_l",at_list=[jumping])
    pause 0.2
    show hikari_26_l
    show hikari_26_l:
        xalign 0.5
        alpha 0.0
    show hikari_26_l:
        xoffset -23
        yoffset 100
    show hikari_26_l:
        linear 0.1 alpha 1.0
    $ renpy.pause(0.1, hard=True)
    hide hikari_41_l
    hk "「喂！界！！你沒東西要買的話，我們先排隊付錢咯~」"
    k "「你...在店內小聲點說話啦。」"
    $show_default("hikari_215_p",0.5,"M")
    $ renpy.pause(0.2, hard=True)
    show hikari_26_l:
        linear 0.1 alpha 0.0
    hk "「額...對不起。嘿嘿。」"
    hide hikari_26_l
    show cwb_logon:
        linear 0.2 xoffset 0
    $hide_default("hikari_215_p","R")
    k "「等等，這套志恆的大冒險居然有特價？」"
    show chihanggame:
        xalign 0.5
        yalign 0.5
    with dissolve
    "那麼我今天也買這套遊戲回去玩一下吧。"
    "嗯，黑髮的女主角好像挺可愛的。"
    "回去後一定先要攻略她。"
    hide chihanggame
    with dissolve
    show cwb_logon:
        linear 0.2 xoffset -50
    $show_default("tsukasa",0.2,"R")
    $show_default("sachi_1_t",0.8,"R")
    t "「吶，幸~ 可以幫我個忙嗎？」"
    #tag: missing emotion
    s "「什麼...？」"
    t "「就是那個...你的能力~~"
    extend "\n\ \ \ 可以幫我複製一個嗎?」"
    #tag: missing emotion
    s "「那麼想練肌肉的話自己買不就好了。{w}我可不願做小偷。」"
    t "「嗚嗚... 好吧... 這個月不能買遊戲了。 」"
    $hide_default("sachi_1_t","R")
    show tsukasa:
        linear 0.2 xalign 0.5
    t "「不過！界，你會借給我玩的吧！！」"
    hide sachi_1_t
    k "「自己不買就借我的？！」"
    t "「我們都是死黨了，對不？」"
    k "「呃，這種時候才認死黨嗎...」"
    t "「說什麼呢~ 一直都是啦好不好~ 界真愛開玩笑！」"
    k "「你來我家玩吧。可不要借給你呢。」"
    t "「也可以！」"
    show tsukasa:
        linear 0.2 xalign 0.2
    $show_default("haruka_162_l",0.8,"R")
    h "「說起來，距離黃昏還有些時間。我們等下要去哪兒呀？」"
    t "「要去打卡嗎！我知道附近有電車可以去一個打卡地點喔！」"
    $hide_default("tsukasa","L")
    $hide_default("haruka_162_l","L")
    $show_default("hikari_42_l",0.5,"M")
    hk "「吾之僕人，立下功勞了。帶吾等前往那約定之地吧！」"
    hide tsukasa
    hide haruka_162_l
    $hide_default("hikari_42_l","L")
    "踏上電車的我們，朝著西環貨櫃碼頭出發。" 
    hide hikari_42_l
    hide cwb_logon
    with dissolve
    #tag: missing bg
    #show tram_cwb
    #pause 1.0
    #show tram_ktown
    #pause 1.0
    show igpier_1
    with dissolve
    $show_default("hikari_95_l",0.5,"M")
    hk "「喔喔喔！這個景色真不錯嘛！"
    $show_default("hikari_85_l", 0.5,"M")
    $show_shock("hk")
    extend "\n\ \ \ 以後這就是吾的據點了！以後在這裡建造聖城吧！」"
    hide hikari_95_l
    $hide_default("shock_animation","M")
    show hikari_85_l:
        linear 0.2 xalign 0.2
    $show_default("tsukasa",0.8,"M")
    t "「啊，這個pose挺好，就這樣站著~"
    #(喀擦)
    #tag: missing sound effect camera
    extend "好，再來一張portrait！"
    #(喀擦)
    #tag: missing sound effect camera
    extend "好了！」" 
    "真的像專業攝影師呀... 說不定司會是絕世好男友？"
    show hikari_78_l
    show hikari_78_l:
        xalign 0.2
        alpha 0.0
    show hikari_78_l:
        xoffset -75
        yoffset 100
    show hikari_78_l:
        linear 0.2 alpha 1.0
    $ renpy.pause(0.2, hard=True)
    show hikari_85_l:
        linear 0.2 alpha 0.0
    hk "「哇哈哈哈哈！」"
    hide hikari_85_l
    "海風吹過，讓光的披風擺動了起來。"
    "瞬間司的電話響起了一連串連拍聲。"
    #tag: missing sound effect explosion
    #——爆!
    camera:
        linear 0.05 xoffset 50
        linear 0.05 xoffset -50
        linear 0.05 xoffset 50
        linear 0.05 xoffset -50
        linear 0.1 xoffset 0
    pause 0.3
    "剛才那爆炸聲真是真實呢。"
    $hide_default("hikari_78_l","M")
    show tsukasa:
        linear 0.2 xalign 0.5
    k "「司，你什麼時候連爆炸效果都準備好了？」"
    hide hikari_78_l
    t "「...界。{w}那不是我啊。」"
    s "「看那邊。」"
    $hide_default("tsukasa","M")
    show tent
    with dissolve
    show speed zorder 100 :
        alpha 0.5
    #tag: missing effect electric aura, like the ones in dragon ball
    "遠處的帳篷內，隱約能看見兩個正在打鬥的人影。"
    hide igpier_1
    "還有他們的技能有如電光石火般，強而有力。"
    "正確來說，是一方設下陷阱，然後另一方不停地閃避、或者抵擋攻擊。"
    "我們走近帳篷，確認一下對方的身分。"
    #tag: missing sprite white tiger
    #tag: missing sprite blue dragon
    s "「什...」"
    t "「啊！那不是『白虎』跟『青龍』學生會會長嗎？！」"
    "開著『觀測』技能的司在一旁這麽說著。\n只見他一臉驚訝，目不轉睛地看他們的數值。"
    "『白虎』...『青龍』...？"
    "在貨櫃碼頭的柏油路上，冒出了兩團澎拜的氣場。"
    "穿著白西裝的男子散發紫色的意志力，而黑風衣的男子則是綠色的意志力氣場。{p}他們各自散發的意志力，都可以蓋過我們小隊全力的氣場。"
    transform shake:
        linear 0.05 xoffset 5
        linear 0.05 xoffset -5
        repeat
    show tent at shake
    "然而氣場並沒有就此停止，反而擴大至旁邊的路燈和貨櫃。"
    "浪潮湧起，海鷗亦瞬速飛走，離開這個戰鬥的爆心地。"
    hk "「氣場讓影像變形了。」"
    show tent:
        parallel:
            linear 5.0 blur 16
        parallel:
            linear 0.05 xoffset 5
            linear 0.05 xoffset -5
            repeat
    "像是被高溫燃燒著一般，氣場裏面的物件形狀開始扭曲，無法觀察清楚。"
    k "「司，能看到數值嗎？」"
    t "「——！{w}這...難以置信。」"
    k "「讀出來看看。」"
    t "「20000...25000......」"
    t "「『白虎』的力量略勝一籌，但『青龍』的技術高得能過扭轉局勢，\n\ \ \ 應該能打成平手。」"
    "司握緊拳頭，緊張地說道。"
    hk "「那... 那有什麼特別？」"
    t "「我們大賽就是要和這種人對戰呀。」"
    s "「...哼。」"
    "身穿白色西裝軍服的男子拿著劍和盾，跟對面身穿黑色皮外套的混混在對峙著。"
    #hide tent
    #pause 0.2
    hide tent
    with wipe_normal
    hide speed
    show igpier_3
    show igpier_3:
        alpha 0.0
    show igpier_3:
        linear 0.1 alpha 1.0
    "以驚濤拍岸為信號，兩人在一瞬間消失在空間之中。"







    

        
    


    

