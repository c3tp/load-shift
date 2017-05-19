# How to test

1. Get access to a kubernetes deployment. 

## Using the elasticsearch instance. 
Run 
```
kubectl create -f elasticsearch-deployment.yaml
kubectl create -f elasticsearch-service.yaml
```

Run 
```
python ./download_image.py --url http://<some-slave-ip>:32111 --period 0
```
inside of some instance with access the kubernetes nodes. 
This will most easily be the master node of the kubernetes cluster. 
This will generate a request to the ip with minimum time between requests at <period> seconds. 

Run
```
kubectl apply -f elasticsearch-deployment-2.yaml
```
This will be a redeployment of the caom-deployment again, but it will try to deploy with nodes that are labeled
`area=two` rather than `area=one`

## Using the built caom2repo from opencadc in dockerhub.
Run 
```
kubectl create -f caom-deployment.yaml
kubectl create -f caom-service.yaml
```

Run 
```
python ./download_image.py --url http://<some-slave-ip>:32700 --period 0
```
inside of some instance with access the kubernetes nodes. 
This will most easily be the master node of the kubernetes cluster. 
This will generate a request to the ip with minimum time between requests at <period> seconds. 

Run
```
kubectl apply -f caom-deployment-2.yaml
```
This will be a redeployment of the caom-deployment again, but it will try to deploy with nodes that are labeled
`area=two` rather than `area=one`
