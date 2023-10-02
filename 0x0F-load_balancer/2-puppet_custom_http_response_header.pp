# Automate the task of creating a custom HTTP header response
exec {'update':
  command  => 'sudo apt-get -y update',
  provider => shell,
  before   => Exec['install_nginx'],
}

exec {'install_nginx':
  command  => 'sudo apt-get -y install nginx',
  provider => shell,
  before   => Exec['add_header'],
}

exec { 'add_header':
  command => '/bin/sed -i "/^\tlocation \/ {.*/a \\\t \tadd_header X-Served-By \$hostname;" /etc/nginx/sites-available/default; /usr/sbin/service nginx restart'
}

exec { 'nginx_restart':
  command  => 'sudo service nginx restart',
  provider => shell,
}
