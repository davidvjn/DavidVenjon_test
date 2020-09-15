from django.db import models

DESCRIPTIONS = {
    'AngelinaJolie' : {'description': 'Angelina Jolie [ænd͡ʒe\ˈliːnɪ d͡ʒoʊˈliː], née Angelina Jolie Voight le 4 juin 1975 à Los Angeles, est une actrice, réalisatrice, scénariste, productrice, mannequin, philanthrope, écrivaine et ambassadrice de bonne volonté américano-cambodgienne. Elle a reçu trois Golden Globes, deux Screen Actors Guild Awards et un Oscar du cinéma. Ambassadrice de bonne volonté, elle a défendu diverses causes humanitaires à travers le monde et est réputée pour son travail en faveur des réfugiés avec le Haut Commissariat des Nations unies pour les réfugiés. Angelina Jolie est également une femme engagée pour la protection de la nature et des animaux. Elle est une amie fidèle du Dr Jane Goodall et membre de l\'Institut Jane Goodall France. Elle a déjà été désignée comme l\'une des plus belles femmes du monde et sa vie hors-caméras est suivie de très près.'},

    'BeyonceKnowles' : {'description': 'Beyoncé [biˈjɑnseɪ], de son nom complet Beyoncé Giselle Carter, née Knowles le 4 septembre 1981 à Houston, au Texas, est une chanteuse, compositrice, danseuse et actrice américaine. Elle est désignée en 2009 comme étant l\'artiste de la décennie 2000 par The Guardian, tandis que New Musical Express la voit comme l\'une des artistes ayant défini la décennie 2010 ; selon Entertainment Weekly, personne n\'a dominé la musique comme elle dans cette dernière décennie. Les critiques musicales de The New Yorker décrivent Beyoncé comme étant la musicienne la plus populaire, la plus importante et la plus influente du xxie siècle'},

    'JenniferAniston' : {'description': 'Jennifer Aniston, née le 11 février 1969 à Los Angeles, est une actrice, réalisatrice et productrice américaine. Elle accède à la notoriété internationale en interprétant, de 1994 à 2004, le personnage de Rachel Green dans la sitcom à succès mondial Friends. Grâce à ce rôle, elle obtient un Emmy Award, un Golden Globe Award et un Screen Actors Guild Award. Elle poursuit ensuite sa carrière au cinéma, alternant cinéma populaire (Bruce tout-puissant, Polly et moi, La Rupture, Marley et Moi, Le Mytho, Comment tuer son boss ?, Les Miller, une famille en herbe, etc.) et films indépendants (35 heures, c\'est déjà trop, The Good Girl, Friends with Money, Life of Crime, Cake, etc.).'},

    'JudeLaw' : {'description': 'Jude Law [ˈd͡ʒuːd lɔː]2= est un acteur, réalisateur et producteur de cinéma britannique, né le 29 décembre 1972 à Lewisham (Londres). Révélé durant les années 1990 par Bienvenue à Gattaca (1997), eXistenZ (1998) et Le Talentueux Mr. Ripley (1999), il joue ensuite dans des grandes productions hollywoodiennes : A.I. Intelligence artificielle (2001), Les Sentiers de la perdition (2002), Retour à Cold Mountain (2003) et le thriller sentimental Entre adultes consentants (2004). Par la suite, il tourne à deux reprises avec Martin Scorsese dans Aviator (2004) et Hugo Cabret (2011), et avec Steven Soderbergh dans Contagion (2011) et Effets secondaires (2013). Il connait son plus gros succès commercial en incarnant le Dr John Watson dans les films Sherlock Holmes (2009) et Sherlock Holmes : Jeu d\'ombres (2011), réalisés par Guy Ritchie.'},
    
    'LeonardoDiCaprio' : {'description': 'Leonardo DiCaprio [ˈliːoʊnɚdoʊ dɪˈkæprioʊ], né le 11 novembre 1974 à Los Angeles, est un acteur, scénariste et producteur de cinéma américain. Grandissant dans les quartiers populaires de Los Angeles tels que Los Feliz puis Hollywood, le jeune Leonardo DiCaprio prend comme modèle le fils de sa belle-mère Peggy Ann Saunders, Adam Farrar, qui commence dès l\'enfance une carrière d\'acteur. Il décide alors de se lancer lui aussi, encouragé par ses parents. Il montre rapidement un talent évident pour la comédie et se voit proposer des rôles à la télévision, puis au cinéma. Après avoir été choisi parmi de très nombreux candidats pour jouer face à son acteur préféré Robert De Niro dans Blessures secrètes en 1993, il se fait particulièrement remarquer la même année grâce à son film suivant, Gilbert Grape, où il incarne face à Johnny Depp un jeune garçon déficient intellectuel, rôle pour lequel il est nommé à l\'Oscar du meilleur acteur dans un second rôle à l\'âge de 19 ans.'},
    
    'MeganFox' : {'description': 'Megan Fox est une actrice et mannequin américaine, née le 16 mai 1986 à Oak Ridge (Tennessee). Elle est révélée au début des années 2000 par des rôles réguliers à la télévision : Ocean Ave (2002-2003), puis la sitcom La Star de la famille (2004-2006). En 2004, elle donne la réplique à deux autres jeunes actrices en pleine ascension : Lindsay Lohan, tête d\'affiche de la comédie musicale Le Journal intime d\'une future star, puis Kaley Cuoco dans le téléfilm romantique Crimes of Fashion. C\'est en 2007 qu\'elle est révélée au grand public par son rôle de Mikaela Banes dans le blockbuster Transformers, réalisé par Michael Bay et produit par Steven Spielberg. En 2009, elle reprend son rôle dans la suite du blockbuster, mais tient aussi le premier rôle de la comédie horrifique Jennifer\'s Body aux cotés d\'Amanda Seyfried et évolue aux côtés de Josh Brolin dans le film de super-héros Jonah Hex. En 2010, elle est la tête d\'affiche du drame Passion Play, aux côtés de Mickey Rourke.'},
    
    'NicoleKidman' : {'description': 'Nicole Kidman [nɪˈkoʊl ˈkɪdmən] est une actrice et productrice de cinéma australo-américaine, née le 20 juin 1967 à Honolulu. Considérée comme l\'une des plus grandes actrices de sa génération, elle est reconnue pour l\'intensité dramatique de ses compositions, sa capacité à s\'effacer derrière ses personnages et l\'audace de ses choix, alternant entre films populaires et cinéma indépendant. Elle a ainsi remporté de multiples récompenses, parmi lesquelles un Oscar, cinq Golden Globes, deux Emmy Awards, un BAFTA, un Ours d\'argent, le Prix anniversaire du Festival de Cannes pour l\'ensemble de son œuvre, et possède une étoile sur le Hollywood Walk of Fame. Au cours de sa carrière, elle interprète de nombreux rôles marquants, notamment dans Prête à tout (1995) de Gus Van Sant, film qui la révèle au grand public et où elle tient le rôle d\'une jeune journaliste obsédée par la célébrité. Ses compositions mémorables incluent le rôle d\'une femme dont le mariage est en difficulté dans le sulfureux dernier film de Stanley Kubrick, Eyes Wide Shut (1999), son interprétation d\'une danseuse de cabaret dans le film musical de Baz Luhrmann, Moulin Rouge (2001), pour lequel elle reçoit sa première nomination à l\'Oscar, ou encore sa performance inquiétante dans le thriller d\'Alejandro Amenábar, Les Autres (2001). Son incarnation de Virginia Woolf dans The Hours en 2002 lui vaut l\'Oscar, le Golden Globe, le BAFTA et l\'Ours d\'argent de la meilleure actrice.'},
    
    'RobertPattinson' : {'description': 'Robert Pattinson, nom de scène de Robert Douglas Thomas Pattinson, né le 13 mai 1986 à Barnes quartier de Londres, en Angleterre, au (Royaume-Uni), est un acteur, mannequin et musicien anglais. Il est révélé durant les années 2000 par des productions destinées aux adolescents comme la franchise Twilight (2008-2012), où il incarne Edward Cullen aux côtés de Kristen Stewart, mais aussi son rôle de Cedric Diggory dans le 4e opus de la saga Harry Potter, Harry Potter et la Coupe de feu (2005). Par la suite, il s\'investit dans des films indépendants réalisés par des cinéastes reconnus : Cosmopolis (2012) et Maps to the Stars (2014), réalisés par David Cronenberg ; The Rover (2014) et The King (2019), de David Michôd ; Queen of the Desert (2014), de Werner Herzog ; Life (2015), d\'Anton Corbijn ; L\'Enfance d\'un chef (2016), de Brady Corbet ; The Lost City of Z (2016), de James Gray ; Good Time (2017), de Ben et Josh Safdie ou encore High Life (2018), de Claire Denis.'},
    
    'RobertRedford' : {'description': 'Charles Robert Redford, Jr., dit Robert Redford, né le 18 août 1936 à Santa Monica (Californie), est un acteur, réalisateur et producteur américain. En 1969, il se fait connaître grâce au western Butch Cassidy et le Kid. Il confirme son ascension avec des films tels que Les Hommes du président, L\'Arnaque, Gatsby le Magnifique, Out of Africa et L\'Homme qui murmurait à l\'oreille des chevaux. En 1981, il remporte l\'Oscar du meilleur réalisateur pour le film Des gens comme les autres, ainsi qu\'un Oscar d\'honneur en 2002 pour l\'ensemble de sa carrière.'},
    
    'SelenaGomez' : {'description': 'Selena Gomez, née le 22 juillet 1992 à Grand Prairie, au Texas, est une chanteuse, actrice et productrice américaine. Elle fait ses débuts de comédienne dans la série pour enfants Barney & Friends (2002-2004), puis se fait connaître du jeune public en interprétant le rôle d\'Alex Russo dans la série humoristique de Disney Channel, Les Sorciers de Waverly Place (2007-2012). Elle joue ensuite dans de nombreux films ou téléfilms tels que Comme Cendrillon 2 (2008), Princess Protection Program (2009), Sœurs malgré elles (Ramona et Beezus, 2010), Bienvenue à Monte-Carlo (2011), Spring Breakers (2012), Getaway (2013) et The Fundamentals of Caring (2016). Elle interprète par ailleurs la voix du personnage Mavis dans les films d\'animation de la franchise Hôtel Transylvanie.'},
}