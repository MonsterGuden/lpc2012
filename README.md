lpc2012
=======

Liberated Pixel Cup 2012 Python game

- Requirements:
python-pygame, python-pyglet, map loader for 'tiled'

-Installation instructions
sudo aptitude install python-pygame
sudo aptitude install python-pyglet
wget https://pytmxloader.googlecode.com/files/tiledtmxloader-3.0.3.114.zip
unzip -x tiledtmxloader-3.0.3.114.zip
cd tiledtmxloader-3.0.3.114
sudo python setup.py install
cd ..
sudo rm -rf tiledtmxloader-3.0.3.114
rm -rf tiledtmxloader-3.0.3.114.zip

- To run the game:
In the folder where you found this file run this command:
python src/run.py

- Controls:
f to toggle between fullscreen and window mode
arrows to move the "character"
escape to exit

- Creating a map:
background in tile layer 0
hero in tile layer 1
collision objects in tile layer 2
mission goal in tile layer 3