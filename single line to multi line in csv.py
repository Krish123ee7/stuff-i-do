# single line data into multiple line data

# Sample data
# apple, banana, orange, grape, kiwi, mango, strawberry, blueberry, raspberry, blackberry, lemon, lime, pineapple, coconut, avocado, tomato, cucumber, carrot, potato, onion, garlic, ginger, turmeric, chili pepper, bell pepper, green bean, broccoli, cauliflower, spinach, kale, lettuce, zucchini, eggplant, mushroom, asparagus, peas, corn, beans, lentils, rice, pasta, bread, pizza, burger, hotdog, sandwich, taco, burrito, sushi, ramen, curry, stir-fry, soup, salad, breakfast, lunch, dinner, snack, dessert, cake, cookie, pie, ice cream, chocolate, candy, gum, popcorn, chips, nuts, seeds, fruit, vegetable, meat, fish, seafood, dairy, grain, cereal, yogurt, cheese, butter, milk, water, juice, soda, coffee, tea, alcohol, wine, beer, liquor, book, magazine, newspaper, novel, story, poem, essay, article, report, letter, email, text message, phone call, video call, meeting, conference, seminar, workshop, class, school, college, university, job, career, work, hobby, interest, passion, love, hate, anger, sadness, joy, happiness, excitement, surprise, fear, worry, hope, dream, ambition, goal, plan, decision, choice, change, opportunity, challenge, problem, solution, success, failure, victory, defeat, competition, game, sport, exercise, fitness, health, wellness, beauty, fashion, style, art, music, dance, theater, film, television, movie, show, game, app, software, technology, computer, internet, website, social media, smartphone, tablet, laptop, desktop, gadget, device, tool, machine, robot, animal, pet, dog, cat, horse, rabbit, guinea pig, hamster, bird, fish, reptile, amphibian, insect, bug, spider, worm, snake, lizard, frog, toad, turtle, crocodile, alligator, shark, dolphin, whale, bear, lion, tiger, leopard, cheetah, elephant, giraffe, zebra, monkey, gorilla, chimpanzee, orangutan, panda, koala, kangaroo, raccoon, fox, squirrel, deer, elk, moose, bison, buffalo, goat, sheep, pig, cow, chicken, duck, goose, turkey, eagle, hawk, owl, dove, pigeon, parrot, canary, finch, hummingbird, butterfly, moth, bee, wasp, ant, termite, grasshopper, cricket, beetle, fly, mosquito, flea, tick, lice, bedbug, cockroach, scorpion, centipede, millipede, worm, slug, snail, clam, oyster, mussel, crab, lobster, shrimp, squid, octopus, jellyfish, starfish, coral, sponge, plankton, algae, bacteria, virus, fungus, plant, tree, flower, grass, weed, shrub, vine, bush, cactus, fern, moss, lichen, mushroom, mold, yeast, bacteria, virus, fungus, rock, stone, mineral, crystal, gem, fossil, meteorite, comet, asteroid, star, planet, moon, sun, galaxy, universe, space, time, matter, energy, force, field, wave, particle, atom, molecule, compound, element, substance, material, object, thing, idea, concept, thought, feeling, emotion, sensation, perception, experience, memory, knowledge, skill, ability, talent, gift, quality, characteristic, trait, attribute, feature, aspect, side, part, piece, portion, bit, chunk, scrap, remnant, vestige, trace, hint, suggestion, implication, inference, deduction, conclusion, assumption, guess, estimate, approximation, calculation, computation, measurement, evaluation, assessment, judgment, decision, choice, selection, preference, option, alternative, possibility, probability, chance, likelihood, odds, fate, destiny, fortune, luck, serendipity, coincidence, accident, incident, event, occurrence, happening, affair, business, deal, transaction, agreement, contract, arrangement, understanding, promise, commitment, obligation, responsibility, duty, task, chore, errand, job, assignment, project, undertaking, venture, enterprise, endeavor, pursuit, activity, occupation, profession, vocation, calling, mission, purpose, meaning, significance, importance, value, worth, price, cost, expense, outlay, investment, return, profit, gain, loss, damage, harm, injury, hurt, pain, suffering, agony, torture, misery, distress, sorrow, grief, sadness, melancholy, gloom, despair, hopelessness, helplessness, powerlessness, weakness, infirmity, disability, handicap, limitation, constraint, restriction, boundary, limit, curb, check, rein, control, regulation, rule, law, order, system, structure, organization, hierarchy, chain, network, web, link, connection, relationship, association, alliance, partnership, cooperation, collaboration, teamwork, synergy

f_name = input("enter file name/location ")
while f_name[-4:] != ".csv":
    print(f_name[-4:])
    if f_name[-4:] == ".csv":
        break
    f_name = input("enter file name/location ")
    

file = open(f_name,'r')
data = file.read().split(', ')
file.close()
print(len(data))

col_no = int(input("enter number of columns/fields "))
while len(data)% col_no != 0:
    print("Error: no. of columns is npt compatable with data")
    col_no = int(input("enter number of columns/fields "))
    if len(data)% col_no == 0:
        break

file = open(f_name, 'w')
new_data = ''
var =1
for cell in data:
    
    if var < col_no:
        new_data = new_data + cell + ','
        var = var + 1
        print("working")
    elif var == col_no:
        new_data = new_data + cell + "\n"
        var = 1
    print(var,cell)

file.write(new_data)
file.close()
