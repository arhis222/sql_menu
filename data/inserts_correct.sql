-- Ajout de données dans la table CentresOrdure
INSERT INTO CentresOrdure (nomCentre, capCentre)
VALUES ('Pittsburg Waste Management', 5000),
       ('GreenCity Trash Services', 7000),
       ('EcoClean Waste Disposal', 10000),
       ('CleanCity Waste Solutions', 8000),
       ('EcoSolutions Recycling Center', 6000),
       ('Pittsburg Recycling Hub', 9000),
       ('Utkuland',1000);

-- Ajout de données dans la table Modeles
INSERT INTO Modeles (nomModele, tailleModele, cap_dep_maxModele)
    VALUES ('FoCle1000', 'Grand', 150),
       ('TenMas2000', 'Grand', 150),
       ('NewDis3000', 'Grand', 150),
       ('EcoCon1453', 'Moyen', 100),
       ('EcoGre1922', 'Moyen', 100),
       ('OtoCar1881', 'Petit', 050),
       ('Varan1923','Petit', 050),
       ('MamaMia2023','Moyen', 090);

-- Ajout de données dans la table CamionsOrdure (plaqueCamion est une clé primaire)
INSERT INTO CamionsOrdure (plaqueCamion, cap_eqCamion, nomModele, nomCentre)
VALUES (123, 08, 'FoCle1000', 'Pittsburg Waste Management'),
       (456, 08, 'TenMas2000', 'GreenCity Trash Services'),
       (789, 08, 'NewDis3000', 'EcoClean Waste Disposal'),
       (101, 06, 'EcoCon1453', 'CleanCity Waste Solutions'),
       (202, 04, 'EcoGre1922', 'EcoSolutions Recycling Center'),
       (303, 04, 'OtoCar1881', 'Pittsburg Recycling Hub'),
       (222, 04, 'Varan1923', 'Pittsburg Recycling Hub'),
       (333, 06, 'Varan1923', 'Utkuland');

-- Ajout de données dans la table Quartiers
INSERT INTO Quartiers (codeQuartier, nomQuartier, popQuartier, nb_poubQuartier)
VALUES (01, 'Downtown', 20000, 20),
       (02, 'Shadyside', 15000, 30),
       (03, 'Squirrel Hill', 18000, 10),
       (04, 'Oakland', 22000, 30),
       (05, 'South Side', 25000, 40),
       (06, 'North Shore', 17000, 50);


-- Ajout de données dans la table Balayeurs (plaqueCamion est une clé étrangère)
INSERT INTO Balayeurs (idBalayeur, pseudoBalayeur, telBalayeur, plaqueCamion)
VALUES (01, 'Sophia', 555123456, 123),
       (02, 'Noah', 555987654, 456),
       (03, 'Olivia', 555234567, 789),
       (04, 'Liam', 555666777, 101),
       (05, 'Ava', 555345678, 202),
       (06, 'Arhan', 555876543, 222),
       (34, 'Utku',555234648,303),
       (07, 'Isabella', 555456789, 101);


-- Ajout de données dans la table Programmations avec le format de date 'jj-mm-aaaa'
INSERT INTO Programmations (codeQuartier, plaqueCamion, heureProg)
VALUES (01, 123, '08:00'),  -- Heure: 08:00
       (02, 456, '10:30'),  -- Heure: 10:30
       (03, 789, '14:15'),  -- Heure: 14:15
       (04, 101, '09:45'),  -- Heure: 09:45
       (05, 202, '12:30'),  -- Heure: 12:30
       (06, 303, '15:15'),  -- Heure: 15:15
       (01, 101, '17:00');  -- Heure: 17:00

-- Nous ajoutons la colonne qua_dechCamion à la table CamionsOrdure pour le view
ALTER TABLE CamionsOrdure ADD COLUMN qua_dechCamion INTEGER;
