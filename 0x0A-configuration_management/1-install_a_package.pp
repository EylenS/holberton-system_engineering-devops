# Install puppet-lint, using Puppet

package { 'puppet-lint':
  ensure   => 'installed',
  provider => 'gem',
}
