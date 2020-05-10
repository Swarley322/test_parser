# Web приложение для путешествий парами (poor-trip)
Целью проекта является создание сервиса, предоставляющий пользователю, который, знает даты, в рамках которых он хотел бы совершить путешествие в другой город, знает свой бюджет, который он готов выделить для путешествия, но не знает куда отправиться. Сервис автоматический подбирает направление, которое не превысит выделенный бюджет.

## Источники данных
Авиабилеты - [Яндекс Авиабилеты](https://avia.yandex.ru/)  
Отели - [Booking](https://www.booking.com/)  
Достопримечательности - [Тонкости Туризма](https://tonkosti.ru/)  
Стоимость продуктов и услуг - [Numbeo](https://www.numbeo.com/cost-of-living/)  

## Используемые технологии
`python3`, `flask`, `celery`, `redis`, `selenium`, `docker`, `postresql`, `nginx`, `docker-compose`, `html`, `css`

## Docker контейнеры
```
+-------------+       +------------+         +--------------+
|             |       |            |         |              |
|    redis    |       | flask app  +---------+   selenium   |
|             |       |            |         |              |
+------+------+       +------+-----+         +--------------+
       |                     |
+------+------+       +------+-----+         +--------------+
|             |       |            |         |              |
|    celery   +-------+ postgresql |         |     nginx    |
|             |       |            |         |              |
+-------------+       +------------+         +--------------+
```

# Установка
Необходимо установить `git`, `docker` и `docker-compose`
### Запуск
```sh
$ git clone https://github.com/Swarley322/poor_trip.git
$ cd poor-trip
$ docker-compose up
```