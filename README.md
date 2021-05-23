# ChatApp
Datenbanken-Projekt DHBW Stuttgart | Entwicklung einer Chat-App mit Python und Redis

## Installation
Die Applikation ist unter Ubuntu 18.04 entstanden und konnte auch nur hier getestet werden. Python sollte als virtual environment (venv) ausgeführt werden, wobei der Interpreter der Python Version 3.6 entsprechen sollte.

Die benötigten Python Bibliotheken finden Sie in der Datei "requirements.txt". Falls Sie nicht wissen, wie man eine requirements-Datei automatisiert einliest, können Sie hier weitere Informationen erhalten: https://stackoverflow.com/questions/7225900/how-can-i-install-packages-using-pip-according-to-the-requirements-txt-file-from.

Hinweis: Als Entwicklungsumgebung verwendete ich Pycharm. Pycharm bietet neben einfachen Möglichkeiten zur Erstellung eines virtual environments auch Funktionen mit welchen sich dei Requirements automatisch installieren lassen.

## Automatisierte Test
Als Test-Framework wählte ich Pytest aus. Pycharm bietet die Möglichkeit das Framework manuell auszuwählen. Gehen Sie hierzu auf "File > Settings > Tools > Python Intergrated Tools > Testing" und wählen Sie im Drop-Down Menü "pytest" aus.
Klicken Sie anschließend die Datei "test_pytest.py" mit der rechten Maustaste an und wählen Sie "run pytest in test_py...", um das automatisierte Testen zu starten. Sie können den Test auch über das Terminal starten.

Bei den automatisierten Tests habe ich misch ausschließlich auf das Backend konzentriert und das Frontend außer Acht gelassen, wie es in der Themenbesprechung abgesprochen wurde.

## Ausführen
Führen Sie die Datei "main.py" aus.

## Weitere Anmerkungen
Die geplante Funktion Bilddateien zu versenden, konnte nicht implementiert werden. Dies ist auf Schwierigkeiten bei der Frontend-Entwicklung zurückzuführen.
Im Backend war es geplant der Klasse "Message" noch ein Attribut "type" hinzuzufügen, welches Auskunft darüber gibt, ob es sich um eine Textnachricht oder ein Bild handelt. Anschließend wäre die Biolddatei in einen String umgewandel und ganz normal als Message versendet worden.

## Fragen & Probleme
Bei weiteren Fragen oder Problemen können Sie mich jederzeit per e-Mail kontaktieren.
