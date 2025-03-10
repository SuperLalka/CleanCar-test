<!-- PROJECT LOGO -->
<div align="center">
  <h2>CleanCar-test</h2>

  <h3 align="center">README тестового задания</h3>

  <p align="center">
    Django-приложение с WebSocket-интеграцией к публичному API Binance.
  </p>
</div>

<a name="readme-top"></a>

<hr>

<!-- ABOUT THE PROJECT -->
## About The Project

Требования:

Требования к API:
1. Подключиться к WebSocket API Binance (Tickers Stream).
2. Получать обновления цен по выбранным криптовалютным парам (например, BTC/USDT, ETH/USDT).
3. Сохранять обновленные данные в PostgreSQL.
4. Предоставить REST API для просмотра истории изменений.
5. Реализовать WebSocket-сервер в Django (Django Channels), который рассылает обновления клиентам в реальном времени.
6. Unit-тесты.

Документация Binance WebSocket API Binance предоставляет WebSocket-соединение для стриминга цен криптовалют. URL:
wss://stream.binance.com:9443/ws/btcusdt@trade

Как это работает?
1. Django устанавливает WebSocket-соединение с Binance.
2. Получает обновления цен в реальном времени.
3. Сохраняет их в PostgreSQL (например, каждую минуту).
4. Django создает WebSocket-сервер (Django Channels).
5. Клиенты могут подключаться по WS и получать обновления в реальном времени.
6. Также можно запросить историю через REST API.

Требуемый стек технологий: Django + Django Channels – WebSockets.
PostgreSQL – хранение данных.
Redis – кеширование (если нужно).
pytest + Mock WebSocket – тестирование.

### Built With

* [![Django][Django-badge]][Django-url]
* [![Postgres][Postgres-badge]][Postgres-url]
* [![Celery][Celery-badge]][Celery-url]
* [![Redis][Redis-badge]][Redis-url]
* [![Docker][Docker-badge]][Docker-url]
* [![Bootstrap][Bootstrap-badge]][Bootstrap-url]
* [![JQuery][JQuery-badge]][JQuery-url]


<!-- GETTING STARTED -->
## Getting Started

### Prerequisites

Copy project to repository on local machine (HTTPS or SSH)
  ```sh
  git clone https://github.com/SuperLalka/CleanCar-test.git
  ```
  ```sh
  git clone git@github.com:SuperLalka/CleanCar-test.git
  ```

### Installation

To start the project, it is enough to build and run docker containers.
Database migration and fixture loading will be applied automatically.

```sh
docker-compose -f docker-compose.yml up -d --build
```


### Documentation

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[Django-badge]: https://img.shields.io/badge/django-%23092E20.svg?style=for-the-badge&logo=django&logoColor=white
[Django-url]: https://docs.djangoproject.com/
[Postgres-badge]: https://img.shields.io/badge/postgresql-%234169E1.svg?style=for-the-badge&logo=postgresql&logoColor=white
[Postgres-url]: https://www.postgresql.org/
[Celery-badge]: https://img.shields.io/badge/celery-%2337814A.svg?style=for-the-badge&logo=celery&logoColor=white
[Celery-url]: https://docs.celeryq.dev/
[Redis-badge]: https://img.shields.io/badge/redis-%23FF4438.svg?style=for-the-badge&logo=redis&logoColor=white
[Redis-url]: https://redis.io/
[Docker-badge]: https://img.shields.io/badge/docker-%230db7ed.svg?style=for-the-badge&logo=docker&logoColor=white
[Docker-url]: https://www.docker.com/
[Bootstrap-badge]: https://img.shields.io/badge/bootstrap-%237952B3.svg?style=for-the-badge&logo=bootstrap&logoColor=white
[Bootstrap-url]: https://getbootstrap.com/
[JQuery-badge]: https://img.shields.io/badge/jquery-%230769AD.svg?style=for-the-badge&logo=jquery&logoColor=white
[JQuery-url]: https://jquery.com/
