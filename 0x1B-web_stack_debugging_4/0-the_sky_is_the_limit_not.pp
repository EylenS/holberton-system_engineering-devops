# change open file allowed - ulimit
exec { 'increase_ulimit':
  command => 'sed -i s/15/4096/g /etc/default/nginx; service nginx restart',
  path    => '/bin',
}
