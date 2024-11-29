# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License.

import os
from openai import AzureOpenAI
from azure.identity import DefaultAzureCredential, get_bearer_token_provider

from botbuilder.core import ActivityHandler, TurnContext
from botbuilder.schema import ChannelAccount, Attachment, Activity, ActivityTypes

from adaptivecards.adaptivecard import AdaptiveCard
from adaptivecards.elements import TextBlock, Image
from adaptivecards.containers import Container

class MyBot(ActivityHandler):
    # See https://aka.ms/about-bot-activity-message to learn more about the message and other activity types.

    # custom code to interact with azure openai endpoint
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.chat_image = os.getenv("CHAT_ADAPTATIVE_CARD_IMAGE_URL")
        self.openai_endpoint = os.getenv("ENDPOINT_URL")
        self.openai_deployment = os.getenv("DEPLOYMENT_NAME")
        self.openai_api_version = os.getenv("API_VERSION")
        token_provider = get_bearer_token_provider(  
            DefaultAzureCredential(logging_enable=True),  
            "https://cognitiveservices.azure.com/.default"  
        ) 
        self.client = AzureOpenAI(  
          azure_endpoint=self.openai_endpoint,  
          azure_ad_token_provider=token_provider,  
          api_version=self.openai_api_version
        ) 

    # method to be consumed by on_message_activity to interact with azure openai endpoint
    async def __get_openai_response(self, user_messasge: str):
        completion = self.client.chat.completions.create(  
            model=self.openai_deployment,  
            messages=[{"role": "user", "content": user_messasge}],  
            max_tokens=800,  
            temperature=0.7,  
            top_p=0.95,  
            frequency_penalty=0,  
            presence_penalty=0,  
            stop=None,  
            stream=False  
        ) 
        return completion.choices[0].message.content
    
    async def __generate_adaptivecard_json(self, cardtext: str):
        card = AdaptiveCard()
        card.body = [
            Container(items=[
                TextBlock(text=cardtext, font_type='Default', size='Medium'),
                Image(url=self.chat_image, size='Large', alt_text='UPBI Logo')
            ])
        ]
        return card

    async def on_message_activity(self, turn_context: TurnContext):
        openai_response = await self.__get_openai_response(turn_context.activity.text)
        # adaptive_card_content = await self.__generate_adaptivecard_json(openai_response)
        adaptive_card_content = {
            "type": "AdaptiveCard",
            "body": [
                {
                    "type": "TextBlock",
                    "text": openai_response,
                    "size": "Medium",
                    "weight": "Bolder",
                    "wrap": True
                },
                {
                    "type": "Image",
                    "url": self.chat_image,  # Replace with your image URL
                    "size": "Large",
                    "altText": "UPBI logo"
                }
            ],
            "$schema": "http://adaptivecards.io/schemas/adaptive-card.json",
            "version": "1.3"
        }

        # Create the Adaptive Card attachment
        attachment = Attachment(
            content_type="application/vnd.microsoft.card.adaptive",
            content=adaptive_card_content
        )

        # Create an Activity to send the attachment
        activity = Activity(
            type=ActivityTypes.message,
            attachments=[attachment]
        )

        # Send the message activity to the user
        await turn_context.send_activity(activity)
        # await turn_context.send_activity(openai_response)
        # await turn_context.send_activity(f"You said '{turn_context.activity.text}'")

    async def on_members_added_activity(
        self,
        members_added: ChannelAccount,
        turn_context: TurnContext
    ):
        for member_added in members_added:
            if member_added.id != turn_context.activity.recipient.id:
                await turn_context.send_activity("Hello and welcome!")

