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

file_line { 'add_header':
  path   => '/etc/nginx/sites-available/default',
  after  => "^\tlocation / {",
  line   => "\n\tadd_header X-Served-By \"${::hostname}\";",
  notify => Exec['nginx_reload'],
}

exec { 'nginx_reload':
  command     => 'service nginx restart',
  path        => '/usr/sbin',
  refreshonly => true,
  subscribe   => File_line['add_header'],
}
