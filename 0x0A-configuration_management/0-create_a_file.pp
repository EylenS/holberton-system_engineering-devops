# Creates a file in /tmp called school with specific requirements

file { 'school':
  path    =>  '/tmp/school',
  mode    =>  '0744',
  owner   =>  'www-data',
  group   =>  'www-data',
  content =>  'I love Puppet',
}
