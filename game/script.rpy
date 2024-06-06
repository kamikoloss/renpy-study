define c = Character("千冬", color="#88FF88")


image black = Solid("#000000")
image white = Solid("#FFFFFF")

image chifuyu move:
    animation
    "chifuyu smile close"
    zoom 1.0
    xalign 0.5
    yalign 0.1
    ease_quint 0.5 zoom 1.5
    ease_quint 0.25 xalign -1.0
    ease_quint 0.25 xalign 2.0
    ease_quint 0.25 xalign 0.5


transform center:
    zoom 1.0
    xalign 0.5
    yalign 0.1

transform left:
    zoom 1.0
    xalign -1.0 # 0.5 - 1.5
    yalign 0.1

transform right:
    zoom 1.0
    xalign 2.0 # 0.5 + 1.5
    yalign 0.1


label start:
    scene black
    with Dissolve(1.0)
    scene bg city
    with Dissolve(1.0)

    "Ren'Py の新しいゲームを作成しました。"
    "{size=*2}普通に使いづらいんだけど！{/size}"
    "俺はとうとう耐えられなくなり――"

    scene white
    pause(0.1)
    scene bg city
    pause(0.1)
    scene white
    pause(0.1)
    scene bg city
    pause(0.1)
    scene white

    "ウッ！！！！！！"

    scene bg city
    with Dissolve(0.5)

    show chifuyu move
    with Dissolve(0.25)
    # move (1.25s)が終わるまで待つ
    pause(1.5)

    show chifuyu smile open
    with Dissolve(0.5)

    c "残像だよ。"

    return


label test:
    show chifuyu smile close at center
    with dissolve
    show chifuyu smile close at left
    with dissolve
    show chifuyu smile close at right
    with dissolve
    show chifuyu smile open at center
    with dissolve
