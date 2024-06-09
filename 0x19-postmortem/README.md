#Postmortem: Outage on June 8, 2024

#Issue Summary
Duration of Outage: June 8, 2024, 03:00 AM to 06:00 AM UTC (3 hours)
Impact: 
Our primary e-commerce platform was down.
Users experienced 502 Bad Gateway errors when attempting to access the site.
Approximately 85% of users were affected.
Root Cause: An unexpected spike in traffic triggered a memory leak in the web server's process, leading to server crashes.

#Timeline
03:00 AM: A monitoring alert was triggered, indicating high response times and increased error rates.
03:05 AM: The on-call engineer noticed the issue and started investigating.
03:15 AM: Initial hypothesis: a network issue due to increased latency observed.
03:30 AM: The network team ruled out any network-related problems.
03:45 AM: Logs reviewed; memory leak suspected in the web server.
04:00 AM: The incident escalated to the web development team.
04:15 AM: The web development team identified a recent update that potentially caused the memory leak.
04:30 AM: Rollback of the latest update initiated.
05:00 AM: Rollback completed; servers restarted.
05:15 AM: Monitoring confirmed the resolution of the issue.
06:00 AM: Full functionality restored; incident declared resolved.

#Root Cause and Resolution
Root Cause:
The outage was caused by a memory leak introduced in the latest update to the web server. This memory leak was triggered by a specific condition that was exacerbated by the unexpected spike in traffic.
Resolution:
The problematic update was rolled back to the previous stable version.
Servers were restarted to clear the memory leak and restore normal operation.

#Corrective and Preventative Measures
Improvements:
Improve traffic spike handling by increasing server capacity and implementing rate limiting.
Enhance monitoring to detect memory leaks and other resource issues earlier.
Conduct thorough load testing before deploying updates.
Tasks:
Patch Web Server: Fix the memory leak in the web server and redeploy the update after rigorous testing.
Add Monitoring: Implement monitoring for memory usage on the web servers.
Upgrade Infrastructure**: Increase server capacity to handle higher traffic volumes.
Rate Limiting: Implement rate limiting to prevent traffic spikes from overwhelming the system.
Load Testing: Introduce comprehensive load testing as part of the deployment pipeline.
Review Update Process: Refine the update process to include more stringent code reviews and testing.

                +------------------+                    
                |  Outage Begins   |                    
                |   (03:00 AM)     |                    
                +--------+---------+                    
                         |                             
                         v                             
                +------------------+                    
                | Initial Hypothesis|                    
                |   (03:15 AM)     |                    
                +--------+---------+                    
                         |                             
                         v                             
                +------------------+                    
                | Network Ruled Out|                    
                |   (03:30 AM)     |                    
                +--------+---------+                    
                         |                             
                         v                             
                +------------------+                    
                |Memory Leak Suspected|                    
                |   (03:45 AM)       |                    
                +--------+---------+                    
                         |                             
                         v                             
                +------------------+                    
                | Incident Escalated|                    
                |    (04:00 AM)     |                    
                +--------+---------+                    
                         |                             
                         v                             
                +------------------+                    
                |  Update Rollback  |                    
                |    (04:30 AM)     |                    
                +--------+---------+                    
                         |                             
                         v                             
                +------------------+                    
                | Incident Resolved |                    
                |    (06:00 AM)     |                    
                +------------------+                    

Engaging Elements
To make this postmortem more engaging, we included:

Humor: "It looks like our servers decided to take a nap during the busiest time! We've given them a good talk."
Diagram: A visual representation of the outage timeline and the steps taken to resolve it.                        |                   
