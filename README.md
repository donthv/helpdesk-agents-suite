# Helpdesk Agents Suite

A multi-agent AI application that routes user requests to specialized helpdesk agents based on the type of request.

## Features

- **Intelligent Request Routing**: Automatically categorizes and routes user requests to the appropriate specialized agent
- **Specialized Helpdesk Agents**:
  - IT Helpdesk: Account locking/unlocking, password reset, etc.
  - DevOps Helpdesk: CI/CD deployment issues
  - Infrastructure Helpdesk: Infrastructure setup and management
  - CAB Helpdesk: Change Advisory Board approvals for deployments

## Installation

```bash
# Clone the repository
git clone https://github.com/yourusername/helpdesk-agents-suite.git
cd helpdesk-agents-suite

# Create a virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

## Usage

```bash
streamlit run app.py
```

Navigate to the provided URL (typically http://localhost:8501) in your web browser.

## Project Structure

- `app.py`: Main Streamlit application
- `coordinator.py`: Coordinator agent that routes requests
- `agents/`: Directory containing specialized helpdesk agents
  - `it_agent.py`: IT Helpdesk agent
  - `devops_agent.py`: DevOps Helpdesk agent
  - `infra_agent.py`: Infrastructure Helpdesk agent
  - `cab_agent.py`: CAB Helpdesk agent
- `utils.py`: Utility functions
- `requirements.txt`: Project dependencies
