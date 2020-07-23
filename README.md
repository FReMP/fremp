# FReMP Stack boilerplate

![FReMP Demo](./demo.png)

## Requirements
- Python3/Flask
- ReactJS
- MongoDB

## Clone & use
You will have to add some data in your MongoDB before starting, so that you can retrieve it in your front-end.
```
$ mongo
$ use fremp_test_app1_db
$ db.fremp_test_app1_col.insertOne({'data': 'Hello World from MongoDB'})
```

Now that you have some data in your MongoDB, you can clone the repository and install the app locally.
```
$ git clone https://github.com/FReMP/fremp
$ cd backend
$ python3 app.py
```
This will run your server locally at http://localhost:5000

```
$ cd ../frontend/
$ yarn start
```
To view the project now, open http://localhost:3000