# Hybrid Passphrase Evaluation Suite

A sophisticated security tool designed to develop, evaluate, and compare hybrid password generation schemes. This project demonstrates the balance between cryptographic entropy and human memorability.

## Core Objectives

1.  **Hybrid Generation Scheme**: Combines the semantic strength of the **EFF Large Wordlist** (7,776 tokens) with random symbol patterns to thwart both dictionary and pattern-recognition attacks.
2.  **Security Strength Evaluation**: Real-time simulation of attack vectors:
    *   **Brute-Force Attack**: Estimates time-to-crack for Desktop vs. Professional hardware.
    *   **Dictionary Attack Resistance**: Grades entropy levels against pre-generated word lists.
3.  **Comparative Analysis**: Provides a side-by-side performance contrast between the **Hybrid Scheme** and **Traditional Random Character Strings**, highlighting why hybrid methods maintain a superior security-to-recall ratio.

## Project Structure

### 🐍 Python CLI Suite (`password_generator_v1.py`)
A fast, terminal-based evaluator for generating and auditing passphrases.
- **Usage**: `python password_generator_v1.py --words 4 --symbols 2`
- **Features**: ANSI colored output, cryptographic security, and human-friendly crack-time estimations.

### 🌐 Hybrid Web Suite (`/password-web`)
A premium, glassmorphic React application for real-time visualization.
- **Technology**: React v19, Vite, Vanilla CSS.
- **Key Features**: Dynamic entropy sliders, interactive memorability index, and secure one-click copying.

## Security Considerations

- **Diceware Strategy**: Selecting words from a large, vetted list ensures high entropy while keeping the phrase semantically structured.
- **Hybrid Patterns**: By interleaving symbols at random junctions (instead of inside words), we maintain the "word mental model" while significantly increasing the search space for attackers.
- **Local Generation**: All passphrase logic occurs on the local machine (client-side in JS, script-side in Python) for maximum privacy.

---

### Comparison of Methods

| Method | Entropy Depth | Memorability | Resistance |
| :--- | :--- | :--- | :--- |
| **Traditional Random** | High | Very Low | Brute-force proof |
| **Diceware Simple** | High | High | Dictionary prone |
| **Hybrid (Proposed)** | **High** | **High** | **Balanced Defense** |

---
*Created as part of the Secure Remote Work Portfolio.*
