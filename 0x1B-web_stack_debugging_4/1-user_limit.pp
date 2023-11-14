# Change the ulimit for the holberton user
exec {'hard_inc':
  provider => shell,
  command  => 'sudo sed -i "s/holberton hard nofile 5/holberton hard nofile 50000/g" /etc/security/limits.conf',
}

exec {'soft_inc':
  provider => shell,
  command  => 'sudo sed -i "s/holberton soft nofile 4/holberton soft nofile 40000/g" /etc/security/limits.conf',
}
