import openai
openai.api_key = "your api key"  #give your api key for smooth running
def generate_story(prompt):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful assistant that generates stories."},
                {"role": "user", "content": prompt}
            ],
            max_tokens=500
        )
        story = response['choices'][0]['message']['content']
        return story
    except Exception as e:
        print(f"An error occurred while generating the story: {e}")
        return None
def save_story_to_file(story, filename="story.txt"):
    try:
        with open(filename, 'w') as file:
            file.write(story)
        print(f"Story successfully saved to {filename}")
    except IOError as e:
        print(f"An error occurred while writing to the file: {e}")
def main():
    prompt = input("Enter a prompt for the story: ")
    story = generate_story(prompt)
    if story:
        print("\nGenerated Story:\n")
        print(story)
        save_story_to_file(story)
    else:
        print("Failed to generate the story.")
if __name__ == "__main__":
    main()

#it uses the model chatgpt-3.5 turbo latest to work but has limits
#The API key can be received by OpenAI platform 
