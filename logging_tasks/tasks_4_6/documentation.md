# Python Game Documentation

## Overview
This documentation provides detailed descriptions of the modules used in the "Type Monkey" game. Each section focuses on a specific module, describing its purpose and functionality.

## Modules

### 1. game.py
#### Purpose
The `game.py` module is the core of the "Type Monkey" game, integrating various components such as rendering, event handling, and word management. It uses the `pygame` library for graphical rendering and interaction.

#### Classes and Functions
- **Class: Main**
  - **Description**: Main game class encapsulating the game logic.
  - **Methods**:
    - `__init__()`: Initializes the game.
    - `update_text_position(self, font, width)`: Updates text position on the screen. As if right now it has to be in the very same file that operates with pygame screen.
    - **Nested Class: Render**
      - `render_all_points`: Renders all points, text and typed text or exit button.
- `playing`:
  - **Description**: Handles the main game loop, iterates over and over and calls every other logic - reffered as well as spine.

#### Global Variables
- `dimension`, `width`, `height`: Screen dimension.
- `screen`: Pygame screen object.
- `x_origin`, `y_origin`: Origin point coordinates.


### 2. killer_functions.py
#### Purpose
Each function is a different abilitiy that grants player an advantage and enhances his ability to eliminate points (words) from the screen faster. Each ability has different keybind {1,2,3,4}.


### 3. level_definition.py
#### Purpose
Defines level progression and experience points (XP).


### 4. meaningful_text.py
#### Purpose
Generates meaningful text, possibly for use in the game.

#### Functions
- `next_word(i)`: Returns the next word from a chosen book in the Gutenberg corpus.


### 5. point_generator.py
#### Purpose
Manages points and their movement in the game.

#### Functions
- `move_points(...)`: generates a vector
- `random_point_generator`: Generates random point for the word that gets displayed.
- `update_all_points`: Moves all points based on the vector from the `move_points` function.

### 6. random_word.py
#### Purpose
Is able to generate relatively common and meaningful word, this word gets displayed by the Render class and belong to some point on the display. and can be removed by typed out on the keyboard.
This function is called every 900ms as if right now.


