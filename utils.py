"""Utility functions for the Helpdesk Agents Suite."""

from typing import List, Tuple, Optional

def get_chat_history(chat_history: List[Tuple[str, str]]) -> str:
    """
    Format the chat history for display.
    
    Args:
        chat_history: List of (user_message, agent_message) tuples
        
    Returns:
        Formatted chat history as a string
    """
    formatted_history = ""
    for user_msg, agent_msg in chat_history:
        if user_msg:  # Only include user message if it's not empty
            formatted_history += f"User: {user_msg}\n"
        formatted_history += f"Agent: {agent_msg}\n\n"
    
    return formatted_history

def extract_agent_switch_command(user_input: str) -> Optional[str]:
    """
    Extract agent switch command from user input.
    
    Args:
        user_input: The user's input text
        
    Returns:
        The agent type to switch to, or None if no switch command is found
    """
    input_lower = user_input.lower()
    
    # Check for explicit switch commands
    if "switch to it" in input_lower or "talk to it" in input_lower or "connect to it helpdesk" in input_lower:
        return "it"
    elif "switch to devops" in input_lower or "talk to devops" in input_lower or "connect to devops helpdesk" in input_lower:
        return "devops"
    elif "switch to infra" in input_lower or "talk to infra" in input_lower or "connect to infrastructure helpdesk" in input_lower:
        return "infra"
    elif "switch to cab" in input_lower or "talk to cab" in input_lower or "connect to cab helpdesk" in input_lower:
        return "cab"
    
    return None

def get_agent_welcome_message(agent_type: str) -> str:
    """
    Get a welcome message for the specified agent type.
    
    Args:
        agent_type: The agent type
        
    Returns:
        A welcome message from the agent
    """
    welcome_messages = {
        "it": "*You've been transferred to the IT Helpdesk Agent. How can I help you with your IT-related issues?*",
        "devops": "*You've been transferred to the DevOps Helpdesk Agent. How can I help you with your CI/CD and deployment issues?*",
        "infra": "*You've been transferred to the Infrastructure Helpdesk Agent. How can I help you with your infrastructure setup and management?*",
        "cab": "*You've been transferred to the CAB Helpdesk Agent. How can I help you with your change approval requests?*"
    }
    
    return welcome_messages.get(agent_type, "*You've been transferred to a helpdesk agent. How can I help you?*")
