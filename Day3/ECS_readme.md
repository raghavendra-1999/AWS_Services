## **Amazon ECS (Elastic Container Service) - Container Orchestration Service**

**What is Amazon ECS?**
Amazon ECS is a fully managed container orchestration service that enables you to run and scale Docker containers on AWS. ECS makes it easy to deploy, manage, and scale containerized applications by handling the underlying infrastructure. You can run your containers on a cluster of EC2 instances or use the serverless Fargate option.

**Advantages of Amazon ECS**
- **Fully Managed**: AWS takes care of the container orchestration, management, and scaling, reducing the operational burden.
- **Scalability**: Automatically scales the number of container instances or tasks to meet demand.
- **Integration with AWS Services**: Seamlessly integrates with other AWS services like EC2, ECR (Elastic Container Registry), IAM, CloudWatch, ALB (Application Load Balancer), and more.
- **High Availability**: Built-in features such as Multi-AZ (Availability Zone) deployment options ensure high availability and fault tolerance for your containerized applications.
- **Cost-Effective**: With ECS Fargate, you only pay for the resources you use without managing underlying EC2 instances. You can also run ECS tasks on EC2 instances if you need more control over your infrastructure.
- **Container Management**: ECS simplifies running, stopping, and managing Docker containers on clusters of EC2 instances. With features like task definitions, service management, and load balancing, it makes container management easier.

**Common Use Cases**
- **Microservices Architecture**: ECS enables you to easily deploy and manage microservices, allowing developers to focus on code while AWS handles scaling and container orchestration.
- **Web and Mobile Applications**: ECS powers containerized applications that need to scale based on demand, such as user-facing websites or mobile app backends.
- **Machine Learning**: Use ECS to deploy machine learning models in containers, enabling scalable inference workloads and handling large datasets.
- **CI/CD Pipelines**: Run containerized continuous integration and deployment pipelines with ECS, automating the build, test, and deployment phases of the software development lifecycle.

**Key Features of ECS**
- **Task Definitions**: ECS allows you to define your container specifications, including which Docker images to use, environment variables, and resource requirements.
- **Service Auto Scaling**: ECS can automatically adjust the number of running instances in a service to meet demand.
- **Integrated Load Balancing**: ECS works with the AWS Application Load Balancer (ALB) and Network Load Balancer (NLB) to distribute traffic across container instances or services.
- **ECR Integration**: You can integrate ECS with Amazon Elastic Container Registry (ECR) to store and manage Docker container images in a secure, scalable registry.
- **Cluster Management**: ECS provides tools to create, manage, and monitor container clusters.

**1. Create an ECS Cluster using AWS CLI**

```sh
aws ecs create-cluster --cluster-name raghav_clust_cli
```

<img width="793" alt="ECS_Cli" src="https://github.com/user-attachments/assets/606bc1de-58ec-43c5-8c6d-dbddfdd670c8" />

**2. Create an ECS Service Using Boto3**



