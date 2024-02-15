define Эми = Character("Эми", color = "#B22222", outlines = [ (absolute(2), "#fff", absolute(0), absolute(0)) ])
image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
define Луна = Character("Луна", color = "#AFEEEE", outlines = [ (absolute(2), "#fff", absolute(0), absolute(0)) ])
define Драко = Character("Драко", color = "#006400", outlines = [ (absolute(2), "#fff", absolute(0), absolute(0)) ])
define Фред = Character("Фред", color = "#800000", outlines = [ (absolute(2), "#fff", absolute(0), absolute(0)) ])
define Джордж = Character("Джордж", color = "#800000", outlines = [ (absolute(2), "#fff", absolute(0), absolute(0)) ])
define Близнец = Character("Фред(?)", color = "#800000", outlines = [ (absolute(2), "#fff", absolute(0), absolute(0)) ])
define Кто = Character("???", color = "#800000", outlines = [ (absolute(2), "#fff", absolute(0), absolute(0)) ])


label blue_start:      
    jump fred_start

label blue_scene1:
    scene black
    with Pause(1)

    play movie "movie_background.ogv" loop
    show movie with dissolve    
    blue_character "Ляляля иду по тропинке!"
    blue_character "Как же здорово, что снег идет"
    "Мы вышли на улицу"
    show lona_smile at left with dissolve
    show neville_smile_1 at right with dissolve
    Луна "Как приятно..."
    "Луна выбежала под снег и закружилась, вздымая вокруг себя белую пыль."
    blue_character "Стой!"
    "Я бросилась за ней, но поскользнулась и улетела вниз"
    hide movie with dissolve
    stop movie
    jump fred_start
 