|                                                              | Tags für eine Fläche                                         | Tags für einen Way                                           |
| ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ |
| ![286_1010-51](img/286_1010-51.png)                          | `restriction:hgv=no_parking`                                 | `parking:right:restriction:hgv=no_parking`                   |
| ![286_1010-62](img/286_1010-62.png)                          | `restriction:motorcycle=no_parking`                          | `parking:right:restriction:motorcycle=no_parking`            |
| ![286_1020-32](img/286_1020-32.png)                          | `restriction=no_parking`<br />`restriction:conditional=free @ residents`<br />`zone=AUSWEIS` | `parking:SEITE:restriction=no_parking`<br />`parking:SEITE:restriction:conditional=free @ residents`<br />`parking:SEITE:zone=AUSWEIS` |
| ![286_1042-33](img/286_1042-33.png)                          | `restriction=no_parking @ (OPENING_HOURS)`                   | `parking:SEITE:restriction=no_parking @ (OPENING_HOURS)`     |
| ![286_1042-33_1020-32](img/286_1042-33_1020-32.png)          | `restriction:conditional=no_parking @ (OPENING_HOURS); free @ residents`<br />`zone=AUSWEIS` | `parking:SEITE:restriction:conditional=no_parking @ (OPENING_HOURS); free @ residents`<br />`parking:SEITE:zone=AUSWEIS` |
| ![314.1_1044-30](img/314.1_1044-30.png)                      | `access=private`<br /><br />`zone=AUSWEIS`                   | `parking:SEITE:access=private`<br />`parking:SEITE:zone=AUSWEIS` |
| ![314_1010-51](img/314_1010-51.png)                          | `access=no`<br />`hgv=designated`                            | `parking:SEITE:access=no`<br />`parking:SEITE:hgv=designated` |
| ![314_1010-57](img/314_1010-57.png)                          | `access=no`<br />`bus=designated`<br />`tourist_bus=designated` | `parking:SEITE:access=no`<br />`parking:SEITE:bus=designated`<br />`parking:SEITE:tourist_bus=designated` |
| ![314_1010-57_1042-33](img/314_1010-57_1042-33.png)          | `access:conditional=no @ (OPENING_HOURS)`<br />`bus:conditional=designated @ (OPENING_HOURS)`<br />`tourist_bus:conditional=designated @ (OPENING_HOURS)`<br />`access=yes`<br /> | `parking:SEITE:access:conditional=no @ (OPENING_HOURS)`<br /><br />`parking:SEITE:access=yes` <br />`parking:SEITE:bus:conditional=designated @ (OPENING_HOURS)`<br />`parking:SEITE:tourist_bus:conditional=designated @ (OPENING_HOURS)` |
| ![314_1010-58](img/314_1010-58.png)                          | `access=no`<br />`motorcar=designated`                       | `parking:SEITE:access=no`<br />`parking:SEITE:motorcar=designated` |
| ![314_1010-59](img/314_1010-59.png)                          | `access=no`<br />`trailer=designated`                        | `parking:SEITE:access=no`<br />`parking:SEITE:trailer=designated` |
| ![314_1010-62](img/314_1010-62.png)                          | `access=no`<br />`motorcycle=designated`                     | `parking:SEITE:access=no`<br />`parking:SEITE:motorcycle=designated` |
| ![314_1040-32](img/314_1040-32.png)                          | `maxstay=TIME`<br />`authentication:disc=yes`                | `parking:SEITE:access=yes`<br />`parking:SEITE:fee=no`<br />`parking:SEITE:maxstay=TIME`<br />`parking:SEITE:authentication:disc=yes` |
| ![314_1040-32_1020-32](img/314_1040-32_1020-32.png)          | `maxstay=TIME`<br />`authentication:disc=yes`<br />`zone=AUSWEIS` | `parking:SEITE:maxstay=TIME`<br />`parking:SEITE:authentication:disc=yes`<br />`parking:SEITE:zone=AUSWEIS` |
| ![314_1040-32_1042-33](img/314_1040-32_1042-33.png)          | `maxstay:conditional=TIME @ (OPENING_HOURS)`<br />`authentication:disc=yes` | `parking:SEITE:access=yes`<br />`parking:SEITE:fee=no`<br />`parking:SEITE:maxstay:conditional=TIME @ (OPENING_HOURS)` |
| ![314_1040-32_1042-33_1020-32](img/314_1040-32_1042-33_1020-32.png) | `maxstay:conditional=TIME @ (OPENING_HOURS)`<br />`authentication:disc=yes`<br />`zone=AUSWEIS` | `parking:SEITE:maxstay:conditional=TIME @ (OPENING_HOURS)`<br />`parking:SEITE:authentication:disc=yes`<br />`parking:SEITE:zone=AUSWEIS` |
| ![314_1042-33](img/314_1042-33.png)                          | `opening_hours=OPENING_HOURS`                                | `parking:SEITE:opening_hours=OPENING_HOURS`                  |
| ![314_1044-10](img/314_1044-10.png)                          | `access=no`<br />`disabled=designated`                       | `parking:SEITE:access=no`<br />`parking:SEITE:disabled=designated` |
| ![314_1044-10_1042-33](img/314_1044-10_1042-33.png)          | `access=yes`<br />`access:conditional=no @ (OPENING_HOURS)`<br />`disabled:conditional=designated @ (OPENING_HOURS)`<br />`fee=no` | `parking:SEITE:access=yes`<br />`parking:SEITE:access:conditional=no @ (OPENING_HOURS)`<br />`parking:SEITE:disabled:conditional=designated @ (OPENING_HOURS)`<br />`fee=no` |
| ![314_1044-11](img/314_1044-11.png)                          | `access=private`<br />`ref=AUSWEIS`                          | `parking:SEITE:access=private`<br />`parking:SEITE:ref=AUSWEIS` |
| ![314_1044-30](img/314_1044-30.png)                          | `access=private`<br />`zone=AUSWEIS`                         | `parking:SEITE:access=private`<br />`parking:SEITE:zone=AUSWEIS` |
| ![314_1050-32](img/314_1050-32.png)                          | `restriction=charging_only`                                  | `parking:SEITE:restriction=charging_only`                    |
| ![314_1050-32_1040-32](img/314_1050-32_1040-32.png)          | `restriction=charging_only`<br />`maxstay=TIME`<br />`authentication:disc=yes` | `parking:SEITE:restriction=charging_only`<br />`parking:SEITE:maxstay=TIME`<br />`parking:SEITE:authentication:disc=yes` |
| ![314_1050-32_1040-32_1042-33](img/314_1050-32_1040-32_1042-33.png) | `restriction=charging_only`<br />`maxstay:conditional=TIME @ (OPENING_HOURS)`<br />`authentication:disc=yes` | `parking:SEITE:restriction=charging_only`<br />`parking:SEITE:maxstay:conditional=TIME @ (OPENING_HOURS)`<br />`parking:SEITE:authentication:disc=yes` |
| ![314_1053-31](img/314_1053-31.png)                          | `fee=yes`<br />`authentication=ticket`                       | `parking:SEITE:fee=yes`<br />`parking:SEITE:authentication=ticket` |
| ![314_1053-31_1020-32](img/314_1053-31_1020-32.png)          | `fee=yes`<br />`zone=AUSWEIS`<br />`authentication:ticket=yes` | `parking:SEITE:fee=yes`<br />`parking:SEITE:zone=AUSWEIS`<br />`parking:SEITE:authentication:ticket=yes` |



##### Platzhalter für Werte

- `SEITE` - Die Seite(n) des Way, für die die condition gilt. right/left/both
- `OPENING_HOURS` - Platzhalter für Zeitspannen, zu denen Beschränkungen gelten
- `TIME` - Zeit, die auf dem Parkscheiben-Schild steht
- `AUSWEIS` - Nr. des Parkausweises, die auf dem Schild angegeben ist
