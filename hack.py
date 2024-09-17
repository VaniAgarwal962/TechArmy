pip install --upgrade google-cloud-aiplatform
!gcloud auth application-default login


##############Implement user interaction for chatbot########################################

import base64
import vertexai
from vertexai.generative_models import GenerativeModel, Part, SafetySetting
def generate():
    vertexai.init(project="ABC", location="us-central1")
    model = GenerativeModel(
        "gemini-1.5-flash-001",
    )
    responses = model.generate_content(
        ["""Implement user interaction for chatbot"""],
        generation_config=generation_config,
        safety_settings=safety_settings,
        stream=True,
    )

    for response in responses:
        print(response.text, end="")


generation_config = {
    "max_output_tokens": 8192,
    "temperature": 1,
    "top_p": 0.95,
}

safety_settings = [
    SafetySetting(
        category=SafetySetting.HarmCategory.HARM_CATEGORY_HATE_SPEECH,
        threshold=SafetySetting.HarmBlockThreshold.BLOCK_MEDIUM_AND_ABOVE
    ),
    SafetySetting(
        category=SafetySetting.HarmCategory.HARM_CATEGORY_DANGEROUS_CONTENT,
        threshold=SafetySetting.HarmBlockThreshold.BLOCK_MEDIUM_AND_ABOVE
    ),
    SafetySetting(
        category=SafetySetting.HarmCategory.HARM_CATEGORY_SEXUALLY_EXPLICIT,
        threshold=SafetySetting.HarmBlockThreshold.BLOCK_MEDIUM_AND_ABOVE
    ),
    SafetySetting(
        category=SafetySetting.HarmCategory.HARM_CATEGORY_HARASSMENT,
        threshold=SafetySetting.HarmBlockThreshold.BLOCK_MEDIUM_AND_ABOVE
    ),
]

generate()

================================================================================================

#Python code
import random

# Define a dictionary of possible responses
responses = {
    "greeting": [
        "Hello there!",
        "Hi, how can I help you today?",
        "Greetings! What can I do for you?"
    ],
    "goodbye": [
        "Goodbye! Have a great day.",
        "See you later! Take care.",
        "It was nice chatting with you. Farewell!"
    ],
    "thank_you": [
        "You're welcome!",
        "No problem, happy to help.",
        "Anytime!"
    ],
        "conference_slogans": [
            "Connect, Collaborate, Innovate",
            "The Future of [Industry] is Here",
            "Thought Leadership at its Best",
        ],
        "conference_images": [
            "https://www.example.com/conference-image1.jpg",
            "https://www.example.com/conference-image2.jpg",
        ],
        "conference_hastags": [
            "#learn and Innovate",
            "#fantastic event",
        ],
         "workshop_slogans": [
            "Hands-on Learning for [Skill]",
            "Master the Art of [Topic]",
            "Unlock Your Potential",
        ],
        "workshop_images": [
            "https://www.example.com/workshop-image1.jpg",
            "https://www.example.com/workshop-image2.jpg",
        ],
        
        "workshop_hastags": [
            "#learn",
            "#tech_training",
        ],
  
        "webinar_slogans": [
            "Get the Insights You Need",
            "Expert Advice on [Topic]",
            "Join the Discussion",
        ],
        "webinar_images": [
            "https://www.example.com/webinar-image1.jpg",
            "https://www.example.com/webinar-image2.jpg",
        ],
        
        "webinar_hastags": [
            "#techies",
            "#fantastic",
        ],
   
        "hackathon_slogans": [
            "Code Your Way to Success",
            "Innovation Unleashed",
            "Build the Future",
        ],
        "hackathon_images": [
            "https://www.example.com/hackathon-image1.jpg",
            "https://www.example.com/hackathon-image2.jpg",
        ],
        "hackathon_hastags": [
            "#Innovate",
            "#learn",
        ]
    
}

def get_response(user_input):
    """
    Generates a response based on the user's input.

    Args:
        user_input: The user's message.

    Returns:
        A chatbot response.
    """

    user_input = user_input.lower()

    # Check for greetings
    if any(word in user_input for word in ["hello", "hi", "greetings"]):
        return random.choice(responses["greeting"])

    # Check for goodbyes
    if any(word in user_input for word in ["goodbye", "bye", "see you later"]):
        return random.choice(responses["goodbye"])

    # Check for thank you
    if "thank you" in user_input:
        return random.choice(responses["thank_you"])
        
    if "conference images" in user_input:
        return random.choice(responses["conference_images"])
        
    if "conference slogans" in user_input:
        return random.choice(responses["conference_slogans"])
        
    if "conference hastags" in user_input:
        return random.choice(responses["conference_hastags"])        
            
    if "workshop slogans" in user_input:
        return random.choice(responses["workshop_slogans"])   
    
            
    if "workshop images" in user_input:
        return random.choice(responses["workshop_images"])   
        
    if "workshop hastags" in user_input:
        return random.choice(responses["workshop_hastags"])        
        
            
    if "webinar images" in user_input:
        return random.choice(responses["webinar_images"])   
        
            
    if "webinar slogans" in user_input:
        return random.choice(responses["webinar_slogans"])   
        
    if "webinar hastags" in user_input:
        return random.choice(responses["webinar_hastags"])  
        
            
    if "hackathon images" in user_input:
        return random.choice(responses["hackathon_images"])   
        
            
    if "hackathon images" in user_input:
        return random.choice(responses["hackathon_images"])
        
    if "hackathon hastags" in user_input:
        return random.choice(responses["hackathon_hastags"])      

    # Default response for unknown inputs
    return "I'm sorry, I don't understand."

# Main chatbot loop
while True:
    user_input = input("You: ")
    if user_input == "quit":
        break
    response = get_response(user_input)
    print("Chatbot:", response)
    print("If you want to quit, just type 'quit' ", response)



#############################Chatbot Backend##########################################
import base64
import vertexai
from vertexai.generative_models import GenerativeModel, Part, SafetySetting


def generate():
    vertexai.init(project="ABC", location="us-central1")
    model = GenerativeModel(
        "gemini-1.5-flash-001",
    )
    responses = model.generate_content(
        ["""Create chatbot which will give slogans, images for events in the organization"""],
        generation_config=generation_config,
        safety_settings=safety_settings,
        stream=True,
    )

    for response in responses:
        print(response.text, end="")


generation_config = {
    "max_output_tokens": 8192,
    "temperature": 1,
    "top_p": 0.95,
}

safety_settings = [
    SafetySetting(
        category=SafetySetting.HarmCategory.HARM_CATEGORY_HATE_SPEECH,
        threshold=SafetySetting.HarmBlockThreshold.BLOCK_MEDIUM_AND_ABOVE
    ),
    SafetySetting(
        category=SafetySetting.HarmCategory.HARM_CATEGORY_DANGEROUS_CONTENT,
        threshold=SafetySetting.HarmBlockThreshold.BLOCK_MEDIUM_AND_ABOVE
    ),
    SafetySetting(
        category=SafetySetting.HarmCategory.HARM_CATEGORY_SEXUALLY_EXPLICIT,
        threshold=SafetySetting.HarmBlockThreshold.BLOCK_MEDIUM_AND_ABOVE
    ),
    SafetySetting(
        category=SafetySetting.HarmCategory.HARM_CATEGORY_HARASSMENT,
        threshold=SafetySetting.HarmBlockThreshold.BLOCK_MEDIUM_AND_ABOVE
    ),
]

generate()


================================================================================================

#Python code

import random

# Sample slogans and image URLs for different event types
event_data = {
    "conference": {
        "slogans": [
            "Connect, Collaborate, Innovate",
            "The Future of [Industry] is Here",
            "Thought Leadership at its Best",
        ],
        "images": [
            "https://www.example.com/conference-image1.jpg",
            "https://www.example.com/conference-image2.jpg",
        ],
    },
    "workshop": {
        "slogans": [
            "Hands-on Learning for [Skill]",
            "Master the Art of [Topic]",
            "Unlock Your Potential",
        ],
        "images": [
            "https://www.example.com/workshop-image1.jpg",
            "https://www.example.com/workshop-image2.jpg",
        ],
    },
    "webinar": {
        "slogans": [
            "Get the Insights You Need",
            "Expert Advice on [Topic]",
            "Join the Discussion",
        ],
        "images": [
            "https://www.example.com/webinar-image1.jpg",
            "https://www.example.com/webinar-image2.jpg",
        ],
    },
    "hackathon": {
        "slogans": [
            "Code Your Way to Success",
            "Innovation Unleashed",
            "Build the Future",
        ],
        "images": [
            "https://www.example.com/hackathon-image1.jpg",
            "https://www.example.com/hackathon-image2.jpg",
        ],
    },
}

def get_event_details(event_type):
    """Generates a random slogan and image URL for the given event type."""
    if event_type in event_data:
        slogan = random.choice(event_data[event_type]["slogans"])
        image_url = random.choice(event_data[event_type]["images"])
        return slogan, image_url
    else:
        return "Event type not found.", None



