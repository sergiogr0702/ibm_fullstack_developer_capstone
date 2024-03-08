![Logo](https://howtolearnmachinelearning.com/wp-content/uploads/2021/04/coursera_machine_learning_ibm-768x110.png)


# IBM Course Project - Dealership and Reviews Service

This Django project is a comprehensive solution for managing reviews on dealerships, leveraging the power of MongoDB for data storage and two Node.js applications for backend processing and interaction with the database. This project is designed to efficiently handle large volumes of data, thanks to MongoDB's scalability and flexibility. 

The Node.js applications play a crucial role in the backend, acting as intermediaries between the Django frontend and the MongoDB database. They handle data processing tasks, ensuring that the data flowing between the frontend and the database is clean, efficient, and secure. These applications can perform complex operations, such as data validation, aggregation, and transformation, before the data is stored in MongoDB. This dual-layered architecture ensures that the system is robust, scalable, and capable of handling high volumes of user interactions and data transactions.


## Badges

[![Mongo](https://img.shields.io/badge/MongoDB-4EA94B?style=for-the-badge&logo=mongodb&logoColor=white)]()

[![Django](https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=green)]()

[![NodeJS](https://img.shields.io/badge/Node%20js-339933?style=for-the-badge&logo=nodedotjs&logoColor=white)]()

[![NPM](https://img.shields.io/badge/npm-CB3837?style=for-the-badge&logo=npm&logoColor=white)]()

[![Express](https://img.shields.io/badge/Express%20js-000000?style=for-the-badge&logo=express&logoColor=white)]()

[![React](https://img.shields.io/badge/React-20232A?style=for-the-badge&logo=react&logoColor=61DAFB)]()

[![Bootstrap](https://img.shields.io/badge/Bootstrap-563D7C?style=for-the-badge&logo=bootstrap&logoColor=white)]()

[![Docker](https://img.shields.io/badge/Docker-2CA5E0?style=for-the-badge&logo=docker&logoColor=white)]()

[![Kubernetes](https://img.shields.io/badge/kubernetes-326ce5.svg?&style=for-the-badge&logo=kubernetes&logoColor=white)]()
## Installation

To run the project, you need to install Node, Kubernetes and Docker

[Install Node](https://nodejs.org/en/download)

[Install Docker](https://docs.docker.com/engine/install/)

[Install Kubernetes](https://kubernetes.io/docs/setup/)
## Run Locally

Clone the project

```bash
  git clone https://github.com/sergiogr0702/ibm_fullstack_developer_capstone.git
```

Go to the project directory

```bash
  cd ibm_fullstack_developer_capstone
```

Launch a new terminal, go to carsInventory folder, build docker image and deploy with docker compose to run the cars Mongo database

```bash
  cd server/carsInventory
  docker build nodeapp .
  docker-compose up
```

Launch a new terminal, go to carsInventory folder, build docker image and deploy with docker compose to run the dealershrip Mongo database

```bash
  cd server/database
  docker build nodeapp .
  docker-compose up
```

Launch a new terminal and deploy the sentiment analyzer microservice with docker

```bash
  cd server/djangoapp/microservice
  docker build -t sentiment_analyzer .
  docker run -d -p 5000:5000 --name analyzer sentiment_analyzer
```

Install dependencies for the frontend react application and build the production code

```bash
  cd server/frontend
  npm install
  npm run build
```

Build the main Django app docker image and run it on kubernetes

```bash
  cd server

  docker build -t dealership .
  docker push dealership

  kubectl apply -f deployment.yaml
  kubectl port-forward deployment.apps/dealership 8000:8000
```

Or built on local with a Python virtual enviorment 

```bash
  cd server

  pip install virtualenv
  virtualenv djangoenv
  source djangoenv/bin/activate

  python3 -m pip install -U -r requirements.txt

  python3 manage.py makemigrations
  python manage.py migrate --run-syncdb

  python3 manage.py runserver
```


## Environment Variables

Once the apis are running, you will need to copy the urls and add the following environment variables to your .env file

`backend_url` The url where the dealerships mongo-node app is running

`searchcars_url` The url where the cars mongo-node app is running

`sentiment_analyzer_url` The url where the sentiment analyzer node app is running



## Authors

- [@lavskillup](https://github.com/lavskillup)
- [@sergiogr0702](https://github.com/sergiogr0702)


## Acknowledgements

 - [Coursera team](https://www.coursera.org/)
 - [IBM hands on labs team](https://www.ibm.com/blog/announcement/new-hands-on-labs-for-ibm-cloud-essentials-course/)
 - [Awesome README](https://github.com/matiassingers/awesome-readme)
 - [How to write a Good readme](https://bulldogjob.com/news/449-how-to-write-a-good-readme-for-your-github-project)
 - [Badges 4 README.md](https://github.com/alexandresanlim/Badges4-README.md-Profile)


## License

[Apache-2.0 license](https://choosealicense.com/licenses/apache-2.0/)
