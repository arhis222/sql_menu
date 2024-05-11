CREATE TABLE IF NOT EXISTS Balayeurs (
	idBalayeur INTEGER NOT NULL PRIMARY KEY,
	pseudoBalayeur TEXT NOT NULL,
	telBalayeur INTEGER,
	plaqueCamion INTEGER NOT NULL,
	CONSTRAINT fk_bal_plaqueCamion FOREIGN KEY (plaqueCamion) REFERENCES CamionsOrdure(plaqueCamion)
);

CREATE TABLE IF NOT EXISTS Quartiers (
	codeQuartier INTEGER NOT NULL PRIMARY KEY,
	nomQuartier TEXT NOT NULL,
	popQuartier INTEGER NOT NULL,
	nb_poubQuartier INTEGER NOT NULL
);

CREATE TABLE IF NOT EXISTS CamionsOrdure (
	plaqueCamion INTEGER NOT NULL PRIMARY KEY,
	cap_eqCamion INTEGER NOT NULL,
	nomModele TEXT,
	nomCentre TEXT,
	CONSTRAINT fk_camion_nomCentre FOREIGN KEY (nomCentre) REFERENCES CentresOrdure(nomCentre),
	CONSTRAINT fk_camion_nomModele FOREIGN KEY (nomModele) REFERENCES Modeles(nomModele)
);

CREATE TABLE IF NOT EXISTS Programmations (
	codeQuartier INTEGER NOT NULL,
	plaqueCamion INTEGER NOT NULL,
	heureProg TEXT NOT NULL CHECK (heureProg LIKE '__:__' AND heureProg >= '05:00' AND heureProg < '19:00'),
	CONSTRAINT pk_prog_codeQuartier_plaqueCamion PRIMARY KEY (codeQuartier, plaqueCamion),
	CONSTRAINT fk_prog_codeQuartier FOREIGN KEY (codeQuartier) REFERENCES Quartiers(codeQuartier),
	CONSTRAINT fk_prog_plaqueCamion FOREIGN KEY (plaqueCamion) REFERENCES CamionsOrdure(plaqueCamion)
);


CREATE TABLE IF NOT EXISTS CentresOrdure (
	nomCentre TEXT NOT NULL PRIMARY KEY,
	capCentre INTEGER
);

CREATE TABLE IF NOT EXISTS Modeles (
	nomModele TEXT NOT NULL PRIMARY KEY,
	tailleModele TEXT NOT NULL,
	cap_dep_maxModele INTEGER,
	CONSTRAINT ck_tailleModele CHECK (tailleModele IN ('Petit', 'Moyen', 'Grand'))
);
