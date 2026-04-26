# python-guess-game
This is a Python Guess Game.
The program generates a random number and the user tries to guess it.
#  Number Guessing Game

<div align="center">

![Python](https://img.shields.io/badge/Python-3.6%2B-blue?style=for-the-badge&logo=python&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Active-brightgreen?style=for-the-badge)
![Contributions](https://img.shields.io/badge/Contributions-Welcome-orange?style=for-the-badge)

A classic terminal-based number guessing game built in Python — with progressive difficulty, smart input validation, and round-based scoring. Simple to play, satisfying to beat.

</div>

---

##  Table of Contents

- [Demo](#-demo)
- [Features](#-features)
- [How to Play](#-how-to-play)
- [Getting Started](#-getting-started)
- [Game Logic](#-game-logic)
- [Project Structure](#-project-structure)
- [Roadmap](#-roadmap)
- [Contributing](#-contributing)
- [License](#-license)

---

##  Demo

```
==============================
Round 1
Guess a number between 1 and 100
You have 7 attempts!
==============================

Enter your guess: 50
Too high

Enter your guess: 25
Too low

Enter your guess: 37
Correct!  You guessed it in 3 attempts.

Do you want to play again? (yes/no): yes

==============================
Round 2
Guess a number between 1 and 150
You have 7 attempts!
==============================
```

---

##  Features

| Feature | Description |
|---|---|
| *Progressive Difficulty** | The number range expands by 50 with every new round |
| **Smart Hints** | Instant "Too high" / "Too low" feedback after each guess |
| **Input Validation** | Non-numeric inputs are rejected without wasting an attempt |
| **Multi-round Play** | Chain rounds together for a longer session |
| **Attempt Tracking** | Know exactly how many guesses it took to win |
|  **Game Over Reveal** | The secret number is revealed if you run out of attempts |

---

##  How to Play

1. A random secret number is chosen within the current range (starts at 1–100).
2. You have **7 attempts** per round to guess the number.
3. After each guess you'll be told if you're **too high** or **too low**.
4. Guess correctly to win the round — then choose to play again.
5. Each new round increases the number range by **50**, making it harder!

**Scoring tip:** The fewer attempts you use, the better your performance.

---

##  Getting Started

### Prerequisites

- Python **3.6** or higher

Check your version:
```bash
python --version
```

### Installation

1. **Clone the repository**
```bash
git clone https://github.com/maahird285-png/number-guessing-game.git
cd number-guessing-game
```

2. **No dependencies needed** — this project uses only the Python standard library.

3. **Run the game**
```bash
python game.py
```

> **Windows users:** You may need to use `python` instead of `python3`.

---

##  Game Logic

```
Start Round
    │
    ▼
Generate secret number (1 → max_number)
    │
    ▼
Player enters guess ──► Invalid input? → Re-prompt (no attempt used)
    │
    ▼
Correct? ──► Yes →  Win! Show attempt count
    │
    No
    ▼
Too high / Too low hint shown
    │
    ▼
Attempts left? ──► No →  Game Over. Reveal number
    │
    Yes (loop back)
    │
    ▼
Play again? ──► Yes → Round + 1, max_number + 50
              ──► No  → Exit
```

### Difficulty Scaling

| Round | Number Range | Max Attempts |
|-------|-------------|--------------|
| 1     | 1 – 100     | 7            |
| 2     | 1 – 150     | 7            |
| 3     | 1 – 200     | 7            |
| N     | 1 – (50N + 50) | 7         |

> The maximum attempts stay fixed at 7, but the pool of possible numbers grows — making each subsequent round statistically harder.

---

## Project Structure

```
number-guessing-game/
│
├── game.py          # Main game script
├── README.md        # Project documentation
└── LICENSE          # MIT License
```

---

##  Roadmap

Planned improvements for future versions:

- [ ] **Scoring system** — track points based on attempts used per round
- [ ] **High score leaderboard** — save top scores to a local file
- [ ] **Difficulty selector** — Easy / Medium / Hard presets at game start
- [ ] **Hint system** — optional range-narrowing hints (at the cost of points)
- [ ] **GUI version** — Tkinter or PyGame graphical interface
- [ ] **Web version** — Flask or FastAPI backend with a browser frontend
- [ ] **Tests** — unit tests with `pytest` for game logic

Have an idea? [Open an issue](https://github.com/your-username/number-guessing-game/issues) and let's discuss it!

---

##  Contributing

Contributions are always welcome!

1. **Fork** the repository
2. **Create** a feature branch
   ```bash
   git checkout -b feature/your-feature-name
   ```
3. **Commit** your changes
   ```bash
   git commit -m "Add: your feature description"
   ```
4. **Push** to your branch
   ```bash
   git push origin feature/your-feature-name
   ```
5. **Open** a Pull Request

Please make sure your code follows the existing style and is well-commented.

---

##  License

This project is licensed under the **MIT License** — see the [LICENSE](LICENSE) file for details.

---

<div align="center">

Made with  and Python · Give this repo a  if you found it fun!

</div>
## Contact Me for any Information
Name: Farhan Dahir Ahmed
Reg.No: 25/BSE/BU/R/0028
