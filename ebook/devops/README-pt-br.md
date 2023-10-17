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

![DevSecOps image]()

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

## Praticas
- Automação de testes contínua
- Monitoramento contínuo
- Segurança como código

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
- https://aws.amazon.com/pt/what-is/devsecops/
- https://www.aquasec.com/cloud-native-academy/devsecops/devsecops-tools/
- https://techcommunity.microsoft.com/t5/desenvolvedores-br/descubra-vulnerabilidades-e-automatize-a-atualiza%C3%A7%C3%A3o-de/ba-p/3335240


### MLOps
### DataOps
### GitOps
### FinOps

## Engenharia de plataforma