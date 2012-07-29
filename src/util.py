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
