import setup
from pyglet.math import Vec2
# devides map in 10 X 10 segmenints
map_segment_x = setup._screen_width / 12
map_segment_y = setup._screen_height / 12


List_of_game_maps = [   
   {
      "map_name"   : "plains",
      "bg_color"   : (150, 230, 100, 255),
      "path_color" : (150, 150, 100, 255),
      "map_path"   : [
         (Vec2(map_segment_x*0   , map_segment_y*6 )), # start, out of bound
         (Vec2(map_segment_x*4   , map_segment_y*6 )), 
         (Vec2(map_segment_x*4   , map_segment_y*10)), 
         (Vec2(map_segment_x*8   , map_segment_y*10)), 
         (Vec2(map_segment_x*8   , map_segment_y*4 )), 
         (Vec2(map_segment_x*13  , map_segment_y*4 )) ] # end, out of bound
   },
   {
      "map_name"   : "art",
      "bg_color"   : (150, 230, 100, 255),
      "path_color" : (150, 150, 200, 255),
      "map_path"   : [
         (Vec2(map_segment_x*2   , map_segment_y*13 )), # start, out of bound
         (Vec2(map_segment_x*2   , map_segment_y*2 )), 
         (Vec2(map_segment_x*10   , map_segment_y*2)), 
         (Vec2(map_segment_x*10   , map_segment_y*10)),
         (Vec2(map_segment_x*4   , map_segment_y*10)), 
         (Vec2(map_segment_x*4   , map_segment_y*3)),  
         (Vec2(map_segment_x*6   , map_segment_y*3 )), 
         (Vec2(map_segment_x*6  , map_segment_y*8 )),
         (Vec2(map_segment_x*-1   , map_segment_y*8))   
         ] # end, out of bound
   },
   {
      "map_name"   : "north",
      "bg_color"   : (150, 230, 100, 255),
      "path_color" : (200, 180, 100, 255),
      "map_path"   : [
         (Vec2(map_segment_x*13   , map_segment_y*-1 )), # start, out of bound
         (Vec2(map_segment_x*2   , map_segment_y*10 )), 
         (Vec2(map_segment_x*2   , map_segment_y*3)), 
         (Vec2(map_segment_x*10   , map_segment_y*10)),
         (Vec2(map_segment_x*10   , map_segment_y*-1))  
         ] # end, out of bound
   },
   {
      "map_name"   : "line",
      "bg_color"   : (150, 230, 100, 255),
      "path_color" : (170, 145, 130, 255),
      "map_path"   : [
         (Vec2(int(map_segment_x*4)   , int(map_segment_y*4))), # start, out of bound
         (Vec2(int(map_segment_x*6)   , int(map_segment_y*4))), 
         (Vec2(int(map_segment_x*6)   , int(map_segment_y*6))), 
         (Vec2(int(map_segment_x*4)   , int(map_segment_y*6))),
         ] # end, out of bound
   },
]
