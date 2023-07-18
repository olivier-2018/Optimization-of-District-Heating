The CSV files contain data for the years 2018 and 2019. Note that there may be gaps (e.g., because certain consumers have been attached only later, etc.) in the data: use the timestamps!

Historical weather data has been obtained from two publicly available sources. Thus, the locations of the weather stations are in the same greater region as the district heating network, yet not necessarily nearby.
	 
![Netzplan](https://github.com/district-heating-2020/data_analysis/raw/master/doc/pictures/W%C3%A4rmeverbund-Netzplan.png?raw=true)

## Daten Wärmezentrale

**1901_protWZ.csv = Wärmezentrale**: Messdaten beim Ausgang/Eingang der Wärmezentrale zum Netz (gelb markiert)

**1006_protWZ.csv = Main Feeder**: Verteiler bei Ausgang Wärmezentrale?

**2901_protWZ.csv = Holzkessel**: Messdaten beim Ausgang/Eingang des Holzkessels (gelb markiert)

**3901_protWZ.csv = Gaskessel 1**: Messdaten beim Ausgang/Eingang des ersten Gaskessels (gelb markiert)

**4901_protWZ.csv = Gaskessel 2**: Messdaten beim Ausgang/Eingang des zweiten Gaskessels (gelb markiert)

Variablen: 

- Timestamp: alle 5min, vom 1. Jan 2018 bis 1. Jan 2020
- WZ Wärmemenge(kWh)
- WZ Leistung(kW)
- WZ Durchfluss(l/h)
- WZ Rücklauftemp.(°C)
- WZ Vorlauftemp.(°C)
- WZ Spreizung(°C): Temperaturunterschied zwischen den Fluss beim Eingang bzw. Ausgang. Diesen Wert probiert man möglichst gross zu halten.

![Heizzentrale](https://github.com/district-heating-2020/data_analysis/blob/master/doc/pictures/Heat-station.png?raw=true)


## Reguläre Kundenschnittstellen (Kunden 1-5 und 7-8)

Für Schemas der einzelnen Kundeninstallationen, siehe die [PPTX Präsentation](https://github.com/district-heating-2020/data_analysis/blob/master/doc/district_heating_challenge_background_information.pptx)

Auf den Schemas sieht man jeweils ein Wärmetauscher = Schnittstelle zwischen Netz und Kunden-Gebäude. Beide Netze sind geschlossene Kreise, darum braucht es einen Wärmetäuchser zwischen den beiden. 

Dateien (eine pro Kunde):

- 1_prot.csv 
- 2_prot.csv
- 3_prot.csv
- 4_prot.csv
- 5_prot.csv
- 7_prot.csv
- 8_prot.csv

Variablen:

- Timestamp
- T6 Aussentemp.(°C)
- T7 RL Primär(°C)
- T8 VL Sekundär(°C)
- T11 RL Sekundär(°C
- Solltemp. VL Sekundär(°C)
- Max.Rücklauftemp.primär(°C)
- B-Solltemp.(°C),B-Status Pumpe
- B-Status Kreis,B-Status Mischer
- Puffer EIN Oben(°C)
- Puffer AUS Unten(°C)
- Ventilstellung(%)
- AT Mittel(°C)
- AT Langzeit(°C)
- WZ Wärmemenge(kWh)
- WZ Leistung(kW)
- WZ Duchfluss(l/h)
- WZ Rücklauftemp.(°C)
- WZ Vorlauftemp.(°C)
- WZ Spreizung(°C): Temperaturunterschied zwischen den Fluss beim Eingang bzw. Ausgang. Diesen Wert probiert man möglichst gross zu halten.
- Ventilstellung Gesamt(%)


## Kunde 6 - 6_protSPS.csv - Industriebetrieb

See schematic on p. 8 of the slides: this consumer can be shut off (load shedding). Therefore, there is a local backup oil-fired boiler. The corresponding details are given in 6_protSPS.csv.

Vairablen: 

- Timestamp: alle 5min, vom 1. Jan 2018 bis 1. Jan 2020
- T6 Aussentemp.(°C): Aussentemperatur 
- T7 RL Primär(°C)
- T8 VL Sekundär(°C)
- T11 RL Sekundär(°C)
- Solltemp. VL Sekundär(°C)
- Max.Rücklauftemp.primär(°C)
- B-Solltemp.(°C)
- B-Status Pumpe
- B-Status Kreis
- B-Status Mischer
- Puffer EIN Oben(°C)
- Puffer AUS Unten(°C)
- Ventilstellung(%)
- AT Mittel(°C)
- AT Langzeit(°C)
- WZ Wärmemenge(kWh)
- WZ Leistung(kW)
- WZ Duchfluss(l/h)
- WZ Rücklauftemp.(°C)
- WZ Vorlauftemp.(°C)
- WZ Spreizung(°C): Temperaturunterschied zwischen den Fluss beim Eingang bzw. Ausgang. Diesen Wert probiert man möglichst gross zu halten.
- Ventilstellung Gesamt(%)
- Ventilstellung gemittelt(%)


## Kunde 9 - Gewerbe

Dateien: 

- 9_prot.csv
- 901_protSPS.csv

Vairablen: 

- Timestamp
- T485 - Aussentemperatur(°C)
- T462 - VL Netz(°C)
- T464 - RL Netz(°C)
- T471 - Pufferfühler 1 (oben)(°C)
- T472 - Pufferfühler 2(°C),T473 - Pufferfühler 3(°C)
- T474 - Pufferfühler 4(°C),T475 - Pufferfühler 5(°C)
- T476 - Pufferfühler 6(°C),T477 - Pufferfühler 7(°C)
- T478 - Pufferfühler 8(°C),T479 - Pufferfühler 9(°C)
- T480 - Pufferfühler 10 (unten)(°C)
- T434 - Vorlauftemperatur GK1(°C)
- T432 - Rücklauftemperatur GK1(°C)
- T444 - Vorlauftemperatur GK2(°C)
- T442 - Rücklauftemperatur GK2(°C)
- DS461 - Druck VL Netz(bar)
- DS462 - Druck RL Netz(bar)
- WE1 K421 - Betrieb Holzkessel
- P431 - Störung Pumpe Gaskessel 1
- "AK480 - Endlagenschalter Bypassklappe kl. Netz ""offen"""
- "AK482 - Endlagenschalter Bypassklappe gr. Netz ""offen"""
- P461 - Freigabe Netzpumpe 1
- P462 - Freigabe Netzpumpe 2
- P463 - Freigabe Netzpumpe 3
- AK480 - Bypassklappe kl. Netz AUF
- AK482 - Bypassklappe gr. Netz AUF
- P431 - Freigabe Pumpe Gaskessel 1
- P441 - Freigabe Pumpe Gaskessel 2
- P471 - Freigabe Pumpe Teilstromfilter
- P461 - Leistungsvorgabe Netzpumpe 1-3(%)
- V481 - Stellsignalvorgabe Netzm. kl. Netz(%)
- V483 - Stellsignalvorgabe Netzm. gr. Netz(%)
- WE1 K421 - Leistungsvorgabe Holzkessel(%)
- WE1 K421 - Temperaturvorgabe Holzkessel(°C)
- WE2 K431 - Temperaturvorgabe Gaskessel 1(°C)
- P431 - Leistungsvorgabe Pumpe Gaskessel 1(%)
- P441 - Leistungsvorgabe Pumpe Gaskessel 2(%)
- Soll VL-Netz(°C),K1-Soll-VL(°C),K2-Soll-VL(°C)
- K3-Soll-VL(°C),SollNiveauK1,Soll-Diff.Druck(bar)
- Ist-Diff.Druck(bar),Anf. Last 6,Stufe Netzmischer
- Wärmemenge(kWh),Volumen(m3)
- Leistung(kW)
- Duchfluss(lph)
- AT Mittel(°C)
- SPLZ Ist Kessel 1(%)
- SPLZ Soll Kessel 1(%)
- SPLZ Ist Kessel 2(%)
- SPLZ Soll Kessel 2(%)
- SPLZ Ist Kessel 3(%)
- SPLZ Soll Kessel 3(%)
- Stellung Netzmischer 1(%)
- Stellung Netzmischer 2(%)
- Hand Lüftung
- AG1 - Sperre Alarmwähler
