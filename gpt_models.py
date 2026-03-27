from openai import OpenAI
import openai
import config

GPT_MODEL = "gpt-5.4-nano"

def generate_text(prompt, max_tokens, temperature):
    response = client.responses.create(
        model=GPT_MODEL,
        input=prompt,
        max_output_tokens=max(max_tokens, 16),  # Responses API requires >= 16
        temperature=temperature,
    )
    return response.output_text.strip()

def text_summarizer(prompt):
    response = client.responses.create(
        model=GPT_MODEL,
        input=[
            {
                "role": "system",
                "content": "You will be provided with a block of text, and your task is to extract a list of keywords from it."
            },
            {
                "role": "user",
                "content": "A flying saucer seen by a guest house, a 7ft alien-like figure coming out of a hedge and a \"cigar-shaped\" UFO near a school yard.\n\nThese are just some of the 450 reported extraterrestrial encounters from one of the UK's largest mass sightings in a remote Welsh village.\n\nThe village of Broad Haven has since been described as the \"Bermuda Triangle\" of mysterious craft sightings and sightings of strange beings.\n\nResidents who reported these encounters across a single year in the late seventies have now told their story to the new Netflix documentary series 'Encounters', made by Steven Spielberg's production company.\n\nIt all happened back in 1977, when the Cold War was at its height and Star Wars and Close Encounters of the Third Kind - Spielberg's first science fiction blockbuster - dominated the box office."
            },
            {
                "role": "assistant",
                "content": "flying saucer, guest house, 7ft alien-like figure, hedge, cigar-shaped UFO, school yard, extraterrestrial encounters, UK, mass sightings, remote Welsh village, Broad Haven, Bermuda Triangle, mysterious craft sightings, strange beings, residents, single year, late seventies, Netflix documentary series, Steven Spielberg, production company, 1977, Cold War, Star Wars, Close Encounters of the Third Kind, science fiction blockbuster, box office."
            },
            {
                "role": "user",
                "content": "Each April, in the village of Maeliya in northwest Sri Lanka, Pinchal Weldurelage Siriwardene gathers his community under the shade of a large banyan tree..."
            },
            {
                "role": "assistant",
                "content": "April, Maeliya, northwest Sri Lanka, Pinchal Weldurelage Siriwardene, banyan tree, wewa, reservoir, tank, Sinhala, rice paddies, agrarian committee, coconut milk, blessings, harvest, irrigation canals, farmers, village life, pagoda, temple."
            },
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=0.5,
        max_output_tokens=256, 
    )
    return response.output_text.strip()

def poetic_chatbot(prompt):
    response = client.responses.create(
        model=GPT_MODEL,
        input = [
            {
                "role": "system",
                "content": "You are a poetic chatbot."
            },
            {
                "role": "user",
                "content": "When was Google founded?"
            },
            {
                "role": "assistant",
                "content": "In the late '90s, a spark did ignite, Google emerged, a radiant light. By Larry and Sergey, in '98, it was born, a search engine new, on the web it was sworn."
            },
            {
                "role": "user",
                "content": "Which country has the youngest president?"
            },
            {
                "role": "assistant",
                "content": "Ah, the pursuit of youth in politics, a theme we explore. In Austria, Sebastian Kurz did implore, at the age of 31, his journey did begin, leading with vigor, in a world filled with din."
            },
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature = 1,
        
    )
    return response.output_text.strip()

if __name__ == "__main__":
    
    client = OpenAI(api_key=config.gpt_api_key)

    # generated_text_prompt = "Once upon a time"
    # generated_text = generate_text(generated_text_prompt, 50, 0)
    # print("\nprompt: ", generated_text_prompt, "\ngenerated_text: ", generated_text)

    # summarized_text_prompt = "Master Reef Guide Kirsty Whitman didn't need to tell me twice. Peering down through my snorkel mask in the direction of her pointed finger, I spotted a huge male manta ray trailing a female in perfect sync – an effort to impress a potential mate, exactly as Whitman had described during her animated presentation the previous evening. Having some knowledge of what was unfolding before my eyes on our snorkelling safari made the encounter even more magical as I kicked against the current to admire this intimate undersea ballet for a few precious seconds more."
    # summarized_text = text_summarizer(summarized_text_prompt)
    # print("\nprompt: ", summarized_text_prompt, "\nsummarized_text: ", summarized_text)

poetic_chatbot_prompt = "When was cheese first made?"
poetic_chatbot_text = poetic_chatbot(poetic_chatbot_prompt)
print("\nprompt: ", poetic_chatbot_prompt, "\npoetic_chatbot_text: ", poetic_chatbot_text)