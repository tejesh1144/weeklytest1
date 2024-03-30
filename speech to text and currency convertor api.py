#!/usr/bin/env python
# coding: utf-8

# In[2]:


from gtts import gTTS
import os

def text_to_speech(text, lang='en'):
    # Create a gTTS object
    tts = gTTS(text=text, lang=lang, slow=False)

    # Save the audio file
    tts.save("output.mp3")

    # Play the audio file
    os.system("afplay output.mp3")  # For macOS
   
if __name__ == "__main__":
    input_text = input(" please Enter the text to convert to speech: ")
    text_to_speech(input_text)
    


# In[4]:


import requests

def fetch_currency_conversion(base_currency, target_currency):
    # API endpoint URL
    url = f"https://api.exchangerate-api.com/v4/latest/{base_currency}"

    try:
        # Send GET request to the API
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for any HTTP errors

        # Parse the JSON response
        data = response.json()

        # Extract the conversion rate for the target currency
        conversion_rate = data["rates"][target_currency]

        return conversion_rate

    except requests.exceptions.RequestException as e:
        print("Error fetching data from the API:", e)
        return None

if __name__ == "__main__":
    base_currency = input("Enter the base currency (e.g., USD, EUR): ").upper()
    target_currency = input("Enter the target currency (e.g., GBP, JPY): ").upper()

    conversion_rate = fetch_currency_conversion(base_currency, target_currency)
    if conversion_rate is not None:
        print(f"1 {base_currency} = {conversion_rate} {target_currency}")


# In[ ]:




