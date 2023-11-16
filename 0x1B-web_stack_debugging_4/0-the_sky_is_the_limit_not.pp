# Fix the issue with failed requests
exec { 'fix-failed-requests':
    command => 'sed -i "s/15/50000/" /etc/default/nginx',
    path    => '/usr/local/bin/:/bin/'
}

exec { 'restart':
    command => 'nginx restart',
    path    => '/etc/init.d/'
}
