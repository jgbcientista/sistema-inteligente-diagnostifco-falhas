# Projeto: Diagnóstico Inteligente de Microserviços com Observabilidade e Machine Learning

Este projeto consiste em um ecossistema de microserviços implementados com **Spring Boot**, integrados a uma infraestrutura completa de **observabilidade (ELK, Prometheus, Grafana)** e um serviço de **Machine Learning** para análise e detecção de anomalias nos logs.

---

## 🧱 Estrutura do Projeto

microservices/
├── pedidos/ # Microserviço de pedidos
├── estoque/ # Microserviço de estoque
├── pagamento/ # Microserviço de pagamento
├── logstash/ # Configuração do Logstash (logstash.conf)
├── prometheus/ # Configuração do Prometheus (prometheus.yml)
├── ml_service/ # Serviço Python de Machine Learning (Isolation Forest)
├── simulator/ # Enviador de logs simulados
├── grafana_dashboards/ # Dashboards JSON e alertas
└── docker-compose.yml # Arquivo unificado para subir todos os serviços

---

## ⚙️ Tecnologias Utilizadas

- **Spring Boot (Java)** - Backend dos microserviços  
- **Elasticsearch + Logstash + Kibana (ELK)** - Monitoramento de logs  
- **Prometheus + Grafana** - Métricas e dashboards  
- **Python (scikit-learn)** - Serviço de detecção de anomalias  
- **Docker Compose** - Orquestração local dos serviços  
- **Webhooks** - Alertas automáticos no Grafana  

---

## 🚀 Como Executar

1. Certifique-se de que o Docker e Docker Compose estão instalados  
2. Navegue até o diretório raiz:

```bash
cd C:/code/fonte/microservices

Suba os serviços:
docker-compose up --build
Acesse os serviços:

Kibana: http://localhost:5601

Grafana: http://localhost:3000 (login padrão: admin/admin)

Prometheus: http://localhost:9090

Microserviços: http://localhost:8081, 8082, 8083

Serviço ML: http://localhost:5050

📊 Dashboards
Grafana
Latency Monitor

Erro por Serviço

Anomalias detectadas pelo ML

Kibana
Visualização dos logs estruturados (índice: ecs-microservices-logs)

Filtros por nível (INFO, ERROR), serviço, timestamp

🔬 Machine Learning
O serviço ml-analyzer utiliza Isolation Forest para identificar padrões de anomalias nos logs. Ele consome arquivos .csv gerados a partir dos logs e responde com a classificação de eventos suspeitos.

📦 Simulador
O serviço simulator envia logs sintéticos para o Logstash e para o serviço de ML, permitindo testes contínuos da arquitetura de observabilidade e inteligência.

🔔 Alertas
Os dashboards Grafana estão configurados com alertas visuais. Também foi incluído um Webhook para integração com endpoints externos.

👨‍💻 Autor
João Guedes de Brito
Desenvolvedor Full Stack | Especialista em Engenharia de Sistemas
G4F - Governo Federal
LinkedIn

📄 Licença
Este projeto é de uso demonstrativo e educacional para fins de seleção acadêmica e não deve ser utilizado em produção sem adaptações de segurança.


