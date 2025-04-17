"""CAB Helpdesk Agent for handling Change Advisory Board approval queries."""

class CABAgent:
    """
    CAB Helpdesk Agent that handles queries related to Change Advisory Board approvals
    for deployments and other changes.
    """
    
    def __init__(self):
        """Initialize the CAB Helpdesk Agent."""
        self.name = "CAB Helpdesk Agent"
        self.capabilities = [
            "Change request submissions",
            "Approval status tracking",
            "Change window scheduling",
            "Emergency change processes",
            "Change documentation requirements",
            "Post-implementation reviews"
        ]
    
    def process_request(self, user_request: str) -> str:
        """
        Process the user request and generate a response.
        
        Args:
            user_request: The user's request text
            
        Returns:
            A response to the user's request
        """
        # Check for common CAB scenarios
        request_lower = user_request.lower()
        
        # Change request submission
        if any(keyword in request_lower for keyword in ["submit", "new", "create", "request", "change"]):
            return self._handle_change_submission(user_request)
        
        # Approval status
        elif any(keyword in request_lower for keyword in ["status", "approved", "rejected", "pending"]):
            return self._handle_approval_status(user_request)
        
        # Change window
        elif any(keyword in request_lower for keyword in ["window", "schedule", "when", "timing", "maintenance"]):
            return self._handle_change_window(user_request)
        
        # Emergency change
        elif any(keyword in request_lower for keyword in ["emergency", "urgent", "immediate", "expedite"]):
            return self._handle_emergency_change(user_request)
        
        # Default response for other CAB queries
        else:
            return (
                "I'm the CAB Helpdesk Agent. I can help with Change Advisory Board approvals, "
                "change request submissions, approval status tracking, and scheduling change windows. "
                "Could you provide more details about your change management needs so I can assist you better?"
            )
    
    def _handle_change_submission(self, request: str) -> str:
        """Handle change request submission queries."""
        return (
            "I understand you want to submit a change request for CAB approval. To proceed, "
            "I'll need the following information:\n\n"
            "1. Change description and purpose\n"
            "2. Systems or services affected\n"
            "3. Proposed implementation date and time\n"
            "4. Estimated duration of the change\n"
            "5. Impact assessment (users/services affected)\n"
            "6. Rollback plan\n"
            "7. Testing plan\n\n"
            "Once you provide these details, I can help you complete the change request form "
            "and submit it to the CAB for review. Standard changes typically require submission "
            "at least 5 business days before implementation. Would you like me to provide a "
            "template for your change request?"
        )
    
    def _handle_approval_status(self, request: str) -> str:
        """Handle approval status queries."""
        return (
            "I understand you're inquiring about the status of a change request. To check "
            "the status, I'll need:\n\n"
            "1. The change request ID or reference number\n"
            "2. The name of the change requester\n\n"
            "Once you provide this information, I can look up the current status in our "
            "change management system. The status could be one of the following: Draft, "
            "Submitted, Under Review, Approved, Rejected, or Completed. I can also provide "
            "any feedback or questions from the CAB if available. Would you like to proceed "
            "with checking the status?"
        )
    
    def _handle_change_window(self, request: str) -> str:
        """Handle change window scheduling queries."""
        return (
            "I understand you're inquiring about change windows for implementation. Our "
            "standard change windows are:\n\n"
            "1. Non-critical systems: Monday-Thursday, 7:00 PM - 11:00 PM\n"
            "2. Critical systems: Saturday-Sunday, 1:00 AM - 5:00 AM\n"
            "3. Quarterly maintenance windows: First weekend of each quarter, full weekend\n\n"
            "To schedule your change in one of these windows, you'll need to submit your "
            "change request at least 5 business days in advance. The CAB meets every Tuesday "
            "at 10:00 AM to review and approve changes for the upcoming windows. Would you "
            "like me to help you identify the most appropriate window for your change?"
        )
    
    def _handle_emergency_change(self, request: str) -> str:
        """Handle emergency change queries."""
        return (
            "I understand you need to process an emergency change. Emergency changes follow "
            "an expedited approval process for critical issues that require immediate attention. "
            "To proceed with an emergency change:\n\n"
            "1. Complete the Emergency Change Form, including:\n"
            "   - Description of the issue and business impact\n"
            "   - Why this requires immediate implementation\n"
            "   - Systems affected and potential risks\n"
            "   - Rollback plan\n"
            "2. Contact the Emergency CAB coordinator at the emergency hotline\n"
            "3. Be prepared to join an emergency CAB call for approval\n\n"
            "Emergency changes still require proper documentation and approval, but the process "
            "is accelerated. Would you like me to provide the Emergency Change Form and the "
            "contact information for the Emergency CAB coordinator?"
        )
