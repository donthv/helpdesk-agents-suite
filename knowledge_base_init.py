"""
Initialize knowledge bases for the Helpdesk Agents Suite.
This script creates sample knowledge base files and initializes vector stores.
"""

import os
from mcp_config import (
    IT_KB_DIR, DEVOPS_KB_DIR, INFRA_KB_DIR, CAB_KB_DIR,
    load_knowledge_base
)

def initialize_knowledge_bases():
    """Initialize all knowledge bases."""
    print("Initializing knowledge bases...")
    
    # Create more detailed sample knowledge base files
    sample_files = {
        # IT knowledge base
        os.path.join(IT_KB_DIR, "password_reset.txt"): 
            """Password Reset Procedure:
            
            1. Verify user identity using two-factor authentication
            2. Generate a secure temporary password
            3. Send the temporary password to the user's registered email
            4. Require password change on next login
            5. Log the password reset action in the security audit log
            
            Note: Password resets for admin accounts require manager approval.
            """,
            
        os.path.join(IT_KB_DIR, "account_unlock.txt"):
            """Account Unlock Procedure:
            
            1. Verify user identity using two-factor authentication
            2. Check account lock reason in the security log
            3. If locked due to failed login attempts, reset the counter
            4. If locked due to policy violation, require manager approval
            5. Unlock the account and notify the user
            6. Log the unlock action in the security audit log
            """,
            
        # DevOps knowledge base
        os.path.join(DEVOPS_KB_DIR, "deployment_issues.txt"):
            """Common Deployment Issues:
            
            1. Pipeline failures:
               - Check build logs for compilation errors
               - Verify test failures and fix failing tests
               - Check for environment variables or secrets issues
            
            2. Environment configuration:
               - Verify environment variables are correctly set
               - Check configuration files for the target environment
               - Validate service connections and dependencies
            
            3. Dependency conflicts:
               - Review package versions and compatibility
               - Check for conflicting library versions
               - Verify dependency resolution in build system
            
            4. Permission issues:
               - Verify deployment service account permissions
               - Check access to required resources
               - Validate security group settings
            """,
            
        os.path.join(DEVOPS_KB_DIR, "ci_cd_pipeline.txt"):
            """CI/CD Pipeline Management:
            
            1. Pipeline Structure:
               - Build stage: Compile code and run unit tests
               - Test stage: Run integration and system tests
               - Quality stage: Run code quality and security scans
               - Deploy stage: Deploy to target environment
            
            2. Common Pipeline Commands:
               - Trigger manual build: `pipeline run --project <project> --branch <branch>`
               - Check build status: `pipeline status --build-id <build-id>`
               - Cancel build: `pipeline cancel --build-id <build-id>`
            
            3. Pipeline Troubleshooting:
               - Check build logs for errors
               - Verify agent pool availability
               - Check resource consumption and quotas
            """,
            
        # Infrastructure knowledge base
        os.path.join(INFRA_KB_DIR, "aws_setup.txt"):
            """AWS Infrastructure Setup:
            
            1. VPC Configuration:
               - Create VPC with appropriate CIDR block
               - Configure subnets across multiple availability zones
               - Set up route tables and internet gateway
               - Configure NAT gateway for private subnets
            
            2. Security Groups:
               - Create security groups for different tiers
               - Configure inbound and outbound rules
               - Follow principle of least privilege
               - Document all security group rules
            
            3. EC2 Instances:
               - Select appropriate instance types
               - Configure auto-scaling groups
               - Set up launch configurations or templates
               - Configure instance profiles with IAM roles
            
            4. Load Balancers:
               - Choose between ALB, NLB, or CLB based on requirements
               - Configure health checks and target groups
               - Set up SSL certificates for HTTPS
               - Configure routing rules and listener rules
            
            5. RDS Databases:
               - Select appropriate database engine
               - Configure multi-AZ for high availability
               - Set up read replicas for read scaling
               - Configure backup and maintenance windows
            """,
            
        os.path.join(INFRA_KB_DIR, "network_troubleshooting.txt"):
            """Network Troubleshooting Guide:
            
            1. Connectivity Issues:
               - Check security group rules
               - Verify network ACLs
               - Test connectivity using ping and telnet
               - Check route tables and network gateways
            
            2. DNS Resolution:
               - Verify DNS server configuration
               - Check Route 53 records if applicable
               - Test DNS resolution using nslookup or dig
               - Check TTL values for DNS records
            
            3. Load Balancer Issues:
               - Check target group health
               - Verify instance health checks
               - Review access logs for error patterns
               - Check SSL certificate validity
            """,
            
        # CAB knowledge base
        os.path.join(CAB_KB_DIR, "approval_process.txt"):
            """Change Advisory Board Process:
            
            1. Submit Change Request:
               - Complete the change request form
               - Include detailed implementation plan
               - Document rollback procedure
               - Specify maintenance window
            
            2. Technical Review:
               - Architecture team reviews technical aspects
               - Security team reviews security implications
               - Performance team reviews performance impact
               - Documentation team reviews documentation updates
            
            3. Impact Assessment:
               - Identify affected systems and services
               - Estimate downtime if applicable
               - Identify user impact
               - Document dependencies
            
            4. Approval Voting:
               - CAB members vote on the change
               - Requires minimum 3 approvals
               - Any rejection requires revision and resubmission
               - Emergency changes require CTO approval
            
            5. Implementation Scheduling:
               - Schedule change for approved maintenance window
               - Notify affected stakeholders
               - Prepare implementation team
               - Schedule post-implementation review
            """,
            
        os.path.join(CAB_KB_DIR, "emergency_changes.txt"):
            """Emergency Change Process:
            
            1. Emergency Criteria:
               - Production outage affecting critical services
               - Security vulnerability requiring immediate patching
               - Compliance issue with regulatory deadline
               - Data loss or corruption risk
            
            2. Emergency Approval Process:
               - Submit emergency change request
               - Obtain CTO or designated approver sign-off
               - Document justification for emergency status
               - Proceed with implementation after approval
            
            3. Post-Implementation Review:
               - Document actual implementation steps taken
               - Record any deviations from plan
               - Document impact and results
               - Submit full report to next regular CAB meeting
            """
    }
    
    # Create sample knowledge base files
    for file_path, content in sample_files.items():
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        with open(file_path, 'w') as f:
            f.write(content)
    
    # Load knowledge bases
    print("Loading IT knowledge base...")
    it_kb = load_knowledge_base(IT_KB_DIR)
    
    print("Loading DevOps knowledge base...")
    devops_kb = load_knowledge_base(DEVOPS_KB_DIR)
    
    print("Loading Infrastructure knowledge base...")
    infra_kb = load_knowledge_base(INFRA_KB_DIR)
    
    print("Loading CAB knowledge base...")
    cab_kb = load_knowledge_base(CAB_KB_DIR)
    
    print("Knowledge bases initialized successfully!")
    
    return {
        "it": it_kb,
        "devops": devops_kb,
        "infra": infra_kb,
        "cab": cab_kb
    }

if __name__ == "__main__":
    initialize_knowledge_bases()
