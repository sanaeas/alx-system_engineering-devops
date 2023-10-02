# Automate the task of creating a custom HTTP header response
exec { 'apt-update':
  command => 'apt-get update',
  path    => '/usr/bin:/bin',
}

package { 'nginx':
  ensure => installed,
}

service { 'nginx':
  ensure  => running,
  enable  => true,
  require => Package['nginx'],
}

exec { 'add_header':
  provider => shell,
  command  => 'sudo sed -i "s/include \/etc\/nginx\/sites-enabled\/\*;/include \/etc\/nginx\/sites-enabled\/\*;\n\tadd_header X-Served-By \"${::hostname}\";/" /etc/nginx/nginx.conf',
  before   => Exec['nginx_restart'],
}

exec { 'nginx_restart':
  command => 'service nginx restart',
  path    => '/usr/sbin',
}
