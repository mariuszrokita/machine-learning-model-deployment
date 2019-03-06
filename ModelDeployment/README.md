# Introduction

The folder contains a definition of a single Dockerfile for the API Flask app. The API is a means to expose trained ML model.

## Building and running the Docker Image

The easiest way to build and run Docker image is to execute following command:

```shell
sh build-and-run-container.sh
```

Once the image is built and run, you can go to your favourite web browser and to the [http://localhost:5000/](http://localhost:5000/) address.

There you should see a simple *Welcome to Titanic Prediction API* message which means that all is up and running.

In order to make test inference execute following command:

(Mac):

```shell
curl -X POST -H "Content-Type: application/json" \
     -d '{ "Pclass": 2, "Sex": 1, "Age": 1, "Fare": 2, "Embarked": 1, "Title": 3, "IsAlone": 0 }' \
     http://localhost:5000/api/predict
```

(Windows):

```shell
curl -X POST -H "Content-Type: application/json" ^
	-d "{ \"Pclass\": 2, \"Sex\": 1, \"Age\": 1, \"Fare\": 2, \"Embarked\": 1, \"Title\": 3, \"IsAlone\": 0 }" ^
	http://localhost:5000/api/predict
```


The response result should look more or less like this one:

```json
[
  {
    "name": "NotSurvived",
    "value": 5.58
  },
  {
    "name": "Survived",
    "value": 94.42
  }
]
```

## Deployment to Azure Kubernetes cluster

This set of instructions is inspired by [Ben Coleman](https://azurecitadel.com/cloud-native/kubernetes/).

**Important!** If using an existing subscription you will need rights to create a service principal in the Azure AD tenant you use. Otherwise you will get the **Directory permission is needed for the current user to register the application** error message and will not be able to proceed.

First, run the following command to sign in to the Azure Portal:

```shell
az login
```

Then, execute deployment script:

```shell
sh ./deploy-to-azure-aks.sh
```