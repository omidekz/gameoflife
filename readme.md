# Conway's Game Of Life [zero player game]
### you can find out from [wiki-pedia](https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life) 

<hr>

## Briefly game is:

  The universe is an infinite matrix and there are some cells and has 3 rules
 
 - Any live cell with two or three live neighbors survives.
 - Any dead cell with three live neighbors becomes a live cell. 
 - All other live cells die in the next generation. Similarly, all other dead cells stay dead.
 
 <hr>
 
 ## Usage
  - ### Configs
      you can edit configs file
   
        width             int, width of the universe
        height            int, height of the universe
        live_cell         str, represents live cells
        dead_cell         str, represents dead cells
        generation_sec    float, sleep time between each generation
        live_possibility  float, possibility of live cell in world init
        circular_world    bool, a bool that say world is circular or not 
  - ### gameoflife.py
      jus run
  
        python gameoflife.py
