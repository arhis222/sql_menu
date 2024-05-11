--Creation d'un view qui compte la quantité totale de déchet portée par les camions dans chaque quartier (on suppose qu'ils prennent tout les déchets dans un quartier quand ils y vont)
--Il peut être null si le camion ne sert pas
CREATE VIEW IF NOT EXISTS Camion_Total_dech AS
SELECT p.plaqueCamion, SUM(q.nb_poubQuartier) AS total_dech
FROM Programmations p
JOIN Quartiers q USING(codeQuartier)
GROUP BY p.plaqueCamion;

-- Ajouter les données de la VIEW Camion_Total_dech à la table CamionsOrdure
UPDATE CamionsOrdure
SET qua_dechCamion = (
    SELECT total_dech
    FROM Camion_Total_dech
    WHERE CamionsOrdure.plaqueCamion = Camion_Total_dech.plaqueCamion
);
