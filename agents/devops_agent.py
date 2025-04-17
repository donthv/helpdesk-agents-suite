"""DevOps Helpdesk Agent for handling CI/CD and deployment-related queries."""

class DevOpsAgent:
    """
    DevOps Helpdesk Agent that handles queries related to CI/CD pipelines,
    deployments, and other DevOps issues.
    """
    
    def __init__(self):
        """Initialize the DevOps Helpdesk Agent."""
        self.name = "DevOps Helpdesk Agent"
        self.capabilities = [
            "CI/CD pipeline troubleshooting",
            "Deployment failure analysis",
            "Build process optimization",
            "Container orchestration issues",
            "Version control integration",
            "Artifact management"
        ]
    
    def process_request(self, user_request: str) -> str:
        """
        Process the user request and generate a response.
        
        Args:
            user_request: The user's request text
            
        Returns:
            A response to the user's request
        """
        # Check for common DevOps scenarios
        request_lower = user_request.lower()
        
        # Pipeline failure
        if any(keyword in request_lower for keyword in ["pipeline", "fail", "broken", "error"]):
            return self._handle_pipeline_failure(user_request)
        
        # Deployment issues
        elif any(keyword in request_lower for keyword in ["deploy", "release", "rollback", "production"]):
            return self._handle_deployment_issue(user_request)
        
        # Container/Kubernetes issues
        elif any(keyword in request_lower for keyword in ["container", "docker", "kubernetes", "k8s", "pod"]):
            return self._handle_container_issue(user_request)
        
        # Default response for other DevOps queries
        else:
            return (
                "I'm the DevOps Helpdesk Agent. I can help with CI/CD pipeline issues, deployment "
                "failures, and other DevOps-related problems. Could you provide more details about "
                "your DevOps issue so I can assist you better?"
            )
    
    def _handle_pipeline_failure(self, request: str) -> str:
        """Handle CI/CD pipeline failure requests."""
        return (
            "I understand you're experiencing a pipeline failure. To help diagnose the issue, "
            "I'll need the following information:\n\n"
            "1. Pipeline name or ID\n"
            "2. Build/job number that failed\n"
            "3. Repository and branch name\n"
            "4. Any error messages you're seeing\n\n"
            "Once you provide these details, I can check the pipeline logs and help identify "
            "the root cause. Common issues include test failures, dependency problems, or "
            "environment configuration issues. Would you like me to guide you through some "
            "initial troubleshooting steps?"
        )
    
    def _handle_deployment_issue(self, request: str) -> str:
        """Handle deployment-related issues."""
        return (
            "I understand you're having an issue with a deployment. To help resolve this, "
            "I'll need to know:\n\n"
            "1. Which environment is affected (dev, staging, production)\n"
            "2. The application or service being deployed\n"
            "3. Version or build number\n"
            "4. When the deployment was initiated\n"
            "5. Any error messages or unexpected behaviors\n\n"
            "Once I have this information, I can check the deployment logs and status. "
            "If needed, I can help you roll back to a previous stable version while we "
            "investigate the issue. Would you like me to check the deployment status now?"
        )
    
    def _handle_container_issue(self, request: str) -> str:
        """Handle container or Kubernetes-related issues."""
        return (
            "I understand you're experiencing an issue with containers or Kubernetes. "
            "To help troubleshoot, I'll need:\n\n"
            "1. Cluster name and namespace\n"
            "2. Pod or container name\n"
            "3. Any error messages from logs\n"
            "4. Recent changes that might have affected the environment\n\n"
            "Common container issues include resource constraints, configuration errors, "
            "or networking problems. I can help check pod status, logs, and resource "
            "utilization to identify the root cause. Would you like me to walk you through "
            "some diagnostic commands to gather more information?"
        )
