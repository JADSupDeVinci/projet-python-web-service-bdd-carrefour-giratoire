CREATE DATABASE IF NOT EXISTS dragon_generator;


USE dragon_generator;


CREATE TABLE IF NOT EXISTS dragon_types (
    id INT AUTO_INCREMENT PRIMARY KEY,
    type_name VARCHAR(50) NOT NULL
);


CREATE TABLE IF NOT EXISTS elements (
    id INT AUTO_INCREMENT PRIMARY KEY,
    element_name VARCHAR(50) NOT NULL
);


CREATE TABLE IF NOT EXISTS colors (
    id INT AUTO_INCREMENT PRIMARY KEY,
    color_name VARCHAR(50) NOT NULL
);


CREATE TABLE IF NOT EXISTS special_features (
    id INT AUTO_INCREMENT PRIMARY KEY,
    feature_name VARCHAR(50) NOT NULL
);

CREATE TABLE IF NOT EXISTS environment (
    id INT AUTO_INCREMENT PRIMARY KEY,
    environment_name VARCHAR(50) NOT NULL
);

INSERT INTO dragon_types (type_name) VALUES ('Dragon occidental'), ('Dragon oriental'), ('Wyvern'), ('Feydragon'), ('Dragonnette'), ('Basilic'), ('Amphiptère'), ('Wyrm'), ('Lindworm'), ('Drake'), ('Hydre'), ('Coatl'), ('Quetzalcoatl'),('Zmeï'), ('Naga'), ('Leviathan'), ('Guivre'), ('Druk');

-- Insérer des éléments
INSERT INTO elements (element_name) VALUES ('de feu'), ('d eau'), ('de terre'), ('d air'), ('de glace'), ('de lave'), ('de foudre'), ('de métal'), ('de bois'), ('de lumière'), ('d obscurité'), ('des étoiles'), ('d ether'), ('d ame'), ('d esprit'), ('de chaos'), ('de gravité'), ('de son'), ('d aether'), ('de sang'), ('de cristal'), ('d ombre'), ('de cendre'), ('de poison'), ('des rêves');

-- Insérer des couleurs
INSERT INTO colors (color_name) VALUES ('Rouge'), ('Vert'), ('Bleu'), ('Jaune'), ('Orange'), ('Violet'), ('Rose'), ('Cyan'), ('Magenta'), ('Brun'), ('Noir'), ('Blanc'), ('Gris'), ('Turquoise'), ('Lavande'), ('Or'), ('Argent'), ('Bordeaux'), ('Lime'), ('Indigo'), ('Fuchsia'), ('Ocre'), ('Pourpre'), ('Émeraude'), ('Marine'), ('Azuré'), ('Marron'), ('Beige'), ('Ivoire'), ('Kaki'), ('Ambre'), ('Carmin'), ('Rouille'), ('Topaze'), ('Écarlate'), ('Chartreuse'), ('Saphir'), ('Améthyste'), ('Cramoisi'),;

-- Insérer des caractéristiques spéciales
INSERT INTO special_features (feature_name) VALUES ('aux yeux bleus'), ('aux ailes d argent'), ('au souffle de feu'), ('à la peau écailleuse'), ('aux griffes acérées'), ('à la queue de serpent'), ('aux écailles d or'), ('à la corne spirale'), ('aux crocs en diamant'), ('aux écailles phosphorescentes'), ('aux pouvoirs psychiques'), ('aux écailles d obsidienne'), ('aux ailes translucides'), ('au rugissement de tonnerre'), ('aux yeux lumineux'), ('à la respiration glaciale'), ('au souffle venimeux'), ('aux écailles de cristal'), ('à la taille gigantesque'), ('aux ailes de chauve-souris'), ('aux écailles argentées'), ('aux pouvoirs de guérison'),('aux griffes empoisonnées'), ('aux yeux de rubis'), ('à la peau de fer'), ('aux ailes de feu');

-- Insérer des environement
INSERT INTO environment (environment_name) VALUES ('des montagnes'), ('des abysses'), ('des cieux'), ('des forêts anciennes'), ('des volcans en éruption'), ('des glaciers éternels'), ('des océans insondables'), ('des tempêtes déchaînées'), ('des rivières de lave'), ('des ruines oubliées'), ('des jungles luxuriantes'), ('des cavernes mystérieuses'), ('des îles flottantes'), ('des plaines infinies'), ('des étoiles filantes'), ('des désert de sable noir'), ('des montagnes suspendues'), ('des vents hurlants'), ('des aurores boréales'), ('des tunnels souterrains'), ('des cercles de pierres anciennes'), ('des crépuscules éternels'), ('des forêts hantées'), ('des mirages mystiques'), ('des éclats de foudre'), ('des cavernes cristallines'), ('des brumes envoûtantes'), ('des océans de nuages'), ('des rituels magiques'), ('des royaumes invisibles');


CREATE OR REPLACE VIEW view_dragon_types AS
SELECT * FROM dragon_types;


CREATE OR REPLACE VIEW view_elements AS
SELECT * FROM elements;


CREATE OR REPLACE VIEW view_colors AS
SELECT * FROM colors;


CREATE OR REPLACE VIEW view_special_features AS
SELECT * FROM special_features;


CREATE OR REPLACE VIEW view_environment AS
SELECT * FROM environment;

CREATE USER 'user'@'localhost' IDENTIFIED BY 'user';

REVOKE ALL PRIVILEGES ON *.* FROM 'user'@'localhost';

GRANT SELECT ON dragon_generator.view_dragon_types TO 'user'@'localhost';
GRANT SELECT ON dragon_generator.view_elements TO 'user'@'localhost';
GRANT SELECT ON dragon_generator.view_colors TO 'user'@'localhost';
GRANT SELECT ON dragon_generator.view_special_features TO 'user'@'localhost';
GRANT SELECT ON dragon_generator.view_environment TO 'user'@'localhost';


GRANT INSERT, DELETE, UPDATE ON dragon_generator.`view_colors` TO 'user'@'localhost';
FLUSH PRIVILEGES;
