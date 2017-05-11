# TO DO
1. Write program to send wgets every few seconds
2. Write script for deployment of pod on specific node
3. Write script for deployment of service
4. Write script to shift from the deployment of pod on specific node to the other one. 
5. Run the shift node while sending the wgets. 

# Test redeploy of nodes

# Test redeploy of service
- to update, we need to just create a new one. 
- LOL: updating was broken for services with dashes in them. 
- see https://github.com/kubernetes/kubernetes/issues/36072

so to test redeployment of a service

Deploy the service:
```
kubectl create -f ./nginx-service.ymal
``` 

Create a service with the same name and slightly modified.
Then apply your changes:

```
kubectl apply -f ./nginx-service.yaml
```