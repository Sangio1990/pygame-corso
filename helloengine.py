import sys
from engine.engine import Engine

# Global state variable
engine = Engine()

# Uncomment this to load the manually writter JSON file
engine.loadScene("savefiles/arkanoid.json")

# Uncomment this to load the savefile
# engine.loadScene("savefiles/prova2.json")

# game loop
engine.gameLoop()

sys.exit()
