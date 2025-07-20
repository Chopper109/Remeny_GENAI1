# quick_ai.py

from transformers import pipeline

print("--- Initializing Generative AI ---")
print("This will download a small pre-trained model (distilgpt2) if not already cached.")

# Use the 'text-generation' pipeline for easy text generation.
# 'distilgpt2' is a smaller, faster version of GPT-2, suitable for quick local use.
# IMPORTANT: This model is a text GENERATOR, not a factual question-answering system.
# It completes prompts based on patterns, it does not retrieve facts.
generator = pipeline('text-generation', model='distilgpt2')

print("\n--- AI Ready! ---")
print("Type your questions or prompts below. Type 'exit' to quit.")
print("-" * 30)

while True:
    user_input = input("\nYou: ")
    if user_input.lower() == 'exit':
        print("AI: Goodbye!")
        break

    # Generate text based on user input
    # max_new_tokens: How many new words the AI should generate.
    # num_return_sequences: How many different responses to generate.
    # do_sample: If True, uses sampling for more creative text; if False, uses greedy decoding.
    # temperature: Controls randomness (higher = more random, lower = more deterministic).
    # top_k: Considers only the top_k most probable words for sampling.
    # no_repeat_ngram_size: Prevents repeating n-grams (sequences of words) to avoid repetitive output.
    try:
        generated_responses = generator(
            user_input,
            max_new_tokens=30, # Reduced from 50 to make responses potentially shorter and more focused
            num_return_sequences=1, # Get one response
            do_sample=True, # Use sampling for more varied responses
            temperature=0.6, # Slightly reduced from 0.7 for less randomness, potentially more coherent output
            top_k=50, # Consider top 50 words for sampling
            no_repeat_ngram_size=2 # Avoid repeating 2-word sequences
        )

        # Print the generated text
        # The pipeline returns a list of dictionaries, each with 'generated_text'
        for i, response in enumerate(generated_responses):
            full_text = response['generated_text']
            # The generated text includes the prompt, so we might want to clean it up
            # For simplicity, we'll just print the full generated text for now
            # In a real app, you'd parse out the new content.
            print(f"AI: {full_text.strip()}")

    except Exception as e:
        print(f"AI: An error occurred during generation: {e}")
        print("Please try again or restart the script.")

print("-" * 30)
print("Script finished.")
