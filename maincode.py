# Hashtag Generator using OpenAI's ChatGPT API

import openai

def generate_hashtags(prompt, api_key):
    """
    Generate hashtags based on a given prompt using OpenAI's API.

    Args:
        prompt (str): The content or topic for which hashtags are to be generated.
        api_key (str): Your OpenAI API key.

    Returns:
        list: A list of generated hashtags.
    """
    openai.api_key = api_key

    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful assistant that generates relevant hashtags."},
                {"role": "user", "content": f"Generate 10 trending and relevant hashtags for: {prompt}"}
            ]
        )

        # Extract the hashtags from the response
        hashtags_text = response['choices'][0]['message']['content']
        hashtags = [tag.strip() for tag in hashtags_text.split("\n") if tag.startswith("#")]
        return hashtags

    except Exception as e:
        print(f"Error: {e}")
        return []

# Example usage
if __name__ == "__main__":
    API_KEY = "your_openai_api_key_here"  # Replace with your actual API key
    topic = "Digital Marketing Trends 2025"

    print("Generating hashtags...")
    generated_hashtags = generate_hashtags(topic, API_KEY)

    if generated_hashtags:
        print("\nGenerated Hashtags:")
        for hashtag in generated_hashtags:
            print(hashtag)
    else:
        print("No hashtags were generated. Please check your API key and input.")
