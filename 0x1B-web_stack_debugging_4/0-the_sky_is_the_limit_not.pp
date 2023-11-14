# Fix the issue with failed requests
# Increase worker processes in nginx.conf
exec { 'increase_worker_processes':
  command => '/bin/sed -i "s/worker_processes 4/worker_processes 8/g" /etc/nginx/nginx.conf',
  notify  => Service['nginx'],
}

service { 'nginx':
  ensure => 'running',
}
