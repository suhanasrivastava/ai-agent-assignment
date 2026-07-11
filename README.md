# AI Agent for Autonomous Carrier Rerouting using LangGraph
# Author: Suhana Kumari
## Project Overview

This project demonstrates a lightweight multi-agent AI system that autonomously handles logistics disruptions. The system receives a shipment telemetry alert, analyzes the severity of the disruption, identifies alternative carrier routes, selects the most suitable carrier, and generates a notification without requiring human intervention.

The implementation is built using **LangGraph**, **LangChain**, and the **Llama 3.3 70B** model served through the **Groq inference platform**.

---

# Business Problem

Logistics companies frequently encounter shipment delays caused by weather conditions, vehicle failures, traffic congestion, or operational issues. Manual rerouting is often slow and requires human decision-making.

The objective of this project is to demonstrate how AI agents can automate this process by analyzing shipment information, evaluating alternative routes, and recommending the best carrier automatically.

---

# Architecture

```
Telemetry Alert
       │
       ▼
┌────────────────────┐
│ Triage Agent       │
│ Analyze Severity   │
└─────────┬──────────┘
          │
          ▼
   Conditional Routing
          │
     Low Severity
          │
         END

Medium / High Severity
          │
          ▼
┌────────────────────┐
│ Route Agent        │
│ Route Selection    │
└─────────┬──────────┘
          ▼
┌────────────────────┐
│ Decision Agent     │
│ Select Best Route  │
└─────────┬──────────┘
          ▼
┌────────────────────┐
│ Notification Agent │
└─────────┬──────────┘
          ▼
         END
```

---

# AI Agents

### 1. Triage Agent

Responsibilities:

* Analyze shipment telemetry.
* Determine disruption severity.
* Assign priority.
* Decide whether rerouting is required.

---

### 2. Route Agent

Responsibilities:

* Retrieve available carrier options using a routing tool.
* Evaluate available routes.
* Pass candidate routes for final decision making.

---

### 3. Decision Agent

Responsibilities:

* Compare candidate carriers.
* Consider ETA, shipment priority, and cost.
* Select the optimal carrier.
* Provide reasoning for the decision.

---

### 4. Notification Agent

Responsibilities:

* Generate the final shipment notification.
* Present the selected carrier and reasoning.

---

# Technologies Used
* Python
* LangGraph
* LangChain
* Groq API
* Llama 3.3 70B
* Google Gemini API (for model comparison)
* Pydantic
* python-dotenv

---

# Project Structure

```
ai_agent_assignment/

├── agents/
│   ├── triage_agent.py
│   ├── route_agent.py
│   ├── decision_agent.py
│   └── notification_agent.py
│
├── graph/
│   └── graph.py
│
├── tools/
│   ├── telemetry.py
│   └── route_tool.py
│
├── state.py
├── config.py
├── llm_factory.py
├── app.py
├── requirements.txt
└── README.md
```

---

# Installation

```bash
git clone <repository>

cd ai_agent_assignment

pip install -r requirements.txt
```

Create a `.env` file:

```
GROQ_API_KEY=YOUR_API_KEY
GEMINI_API_KEY = YOUR_API_KEY
```

Run the project:

```bash
python app.py
```

---

# Sample Output

```
Telemetry Received

↓

Triage Agent

Severity : High

↓

Route Agent

FedEx
DHL

↓

Decision Agent

Selected Carrier : FedEx

↓

Notification

Shipment reassigned successfully.
```

---

# Future Improvements

* Integrate live logistics APIs.
* Add real-time shipment tracking.
* Compare open-source and closed-source foundation models.
* Add human approval workflow for high-value shipments.
* Deploy using FastAPI and Docker.

---

# AI Decision Log

AI coding assistants were used to accelerate development by generating boilerplate code, refining prompts, and suggesting LangGraph workflow structures. All architectural decisions, workflow design, agent responsibilities, conditional routing logic, and testing were reviewed and implemented manually. Generated suggestions were modified where necessary to align with the assignment requirements and the chosen logistics use case.
