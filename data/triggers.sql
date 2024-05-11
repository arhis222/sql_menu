-- Création des déclencheurs

DROP TRIGGER IF EXISTS check_capacity_insert;
DROP TRIGGER IF EXISTS check_capacity_update;

CREATE TRIGGER check_capacity_insert
BEFORE INSERT ON CamionsOrdure
FOR EACH ROW
BEGIN
    SELECT CASE
        WHEN ((SELECT cap_dep_maxModele FROM Modeles WHERE nomModele = NEW.nomModele) < NEW.qua_dechCamion)
        THEN RAISE (ABORT, 'La quantite  du dechet du camion dépasse la capacité maximale du modèle')
    END;
END;

CREATE TRIGGER check_capacity_update
BEFORE UPDATE ON CamionsOrdure
FOR EACH ROW
BEGIN
    SELECT CASE
        WHEN ((SELECT cap_dep_maxModele FROM Modeles WHERE nomModele = NEW.nomModele) < NEW.qua_dechCamion)
        THEN RAISE (ABORT, 'La quantite  du dechet du camion dépasse la capacité maximale du modèle')
    END;
END;
