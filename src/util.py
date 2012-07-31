# LPC 2012 Coding competition entry
# Copyright (C) 2012  Lucas Robsahm
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

# Defines the different states
STATE_InGame = 1
STATE_NewGame = 2
STATE_GameOver = 3
STATE_GameComplete = 4

# Get the neighbour tiles to the position rec_center in tile_layer
def neighbour_tiles(rect_center, tile_layer):
    (pos_x, pos_y) = rect_center
    tile_rects = []
    # find the tile location
    tile_x = int((pos_x) // tile_layer.tilewidth)
    tile_y = int((pos_y) // tile_layer.tileheight)
    for diry in (-1, 0, 1):
        for dirx in (-1, 0, 1):
            try:
                if tile_layer.content2D[tile_y+diry][tile_x+dirx] is not None:
                    tile_rects.append(tile_layer.content2D[tile_y+diry][tile_x+dirx].rect)
            except:
                continue
    return tile_rects
