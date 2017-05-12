# How to test
get access to a kubernetes deployment. 

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
