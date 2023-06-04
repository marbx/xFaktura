[Zur Webseite](https://marbx.github.io/xFaktura)

## MacTex installieren
MacTex erzeugt das pdf aus der Vorlage.
Der einfachste Weg es zu installieren ist [dieser](https://tug.org/mactex/mactex-download.html).



## Erste Installation von xFaktura oder neue Version installieren
Beachte:
- Der Download der zip-Datei führt über eine rote Warnseite von Google, weil es das Programm nicht kennt.
- Safari warnt ebenfalls, aus dem gleichen Grund.
- Die Lösung ist ein Zertifikat von Apple, das 100$ im Jahr kostet.


In dieser Reihenfolge:
- Speichere die zip-Datei [xFaktura-Upgrade.tbz.zip](https://downgit.github.io/#/home?url=https://github.com/marbx/xFaktura/blob/master/solution/xFaktura-Upgrade.tbz).
- Verschiebe die Zip Datei aus dem Download Ordner.
- Doppelklick erzeugt das Verzeichnis xFaktura-Upgrade:
  - Dort den Befehl `install_pip_SIMPLE.command` ausführen (Siehe unten wie) um Programm-Bibliotheken zu installieren
  - Dazu das Passwort für Installation eingeben.
- Verschiebe  alle nötigen Dateien in das Arbeitsverzeichnis:
  - das Script `xFaktura.py`
  - den Befehl `xFaktura.command`
    - Nur beim ersten Mal die Excel Datei .xlsx und die Rechnungsvorlage .tex, die umgenannt werden können.
- Zum Schluss `xFaktura-Upgrade` zip-Datei und Ordner löschen.

Screenshot![image](https://user-images.githubusercontent.com/8489107/218341316-296eec24-636f-4c45-92a1-6e6209644678.png)



## Rechnungen erzeugen
- Alle pdf Rechnungen in ein Verzeichnis `Pdf` verschieben.
- Doppelklick auf den Befehl `xFaktura.command`



## Kommandos .command zum ersten Mal ausführen
- Zur Sichherheit müssen Kommnandos das erste Mal freigeschaltet werden:
- Control-Klick (oder rechte-Maustaste Klick) auf den Befehl.
- Aus dem Kontextmenü Öffnen wählen
- In dem Fenster Öffnen wählen

