"# Intro-AI-Pj"
This is my AI lab 1 report and source code. In order to run my code, you just open folder search and compile file pacman.py

    + Cmd to check the behavior of RandomAgent:
        python pacman.py --layout testMaze --pacman RandomAgent
        python pacman.py --layout tinyMaze --pacman RandomAgent
        python pacman.py --layout mediumMaze --pacman RandomAgent
        python pacman.py --layout bigMaze --pacman RandomAgent
    + cmd to check the behavior of BetterRandomAgent:
        python pacman.py --layout testMaze/tinyMaze/mediumMaze/bigMaze/myLayout/openSearch/... --pacman BetterRandomAgent
    + cmd to check the behavior of ReflexAgent:
        python pacman.py --layout myLayout --pacman BetterRandomAgent
        python pacman.py --layout openSearch --pacman BetterRandomAgent
