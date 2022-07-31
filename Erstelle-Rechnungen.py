import pandas as pd
import numpy as np
import locale
import re
import glob
import datetime
import os
import subprocess

locale.setlocale(locale.LC_ALL, 'de_DE.UTF-8')  # Voraussetzung für Komma bei Zahlen

# DataFrame ist ein Array aus Sheet, Column, Row. Leere Zellen, auch Text, werden zu float NaN
df_sheets = pd.read_excel('Praxis1.xlsx', sheet_name=None)
Anzahl_pdf_nicht_überschrieben = 0


def format_datetime(datum_oder_text):
    if type(datum_oder_text) == type(None): return ''
    elif type(datum_oder_text) == type(str()): return datum_oder_text
    elif type(datum_oder_text) == type(pd.Timestamp.now()): return datum_oder_text.strftime('%d.%m.%Y')
    elif type(datum_oder_text) == type(datetime.datetime.now()): return datum_oder_text.strftime('%d.%m.%Y')
    else: return str(datum_oder_text)


def format_text(text_oder_float_nan):
    # pandas gibt flot nan als Leere Zelle zurück
    if type(text_oder_float_nan) == type(None): return ''
    elif type(text_oder_float_nan) == type(str()): return text_oder_float_nan.rstrip()
    elif type(text_oder_float_nan) == type(1.0):
        if np.isnan(text_oder_float_nan):
            return ''
        else:
            return str(text_oder_float_nan)
    else: return str(text_oder_float_nan)


def write_error(txt):
    print(txt)
    #quit()

def lösche_datei(datei):
    if os.path.exists(datei):
        os.remove(datei)


try:
    Rechnungsnummern = sorted(df_sheets["Behandlungen"].Rechnung.unique())
    if len(Rechnungsnummern) == 0:
        write_error('Keine Rechnungsnummern')

    for rechnr in Rechnungsnummern:
        if not re.match('^20\d\d-\d\d\d$', rechnr):
            write_error(f'{rechnr} auf dem Blatt Behandlugnen hat nicht das Format 20##-###')
except KeyError as exc:
    write_error(f'In Excel fehlt das Blatt oder die Spalte {exc}')


def Diese_Rechnung(Rechnungsnummer):
    global Anzahl_pdf_nicht_überschrieben
    pdfglob  = f'Praxis1-Rechnung-{Rechnungsnummer}-*.pdf'
    if len(glob.glob(pdfglob)) > 0:
        #print(f"{pdfglob} nicht überschrieben")
        Anzahl_pdf_nicht_überschrieben += 1
        return

    #print(f'...{Rechnungsnummer}...', end='')
    Datum_Rechnung        = "fehlt"
    Anrede                = "fehlt"
    Vorname               = "fehlt"
    Nachname              = "fehlt"
    Straße                = "fehlt"
    Stadt                 = "fehlt"
    Arzt                  = None
    Datum_Verordnung      = None
    Diagnose              = None
    BEHANDLUNGEN          = ''
    RECHNUNGSBETRAG_zahl  = 0

    try:
        # Sammele Rechnungsdaten
        rechnung_df = df_sheets["Rechnungen"][(df_sheets["Rechnungen"]['Rechnung'] == Rechnungsnummer)]
        if rechnung_df['Rechnung'].size != 1:
            write_error(f'{Rechnungsnummer} steht im Blatt Rechnungen {rechnung_df.size}-fach')
            return
        Vorname          = format_text(rechnung_df['Vorname'].item())    # LEARN DataFrame Daten sind items
        Nachname         = format_text(rechnung_df['Nachname'].item())
        Straße           = format_text(rechnung_df['Straße'].item())
        Stadt            = format_text(rechnung_df['Stadt'].item())
        HerrFrau         = format_text(rechnung_df['Anrede'].item())
        Diagnose         = format_text(rechnung_df['Diagnose'].item())
        Arzt             = format_text(rechnung_df['Arzt'].item())
        Datum_Rechnung   = format_datetime(rechnung_df['Datum Rechnung'].item())
        Datum_Verordnung = format_datetime(rechnung_df['Datum Verordnung'].item())
        if 'Herr' in HerrFrau:
            Anrede = f'Sehr geehrter {HerrFrau}'
            PATIENT = 'Patient'
        else:
            Anrede = f'Sehr geehrte {HerrFrau}'
            PATIENT = 'Patientin'

        if len(Diagnose) > 3:
            DiagnoseEinschub = f" mit Diagnose: & {Diagnose} "
        else:
            DiagnoseEinschub = ""

        if len(Arzt) > 3 and len(Datum_Verordnung) > 3:
            Einleitung = fr"""aufgrund der Verordnung von {Arzt} \medskip \\
\begin{{tabularx}}{{\textwidth}}{{lX}}
%\begin{{tabular}}{{ll}}
vom: & {Datum_Verordnung} \\
{DiagnoseEinschub}
%\end{{tabular}}
\end{{tabularx}}  \medskip  \\
erlaube ich mir folgende Leistungen in Rechnung zu stellen:"""
        else:
            Einleitung = """ich erlaube mir folgende Leistungen in Rechnung zu stellen:"""

        # Suche Behandlungsarten
        Behandlungsarten = []
        headersAb2 = df_sheets["Behandlungen"].columns[2:]
        # Beginne hinter Rechnung oder Rechnung.1 (Name der Spalte mehrfach)
        # Starte ab der 2. Spalte
        # Header vor Rechnung und ab Ausgaben aulassen
        header_auslassen = True
        for header in headersAb2:
            if header.startswith('Ausgaben'): header_auslassen = True
            if not header_auslassen: Behandlungsarten.append(header)
            if header.startswith('Rechnung'): header_auslassen = False
        #print(f'{Behandlungsarten=}')

        # Dataframe dieser Rechnungsnummer, mit allen Behandlungsarten
        behandlungen_df = df_sheets["Behandlungen"][(df_sheets["Behandlungen"]['Rechnung'] == Rechnungsnummer)]

        BEHANDLUNGSTERMINE_list_of_string = []
        for datum_oder_text in behandlungen_df['Behandlung']:
            BEHANDLUNGSTERMINE_list_of_string.append(format_datetime(datum_oder_text))
        BEHANDLUNGSTERMINE = ', '.join(BEHANDLUNGSTERMINE_list_of_string)

        # Pro Behandlungsart
        # ANZAHL & BEHANLDUNG &  EINZELPREIS\,€ &  GESAMTPREIS\,€ \\
        for Behandlungsart in Behandlungsarten:
            df_behandlung = behandlungen_df[Behandlungsart]
            if df_behandlung.count() > 0:
                Anzahl      = df_behandlung.count()
                Einzelpreis = locale.format_string('%.2f', df_behandlung.mean())
                Gesamtpreis = locale.format_string('%.2f', df_behandlung.sum())
                # Das geht durch ein replace,  dafür muß ich \ escapen
                BEHANDLUNGEN += fr'  {Anzahl} & {Behandlungsart} & {Einzelpreis}\\,€ & {Gesamtpreis}\\,€ \\\\' + '\n'
                RECHNUNGSBETRAG_zahl += df_behandlung.sum()
        RECHNUNGSBETRAG = locale.format_string('%.2f', RECHNUNGSBETRAG_zahl)
        # Debug
        #print(f'{BEHANDLUNGEN=}')
        #print(f'{RECHNUNGSBETRAG=}')
    except KeyError as exc:
        write_error(f'In Excel fehlt das Blatt oder die Spalte {exc}')
        return


    # Benutze Vorlage und ersetze Werte
    output = ''
    inside_document = False
    kopie = ''
    with open('Praxis1-Vorlage.tex', encoding='utf8') as file:
        for line in file:
            # Füge (Kopie) in der Kopie hinzu
            if r'\textbf{RECHNUNG}' in line:
                für_ORIG  = re.sub(r'\\textbf{RECHNUNG}', r'\\textbf{Rechnung}', line)
                für_KOPIE = re.sub(r'\\textbf{RECHNUNG}', r'\\textbf{Rechnung} (Kopie)', line)
                output += für_ORIG
                kopie += für_KOPIE
                continue

            # Ersetze die Platzhalter
            #         ANZAHL & BEHANDLUNG & EINZELPREIS\,€ & GESAMTPREIS\,€ \\
            line = re.sub(r'\bRECHNUNGSNUMMER\b', Rechnungsnummer, line)
            line = re.sub(r'\bRECHNUNGSDATUM\b', Datum_Rechnung, line)
            line = re.sub(r'\bANREDE\b', Anrede, line)
            line = re.sub(r'\bPATIENT\b', PATIENT, line)
            line = re.sub(r'\bVORNAME\b', Vorname, line)
            line = re.sub(r'\bNACHNAME\b', Nachname, line)
            line = re.sub(r'\bSTRAßE\b', Straße, line)
            line = re.sub(r'\bSTADT\b', Stadt, line)
            line = line.replace("EINLEITUNG", Einleitung)
            line = re.sub(r'\bRECHNUNGSBETRAG\b', RECHNUNGSBETRAG, line)
            line = re.sub(r'ANZAHL & BEHANDLUNG & EINZELPREIS\\,€ & GESAMTPREIS\\,€ \\\\', BEHANDLUNGEN, line)
            line = re.sub(r'\bBEHANDLUNGSTERMINE\b', BEHANDLUNGSTERMINE, line)

            # Erstelle Kopie
            if r'\end{document}' in line:
                output += r'\newpage'
                output += r'\addtolength{\headsep}{-9mm}'      # HACK
                output += kopie
            output += line
            if inside_document:
                kopie += line
            if r'\begin{document}' in line:
                inside_document = True


    import platform
    tmpdir = '/tmp/'
    if platform.system() == 'Windows':
        tmpdir = 'C:\\tmp\\'

    Basisname_der_Datei = f'Praxis1-Rechnung-{Rechnungsnummer}-{Nachname}'
    pdfdatei =          Basisname_der_Datei + '.pdf'
    texdatei = tmpdir + Basisname_der_Datei + '.tex'
    dvidatei = tmpdir + Basisname_der_Datei + '.dvi'
    auxdatei = tmpdir + Basisname_der_Datei + '.aux'
    logdatei = tmpdir + Basisname_der_Datei + '.log'

    with open(texdatei, 'w', encoding='utf8') as fout:
        fout.write(output)

    import platform
    if platform.system() == 'Darwin':
        pdfbinary = '/Library/TeX/texbin/lualatex'   # TODO GIBT ES DAS???????
    else:
        pdfbinary = 'latex'
        pdfbinary = 'lualatex'
    #print(f'{pdfbinary} --interaction=nonstopmode -output-directory={tmpdir} -output-format=dvi {texdatei}')
    #print(f'{pdfbinary} --interaction=nonstopmode -output-directory={tmpdir} {texdatei}')
    
    p = subprocess.run([ pdfbinary, '--interaction=nonstopmode', '-output-directory='+tmpdir, '-output-format=dvi', texdatei ], capture_output=True)
    #p = subprocess.run([ pdfbinary, '--interaction=nonstopmode', '-output-directory='+tmpdir, texdatei ], capture_output=True)
    print( f'{Basisname_der_Datei}  latex {p.returncode}', end='')
    if p.returncode == 0:
        if platform.system() == 'Darwin':
            pdfbinary2 = '/Library/TeX/texbin/dvipdfmx'
        else:
            pdfbinary2 = 'dvipdfmx'
        pdf_process = subprocess.run([ pdfbinary2, '-o', pdfdatei, dvidatei ], capture_output=True)
        print( f'  pdf {pdf_process.returncode}')
        lösche_datei(dvidatei)
        lösche_datei(auxdatei)
        lösche_datei(logdatei)
        lösche_datei(texdatei)
    else:
        print('')



########################################################
# Main
########################################################
#Diese_Rechnung('2022-007')

for rng in Rechnungsnummern:
    Diese_Rechnung(rng)

print(f'{Anzahl_pdf_nicht_überschrieben} pdf Rechungen gefunden')
