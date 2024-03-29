#Introduction to Puppet from Configuration Management and the Cloud (Google IT Automation with Python)
#Make sure to install Puppet before coding this

#Example One
#To install the pseudo package in a package
class sudo {
 
  package { 'sudo': #used the package keyword declaring a package resource
    ensure => present,
  }
}
#Example Two
#Defining a file resource
class sysctl {
  #Make sure the directory exists, some distros don't have it
  file { '/etc/sysctl.d': #directory - after the colon come the attribute to set for resource
    ensure => directory,
  }
}
#Example Three
#Using a file resource to configure the contents of etc/timezone
class timezone {
      file { '/etc/timezone':
        ensure  => file,
        content => "UTC\n",
        replace => true,
      }
}
#Example Four
#three resources, a package, a file, and a service  related to the Network Time Protocol (NTP)
class ntp {
  package { 'ntp':
    ensure => latest, # to synchronize the clocks
  }
  file { '/etc/ntp.conf':
    source => 'puppet:///modules/ntp/ntp.conf' # making sure that the NTP package is always upgraded to the latest version
    replace => true,
  }
  service { 'ntp':
    enable  => true,
    ensure  => running,
  }
}
#Example Five
#Built-in facts
#is-virtual fact together with conditional statement to devide whether the smartmontools package should be installed or purged
if $fact['is_virtual']{ # Fact is variable and all variable names are preceded by a dollar sign in Puppet's DSL
    package {'smartmontools' # each condition contain package resource
      ensure => purged, # equal greater than is to assign value to the attributes 
    }
} else {
    package {'smartmontools'
      ensure => installed,
    }
}
#Example Six
#Managing resource relationship
# write resource types in lowercase when declaring them, but capitalize them when referring to them from another resource's attributes.
vim ntp.pp
class ntp {
  package { 'ntp':
    ensure => latest,
  } 
  file { '/etc/ntp.conf':
    source => '/home/user/ntp.conf',
    replace => true,
    require => Package['ntp'], # resource types are written in lowercase, but relationships use uppercase for the 
first letter of the resource. 
    notify  => Service['ntp'],
  }
  service { 'ntp':
    enable  => true,
    ensure  => running,
    require => File['/etc/ntp.conf'],
  }
}
include ntp # tell Puppet that we want to apply the rules described in a class
