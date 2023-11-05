
from gpt_models import use_gpt
import random

questions = [
    "What did Lily find in the woods near her house?",
    "What happened when Lily touched the leaves of the tree?",
    "What creatures did Lily befriend in the woods?",
    "What did Lily have to do to return to her normal size?",
    "How did Lily feel after she grew back to her natural size?",
    "What kind of creature was on its way to becoming a butterfly?",
    "Why did Lily have to leave her new friends in the woods?",
    "Who showed Lily how to reverse the spell and grow back to her normal size?",
    "What did Lily learn from her experience in the woods?",
    "What was the name of the magical tree that Lily had to find?"
]

answers = [
    "She found a magical tree with shimmering leaves.",
    "She shrunk down to the size of a ladybug.",
    "She became friends with ants and a caterpillar.",
    "She had to eat a berry from the tree of life.",
    "She had a newfound appreciation for the world around her.",
    "A caterpillar.",
    "She knew she had to find a way back to her normal size.",
    "A fairy who lived in the woods.",
    "She learned to appreciate the world around her and the creatures that live in it.",
    "The tree of life."
]

affirmations = ["Correct, keep going!", "Nice one!", "Excellent!", "You're on fire!"]

def play_game():
    '''one of the features under the literacy lab'''

    role = """you are tasked with checking wether two statments are the same or not. If they are the similar, respond with just 'true'
        else 'false'. Ignore the case and focus on the gist of the statement"""
    
    print("Read the following story and answer the questions that follow:\n\n")
    read_story_from_file()
    
    while(True):
        for i in range(len(questions)):
            user_ans = input(questions[i])
            prompt = f"Is '{user_ans}' similar to '{answers[i]}' ?'"
            result: str = use_gpt(role, prompt)
            print(result.upper())
            while not (result.lower()[:4] == 'true'):
                print("Not quite, try again\n")
                user_ans = input(questions[i])
                prompt = f"Is '{user_ans}' similar to '{answers[i]}' ?'"
                result: str = use_gpt(role, prompt)
            else:
                print(random.choice(affirmations) + '\n')
                continue
        
        print("Great Work. You have shown a brilliant understanding of the short story!!")
        break


def read_story_from_file():
    '''opens the txt files that contains the comprehension text'''

    with open('webapp/story.txt') as file:
        print(file.readlines())
