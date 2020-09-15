# DevOps Challenge

## Instructions

Your goal is to deploy this application using a container orchestration solution.


We won't look at your account or call your application already running, we want you to create a way that we can recreate all your infrastructure in our account in a simple way.

Create a private github repository with your code, add [rscoz](https://github.com/rscoz) as a contributor, the history of commits is important.

## Deliverables
1. Create a clean [app](./app) `Dockerfile`
2. Push this image to a public registry
3. Using IAC(infrastructure as code) create a Kubernetes cluster
4. Deploy this app as [deployment](https://kubernetes.io/docs/concepts/workloads/controllers/deployment/) in Kubernetes cluster with a [ingress](https://kubernetes.io/docs/concepts/services-networking/ingress/) solution
5. Tell us how to access with [curl](https://curl.haxx.se/) the public api using Bearer Authentication


If you choose aws for this challenge, you will probably need to create a [free-tier](https://aws.amazon.com/free/) account on AWS, or use an existing one.
\
