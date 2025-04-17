"""Infrastructure Helpdesk Agent for handling infrastructure-related queries."""

class InfraAgent:
    """
    Infrastructure Helpdesk Agent that handles queries related to infrastructure setup,
    cloud resources, networking, and other infrastructure issues.
    """
    
    def __init__(self):
        """Initialize the Infrastructure Helpdesk Agent."""
        self.name = "Infrastructure Helpdesk Agent"
        self.capabilities = [
            "Cloud resource provisioning",
            "Network configuration",
            "Security group management",
            "Infrastructure as Code (IaC) assistance",
            "Database infrastructure",
            "Serverless architecture setup"
        ]
    
    def process_request(self, user_request: str) -> str:
        """
        Process the user request and generate a response.
        
        Args:
            user_request: The user's request text
            
        Returns:
            A response to the user's request
        """
        # Check for common infrastructure scenarios
        request_lower = user_request.lower()
        
        # Cloud resources
        if any(keyword in request_lower for keyword in ["aws", "azure", "gcp", "cloud", "ec2", "s3", "lambda"]):
            return self._handle_cloud_resource_request(user_request)
        
        # Networking
        elif any(keyword in request_lower for keyword in ["network", "vpc", "subnet", "routing", "firewall", "security group"]):
            return self._handle_networking_request(user_request)
        
        # Infrastructure as Code
        elif any(keyword in request_lower for keyword in ["terraform", "cloudformation", "iac", "infrastructure as code"]):
            return self._handle_iac_request(user_request)
        
        # Default response for other infrastructure queries
        else:
            return (
                "I'm the Infrastructure Helpdesk Agent. I can help with cloud resources, networking, "
                "infrastructure as code, and other infrastructure-related issues. Could you provide "
                "more details about your infrastructure needs so I can assist you better?"
            )
    
    def _handle_cloud_resource_request(self, request: str) -> str:
        """Handle cloud resource-related requests."""
        return (
            "I understand you need assistance with cloud resources. To help you effectively, "
            "I'll need the following information:\n\n"
            "1. Which cloud provider are you using (AWS, Azure, GCP)?\n"
            "2. What specific resources are you working with (EC2, S3, Lambda, etc.)?\n"
            "3. What environment is this for (dev, test, prod)?\n"
            "4. What are you trying to accomplish?\n\n"
            "Once you provide these details, I can help with resource provisioning, "
            "configuration, troubleshooting, or optimization. Would you like me to explain "
            "any best practices for the specific resources you're working with?"
        )
    
    def _handle_networking_request(self, request: str) -> str:
        """Handle networking-related requests."""
        return (
            "I understand you need assistance with networking infrastructure. To help you "
            "effectively, I'll need to know:\n\n"
            "1. What networking components are involved (VPC, subnets, security groups, etc.)?\n"
            "2. Are you setting up new networking resources or troubleshooting existing ones?\n"
            "3. What connectivity requirements do you have?\n"
            "4. Any specific security or compliance requirements?\n\n"
            "Networking issues can be complex, but with these details, I can help design, "
            "configure, or troubleshoot your network infrastructure. Would you like me to "
            "provide some network architecture best practices while we discuss your specific needs?"
        )
    
    def _handle_iac_request(self, request: str) -> str:
        """Handle Infrastructure as Code (IaC) requests."""
        return (
            "I understand you're working with Infrastructure as Code. To assist you better, "
            "I'll need to know:\n\n"
            "1. Which IaC tool are you using (Terraform, CloudFormation, etc.)?\n"
            "2. What resources are you trying to define or manage?\n"
            "3. Are you creating new infrastructure or modifying existing resources?\n"
            "4. Have you encountered any specific errors or issues?\n\n"
            "Infrastructure as Code helps maintain consistency and enables version control "
            "for your infrastructure. I can help with template creation, best practices, "
            "or troubleshooting issues in your IaC implementation. Would you like me to "
            "review your current approach or suggest improvements?"
        )
