-- Tentative d'insertion de données qui violent les contraintes

-- Violation de la contrainte de CHECK FORMAT sur heureProg (08:00 au lieu de 08.00)
INSERT INTO Programmations (codeQuartier, plaqueCamion, heureProg) VALUES (06, 123, '08.00');

-- Violation de la contrainte de CHECK L'intervalle sur heureProg (04:00 n'est pas dans l'intervalle 05:00<= heureProg < 19:00 )
INSERT INTO Programmations (codeQuartier, plaqueCamion, heureProg) VALUES (06, 123, '04:00');

 -- Violation de la contrainte de CHECK qua_dechCamion <= cap_dep_maxModele avec une trigger
INSERT INTO CamionsOrdure (plaqueCamion, qua_dechCamion, cap_eqCamion, nomModele, nomCentre) VALUES (444, 100, 3, 'OtoCar1881', 'EcoSolutions Recycling Center');

-- Violation de la contrainte PRIMARY KEY sur idBalayeur (UNIQUE constraint)
INSERT INTO Balayeurs (idBalayeur, pseudoBalayeur, telBalayeur, plaqueCamion) VALUES (05, 'Mahmut', 0987654321, 222);

-- Violation de la contrainte PRIMARY KEY sur idBalayeur et plaqueCamion (UNIQUE constraint)
INSERT INTO Programmations (codeQuartier, plaqueCamion, heureProg) VALUES (01, 123, '12:00');

--Violation de la contrainte FOREIGN KEY (il n y a pas la plaque camion 991 dans CamionsOrdure qui est une foreign key)
INSERT INTO Balayeurs(idBalayeur, pseudoBalayeur, telBalayeur, plaqueCamion) VALUES (09, 'Konur', 515486789, 991);