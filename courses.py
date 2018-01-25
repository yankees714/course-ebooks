from markov import MarkovChainer


#source = "./courses.txt"
source = "./spring2014.txt"

generator = MarkovChainer(2)
with open(source) as f:
    generator.add_text(f.read())

generated_description = generator.generate_sentence()
while len(generated_description) < 100:
	generated_description = generator.generate_sentence()

print generated_description
