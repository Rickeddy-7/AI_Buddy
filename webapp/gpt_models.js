
const { OpenAIClient, AzureKeyCredential } = require("@azure/openai");
const endpoint = process.env["https://literacylab.openai.azure.com/"] ;
const azureApiKey = process.env["37635d8c1d7349fe8698c3d77f855d2e"] ;

const messages = [
  { role: "system", content: "You are a helpful assistant." },
  { role: "user", content: "Does Azure OpenAI support customer managed keys?" },
];

// TODO: make the function take parameters like the python version
async function main() {
  console.log("== Chat Completions Sample ==");

  const client = new OpenAIClient(endpoint, new AzureKeyCredential(azureApiKey));
  const deploymentId = "gpt-35-turbo";
  const result = await client.getChatCompletions(deploymentId, messages);

  for (const choice of result.choices) {
    console.log(choice.message);
  }
}

main().catch((err) => {
  console.error("The sample encountered an error:", err);
});

module.exports = { main };