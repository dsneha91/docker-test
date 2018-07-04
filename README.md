# docker-test

Dockerized a simple Flask REST API to read a MySql database. 

To install Docker:
  Mac installation
    https://store.docker.com/editions/community/docker-ce-desktop-mac
  Ubuntu installation
    https://docs.docker.com/install/linux/docker-ce/ubuntu/#install-docker-ce-1
    
Join Docker Hub(this will allow to install public version of image)
  https://hub.docker.com/
    
Once installed, run docker.
    
To create and run the image on the terminal:
  1. Git clone
      git clone https://github.com/dsneha91/docker-test.git
  2. Go to the flask app
      cd docker-test
  3. Docker-compose:
      docker-compose up
  4. Check the browser
      http://0.0.0.0:5000
      
      
  Terminate using ->  docker-compose down.
