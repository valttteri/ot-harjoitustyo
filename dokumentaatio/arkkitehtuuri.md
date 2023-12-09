Ohjelman rakenne on suunnilleen seuraavanlainen

```mermaid
 classDiagram
    main -- loop
    loop -- gamestate
    gamestate -- levelhandler
    gamestate -- database_handler
    gamestate -- renderer
    levelhandler -- objects
    renderer -- displays

  class displays {
    default
    scores
}

  class objects {
    snake
    wall
    food
    grass
}
```

Ohjelma toimii seuraavalla tavalla, kun käyttäjä aloittaa uuden pelin:

```mermaid
sequenceDiagram
  actor User
  participant PygameWindow
  participant Main
  participant GameLoop
  participant GameStateHandler
  participant Renderer
  User->>Main: start program
  Main->>GameLoop: execute()
  GameLoop->>GameStateHandler: execute_state("start")
  GameStateHandler->>Renderer: render_screen("start")
  Renderer-->>PygameWindow: renders the starting screen
  User->>PygameWindow: press 1 to start
  PygameWindow-->>GameLoop: user pressed 1
  GameLoop->>GameStateHandler: execute_state("game_on")
  GameStateHandler->GameStateHandler: get_game_events()
  GameStateHandler->>Renderer: render the game screen
  Renderer-->>PygameWindow: renders the game screen
```
