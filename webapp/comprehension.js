const questions = [
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
];

const answers = [
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
];

const affirmations = ["Correct, keep going!", "Nice one!", "Excellent!", "You're on fire!"];

function playGame() {
    /* one of the features under the literacy lab */

    const role = "you are tasked with checking whether two statements are the same or not. If they are similar, respond with just 'true', else 'false'. Ignore the case and focus on the gist of the statement";

    console.log("Read the following story and answer the questions that follow:\n\n");
    readStoryFromFile();

    while (true) {
        for (let i = 0; i < questions.length; i++) {
            const userAns = prompt(questions[i]);
            const prompt = `Is '${userAns}' similar to '${answers[i]}' ?`;
            const result = useGpt(role, prompt);
            console.log(result.toUpperCase());
            while (!(result.toLowerCase().substring(0, 4) === 'true')) {
                console.log("Not quite, try again\n");
                const userAns = prompt(questions[i]);
                const prompt = `Is '${userAns}' similar to '${answers[i]}' ?`;
                const result = useGpt(role, prompt);
            }
            console.log(affirmations[Math.floor(Math.random() * affirmations.length)] + '\n');
            continue;
        }

        console.log("Great Work. You have shown a brilliant understanding of the short story!!");
        break;
    }
}

function readStoryFromFile() {
    /* opens the txt files that contain the comprehension text */
    console.log("Simulated read story from file.");
}

function useGpt(role, prompt) {
    /* Simulated use of GPT model */
    const randomBool = Math.random() < 0.5;
    return randomBool ? 'true' : 'false';
}

playGame();
