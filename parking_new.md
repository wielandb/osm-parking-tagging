|                                                              | Tags für eine Fläche                                         | Tags für einen Way                                           |
| ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ |
| ![283](img/283.png)                                          | `restriction=no_stopping`                                    | `parking:SEITE:restriction=no_stopping`                      |
| ![283_1042-33](img/283_1042-33.png)                          | `restriction=no_stopping @ (OPENINGHOURS)`                   | `parking:SEITE:restriction=no_stopping @ (OPENINGHOURS)`     |
| ![286](img/286.png)                                          | `restriction=no_parking`                                     | `parking:SEITE:restriction=no_stopping`                      |
| ![286_1010-51](img/286_1010-51.png)                          | `restriction:hgv=no_parking`                                 | `parking:SEITE:restriction:hgv=no_parking`                   |
| ![286_1010-62](img/286_1010-62.png)                          | `restriction:motorcycle=no_parking`                          | `parking:SEITE:restriction:motorcycle=no_parking`            |
| ![286_1020-32](img/286_1020-32.png)                          | `restriction=no_parking`<br />`restriction:conditional=free @ residents`<br />`zone=AUSWEIS` | `parking:SEITE:restriction=no_parking`<br />`parking:SEITE:restriction:conditional=free @ residents`<br />`parking:SEITE:zone=AUSWEIS` |
| ![286_1042-33](img/286_1042-33.png)                          | `restriction=no_parking @ (OPENINGHOURS)`                    | `parking:SEITE:restriction=no_parking @ (OPENINGHOURS)`      |
| ![286_1042-33_1020-32](img/286_1042-33_1020-32.png)          | `restriction:conditional=no_parking @ (OPENINGHOURS); free @ residents`<br />`zone=AUSWEIS` | `parking:SEITE:restriction:conditional=no_parking @ (OPENINGHOURS); free @ residents`<br />`parking:SEITE:zone=AUSWEIS` |
| ![314.1_1044-30](img/314.1_1044-30.png)                      | `access=private`<br /><br />`zone=AUSWEIS`                   | `parking:SEITE:access=private`<br />`parking:SEITE:zone=AUSWEIS` |
| ![314.1_1051-33](img/314.1_1051-33.png)                      | `fee=yes`<br />`authentication:ticket=yes`                   | `parking:SEITE:fee=yes`<br />`parking:SEITE:authentication:ticket=yes` |
| ![314_1010-51](img/314_1010-51.png)                          | `access=no`<br />`hgv=designated`                            | `parking:SEITE:access=no`<br />`parking:SEITE:hgv=designated` |
| ![314_1010-57](img/314_1010-57.png)                          | `access=no`<br />`bus=designated`<br />`tourist_bus=designated` | `parking:SEITE:access=no`<br />`parking:SEITE:bus=designated`<br />`parking:SEITE:tourist_bus=designated` |
| ![314_1010-57_1042-33](img/314_1010-57_1042-33.png)          | `access:conditional=no @ (OPENINGHOURS)`<br />`bus:conditional=designated @ (OPENINGHOURS)`<br />`tourist_bus:conditional=designated @ (OPENINGHOURS)`<br />`access=yes`<br /> | `parking:SEITE:access:conditional=no @ (OPENINGHOURS)`<br /><br />`parking:SEITE:access=yes` <br />`parking:SEITE:bus:conditional=designated @ (OPENINGHOURS)`<br />`parking:SEITE:tourist_bus:conditional=designated @ (OPENINGHOURS)` |
| ![314_1010-58](img/314_1010-58.png)                          | `access=no`<br />`motorcar=designated`                       | `parking:SEITE:access=no`<br />`parking:SEITE:motorcar=designated` |
| ![314_1010-59](img/314_1010-59.png)                          | `access=no`<br />`trailer=designated`                        | `parking:SEITE:access=no`<br />`parking:SEITE:trailer=designated` |
| ![314_1010-62](img/314_1010-62.png)                          | `access=no`<br />`motorcycle=designated`                     | `parking:SEITE:access=no`<br />`parking:SEITE:motorcycle=designated` |
| ![314_1040-32](img/314_1040-32.png)                          | `maxstay=TIME`<br />`authentication:disc=yes`                | `parking:SEITE:access=yes`<br />`parking:SEITE:fee=no`<br />`parking:SEITE:maxstay=TIME`<br />`parking:SEITE:authentication:disc=yes` |
| ![314_1040-32_1020-32](img/314_1040-32_1020-32.png)          | `maxstay=TIME`<br />`authentication:disc=yes`<br />`zone=AUSWEIS` | `parking:SEITE:maxstay=TIME`<br />`parking:SEITE:authentication:disc=yes`<br />`parking:SEITE:zone=AUSWEIS` |
| ![314_1040-32_1042-33](img/314_1040-32_1042-33.png)          | `maxstay:conditional=TIME @ (OPENINGHOURS)`<br />`authentication:disc=yes` | `parking:SEITE:access=yes`<br />`parking:SEITE:fee=no`<br />`parking:SEITE:maxstay:conditional=TIME @ (OPENINGHOURS)` |
| ![314_1040-32_1042-33_1020-32](img/314_1040-32_1042-33_1020-32.png) | `maxstay:conditional=TIME @ (OPENINGHOURS)`<br />`authentication:disc=yes`<br />`zone=AUSWEIS` | `parking:SEITE:maxstay:conditional=TIME @ (OPENINGHOURS)`<br />`parking:SEITE:authentication:disc=yes`<br />`parking:SEITE:zone=AUSWEIS` |
| ![314_1042-33](img/314_1042-33.png)                          | `opening_hours=OPENINGHOURS`                                 | `parking:SEITE:opening_hours=OPENINGHOURS`                   |
| ![314_1044-10](img/314_1044-10.png)                          | `access=no`<br />`disabled=designated`                       | `parking:SEITE:access=no`<br />`parking:SEITE:disabled=designated` |
| ![314_1044-10_1042-33](img/314_1044-10_1042-33.png)          | `access=yes`<br />`access:conditional=no @ (OPENINGHOURS)`<br />`disabled:conditional=designated @ (OPENINGHOURS)`<br />`fee=no` | `parking:SEITE:access=yes`<br />`parking:SEITE:access:conditional=no @ (OPENINGHOURS)`<br />`parking:SEITE:disabled:conditional=designated @ (OPENINGHOURS)`<br />`fee=no` |
| ![314_1044-11](img/314_1044-11.png)                          | `access=private`<br />`ref=AUSWEIS`                          | `parking:SEITE:access=private`<br />`parking:SEITE:ref=AUSWEIS` |
| ![314_1044-30](img/314_1044-30.png)                          | `access=private`<br />`zone=AUSWEIS`                         | `parking:SEITE:access=private`<br />`parking:SEITE:zone=AUSWEIS` |
| ![314_1050-32](img/314_1050-32.png)                          | `restriction=charging_only`                                  | `parking:SEITE:restriction=charging_only`                    |
| ![314_1050-32_1040-32](img/314_1050-32_1040-32.png)          | `restriction=charging_only`<br />`maxstay=TIME`<br />`authentication:disc=yes` | `parking:SEITE:restriction=charging_only`<br />`parking:SEITE:maxstay=TIME`<br />`parking:SEITE:authentication:disc=yes` |
| ![314_1050-32_1040-32_1042-33](img/314_1050-32_1040-32_1042-33.png) | `restriction=charging_only`<br />`maxstay:conditional=TIME @ (OPENINGHOURS)`<br />`authentication:disc=yes` | `parking:SEITE:restriction=charging_only`<br />`parking:SEITE:maxstay:conditional=TIME @ (OPENINGHOURS)`<br />`parking:SEITE:authentication:disc=yes` |
| ![314_1053-31](img/314_1053-31.png)                          | `fee=yes`<br />`authentication=ticket`                       | `parking:SEITE:fee=yes`<br />`parking:SEITE:authentication=ticket` |
| ![314_1053-31_1020-32](img/314_1053-31_1020-32.png)          | `fee=yes`<br />`zone=AUSWEIS`<br />`authentication:ticket=yes` | `parking:SEITE:fee=yes`<br />`parking:SEITE:zone=AUSWEIS`<br />`parking:SEITE:authentication:ticket=yes` |



##### Platzhalter für Werte

- `SEITE` - Die Seite(n) des Way, für die die condition gilt. right/left/both
- `OPENINGHOURS` - Platzhalter für Zeitspannen, zu denen Beschränkungen gelten
- `TIME` - Zeit, die auf dem Parkscheiben-Schild steht
- `AUSWEIS` - Nr. des Parkausweises, die auf dem Schild angegeben ist
