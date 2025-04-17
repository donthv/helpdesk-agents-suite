"""Coordinator agent that routes requests to specialized helpdesk agents."""

from typing import Dict, List, Optional, Tuple
import re
from langchain_openai import ChatOpenAI
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Initialize OpenAI API with a fallback for demonstration
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "sk-dummy-key-for-testing")
OPENAI_MODEL = os.getenv("OPENAI_MODEL", "gpt-3.5-turbo")

# Initialize LLM with error handling
try:
    llm = ChatOpenAI(temperature=0, model=OPENAI_MODEL)
except Exception as e:
    print(f"Warning: Could not initialize ChatOpenAI: {e}")
    # Create a mock LLM for demonstration purposes
    from langchain.llms.fake import FakeListLLM
    llm = FakeListLLM(responses=["This is a mock response for demonstration purposes."])

class CoordinatorAgent:
    """
    Coordinator agent that analyzes user requests and routes them to the appropriate
    specialized helpdesk agent.
    """
    
    def __init__(self, knowledge_bases=None):
        """Initialize the coordinator agent with routing rules and knowledge bases."""
        # Define keywords for each agent type
        self.agent_keywords = {
            "it": [
                "password", "reset", "account", "locked", "unlock", "login", 
                "credentials", "access", "permission", "email", "username", 
                "authentication", "mfa", "multi-factor", "2fa", "two-factor"
            ],
            "devops": [
                "pipeline", "ci", "cd", "continuous integration", "continuous deployment",
                "build", "jenkins", "github actions", "gitlab", "deployment", "release",
                "version", "artifact", "docker", "container", "kubernetes", "k8s"
            ],
            "infra": [
                "server", "cloud", "aws", "azure", "gcp", "ec2", "instance", "vm",
                "virtual machine", "network", "vpc", "subnet", "security group",
                "database", "rds", "s3", "storage", "lambda", "function", "iam",
                "role", "policy", "permission", "terraform", "cloudformation"
            ],
            "cab": [
                "approval", "change", "cab", "advisory", "board", "review", "production",
                "prod", "deploy", "schedule", "window", "maintenance", "emergency",
                "request", "change management", "itil", "sign-off", "sign off"
            ]
        }
        
        # Store knowledge bases if provided
        self.knowledge_bases = knowledge_bases
        
        # Store last routing decision
        self.last_routing_decision = None
        self.routing_method = None
        self.routing_context = None
    
    def route_request(self, user_request: str) -> str:
        """
        Route the user request to the appropriate specialized agent.
        
        Args:
            user_request: The user's request text
            
        Returns:
            The agent type to route the request to
        """
        # Convert request to lowercase for case-insensitive matching
        request_lower = user_request.lower()
        
        # Count keyword matches for each agent type
        agent_scores = {agent_type: 0 for agent_type in self.agent_keywords}
        
        for agent_type, keywords in self.agent_keywords.items():
            for keyword in keywords:
                if keyword in request_lower:
                    agent_scores[agent_type] += 1
        
        # Find the agent with the highest score
        max_score = 0
        selected_agent = "it"  # Default to IT agent
        
        for agent_type, score in agent_scores.items():
            if score > max_score:
                max_score = score
                selected_agent = agent_type
        
        # Store routing decision
        self.last_routing_decision = selected_agent
        self.routing_method = "keyword"
        
        return selected_agent
    
    def get_agent_description(self, agent_type: str) -> str:
        """
        Get a description of the specified agent type.
        
        Args:
            agent_type: The agent type
            
        Returns:
            A description of the agent
        """
        descriptions = {
            "it": "IT Helpdesk Agent - Handles account-related issues like password resets and access permissions.",
            "devops": "DevOps Helpdesk Agent - Handles CI/CD pipeline issues and deployment problems.",
            "infra": "Infrastructure Helpdesk Agent - Handles infrastructure setup and management.",
            "cab": "CAB Helpdesk Agent - Handles Change Advisory Board approvals for deployments."
        }
        
        return descriptions.get(agent_type, "Unknown Agent Type")
