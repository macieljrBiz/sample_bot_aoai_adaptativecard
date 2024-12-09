# sample_bot_aoai_adaptivecard

Demonstrate the core capabilities of the Microsoft Bot Framework connected with an AOAI (Azure Open AI) Service, to implement a chat with the LLM of choice and demonstrate the usage of AdaptiveCards for chat output formatting.

This bot has been created using [Bot Framework](https://dev.botframework.com). Originally, it shows how to create a simple bot that accepts input from the user and echoes it back. This one is modified to implement answers from an LLM like AOAI GPT instead. The original code is preserved but commented out.

## Prerequisites

This sample **requires** prerequisites in order to run.

### Install Python 3.6

## Deploy an AOAI resource and a suitable model
- Deploy a model such as GPT-4, GPT-4o, GPT-4o-mini, etc.

## Set environment variables
- This code uses some variables in the .env file that need to be set.
- For security, copy the .env file as DEBUG.env file (make sure it's not committed to your version control). This helps to maintain your endpoint information private in the development environment.
- ONLY use the default .env file in production (starting the app without the "--debug" flag).
- The variables are:
   - `ENDPOINT_URL` your chosen Azure OpenAI endpoint (such as: https://aoai-deploy-name.openai.azure.com)
   - `DEPLOYMENT_NAME` the name you created for the deployed model you want to use (such as gpt-4o-mini)
   - `API_VERSION` the deploy's API version (such as: 2024-05-01-preview)
   - `CHAT_ADAPTIVE_CARD_IMAGE_URL` the URL of an image (190x74 recommended) used as the bot's signature in the chat's adaptive card.

## Set Managed Identity (MI) permissions
- This code implements Managed Identity to avoid the insecure transit of keys.
- The Managed Identity in this code is used to implement authentication to AOAI without needing to pass an API key.
- The code is already as it needs to be. No implementation required, but you need to perform configurations at the Azure Portal to make it work.
- Check this reference to implement: [How to configure Azure OpenAI Service with Microsoft Entra ID authentication](https://learn.microsoft.com/en-us/azure/ai-services/openai/how-to/managed-identity)
- Basically, you need to create an MI, go to AOAI IAM, add "Cognitive Services OpenAI User" access to your user on it, and authenticate with the Azure CLI (`az login`) with that user before running the code.

## Running the sample
- Run `pip install -r requirements.txt` to install all dependencies.
- Run `python app.py --debug`.

## Testing the bot using Bot Framework Emulator

[Bot Framework Emulator](https://github.com/microsoft/botframework-emulator) is a desktop application that allows bot developers to test and debug their bots on localhost or running remotely through a tunnel.

- Install the Bot Framework Emulator version 4.3.0 or greater from [here](https://github.com/Microsoft/BotFramework-Emulator/releases).

### Connect to the bot using Bot Framework Emulator

- Launch Bot Framework Emulator.
- Enter a Bot URL of `http://localhost:3978/api/messages`.

### Further reading

- [Bot Framework Documentation](https://docs.botframework.com)
- [Bot Basics](https://docs.microsoft.com/azure/bot-service/bot-builder-basics?view=azure-bot-service-4.0)
- [Dialogs](https://docs.microsoft.com/azure/bot-service/bot-builder-concept-dialog?view=azure-bot-service-4.0)
- [Gathering Input Using Prompts](https://docs.microsoft.com/azure/bot-service/bot-builder-prompts?view=azure-bot-service-4.0&tabs=csharp)
- [Activity processing](https://docs.microsoft.com/en-us/azure/bot-service/bot-builder-concept-activity-processing?view=azure-bot-service-4.0)
- [Azure Bot Service Introduction](https://docs.microsoft.com/azure/bot-service/bot-service-overview-introduction?view=azure-bot-service-4.0)
- [Azure Bot Service Documentation](https://docs.microsoft.com/azure/bot-service/?view=azure-bot-service-4.0)
- [Azure CLI](https://docs.microsoft.com/cli/azure/?view=azure-cli-latest)
- [Azure Portal](https://portal.azure.com)
- [Language Understanding using LUIS](https://docs.microsoft.com/azure/cognitive-services/luis/)
- [Channels and Bot Connector Service](https://docs.microsoft.com/azure/bot-service/bot-concepts?view=azure-bot-service-4.0)
