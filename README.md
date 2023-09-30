# d5

1. В классе-представлении редактирования новости добавлена проверка аутентификации.
2. Выполнены необходимые настройки пакета allauth в файле конфигурации.
3. В файле конфигурации определен адрес для перенаправления на страницу входа в систему и адрес перенаправления после успешного входа.
4. Реализован шаблон с формой входа в систему и выполнена настройку конфигурации URL.
5. Реализован шаблон страницы регистрации пользователей.
6. Реализована возможность регистрации через Google-аккаунт.
7. Созданы группы common и authors.
8. Реализовано автоматическое добавление новых пользователей в группу common.
9. Создана возможность стать автором (быть добавленным в группу authors).
10. Для группы authors предоставлены права создания, редактирования, удаления (чтобы удалять контент могли только пользователи из группы "authors") объектов модели Post (новостей и статей).
11. В классах-представлениях добавления, редактирования, удаления (чтобы удалять контент могли только пользователи из группы "authors") новостей и статей добавлена проверка прав доступа.
