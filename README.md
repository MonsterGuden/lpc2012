lpc2012
=======

Liberated Pixel Cup 2012 Python game

- Requirements: python python-pygame, python-pyglet, map loader for 'tiled'

- Installation instructions
- - sudo aptitude install python-pygame
- - sudo aptitude install python-pyglet
- - wget https://pytmxloader.googlecode.com/files/tiledtmxloader-3.0.3.114.zip
- - unzip -x tiledtmxloader-3.0.3.114.zip
- - cd tiledtmxloader-3.0.3.114
- - sudo python setup.py install
- - cd ..
- - sudo rm -rf tiledtmxloader-3.0.3.114
- - rm -rf tiledtmxloader-3.0.3.114.zip

- To run the game:
- - In the folder where you found this file run this command: python src/run.py

- Controls:
- - f to toggle between fullscreen and window mode
- - n in menu to start a new game
- - arrows to move the "character"
- - escape to exit

- Creating a map:
- - background in tile layer 0
- - hero in tile layer 1
- - collision objects in tile layer 2
- - mission goal in tile layer 3
- - enemies as object layer
- - - enemie object properties (type enemy)
- - - - sprite - path to the sprite
- - - - sprite_height - height of the sprite
- - - - sprite_width - width of the sprite
- - - enemie waypoint object properties (type waypoint)
- - - - number - the numer in the order the enemy should walk
- - hero object properties
- - - sprite - path to the sprite
- - - sprite_height - height of the sprite
- - - sprite_width - width of the sprite
