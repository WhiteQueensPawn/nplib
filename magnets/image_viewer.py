import pyglet

window = pyglet.window.Window()
image = pyglet.resource.image('np_panda.png')


@window.event
def on_key_press(symbol, modifiers):
    if symbol == pyglet.window.key.A:
        print 'The "A" key was pressed.'
    elif symbol == pyglet.window.key.LEFT:
        print 'The left arrow key was pressed.'
    elif symbol == pyglet.window.key.RIGHT:
        print 'The right arrow key was pressed.'
    elif symbol == pyglet.window.key.UP:
        print 'The up arrow key was pressed.'
    elif symbol == pyglet.window.key.DOWN:
        print 'The down arrow key was pressed.'
    elif symbol == pyglet.window.key.ENTER:
        print 'The enter key was pressed.'


@window.event
def on_draw():
    window.clear()
    image.blit(0, 0)

pyglet.app.run()
