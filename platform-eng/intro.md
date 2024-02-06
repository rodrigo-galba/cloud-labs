<!-- https://www.youtube.com/watch?v=ghzsBm8vOms -->

### Introduction (00:00 - 09:56)

- Platform engineering is a new topic in DevOps and Cloud space.
- There's a lot of discussion about whether platform engineering replaces DevOps or is an addition to it.
- Platform engineering changes established rules of DevOps, SRE and Cloud engineering.

### Problems with Traditional Dev and Ops Teams

- Developers and operations working in separate teams caused an inflexible and slow process.
- DevOps was introduced to unite those teams and remove communication challenges and knowledge silos.
- DevOps teams became responsible for the application as well as the underlying runtime and infrastructure.
- This increased flexibility and speed of work but added tremendous cognitive load and responsibility.

### Challenges with DevOps Teams

- DevOps teams are responsible for many tasks including setting up CI/CD platforms, creating pipelines, writing Terraform scripts, configuring Kubernetes clusters, adding security scans, and maintaining Helm charts.
- DevOps teams have less time to build business value in the application.
- DevOps teams may not have enough expertise to do everything correctly.
- Each team builds and operates its own platform, leading to inefficiency and inconsistency across the organization.

### What is Platform Engineering?

- Platform engineering takes the tools needed for deploying and running the application and standardizes their usage across teams.
- Platform engineers standardize everything that is part of the application's non-functional requirements.
- These requirements include version control systems, CI/CD pipelines, runtime environments like Kubernetes, underlying infrastructure like AWS Cloud, logging and monitoring, and proper security.

### Benefits of Platform Engineering

- Platform engineering reduces cognitive load and organization-wide inconsistency.
- Platform engineering ensures that all applications meet the same non-functional requirements.
- Platform engineering helps to scale and reduces human resource costs.
- Platform engineering ensures proper security and compliance across the organization.

### Platform Engineering Responsibilities (10:02 - 19:57)

- Platform engineers standardize usage of tools that offer CI/CD services for the platform.
- Platform engineering is responsible for managing and operating the admin side of tools like gitlab, Kubernetes, Jenkins, Cloud platforms, databases, etc.
- Platform engineers take over the operation side of these tools to standardize the tools across teams.
- Platform engineers need to select the standard tools and set them up with production and security best practices.
- Platform engineers build the internal developer platform (IDP) which hides away and abstracts the complexity of operating and managing the services that developers need to release and run their applications.

### Benefits of Platform Engineering

- Platform engineering takes the load off the application developers.
- Platform engineering extracts the need for expertise to administer these tools from the application teams.
- Platform engineering distributes the pressure, responsibility, and the need for expertise among multiple application teams and one organization-wide platform team.
- Platform engineering offers a ready solution for the application teams, which means that individual application teams don't need to decide which CI/CD tool to use or which Kubernetes cluster set up to use.
- Platform engineering standardizes the pipeline steps with security scans and offers them to application teams, which means regulation-specific scans will be part of every pipeline by default.

### Internal Developer Platform (IDP)

- Platform engineers create an abstraction layer on top of tools with a user-friendly interface like a UI or API.
- Application teams can self-service whatever services and tools they need.
- Provisioned, configured, secured services with an interface to easily interact and access them to use for the applications is a platform and since developers can just log in and self-service without going to the platform team to ask for the resources it is a platform as a service for the internal developer teams or also called an internal developer platform or IDP.

### Platform Flexibility

- Platform engineers standardize the tools that are used across teams.
- Platform engineers offer gitlab CI/CD as a standard solution, but application teams can choose to use other modern tools or tools that fit their workflow better.
- Platform engineers help application teams set up and configure their preferred tools with best practices.
- Platform engineers can integrate new services and tools in the platform and offer them to other teams as well who may also benefit from using them.

### Introduction (20:03 - 30:00)

- Platform engineering is a step forward from DevOps, not a step backwards with Dev and Ops separated again.
- Platform engineering is about keeping the platform flexible while adding guard rails and pre-configurations to ensure security consistency, proper configuration, and so on.

### Infrastructure as Code Tools are Essential Component of IDP

- Avoid strict rules for selecting and using tools.
- Platform engineering team can leverage infrastructure as code tools like Terraform, Ansible, or Pulumi to create templates.
- Templates can have baked-in best practice configurations and be used to automate provisioning of resources.
- This leads to a fully automated self-service process with high flexibility.

### Implementing Platform Engineering Teams Successfully

- Treat the IDP as a product and continuously improve it over time.
- Start with small steps that can immediately add value to at least one team.
- Work closely with application teams to identify common tools that many teams are using across the organization.
- Start with low hanging fruits like integrating common tools that can be offered as a service.
- Building a platform team is as much about human aspect and how to manage the work with application teams as it is about tools and technologies.
- Create a culture around collaboration rules and clear responsibilities.
- In the long term, have a company-wide platform engineer team and a bunch of app teams that use pre-configured services that they can self-service via a platform that platform team.

### Role of DevOps Engineer in Platform and Application Teams (30:07 - 40:05)

- Platform team takes over the operations part while application team is responsible for properly using the tools and integrating them into their development workflow.
- Application teams don't need to set up and operate the cluster but they still need to know how to deploy their applications into the cluster properly.
- DevOps engineers are still needed in product teams but they now have shared their cognitive load and don't have to have deep expertise in cloud and Kubernetes and Helm charts monitoring security compliance development and hundred other things because now they are focused on properly using those non-functional tools rather than operating them.

### DevOps Processes in Platform and Application Development

- DevOps processes are needed both in the application and platform development.
- Companies may have a separate DevOps engineer role in both teams or make these tasks as part of developer work.
- Platform just like the application needs a continuous development with many feedback iterations and close input Gathering From The End users which are mostly application teams but sometimes also governance and compliance people.

### Teaching Application vs Platform DevOps in Courses

- In the DevOps bootcamp, you learn both parts of DevOps administering and operating or setting up the tools as well as using those tools to streamline the development process.
- In Kubernetes module, you learn mostly the Kubernetes usage side but also the part of configuring proper monitoring and setting up alerting in the cluster.
- In the GitLab CI/CD course, you learn not only how to set up the CI/CD pipeline for the microservices application but also the architecture of GitLab CI/CD and how to configure Runners locally as well as on AWS virtual machine.

### Difference between Platform and Cloud Engineer

- Platform engineering is an enhancement of all other concepts like DevOps, Cloud SRE.
- Cloud engineer needs to know cloud services be expert in that usually even specializing in one of the cloud platforms.

### Platform Engineering (40:11 - 42:35)

- Combines cloud services to build infrastructure that maps to company needs
- Offers a wider range of knowledge and tools outside of the cloud alone
- Builds a platform for developers or product teams to self-service resources on top of cloud resources and various other tools
- Takes the infrastructure and services that AWS offers and creates a custom platform as a service for internal teams

### Team Structure

- Smaller companies: Platform Engineers take over DevOps role
- Larger companies: Cloud team works with platform team and share expertise
- Industry standard has not yet evolved for structuring teams

### Benefits for Engineers

- Helps with job search and understanding of responsibilities
- Provides clarity around roles for teams and companies
