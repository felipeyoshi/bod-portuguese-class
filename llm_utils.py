import openai

class LLM:
    def __init__(self, api_key):
        openai.api_key = api_key

    # Function to generate text with context
    def generate_text_with_context(self, conversation_history, prompt):
        # Append the new prompt to the conversation history
        conversation_history.append({"role": "user", "content": prompt})
        
        # Generate response
        response = openai.chat.completions.create(
            model="gpt-4o",
            messages=conversation_history
        )

        # Extract and save the response
        message = response.choices[0].message.content
        conversation_history.append({"role": "assistant", "content": message})
        return message, conversation_history

    # Function to generate image
    def generate_image(self, prompt, artist):
        prompt_image = [{"role": "user", "content": f"Create a short image prompt themed colors and style of {artist}, for the following text. Do not generate the main character, just the scene. " + prompt}]
        
        # Generate prompt image
        response_text = openai.chat.completions.create(
            model="gpt-4o",
            messages=prompt_image
        )

        # Generate image
        response_image = openai.images.generate(
            model="dall-e-3",
            prompt=response_text.choices[0].message.content,
            size="1024x1024",
            quality="standard",
            n=1,
        )
        
        # Extract and save the response and the image
        message = response_text.choices[0].message.content
        image_url = response_image.data[0].url
        return image_url, message