# Fix 500 error and Automating using Puppet
exec { 'modify_file':
  command => "sed -i 's/phpp/php/g' /var/www/html/wp-settings.php",
  path    => '/bin',
}
