from markov import MarkovChainer

#https://prod-ssb-vip-prod.bowdoin.edu/prod/bzskfcls.P_GetCrse_Advanced
f = open("courses.txt","r")
descriptions = f.read()

generator = MarkovChainer(2)
generator.add_text(descriptions)

generated_description = generator.generate_sentence()
while len(generated_description) < 100:
	generated_description = generator.generate_sentence()

print generated_description