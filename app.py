"""
Helpdesk Agents Suite - Main Streamlit Application

A multi-agent AI application that routes user requests to specialized helpdesk agents
based on the type of request.
"""

import streamlit as st
from coordinator import CoordinatorAgent
from agents.it_agent import ITAgent
from agents.devops_agent import DevOpsAgent
from agents.infra_agent import InfraAgent
from agents.cab_agent import CABAgent
from utils import get_chat_history, extract_agent_switch_command, get_agent_welcome_message

# Set page configuration
st.set_page_config(
    page_title="Helpdesk Agents Suite",
    page_icon="🤖",
    layout="wide"
)

# Initialize session state
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

if "current_agent" not in st.session_state:
    st.session_state.current_agent = None

# Initialize agents
@st.cache_resource
def load_agents():
    coordinator = CoordinatorAgent()
    it_agent = ITAgent()
    devops_agent = DevOpsAgent()
    infra_agent = InfraAgent()
    cab_agent = CABAgent()
    
    return {
        "coordinator": coordinator,
        "it": it_agent,
        "devops": devops_agent,
        "infra": infra_agent,
        "cab": cab_agent
    }

agents = load_agents()

# App title and description
st.title("🤖 Helpdesk Agents Suite")
st.markdown("""
This application routes your helpdesk requests to specialized agents based on the type of request:
- **IT Helpdesk**: Account locking/unlocking, password reset, etc.
- **DevOps Helpdesk**: CI/CD deployment issues
- **Infrastructure Helpdesk**: Infrastructure setup and management
- **CAB Helpdesk**: Change Advisory Board approvals for deployments
""")

# Sidebar with agent information and switching options
with st.sidebar:
    st.header("Current Agent")
    if st.session_state.current_agent:
        agent_type = st.session_state.current_agent
        st.info(agents["coordinator"].get_agent_description(agent_type))
    else:
        st.info("No agent assigned yet. You can select an agent below or submit a request to be automatically connected with a specialized agent.")
    
    # Agent switching section - always visible
    st.header("Select Agent")
    st.write("Choose an agent to talk with:")
    
    # Create buttons for each agent type
    if st.button("IT Helpdesk", key="it_button"):
        previous_agent = st.session_state.current_agent
        st.session_state.current_agent = "it"
        
        # Only add the transition message if this is a switch (not initial selection)
        if previous_agent and previous_agent != "it":
            st.session_state.chat_history.append(
                ("I'd like to switch to the IT Helpdesk agent.", 
                 "*You've been transferred to the IT Helpdesk Agent. How can I help you with your IT-related issues?*")
            )
        elif not previous_agent:  # First selection
            st.session_state.chat_history.append(
                ("", "*You're now connected to the IT Helpdesk Agent. How can I help you with your IT-related issues?*")
            )
        st.rerun()
    
    if st.button("DevOps Helpdesk", key="devops_button"):
        previous_agent = st.session_state.current_agent
        st.session_state.current_agent = "devops"
        
        if previous_agent and previous_agent != "devops":
            st.session_state.chat_history.append(
                ("I'd like to switch to the DevOps Helpdesk agent.", 
                 "*You've been transferred to the DevOps Helpdesk Agent. How can I help you with your CI/CD and deployment issues?*")
            )
        elif not previous_agent:  # First selection
            st.session_state.chat_history.append(
                ("", "*You're now connected to the DevOps Helpdesk Agent. How can I help you with your CI/CD and deployment issues?*")
            )
        st.rerun()
    
    if st.button("Infrastructure Helpdesk", key="infra_button"):
        previous_agent = st.session_state.current_agent
        st.session_state.current_agent = "infra"
        
        if previous_agent and previous_agent != "infra":
            st.session_state.chat_history.append(
                ("I'd like to switch to the Infrastructure Helpdesk agent.", 
                 "*You've been transferred to the Infrastructure Helpdesk Agent. How can I help you with your infrastructure setup and management?*")
            )
        elif not previous_agent:  # First selection
            st.session_state.chat_history.append(
                ("", "*You're now connected to the Infrastructure Helpdesk Agent. How can I help you with your infrastructure setup and management?*")
            )
        st.rerun()
    
    if st.button("CAB Helpdesk", key="cab_button"):
        previous_agent = st.session_state.current_agent
        st.session_state.current_agent = "cab"
        
        if previous_agent and previous_agent != "cab":
            st.session_state.chat_history.append(
                ("I'd like to switch to the CAB Helpdesk agent.", 
                 "*You've been transferred to the CAB Helpdesk Agent. How can I help you with your change approval requests?*")
            )
        elif not previous_agent:  # First selection
            st.session_state.chat_history.append(
                ("", "*You're now connected to the CAB Helpdesk Agent. How can I help you with your change approval requests?*")
            )
        st.rerun()
    
    st.header("Reset Conversation")
    if st.button("Start New Conversation", key="reset_button"):
        st.session_state.chat_history = []
        st.session_state.current_agent = None
        st.rerun()

# Display chat history
st.subheader("Conversation")
chat_container = st.container(height=400)

with chat_container:
    for user_msg, agent_msg in st.session_state.chat_history:
        if user_msg:  # Only show user message if it's not empty
            with st.chat_message("user"):
                st.write(user_msg)
        with st.chat_message("assistant"):
            st.write(agent_msg)

# User input
user_input = st.chat_input("Type your helpdesk request here...")

if user_input:
    # Display user message
    with st.chat_message("user"):
        st.write(user_input)
    
    # Check if the user is requesting to switch agents
    requested_agent = extract_agent_switch_command(user_input)
    if requested_agent:
        # Switch to the requested agent
        previous_agent = st.session_state.current_agent
        st.session_state.current_agent = requested_agent
        
        # Only get a new response if we're actually switching agents
        if previous_agent != requested_agent:
            agent_response = get_agent_welcome_message(requested_agent)
        else:
            # If "switching" to the same agent, acknowledge but don't show welcome again
            agent_response = f"*You're already talking to the {agents['coordinator'].get_agent_description(requested_agent)}. How can I help you?*"
    else:
        # Process the request with the current or new agent
        if not st.session_state.current_agent:
            # Route the request to the appropriate agent
            agent_type = agents["coordinator"].route_request(user_input)
            st.session_state.current_agent = agent_type
            
            # Get response from the assigned agent
            agent_response = agents[agent_type].process_request(user_input)
            
            # Add coordinator's routing information
            agent_response = (
                f"*Your request has been routed to the {agents['coordinator'].get_agent_description(agent_type)}*\n\n"
                f"{agent_response}"
            )
        else:
            # Use the current agent to process the request
            agent_type = st.session_state.current_agent
            agent_response = agents[agent_type].process_request(user_input)
    
    # Display agent response
    with st.chat_message("assistant"):
        st.write(agent_response)
    
    # Update chat history
    st.session_state.chat_history.append((user_input, agent_response))

# Footer
st.markdown("---")
st.caption("Helpdesk Agents Suite - Powered by AI")
