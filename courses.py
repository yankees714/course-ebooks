from markov import MarkovChainer
import string


# courses = ["Anthropologists have long been fascinated with defining who is related to whom. Students read works by leading anthropologists to gain an understanding of the various ways kinship has been defined in anthropology and in a diversity of cultures. Elucidates various kinship systems throughout the world and explores how anthropologists have worked with the concept of relatedness. Examines contemporary issues and discusses current kinship studies of relatedness and how those apply to new reproductive technologies such as surrogate mothers, in vitro fertilization, the buying and selling of eggs and sperm, and the legal implications of these new ways of having children.",
# "An introduction to economic analysis and institutions, with special emphasis on the allocation of resources through markets. The theory of demand, supply, cost, and market structure is developed and then applied to problems in antitrust policy, environmental quality, energy, education, health, the role of the corporation in society, income distribution, and poverty. Students desiring a comprehensive introduction to economic reasoning should take both Economics 1101 101 and 1102 102.",
# "Seminar. Standard economics (i.e., neoclassical economics) assumes that individuals are self-interested, rational actors, who optimize well-defined, stable objective functions. Behavioral economics is the study of systematic departures from these assumptions, and the implications for economic outcomes. Topics include errors in information-processing and belief formation, behavioral choice under uncertainty (loss aversion, reference dependence), time inconsistent behavior (self-control problems), and social preferences (altruism, fairness and reciprocity).",
# "Cultural anthropology explores the diversities and commonalities of cultures and societies in an increasingly interconnected world. Introduces students to the significant issues, concepts, theories, and methods in cultural anthropology. Topics may include cultural relativism and ethnocentrism, fieldwork and ethics, symbolism, language, religion and ritual, political and economic systems, family and kinship, gender, class, ethnicity and race, nationalism and transnationalism, and ethnographic representation and validity.",
# "Uses archaeology to explore the experience of Africans and their descendants in the Atlantic World from the fifteenth century onward. Examines archaeological sites in Africa, the New World, and the Atlantic islands that are implicated in the trans-Atlantic slave trade and in other forms of interaction between African and non-African communities. Particular topics to be explored will include comparisons between archaeological and historical documentation, archaeological evidence for domination and resistance, and the material traces of cultural contacts and hybridity."
# "Explores the American Civil War through an examination of popular films dedicated to the topic. Students analyze films as a representation of the past, considering not simply their historical subject matter, but also the cultural and political contexts in which they are made. Films include The Birth of a Nation, Gone with the Wind, Glory, and Cold Mountain. Weekly evening film screenings.",
# "Explores the ways in which the idea of American freedom has been defined both with and against slavery through readings of legal and literary texts. Students come to terms with the intersections between the political, literary, and historical concept of freedom and its relation to competing definitions of American citizenship.",
# "Examines issues of racism in the United States, with attention to the social psychology of racism, its history, its relationship to social structure, and its ethical and moral implications.",
# "Explores how Christianity, Islam, and indigenous African religious beliefs shaped the formation of West African states from the nineteenth century Islamic reformist movements and mission Christianity, to the formation of modern nation-states in the twentieth century. While the course provides a broad regional West African overview, we will focus careful attention on how religious themes shaped the communities of the Nigerian region--a critical West African region where Christianity and Islam converged to transform a modern state and society. Drawing on primary and secondary historical texts as well as Africanist works in sociology and comparative politics, this Nigerian experience will illuminate broader West African, African, and global perspectives that underscore the historical significance of religion in politics and society, especially in non-Western contexts."
# "Explores rich traditions of African American humor in fiction, comics, graphic narratives, and film. Considers strategies of cultural survival and liberation, as well as folkloric sources, trickster storytellers, comic double-voicing, and the lampooning of racial ideologies. Close attention paid to modes of burlesque, satirical deformation, caricature, tragicomedy, and parody in historical and contemporary contexts, including such writers and performers as Charles Chesnutt, Bert Williams, Langston Hughes, Zora Neale Hurston, Richard Pryor, Ishmael Reed, Aaron McGruder, Dave Chappelle, and Suzan-Lori Parks. Note: This course fulfills the literature of the Americas requirement for English majors.",
# ]

f = open("courses.txt","r")
descriptions = f.read()


a = MarkovChainer(2)

a.add_text(descriptions)

#print a.beginnings

generated_description = a.generate_sentence()
while len(generated_description) < 100:
	generated_description = a.generate_sentence()

print generated_description



