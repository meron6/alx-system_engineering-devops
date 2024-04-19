# Puppet manifest to execute a command to kill a process named 'killmenow'

exec { 'killmenow':
  command     => '/usr/bin/pkill killmenow',
  path        => ['/bin', '/usr/bin'],
  refreshonly => true,
}
