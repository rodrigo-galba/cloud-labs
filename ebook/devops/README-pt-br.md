# DevOps ebook

Esse livro irá abordar DevOps de uma perspectiva geral. Não é focado em exercicíos práticos ou detalhes excessivamente tecnicos.
Linguagens suportadas: en-us, pt-br.

## Capitulos

- DevOps aplicado
  - MLOps
  - DataOps
  - GitOps
  - FinOps

- Engenharia de plataforma

## DevOps aplicado

**Contexto**  
Os principios e práticas DevOps tem sido aplicados e adotados de forma ampla. Várias áreas que inicialmente trabalhavam de outra forma, foram se modaldno e até mesmo sendo criadas. Veremos como DevOps está sendo aplicados nessas áreas. 

### SecOps

O que é DevSecOps?

> SecOps, também conhecido como SecDevOps ou DevSecOps, é uma denominação da Ciência da Computação que surgiu com o objetivo de definir a integração de processos de segurança da informação às atividades de desenvolvimento e operações dentro do segmento de tecnologia. Formado por profissionais especializados em segurança e TI, o time de SecOps determina o sucesso na prevenção a ataques cibernéticos. - Wikipedia

> DevSecOps é a prática de integrar testes de segurança a todas as etapas do processo de desenvolvimento de software. Inclui ferramentas e processos que incentivam a colaboração entre desenvolvedores, especialistas em segurança e equipes de operação para criar software eficiente e seguro. O DevSecOps promove uma transformação cultural que torna a segurança uma responsabilidade compartilhada por todos que estão criando o software. - Amazon Web Services

![DevSecOps](./images/Fig_1_DevOps_Evolution.original.png)

> O termo nasceu a partir da ascensão da metodologia DevOps e consequentemente com o aumento da arquitetura de Software como serviço, onde o software desenvolvido é essencialmente hospedado em ambientes nuvem, com integração e entrega contínuas surgiu a necessidade do mercado de integrar processos de segurança dentro desse escopo de agilidade, além de tentar sobrepor as dificuldades no gerenciamento de software entre times de maneira confiável. - Wikipedia

## Caracteristicas

- Cultura
  - Promover colaboração entre os times de desenvolvimento, segurança e operações, disseminando a ideia de um mesmo principio: a entrega de software para o usuário final.
- Automação
  - Uso de automação para alcançar entregas e feedback mais rápido. É importante que a abordagem na implementação não impact na agilidade.
- Monitoramento
  - o monitoramento é muito focado em ameaças e vulnerabilidades em tempo real, com o objetivo de observar a qualidade e a segurança do objeto de estudo em todas as fases de implantação.

- Compartilhamento
  - Tradicionalmente a equipe de segurança dentro do processo de desenvolvimento de software fica mais próxima do fim do ciclo de projeto
  - SecOps promove a integração desse time dentro do escopo de concepção e desenvolvimento, tanto com objetivo de mudar a mentalidade de todo processo como de incluir maturidade no que tange aspectos relacionados à segurança da informação. 

## Práticas
- Automação de testes contínua
  - Controles de segurança automatizados em todas as partes do desenvolvimento de software são fatores importantes para garantir entregas seguras e permitir que os testes detectem anomalias em diferentes fases do processo.
- Monitoramento contínuo
  - É importante gerar evidências dos controles de segurança automatizados ao longo do processo, para que estes possam gerar o melhor resultado possível é necessário o acompanhamento de ponta-a-ponta.
- Segurança como código
  - processo de definir políticas de segurança com o uso de modelos de script (templates) ou arquivos de configuração que podem ser ativados automaticamente de acordo com agendamentos ou manualmente pelo usuário.

## Benefícios
- Proteção contínua
- Respostas rápidas e efetivas
- Diminuição nos custos de operações e violações
- Prevenção de ameaças
- Expertise de Segurança
- Conformidade
- Comunicação e colaboração
- Integração da equipe de segurança nos processos de concepção
- Automações

## Ferramentas
- Veracode
  - Veracode is an cloud-based security tool created to simplify developer security testing. It provides comprehensive visibility into your application’s security posture and offers remediation tips for any vulnerabilities it detects.
- OWASP Zed Attack Proxy (ZAP)
  - OWASP ZAP is a free and open-source web application security scanner. It is highly customizable and can identify vulnerabilities in your application and works by intercepting аnd modifying HTTР аnd HTTРS trаffic between the wеb аpplicаtion аnd сlient. ZAP has the capability to scan for a range of security issues and includes аutomаted аnd mаnuаl scаnning modes.
- SonarQube
  - SonarQube is a popular code quality tool that offers security-focused plugins to help identify code vulnerabilities during development, provides continuous feedback on your code, and enables you to maintain high code quality.
- Fortify
  - Fortify is an industry-leading application security tool that offers comprehensive testing capabilities, including static, dynamic, and interactive application security testing. It also offers integrations with leading tools for seamless DevSecOps.
- Dependabot Github
  - Dependabot é uma ferramenta que identifica vulnerabilidades nas dependências do seu código e cria Pull Requests com a atualização da dependência com a versão já corrigida.
- Snyk
  - Snyk is a popular developer-first application security tool that integrates directly into your development tools and workflows. It supports multiple languages and offers actionable insight into your app’s security posture.
- Trivy
  - Trivy is an easy-to-use open source vulnerability scanner for container images. It is stateless, is easy to deploy, and can scan images quickly without needing to download vulnerability databases. Trivy detects vulnerabilities in operating system packages (Alpine, RHEL, CentOS, etc.) and application dependencies included in container images.


Referências
- https://pt.wikipedia.org/wiki/SecOps
- https://insights.sei.cmu.edu/blog/a-framework-for-devsecops-evolution-and-achieving-continuous-integrationcontinuous-delivery-cicd-capabilities/
- https://aws.amazon.com/pt/what-is/devsecops/
- https://www.aquasec.com/cloud-native-academy/devsecops/devsecops-tools/
- https://techcommunity.microsoft.com/t5/desenvolvedores-br/descubra-vulnerabilidades-e-automatize-a-atualiza%C3%A7%C3%A3o-de/ba-p/3335240


### GitOps 

**O que é Git?**  
Git é um sistema de controle de versão distribuído utilizado para gerenciar arquivos de diversos tipos e também uma ferramenta para colaboração de times para gerenciar o código fonte de uma aplicação.  

**O que é GitOps?**  
> O GitOps usa repositórios Git como uma única fonte de informações para oferecer **infraestrutura como código**. O código enviado verifica o **processo de CI**, enquanto o **processo de CD** verifica e aplica os requerimentos de elementos como **segurança**, **infraestrutura como código** ou quaisquer outros limites definidos para a framework de aplicações. Todas as alterações de código são acompanhadas, facilitando as atualizações e oferecendo controle de versão, caso uma reversão seja necessária. - RedHat

## Benefícios

- Um fluxo de trabalho padrão para o desenvolvimento de aplicações.
- Aumento da segurança para definir antecipadamente requisitos da aplicação.
- Maior confiabilidade com visibilidade e controle de versão pelo Git.
- Consistência entre quaisquer ambientes on-premise, clusters e nuvem.

## Caso de uso

> Imagine o seguinte cenário: você tem várias alterações a serem aplicadas em diferentes aplicações sendo executadas em diferentes clusters Kubernetes, distribuídos em mais de um cloud provider e/ou no ambiente on-premisse. Para fazer isso, você pode executar de forma manual ou desenvolver um ou mais pipelines. De qualquer forma, neste cenário existe uma grande complexidade e o esforço técnico de um time de operação, além do risco envolvido quando for necessário fazer rollback. Outra preocupação é evitar as divergências entre o que está aplicado no cluster Kubernetes e o que está versionado no git.

> Para ajudar na execução de atividades semelhantes a essa, a abordagem GitOps trata a infraestrutura como código tendo as informações versionadas em um ou mais repositórios git, tratando-os como fonte da verdade e faz uso de ferramentas para aplicar continuamente as mudanças a partir de um ponto central.

## CICD

> Em contraste com uma esteira de Implantação Contínua (CD) tradicional, onde temos um estágio executando intervenção direta no nosso ambiente, com GitOps temos um mecanismo automatizado de detecção de desvios (“drift”) que identifica se o estado desejado armazenado no repositório Git foi alterado e implementa as modificações necessárias de forma autônoma. A abordagem proposta pelo GitOps busca eliminar intervenções diretas na infraestrutura e simplificar o processo de Implantação Contínua em ambientes distribuídos, além de melhorar a governança através das informações de rastreabilidade fornecidas pelo Git. - Amazon Web Services

Reconciliação ou Sincronização é o ato de modificar o estado do cluster para equiparar com a versão armazenada no Git.

## Ferramentas

- ArgoCD
  - Argo CD, é uma ferramenta declarativa que usa a abordagem GitOps para implantar aplicações no Kubernetes.
  - Pode ser usado para gerenciar várias aplicações em diferentes clusters Kubernetes a partir de um único repositório.
  - Ele pode se conectar a repositórios git públicos e privados
  - é gratuito, tem o código fonte aberto, é um projeto incubado pela CNCF,
  - Possui uma interface web de visualização e gerenciamento dos recursos,
  - Também pode ser configurado via linha de comando.
  - https://github.com/argoproj/argo-cd
  - ArgoCon: https://events.linuxfoundation.org/kubecon-cloudnativecon-north-america/co-located-events/argocon/#about
- FluxCD
  - https://fluxcd.io/
  -  é uma ferramenta para manter clusters Kubernetes em sincronia com fontes de configuração (como repositórios Git) e automatizar atualizações de configuração quando há uma nova versão a ser implantada.
  - A versão 2 desta ferramenta foi desenvolvida do zero para usar o sistema de extensão da API do Kubernetes e se integrar com restante do ecossistema do Kubernetes.
  - Não possui interface web, somente linha de comando.


## GitOps Best practices

- #1: Two Repos: One For App Source Code, Another For Manifests
- #2: Choose The Right Number Of Deployment Config Repos
- #3: Test Your Manifests Before You Commit
- #4: Git Manifests Should Not Change Due To External Changes
- #5: Plan How You’ll Manage Secrets

Referências
- https://www.redhat.com/pt-br/topics/devops/what-is-gitops
- https://blog.aeciopires.com/usando-o-argo-cd-para-implementar-a-abordagem-gitops-nos-clusters-kubernetes/
- https://landscape.cncf.io/?project=incubating&selected=argo
- https://medium.com/trendyol-tech/how-to-use-gitops-with-argocd-1782b8493cc3
- https://levelup.gitconnected.com/gitops-in-kubernetes-with-gitlab-ci-and-argocd-9e20b5d3b55b
- https://blog.argoproj.io/5-gitops-best-practices-d95cb0cbe9ff
- https://aws.amazon.com/pt/blogs/aws-brasil/implementando-gitops-no-amazon-eks-com-fluxcd/

### DataOps
### MLOps
### FinOps

## Engenharia de plataforma