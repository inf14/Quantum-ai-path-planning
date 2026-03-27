# Hybrid Classical–Quantum Path Planning System

## 📌 Project Overview
This project presents a grid-based path planning system that combines **classical algorithms** and **quantum-inspired techniques**.

The system operates in a 2D grid environment with obstacles and aims to find a path from a start point to a goal point. It compares a deterministic classical approach (A*) with a probabilistic quantum-inspired method.

This project is part of a larger system that will later include AI-based explanation modules and containerized deployment.

---

## 🎯 Objectives
- To implement classical path planning using the A* algorithm  
- To explore quantum-inspired decision-making using simple quantum circuits  
- To compare deterministic and probabilistic approaches  
- To visualize and analyze path planning behavior  

---

## 🧠 Classical Approach (A*)

The A* algorithm is used as the baseline path planning method.

### Key Concepts:
- **g(n):** Cost from start node  
- **h(n):** Heuristic (Manhattan distance)  
- **f(n) = g(n) + h(n)**  

### Features:
- Guaranteed shortest path (if exists)  
- Efficient exploration using heuristic  
- Tracks explored nodes and path  

---

## ⚛️ Quantum-Inspired Approach

This module introduces a probabilistic method using a **Grover-inspired quantum circuit**.

### Key Idea:
- Classical logic determines best possible moves  
- If multiple optimal moves exist → quantum circuit selects one  

### Characteristics:
- Probabilistic decision-making  
- No guarantee of optimal path  
- Can behave differently across runs  

---

## ⚖️ Classical vs Quantum Comparison

| Feature | A* | Quantum |
|--------|----|--------|
| Type | Deterministic | Probabilistic |
| Path Optimality | Guaranteed | Not guaranteed |
| Decision Making | Global | Local |
| Reliability | High | Lower |

---

## 📊 Experimentation

Both approaches are tested across multiple runs with random obstacle configurations.

### Metrics Collected:
- Success rate  
- Path length  
- Number of explored nodes  

Logs are generated as JSON files:
- `astar_logs.json`  
- `quantum_path_logs.json`  

---

## 📈 Visualization

The system provides graphical output showing:

- Black cells → Obstacles  
- Light blue cells → Explored nodes  
- Path → Final route  
- S → Start  
- G → Goal  

---

## 📁 Project Structure

    classical/
        astar.py

    quantum/
        quantum_path.py

---

## ▶️ How to Run

Install dependencies:

    pip install numpy matplotlib qiskit qiskit-aer

Run A*:

    python classical/astar.py

Run Quantum:

    python quantum/quantum_path.py

---

## 🚀 Future Work

- Integrate LLM-based explanation module  
- Add comparison visualizations (graphs, metrics)  
- Implement Docker containerization  
- Extend quantum logic for improved decision-making  

---

## 👨‍💻 Authors

Anant Jain  
Viplav Kumar  
Ehsaas Bhalla  

---

## 📧 Contact

For any queries or collaboration:

anant.inf.12.28@gmail.com
