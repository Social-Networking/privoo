# Installation
Get code: `git clone https://github.com/itsMichael/privoo`

# In vagrant
Install vagrant and provider (like virtualbox).
Change directory and build machine - `cd privoo/vagrant && vagrant up`
Build docker: `sudo docker-compose build`
Run migrations: `sudo docker-compose run web python3 manage.py migrate`
Create superuser: `sudo docker-compose run web python3 manage.py createsuperuser`
Run website: `rs`

# Without vagrant
On your operating system install docker and docker-compose. (In Ubuntu: `sudo apt install docker docker-compose`)
Change directory and build docker: `cd privoo && sudo docker-compose build`
Run migrations: `sudo docker-compose run web python3 manage.py migrate`
Create superuser: `sudo docker-compose run web python3 manage.py createsuperuser`
Run website: `sudo docker-compose up`


# All
Website in web browser: http://127.0.0.1:8000
Admin panel: http://127.0.0.1:8000/admin
