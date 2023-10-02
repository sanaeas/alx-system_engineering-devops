# Automate the task of creating a custom HTTP header response
exec { 'apt-update':
  command => 'apt-get update',
  path    => '/usr/bin',
}

package { 'nginx':
  ensure => installed,
}

service { 'nginx':
  ensure  => running,
  enable  => true,
  require => Package['nginx'],
}

file { '/etc/nginx/sites-available/default':
  ensure => 'present',
  path   => '/etc/nginx/sites-available/default',
  match  => 'listen 80 default_server',
  line   => '\n\tadd_header X-Served-By "${::hostname}";',
}

exec { 'nginx_reload':
  command  => 'sudo service nginx restart',
  provider => shell,
}
