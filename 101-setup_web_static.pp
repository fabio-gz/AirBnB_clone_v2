# Redo the task #0 but by using Puppet

exec { 'runupdate':
  command  => 'sudo apt-get -y update',
  provider => shell
}
exec { 'install nginx':
  command  => 'sudo apt-get -y install nginx',
  provider => shell,
  require  => Exec['Update bash']
}
exec { 'create shared':
  command  => 'sudo mkdir -p /data/web_static/shared/',
  provider => shell,
  require  => Exec['Install NGINX']
}
exec { 'create test':
  command  => 'sudo mkdir -p /data/web_static/releases/test/',
  provider => shell,
  require  => Exec['Create shared path']
}
exec { 'html content':
  command  => 'echo "FakeHTML" | sudo tee /data/web_static/releases/test/index.html',
  provider => shell,
  require  => Exec['Create test path'],
  returns  => [0, 1]
}
exec { 'symbolic link':
  command  => 'sudo ln -sf /data/web_static/releases/test/ /data/web_static/current',
  provider => shell,
  require  => Exec['Adding fake HTML']
}
exec { 'add permissions':
  command  => 'sudo chown -R root:root /data/',
  provider => shell,
  require  => Exec['Symbolic link']
}
exec { 'insert location':
  command  => 'sudo sed -i "38i\\\n\tlocation \/hbnb_static\/ {\n\t\talias \/data\/web_static\/current\/;\n\t\tautoindex off;\n\t}" /etc/nginx/sites-available/default',
  provider => shell,
  require  => Exec['Permissions']
}
exec { 'restart nginx':
  command  => 'sudo service nginx restart',
  provider => shell,
  require  => Exec['Adding location']
}
