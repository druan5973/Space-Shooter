from gamelib import *

game = Game(700,500,"space shooter!",20)
monster = Image("monster.jpg",game)
monster.resizeTo(monster.width / 2, monster.height / 2)

monster.setSpeed(2,60)

cross = Image("images\\crosshair.png",game)
bk = Image("images\\space.jpg",game)
bk.resizeTo(game.width, game.height)

#game.viewMouse(False)

#Game Loop
while not game.over:
        game.processInput()
        bk.draw()
        monster.move(True)
        cross.moveTo(mouse.x,mouse.y)

        if monster.collidedWith(mouse):
                game.score += 10
                x = randint(monster.width,game.width - monster.width)
                y = randint(monster.height,game.height-monster.height)
                monster.moveTo(x, y)
                choice = randint(1,3)
                if choice == 1:
                        monster.speed += 4
                        game.time += 5
                elif choice == 2:
                        monster.resizeBy(-5)

        game.displayTime(200,0)
        game.displayScore(0,0)
        if game.time <= 0:
                game.over = True
        game.update(60)
#End Loop
game.drawText("Press [Space] to exit.",250,250,white,True)
game.wait(K_SPACE)

game.quit()
