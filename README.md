# number-theory-crypto-wallet-sim

This project is a Python-based desktop application developed using **Tkinter** that simulates the mathematical foundations of cryptographic wallet key generation and transaction security. It bridges pure mathematics and software engineering by implementing fundamental number theory concepts into a functional graphical user interface (GUI).

## Technical Overview & Mathematics
Instead of relying on high-level external crypto libraries, this project implements core cryptographic algorithms from scratch using modular arithmetic:
* **Primes & Data Integrity:** Uses deterministic mathematical logic to check for prime numbers ($p$ and $q$) as the root of secure key creation.
* **Extended Euclidean Algorithm:** Implements custom functions to calculate the Greatest Common Divisor ($GCD$) and modular multiplicative inverse ($mod\_tersi$).
* **Asymmetric Key Setup Setup:** Simulates the structural concepts behind asymmetric encryption principles (resembling frameworks like RSA) for wallet security.

## Technologies Used
* **Python 3**
* **Tkinter:** For building the graphical user interface (GUI) desktop application.
* **OS & Messagebox Modules:** For system-level environment checks and dynamic user alerts.

## Key Features
* **Key Generation Simulation:** Users can input prime numbers to generate simulated private/public cryptographic wallet keys.
* **Modular Arithmetic Engine:** Built-in calculation algorithms to verify mathematical correctness before creating keys.
* **User-Friendly Desktop Interface:** Clean layout structures divided into intuitive operational steps (e.g., Key Generation, Transaction Verification).

## Core Architecture (Code Highlights)
* `asal_mi(n)`: Optimized loop structure to check prime properties up to $\sqrt{n} + 1$.
* `mod_tersi(e, phi)`: Pure algorithmic implementation of the Extended Euclidean Algorithm to solve modular equations dynamically.
* `KriptoCuzdanApp`: Object-oriented Tkinter class that structure coordinates the visual components and anchors data inputs seamlessly.

## How to Run
1. Ensure Python 3.x is installed on your local machine.
2. Clone this repository.
3. Run the main application file:
   ```bash
   python "import tkinter as tk 1.py"
