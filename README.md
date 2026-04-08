# 🚀 Hybrid Classical–Quantum Path Planning System

## 📌 Overview

This project implements a **Hybrid AI Path Planning System** that combines:

* 🧠 Classical algorithm (**A***)
* ⚛️ Quantum-inspired probabilistic approach
* 🤖 LLM-based reasoning (Google Gemini)
* 📊 Data analysis & visualization
* 📄 Automated PDF report generation
* 🌐 Interactive UI using Streamlit
* 🔁 CI/CD using GitHub Actions

The system operates in a **2D grid environment with obstacles**, finding optimal paths and comparing deterministic vs probabilistic decision-making.

---

## 🎯 Objectives

* Implement efficient path planning using **A***
* Explore **quantum-inspired probabilistic navigation**
* Compare both approaches using metrics
* Integrate **LLM-based explanations**
* Automate **analysis + reporting pipeline**
* Deploy an **interactive UI for demonstration**

---

## 🧠 Classical Approach (A*)

* Uses heuristic-based search
* Guarantees shortest path (if exists)

### Formula:

f(n) = g(n) + h(n)

* g(n): Cost from start
* h(n): Manhattan distance

---

## ⚛️ Quantum-Inspired Approach

* Inspired by **Grover-like probabilistic selection**
* Chooses among optimal moves randomly

### Characteristics:

* Probabilistic decisions
* Non-deterministic output
* Varies across runs

---

## ⚖️ Comparison

| Feature      | A*            | Quantum          |
| ------------ | ------------- | ---------------- |
| Type         | Deterministic | Probabilistic    |
| Optimal Path | ✅ Guaranteed  | ❌ Not guaranteed |
| Reliability  | High          | Medium           |
| Behavior     | Consistent    | Variable         |

---

## 📊 System Architecture

```
Quantum-ai-path-planning/
│
├── classical/                # A* Algorithm
├── quantum/                  # Quantum-inspired logic
├── LLM Explanation/          # AI + Analytics pipeline
│   ├── app.py
│   ├── metrics.py
│   ├── visualization.py
│   ├── llm_module.py
│   ├── pdf_report.py
│   └── requirements.txt
│
├── app_ui.py                 # Streamlit UI
├── test_astar.py             # Unit tests
├── .github/workflows/ci.yml  # CI/CD pipeline
└── README.md
```

---

## ⚙️ Features

### ✅ Path Planning

* A* shortest path algorithm
* Quantum-inspired probabilistic navigation

### 📊 Analytics

* Success rate
* Path length
* Explored nodes

### 🤖 AI Integration

* LLM-based explanation using **Google Gemini**
* Failure analysis & decision insights

### 📈 Visualization

* Graphs and comparison plots
* Performance metrics

### 📄 Reporting

* Auto-generated **PDF report** with insights

### 🌐 UI (Streamlit)

* Interactive execution
* Real-time algorithm demo

### 🔁 CI/CD

* Automated pipeline using GitHub Actions
* Runs tests on every push

---

## ▶️ How to Run

### 🔹 1. Clone Repository

```
git clone https://github.com/iamviplavkr/Quantum-ai-path-planning.git
cd Quantum-ai-path-planning
```

---

### 🔹 2. Create Virtual Environment

```
python -m venv venv
venv\Scripts\activate
```

---

### 🔹 3. Install Dependencies

```
pip install -r "LLM Explanation/requirements.txt"
pip install streamlit matplotlib pytest
```

---

### 🔹 4. Run Streamlit UI

```
python -m streamlit run app_ui.py
```

👉 Open in browser:
http://localhost:8501

---

### 🔹 5. Run CI Tests Locally

```
pytest
```

---

## 🔁 CI/CD Pipeline

Implemented using **GitHub Actions**:

* Installs dependencies
* Runs algorithm validation
* Executes tests automatically

---

## 📊 Output

* Path visualization
* Performance metrics
* AI-generated insights
* 📄 `Hybrid_AI_Report.pdf`

---


## 💡 Technologies Used

* Python
* NumPy, Pandas
* Matplotlib, Seaborn
* Streamlit
* ReportLab
* Google Gemini API
* GitHub Actions (CI/CD)

---

## 🔮 Future Improvements

* Docker containerization
* Microservices architecture
* Advanced quantum algorithms
* Real-time simulation dashboard
* Cloud deployment (AWS/Azure)

---

## 👨‍💻 Authors

* Anant Jain
* Ehsaas Bhalla
* Viplav Kumar

---

## 📌 Conclusion

This project demonstrates how **classical algorithms, quantum-inspired logic, and modern AI (LLMs)** can be integrated into a unified system for intelligent, explainable, and scalable path planning.

---

## 📫 Contact

For academic discussion or collaboration, please reach out via **anant.inf.12.28@gmail.com**.

