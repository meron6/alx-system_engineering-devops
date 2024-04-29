## 0x0F. Load Balancer

## Overview

This repository contains scripts and configurations related to the implementation of a load balancer for distributing web traffic across multiple web servers. The task involves configuring Nginx to serve as a load balancer and ensuring that it distributes incoming HTTP requests evenly across two web servers (`web-01` and `web-02`). Additionally, a custom HTTP response header is added to identify which server handled each request.

## Files

- `0-custom_http_response_header`: Bash script to configure a new Ubuntu machine to include a custom HTTP response header (`X-Served-By`) in its Nginx configuration. This script installs Nginx, adds the custom header to the default Nginx configuration, and restarts Nginx to apply the changes.

## Usage

1. Clone the repository:

2. Navigate to the `0x0F-load_balancer` directory:

3. Make the script executable (if not already):

4. Execute the script on the target machine to configure Nginx with the custom HTTP response header:

5. Verify the configuration by sending HTTP requests to the servers and checking for the presence of the custom header `X-Served-By`.

## Example

After running the script on both `web-01` and `web-02`, you can verify the configuration using `curl`:


Replace `<web-server-ip>` with the IP address of each web server. You should see a response containing `X-Served-By` header indicating the hostname of the server that handled the request.

## Notes

- Ensure that the servers are properly configured and accessible over the network before running the script.
- The script assumes Ubuntu as the operating system. Adjustments may be needed for other distributions.
- This setup provides a basic configuration for load balancing HTTP traffic. Further customization and optimization may be required for production environments.
