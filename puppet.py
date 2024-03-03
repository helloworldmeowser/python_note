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