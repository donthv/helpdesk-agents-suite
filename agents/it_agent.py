"""IT Helpdesk Agent for handling account and access-related queries."""

class ITAgent:
    """
    IT Helpdesk Agent that handles queries related to account locking/unlocking,
    password resets, and other IT support issues.
    """
    
    def __init__(self):
        """Initialize the IT Helpdesk Agent."""
        self.name = "IT Helpdesk Agent"
        self.capabilities = [
            "Password resets",
            "Account unlocking",
            "Access management",
            "Email issues",
            "Authentication problems",
            "MFA setup and troubleshooting"
        ]
    
    def process_request(self, user_request: str) -> str:
        """
        Process the user request and generate a response.
        
        Args:
            user_request: The user's request text
            
        Returns:
            A response to the user's request
        """
        # Check for common IT support scenarios
        request_lower = user_request.lower()
        
        # Password reset request
        if any(keyword in request_lower for keyword in ["password", "reset", "forgot", "change"]):
            return self._handle_password_reset(user_request)
        
        # Account locked
        elif any(keyword in request_lower for keyword in ["locked", "unlock", "can't login", "cannot login"]):
            return self._handle_account_unlock(user_request)
        
        # Access request
        elif any(keyword in request_lower for keyword in ["access", "permission", "authorize"]):
            return self._handle_access_request(user_request)
        
        # Default response for other IT queries
        else:
            return (
                "I'm the IT Helpdesk Agent. I can help with password resets, account unlocking, "
                "and access management issues. Could you provide more details about your IT "
                "support needs so I can assist you better?"
            )
    
    def _handle_password_reset(self, request: str) -> str:
        """Handle password reset requests."""
        return (
            "I understand you need to reset your password. For security reasons, "
            "I'll need to verify your identity first:\n\n"
            "1. Please confirm your username or employee ID\n"
            "2. Verify your department or manager's name\n\n"
            "Once verified, I can initiate a password reset link to your registered email address. "
            "The link will expire in 30 minutes. If you don't receive the email, please check your "
            "spam folder or contact us again."
        )
    
    def _handle_account_unlock(self, request: str) -> str:
        """Handle account unlock requests."""
        return (
            "I see that your account is locked. This typically happens after multiple "
            "failed login attempts. To unlock your account:\n\n"
            "1. Please confirm your username or employee ID\n"
            "2. Verify your department or manager's name\n\n"
            "Once verified, I can unlock your account immediately. You'll then need to "
            "reset your password using the temporary password I'll provide. Would you "
            "like to proceed with the account unlock process?"
        )
    
    def _handle_access_request(self, request: str) -> str:
        """Handle access permission requests."""
        return (
            "I understand you're requesting access to a system or resource. To process "
            "this request, I'll need the following information:\n\n"
            "1. The specific system or resource you need access to\n"
            "2. Your role and department\n"
            "3. The reason for access\n"
            "4. The level of access needed (read, write, admin, etc.)\n"
            "5. How long you'll need this access\n\n"
            "Once you provide these details, I'll create an access request ticket and "
            "route it to the appropriate approval manager. Access requests typically "
            "take 24-48 hours to process."
        )
