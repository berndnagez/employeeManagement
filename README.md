# employeeManagement

Eine Website zur Verwaltung von Angestellten.

FH-Lübeck, Sommersemester 2018

## Autor

<a href="mailto:bjoern.nagel@stud.fh-luebeck.de">Björn Nagel</a>

### Beschreibung

Die Website wurde mit Django 2.0.6 erstellt. Für die Templates kommt bootstrap zur Anwendung.

Am Backend können Angestellte angelegt und verwaltet werden.

Dafür muss nächst ein Superuser erstellt werden:

```
$ python manage.py createsuperuser
```

Der Superuser kann sich am backend anmelden:

```
http://localhost:8000/admin
```

#### Das Backend

Im Backend können mit dem Modul MANAGEMENT neue Angestellte angelegt, bearbeitet und gelöscht werden.

Zu jedem Angestellten / jeder Angestellten werden

der Vorname,

der Nachname,

die E-Mail,

der Geburtstag,

die Straße,

die Postleitzahl,

die geleisteten Überstunden sowie

der Urlaubsanspruch gespeichert.


#### Das Frontend

Angestellte, die im Backend angelegt wurden, können sich am Frontend anmelden:

```
http://localhost:8000/
```

Wenn sie angemeldet sind, können sie alle Daten einsehen, die zu ihrer Person gespeichert sind.

## Besonderheiten

Ein Schwerpunkt wurde auf ein ausgeklügeltes User-Managment gelegt. Das System sieht eine Anmeldung der User ausschließlich durch den Admin am Backend vor.

Wenn ein neuer Employee angelegt wurde, wird nicht nur automatisch ein User angelegt, sondern auch automatisch eine E-Mail vom System an die E-Mailadresse des neuen Employee geschickt.
 
Diese E-Mail enthält einen Link, mit dem man sich einmal anmelden kann, um sein Passwort zu ändern.

Zu Testzwecken findet sich in den letzten beiden Zeilen der <a href="https://github.com/berndnagez/employeeManagement/blob/master/employeeManagement/settings.py">settings.py</a> eine Konfiguration, die dafür sort, dass gesenden Mails im Ornder

```
/sent_mails
```

landen. Diese Test-Mails mit ihren Links können auch verwendet werden, um die Change-Password-View zu testen.

Für den Produktivbetrieb müsste ein SMTP Email Service konfiguriert werden.

# Viel Spaß. 