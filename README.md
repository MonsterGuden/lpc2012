LPC2012 code competition game
=======

The competition is to create a game with given graphics in one month. First time ever for me to code a project in python but it worked out fine thanks to pygame.<br><br>
More information about the competition at http://lpc.opengameart.org/<br><br>
I hope that you like the game, enjoy!

Requirements
-------
python python-pygame, python-pyglet, map loader for 'tiled'

Installation instructions
-------

    sudo apt-get install --yes git python-pygame python-pyglet
    wget https://pytmxloader.googlecode.com/files/tiledtmxloader-3.0.3.114.zip
    unzip -x tiledtmxloader-3.0.3.114.zip
    cd tiledtmxloader-3.0.3.114
    sudo python setup.py install
    cd ..
    sudo rm -rf tiledtmxloader-3.0.3.114
    rm -rf tiledtmxloader-3.0.3.114.zip

To run the game
-------
In the folder where you found this file run this command: python src/run.py

    mkdir MonsterGuden
    cd MonsterGuden
    git clone git://github.com/MonsterGuden/lpc2012.git
    cd lpc2012
    python src/run.py

Controls
-------
- f to toggle between fullscreen and window mode
- n in menu to start a new game
- arrows to move the "character"
- escape to exit

Creating a tilemap
-------
- background in tile layer 0
- hero in tile layer 1
- collision objects in tile layer 2
- mission goal in tile layer 3
- hero object properties
    - sprite - path to the sprite
    - sprite_height - height of the sprite
    - sprite_width - width of the sprite
- enemies as object layer
    - enemie object properties (type enemy)
        - sprite - path to the sprite
        - sprite_height - height of the sprite
        - sprite_width - width of the sprite
    - enemie waypoint object properties (type waypoint)
        - number - the numer in the order the enemy should walk
