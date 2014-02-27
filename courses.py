from markov import MarkovChainer

#source = "./courses.txt"
source = "./spring2014.txt"

f = open(source,"r")
descriptions = f.read()
f.close()

generator = MarkovChainer(2)
generator.add_text(descriptions)

generated_description = generator.generate_sentence()
while len(generated_description) < 100:
	generated_description = generator.generate_sentence()

print generated_description
