---
sidebar_position: 2
---

# Установка на Windows

## Определение архитектуры Windows {#defining-windows-architecture}

Сначала смотрим, какая архитектура у нашей операционной системы.

Нажимаем правой кнопкой мыши на кнопку **Пуск**, в появившемся диалоговом окне выбираем пункт **Система**, и в разделе **О системе** смотрим пункт **Тип системы**.

![О системе](/images/python-language/installing-and-configuring/installing-on-windows/windows-architecture.png "О системе")

## Установка Python на Windows {#installing-python-on-windows}

Если в пункте **Тип системы** написано **64-разрядная операционная система, процессор x64**, заходим на официальный сайт Python в раздел [Downloads](https://www.python.org/downloads/), выбираем последний релиз (на данный момент — Python 3.8.2), переходим в раздел **Files** и скачиваем **Windows x86-64 executable installer** .

Если в пункте **Тип системы** написано **32-разрядная операционная система**, скачиваем **Windows x86 executable installer**.

![Скачивание дистрибутива Python 3](/images/python-language/installing-and-configuring/installing-on-windows/python-download.png "Скачивание дистрибутива Python 3")

Скачав нужную версию дистрибутива, запускаем установку. Отмечаем флажок **Add Python 3.8 to PATH**. Это позволит вызывать интерпретатор `python` и пакетный менеджер `pip` в командной строке, не вводя полный путь к исполняемым файлам.

Выбираем пункт **Customize installation**.

![Установка Python 3, шаг 1](/images/python-language/installing-and-configuring/installing-on-windows/python-install-step-1.png "Установка Python 3, шаг 1")

Нажимаем **Next**.

![Установка Python 3, шаг 2](/images/python-language/installing-and-configuring/installing-on-windows/python-install-step-2.png "Установка Python 3, шаг 2")

Выставляем флажок **Install for all users**.

Место установки Python при этом должно автоматически поменяться на `C:\Program Files\Python38`.

Нажимаем **Install**.

![Установка Python 3, шаг 3](/images/python-language/installing-and-configuring/installing-on-windows/python-install-step-3.png "Установка Python 3, шаг 3")

Следим за процессом установки.

![Установка Python 3, шаг 4](/images/python-language/installing-and-configuring/installing-on-windows/python-install-step-4.png "Установка Python 3, шаг 4")

Закрываем окно установщика.

![Установка Python 3, шаг 5](/images/python-language/installing-and-configuring/installing-on-windows/python-install-step-5.png "Установка Python 3, шаг 5")

Теперь мы должны убедиться, что установка прошла успешно.

Нажимаем **Пуск**, находим пункт **Служебные** и запускаем **командную строку**. Или вводим команду `cmd` в поле **Введите здесь текст для поиска** и нажимаем <kbd>Enter</kbd>.

![Запуск командной строки Windows](/images/python-language/installing-and-configuring/installing-on-windows/cmd.png "Запуск командной строки Windows")

В командной строке вводим `python --version` и нажимаем <kbd>Enter</kbd>. В окне командной строки должна появиться информация об установленной версии интерпретатора Python 3.

![Вывод информации о версии Python 3 в командной строке](/images/python-language/installing-and-configuring/installing-on-windows/python-version.png "Вывод информации о версии Python 3 в командной строке")

Установка успешно завершена.

## Установка PyCharm CE на Windows {#installing-pycharm-ce-on-windows}

Заходим на сайт JetBrains и скачиваем [PyCharm Community Edition](https://www.jetbrains.com/pycharm/) для Windows.

![Скачивание дистрибутива PyCharm Community Edition](/images/python-language/installing-and-configuring/installing-on-windows/pycharm-ce-download.png "Скачивание дистрибутива PyCharm Community Edition")

Запускаем установку. Нажимаем **Next**.

![Установка PyCharm Community Edition, шаг 1](/images/python-language/installing-and-configuring/installing-on-windows/pycharm-ce-install-step-1.png "Установка PyCharm Community Edition, шаг 1")

Ещё раз нажимаем **Next**.

![Установка PyCharm Community Edition, шаг 2](/images/python-language/installing-and-configuring/installing-on-windows/pycharm-ce-install-step-2.png "Установка PyCharm Community Edition, шаг 2")

Добавляем исполняемый файл PyCharm Community Edition в переменную `PATH` и ассоциируем файлы с исходным кодом Python с PyCharm Community Edition. Нажимаем **Next**.

![Установка PyCharm Community Edition, шаг 3](/images/python-language/installing-and-configuring/installing-on-windows/pycharm-ce-install-step-3.png "Установка PyCharm Community Edition, шаг 3")

Нажимаем **Install**.

![Установка PyCharm Community Edition, шаг 4](/images/python-language/installing-and-configuring/installing-on-windows/pycharm-ce-install-step-4.png "Установка PyCharm Community Edition, шаг 4")

Следим за процессом установки.

![Установка PyCharm Community Edition, шаг 5](/images/python-language/installing-and-configuring/installing-on-windows/pycharm-ce-install-step-5.png "Установка PyCharm Community Edition, шаг 5")

Выбираем **Reboot now** для немедленной перезагрузки компьютера или выбираем **I want to reboot later**, чтобы перезагрузить компьютер позже. Помним, что перед первым запуском PyCharm Community Edition мы должны перезагрузить компьютер.

![Установка PyCharm Community Edition, шаг 6](/images/python-language/installing-and-configuring/installing-on-windows/pycharm-ce-install-step-6.png "Установка PyCharm Community Edition, шаг 6")

Установка успешно завершена.

## Установка Far Manager на Windows {#installing-far-manager-on-windows}

Для комфортной работы в Windows нам может понадобиться консольный двухпанельный файловый менеджер — **Far Manager**.

Заходим на сайт [Far Manager](https://www.farmanager.com/) и скачиваем установщик **msi**, соответствующий архитектуре Windows.

![Скачивание дистрибутива Far Manager](/images/python-language/installing-and-configuring/installing-on-windows/far-manager-download.png "Скачивание дистрибутива Far Manager")

Запускаем установщик и нажимаем **Next**.

![Установка Far Manager, шаг 1](/images/python-language/installing-and-configuring/installing-on-windows/far-manager-install-step-1.png "Установка Far Manager, шаг 1")

Нажимаем **Next**.

![Установка Far Manager, шаг 2](/images/python-language/installing-and-configuring/installing-on-windows/far-manager-install-step-2.png "Установка Far Manager, шаг 2")

Оставляем всё как есть и нажимаем **Next**.

![Установка Far Manager, шаг 3](/images/python-language/installing-and-configuring/installing-on-windows/far-manager-install-step-3.png "Установка Far Manager, шаг 3")

Нажимаем **Install**.

![Установка Far Manager, шаг 4](/images/python-language/installing-and-configuring/installing-on-windows/far-manager-install-step-4.png "Установка Far Manager, шаг 4")

Нажимаем **Finish**.

![Установка Far Manager, шаг 5](/images/python-language/installing-and-configuring/installing-on-windows/far-manager-install-step-5.png "Установка Far Manager, шаг 5")

Установка успешно завершена.

## Дополнительные ссылки {#additional-links}

- [Интегрированная среда разработки](https://ru.wikipedia.org/wiki/Интегрированная_среда_разработки)
- [PyCharm](https://ru.wikipedia.org/wiki/PyCharm)
- [FAR Manager](https://ru.wikipedia.org/wiki/FAR_Manager)
- [Переменная PATH](https://ru.wikipedia.org/wiki/PATH_(переменная))
- [Интерфейс командной строки](https://ru.wikipedia.org/wiki/Интерфейс_командной_строки)
- [Cmd.exe](https://ru.wikipedia.org/wiki/Cmd.exe)
