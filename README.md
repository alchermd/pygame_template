# RZD

A barebones template for creating a new Pygame project.

## Quick Structure Overview

````
.
├──  rzd 
|    ├── assets
│    |  ├── audio
│    |  └── image 
|    ├── gamelib
|    │   ├── __init__.py
|    │   ├── palette.py
|    │   └── sprite.py
|    └── game.py 
├── run.py 
├── LICENSE
├── README.md
└── requirements.txt
````

* `rzd` - contains all game related data.

  * `rzd/assets` - contains audio and image files.

  * `rzd/gamelib` - contains classes for creating sprites and colors.

  * `rzd/game.py` - contains the `Game` class. The class is responsible for event handling, game logic, and draw functions.

* `run.py` - instantiates the `Game` class and runs the game. It also initializes the `pygame` engine.

  

## License

See [LICENSE](./LICENSE) for more information.