# 7-puppet_install_nginx_web_server.pp

# Install Nginx package
package { 'nginx':
  ensure => installed,
}

# Configure Nginx to listen on port 80
file { '/etc/nginx/sites-available/default':
  content => "
    server {
      listen 80 default_server;
      server_name _;
      location / {
        root /var/www/html;
        index index.html;
      }
      location /redirect_me {
        return 301 https://www.youtube.com/watch?v=QH2-TGUlwu4;
      }
    }
  ",
}

# Create a simple HTML page with "Hello World!"
file { '/var/www/html/index.html':
  content => '<html><body>Hello World!</body></html>',
}

# Restart Nginx service
service { 'nginx':
  ensure => running,
  enable => true,
}
