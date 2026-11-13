# Design and Analysis of Algorithms (DAA) & AI Lab Repository

**Name:** Ayush Jaiswal  
**Roll Number / ID:** IC-2K23-16  
**Repository:** `IC-2K23-16-AI-AYUSH-JAISWAL`

---

## Overview

This repository contains the lab assignments, implementations, and data analysis notebooks completed as part of the **Design and Analysis of Algorithms / Artificial Intelligence Lab** coursework. The implementations cover foundational search strategies, heuristic optimization, data analysis, machine learning classification, and knowledge representation techniques using C++ and Python.

---

## Repository Structure

```text
.
├── LAB_1
│   ├── README.md
│   └── Task1_water_in_jug.cpp
├── LAB_2
│   ├── BFS.py
│   ├── DFS.py
│   └── Hill_Climbing
│       ├── RandomRestart.py
│       └── SteepestAscent.py
├── LAB_3
│   ├── analysis.ipynb
│   └── datasets
│       └── EVData.csv
├── LAB_4
│   ├── datasets
│   └── decisionTreeClassifier.ipynb
└── LAB_5
    ├── RuleBasedSystem.py
    └── SemanticNetwork.ipynb
```

---

## Lab-wise Breakdown

### **LAB 1: State Space Search**
* **`Task1_water_in_jug.cpp`**: C++ implementation solving the classic Water Jug Problem using state-space search techniques.
* **`README.md`**: Documentation and problem breakdown for Lab 1.

### **LAB 2: Uninformed & Heuristic Search Algorithms**
* **`BFS.py`**: Implementation of Breadth-First Search for graph/tree traversal.
* **`DFS.py`**: Implementation of Depth-First Search for graph/tree traversal.
* **`Hill_Climbing/`**:
  * **`SteepestAscent.py`**: Implementation of the Steepest-Ascent Hill Climbing heuristic search algorithm.
  * **`RandomRestart.py`**: Implementation of Random-Restart Hill Climbing to overcome local optima.

### **LAB 3: Exploratory Data Analysis (EDA)**
* **`analysis.ipynb`**: Jupyter Notebook performing data cleaning, visualization, and statistical analysis on Electric Vehicle (EV) data.
* **`datasets/EVData.csv`**: Dataset used for the EV analysis.

### **LAB 4: Supervised Machine Learning**
* **`decisionTreeClassifier.ipynb`**: Implementation and evaluation of a Decision Tree Classifier model.
* **`datasets/`**: Directory housing the datasets used for training and testing the classifier.

### **LAB 5: Knowledge Representation & Reasoning**
* **`RuleBasedSystem.py`**: Python script implementing a basic rule-based expert system using conditional logic/inference rules.
* **`SemanticNetwork.ipynb`**: Jupyter Notebook demonstrating knowledge representation using semantic networks and graph relationships.

---

## Technologies & Prerequisites

* **Languages:** C++ (GCC/G++), Python 3.x
* **Libraries & Tools:** 
  * Jupyter Notebook / JupyterLab
  * `pandas`, `numpy`, `matplotlib` / `seaborn` (for data analysis)
  * `scikit-learn` (for Decision Tree classification)
  * `networkx` (for Semantic Networks, if applicable)

---

## How to Run

### **1. Clone the Repository**
```bash
git clone https://github.com/<your-username>/IC-2K23-16-AI-AYUSH-JAISWAL.git
cd IC-2K23-16-AI-AYUSH-JAISWAL
```

### **2. Running C++ Programs (Lab 1)**
```bash
cd LAB_1
g++ Task1_water_in_jug.cpp -o water_jug
./water_jug
```

### **3. Running Python Scripts (Lab 2 & Lab 5)**
```bash
cd LAB_2
python3 BFS.py
```

### **4. Running Jupyter Notebooks (Lab 3, Lab 4, Lab 5)**
Ensure you have Jupyter installed, then launch the notebook server from the root directory:
```bash
jupyter notebook
```
Navigate to the respective `.ipynb` file in your browser to view and execute the cells.