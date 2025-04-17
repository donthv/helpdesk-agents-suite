"""
Run the original Helpdesk Agents Suite application.
This script runs the Streamlit app with the original implementation.
"""

import os
import sys
import subprocess

def main():
    """Run the Streamlit app with the original implementation."""
    print("Starting Helpdesk Agents Suite...")
    
    # Check if streamlit is installed in the current environment
    try:
        import streamlit
        print(f"Using Streamlit from: {streamlit.__file__}")
        streamlit_cmd = [sys.executable, "-m", "streamlit", "run", "app.py"]
    except ImportError:
        print("Warning: Streamlit not found in current environment.")
        print("Attempting to run using system streamlit...")
        streamlit_cmd = ["streamlit", "run", "app.py"]
    
    try:
        # Run the Streamlit app
        print("Starting Streamlit app...")
        print(f"Command: {' '.join(streamlit_cmd)}")
        subprocess.run(streamlit_cmd)
    except Exception as e:
        print(f"Error running Streamlit: {e}")
        print("\nTo run the app manually, use the following command:")
        print("streamlit run app.py")

if __name__ == "__main__":
    main()
