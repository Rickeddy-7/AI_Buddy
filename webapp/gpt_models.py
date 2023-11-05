
import openai

openai.api_type = "azure"
openai.api_version = "2023-05-15"
openai.api_key = "37635d8c1d7349fe8698c3d77f855d2e"
openai.api_base = "https://literacylab.openai.azure.com/"


def use_gpt(role: str, prompt: str):
    '''the general version of the model where the user gives personal prompts and the
        model responds as instructed(specified by role)'''
    
    response = openai.ChatCompletion.create(
        engine="literacylab",
        messages=[
            {"role": "system", "content": f"{role}"},
            {"role": "user", "content": f"{prompt}"}
        ]
    )
    return response['choices'][0]['message']['content']


role = "you are a grade four english teacher who is friendly and helpful"
prompt = """generate a fun and interesting story of about 4/5 paragraphs for the student and thereafter
            generate ten quesions along with their answers to test their understanding."""
# response = use_gpt(role, prompt)
# print(f'GPT >> {response}')
