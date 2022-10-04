---
sidebar_position: 3
---

# Установка на Ubuntu

## Установка Python на Ubuntu {#installing-python-on-ubuntu}

### Установка Python из официального репозитория main {#installing-python-from-the-official-main-repository}

Если вы работаете в Ubuntu или Debian, пакет `python3` должен быть уже установлен в системе.

Проверить, установлен ли пакет `python3`, можно командой `apt list --installed | grep python3`.

Если пакет не установлен, открываем эмулятор терминала, вводим команду `sudo apt install python3`, нажимаем <kbd>Enter</kbd>, вводим пароль и ждём окончания установки.

Команда `whereis python3` показывает, где в системе находятся файлы пакета.

Также для работы нужно установить пакетный менеджер `pip3`.

Если пакет не установлен, открываем эмулятор терминала, вводим команду `sudo apt install python3-pip`, нажимаем <kbd>Enter</kbd>, вводим пароль и ждём окончания установки.

Команда `whereis pip3` показывает, где в системе находятся файлы пакета.

Если в системе не установлен пакет `python3-doc`, его тоже нужно установить командой `sudo apt install python3-doc`.

Чтобы запустить интерпретатор Python 3 в интерактивном режиме, в эмуляторе терминала вводим команду `python3`. Открывается приглашение для ввода команд.

Чтобы посмотреть версию Python 3, вводим в эмуляторе терминала `python3 --version`.

Чтобы интерпретатор `python3` вызывался командой `python` (как в Windows), начиная с версии Ubuntu 20.04 можно установить дополнительный пакет `python-is-python3` командой `sudo apt install python-is-python3`. Этот пакет устанавливает символическую ссылку на текущий интерпретатор `python3` по адресу `/usr/bin/python`. Этот пакет может потребоваться для работы некоторых программ, ранее работавших на Python 2, после избавления от Python 2 в системе.

### Установка свежих версий Python из PPA deadsnakes {#installing-fresh-versions-of-python-from-the-deadsnakes-ppa}

Поскольку цикл разработки Python не совпадает с циклом разработки Ubuntu, официальный репозиторий **main** может содержать не самую свежую версию Python. Особенно это касается релизов Ubuntu с длительным сроком поддержки, которые выпускаются раз в два года — в них, скорее всего, будет устаревшая версия Python.

Если вы хотите установить в Ubuntu самую свежую версию Python, можно воспользоваться персональным репозиторием команды [deadsnakes team](https://launchpad.net/~deadsnakes). Для этого нужно подключить нужный репозиторий, обновить список пакетов и установить пакеты. После установки в системе появится ещё одна или несколько версий Python.

:::info внимание

Сборки Python от команды deadsnakes предназначены для выпусков Ubuntu с [длительным сроком поддержки](https://ru.wikipedia.org/wiki/Долгосрочная_поддержка_программного_обеспечения). Репозитории deadsnakes могут быть использованы совместно с обычными выпусками Ubuntu, а также с Debian, но работоспособность сборок Python на них не тестируется и не гарантируется командой deadsnakes.

:::

У команды deadsnakes есть два репозитория:

- [New Python Versions](https://launchpad.net/~deadsnakes/+archive/ubuntu/ppa) — свежие версии стабильных выпусков Python, а также версии Release candidate.
- [nightly python builds ](https://launchpad.net/~deadsnakes/+archive/ubuntu/nightly) — ночные сборки версий Python, находящихся в разработке.

Например, чтобы установить Python 3.10 из репозитория [New Python Versions](https://launchpad.net/~deadsnakes/+archive/ubuntu/ppa):

- подключаем репозиторий командой `sudo add-apt-repository ppa:deadsnakes/ppa`;
- обновляем список пакетов командой `sudo apt update`;
- устанавливаем Python 3.10 командой `sudo apt install python3.10-full`.

:::info внимание

При использовании Python из репозитория команды deadsnakes нужно создавать виртуальное окружение Python, если планируется устанавливать сторонние библиотеки.

:::

## Установка GNU Midnight Commander на Ubuntu {#installing-gnu-mc-on-ubuntu}

Для удобства работы в командной строке нам понадобится консольный файловый менеджер GNU Midnight Commander. Он находится в пакете `mc`.

Открываем эмулятор терминала, вводим команду `sudo apt install mc`, нажимаем <kbd>Enter</kbd>, вводим пароль и ждём окончания установки.

Запускаем GNU Midnight Commander в эмуляторе терминала командой `mc`.

## Установка PyCharm CE на Ubuntu {#installing-pycharm-ce-on-ubuntu}

На Ubuntu PyCharm Community Edition можно установить двумя разными способами:

1. из snap-пакета,
2. вручную, скачав с сайта компании JetBrains архив tar.gz.

### Первый способ (рекомендуемый) {#first-way-recommended}

Открываем  эмулятор терминала и вводим команду `sudo snap install pycharm-community --classic`, нажимаем <kbd>Enter</kbd>, вводим пароль и ждём окончания установки.

После установки в меню в разделе **Разработка** появится иконка **Pycharm Community Edition**.

### Второй способ (подходит также для Debian и Linux Mint) {#second-way}

Заходим на сайт JetBrains и скачиваем [PyCharm Community Edition](https://www.jetbrains.com/pycharm/) для Linux в домашний каталог (или в любой каталог, на запись в которую у нас есть права).

![Скачивание дистрибутива PyCharm Community Edition](/images/python-language/installing-and-configuring/installing-on-ubuntu/pycharm-ce-download.png "Скачивание дистрибутива PyCharm Community Edition")

Затем переходим в этот каталог и распаковываем сохранённый архив командой `tar -xzf pycharm-community-2020.1.tar.gz`, где `pycharm-community-2020.1.tar.gz` — название архива.

Исполняемый файл вызывается командой `pycharm-community-2020.1/bin/pycharm.sh`, где `pycharm-community-2020.1` — каталог, в котором находится распакованный дистрибутив.

Затем нужно отредактировать меню запуска приложений и добавить туда команду для запуска исполняемого файла PyCharm Community Edition (примерно такую: `"/home/<имя пользователя>/pycharm-community-2020.1/bin/pycharm.sh" %f`, где `/home/<имя пользователя>` — домашний каталог пользователя или другой каталог, где находится распакованный дистрибутив PyCharm Community Edition) и иконку для запуска IDE.

Ниже приведён пример добавления PyCharm Community Edition в меню приложений KDE.

![Пример добавления PyCharm Community Edition в меню приложений KDE](/images/python-language/installing-and-configuring/installing-on-ubuntu/pycharm-ce-kde-menu-editor.png "Пример добавления PyCharm Community Edition в меню приложений KDE")

## Дополнительные ссылки {#additional-links}

- [Интерфейс командной строки](https://ru.wikipedia.org/wiki/Интерфейс_командной_строки)
- [Эмулятор терминала](https://ru.wikipedia.org/wiki/Эмулятор_терминала)
- [Репозиторий](https://ru.wikipedia.org/wiki/Репозиторий)
- [Система управления пакетами](https://ru.wikipedia.org/wiki/Система_управления_пакетами)
- [dpkg](https://ru.wikipedia.org/wiki/Dpkg)
- [Advanced Packaging Tool](https://ru.wikipedia.org/wiki/Advanced_Packaging_Tool)
- [Инструменты APT](https://www.debian.org/doc/manuals/debian-handbook/apt.ru.html)
- [Персональные архивы пакетов (PPA)](https://help.ubuntu.ru/wiki/ppa)
- [Snappy](https://ru.wikipedia.org/wiki/Snappy_(система_управления_пакетами))
- [Snapcraft](https://snapcraft.io/)
- [Стадии разработки программного обеспечения](https://ru.wikipedia.org/wiki/Стадии_разработки_программного_обеспечения)
- [Долгосрочная поддержка программного обеспечения](https://ru.wikipedia.org/wiki/Долгосрочная_поддержка_программного_обеспечения)
