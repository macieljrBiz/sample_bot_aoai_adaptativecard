# sample_bot_aoai_adaptativecard

Demonstrate the core capabilities of the Microsoft Bot Framework

This bot has been created using [Bot Framework](https://dev.botframework.com), it shows how to create a simple bot that accepts input from the user and echoes it back.

Also, it demonstrates hot to integrate it with AOAI endpoint as well as the use of AdaptativeCards to format bot's responses.

## Prerequisites

This sample **requires** prerequisites in order to run.

### Install Python 3.6

## Set environment variables
- This code uses some variables in the .env file that needs to be set
- For security, copy the .env file as DEBUG.env file (make sure it's not commited to your versioning control). This helps to mantain your endpoint information private on development environment.
- ONLY use the default .env file on production (starting the app without the "--debug" flag).
- The variables is:
   - `ENDPOINT_URL` your Azure OpenAI published endpoint
   - `DEPLOYMENT_NAME` the name you created for the model you published you want to use
   - `API_VERSION` the API version you want to use. At the time of the creation of this code, the recommended version was: '2024-05-01-preview'
   - `CHAT_ADAPTATIVE_CARD_IMAGE_URL` the URL of an image (190x74 recommended) used as the bot's signature in the chat's adaptative card.

## Set Managed Identity permissions
- This code implements Managed Identity to avoid the insecure transit of keys
- Check this reference to implement: [How to configure Azure OpenAI Service with Microsoft Entra ID authentication](https://learn.microsoft.com/en-us/azure/ai-services/openai/how-to/managed-identity)

## Running the sample
- Run `pip install -r requirements.txt` to install all dependencies
- Run `python app.py --debug`

## Testing the bot using Bot Framework Emulator

[Bot Framework Emulator](https://github.com/microsoft/botframework-emulator) is a desktop application that allows bot developers to test and debug their bots on localhost or running remotely through a tunnel.

- Install the Bot Framework Emulator version 4.3.0 or greater from [here](https://github.com/Microsoft/BotFramework-Emulator/releases)

### Connect to the bot using Bot Framework Emulator

- Launch Bot Framework Emulator
- Enter a Bot URL of `http://localhost:3978/api/messages`

### Testing with Teams

- Publish this code using some preffered service for [continuous integration on Azure and GitHub](https://learn.microsoft.com/pt-br/azure/bot-service/bot-service-build-continuous-deployment?view=azure-bot-service-4.0). If you domain the related security risks and concerns, you can make use of services like [ngrok](https://ngrok.com) just for testing purposes.
- [Set up the Bot Service](https://learn.microsoft.com/en-us/azure/bot-service/bot-service-quickstart-registration?view=azure-bot-service-4.0&tabs=userassigned) and configure the Teams channel.


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