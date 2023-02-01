import cv2
import numpy as np
import requests
import json

def identify_animal(image_path):
    # Use an object detection API to identify the animal in the image
    api_key = "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"
    url = "https://api.openai.com/v1/images/models/aaa03c23b3724a16a56b629203edc62c/outputs"

    image = cv2.imread(image_path)
    image = cv2.resize(image, (224, 224))  # resize image to the required input size

    headers = {
    'Content-Type': 'application/json',
    'Authorization': 'Bearer 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'
    }
    data = {
        "data": [{
            "image": {
                "base64": image_path
            }
        }]
    }
    response = requests.post(url, headers=headers, data=data)
    #if response.status_code != 200:
    #    raise Exception("Failed to identify animal")
    print(response.text)
    result = json.loads(response.text)['data'][0]['concepts'][0]
    #response = requests.post(
    #    url,
    #    headers={
    #        "Content-Type": "application/json",
    #       "Authorization": f"Bearer {api_key}"
    #    },
    #    json={
    #        "data": [{
    #            "image": {
    #                "file_path": image_path
    #            }
    #        }]
    #    }
    #)

    # Get the top result and extract the label and confidence
    result = json.loads(response.text)['data'][0]['concepts'][0]
    animal = result['name']
    confidence = result['value']

    # Get information about the animal from a separate API
    api_key = "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"
    url = f"https://api.openai.com/v1/engines/babbage/jobs"

    response = requests.post(
        url,
        headers={
            "Content-Type": "application/json",
            "Authorization": f"Bearer {api_key}"
        },
        json={
            "model": "text-davinci-002",
            "prompt": f"What is a {animal}?"
        }
    )

    # Extract the information about the animal
    info = json.loads(response.text)['choices'][0]['text']

    return animal, confidence, info

def draw_text_on_image(image_path, animal, confidence, info):
    # Load the image
    image = cv2.imread(image_path)

    # Draw the animal name and confidence on the image
    font = cv2.FONT_HERSHEY_SIMPLEX
    text = f"{animal} ({confidence:.2f})"
    color = (255, 255, 255)
    thickness = 2
    (text_width, text_height), baseline = cv2.getTextSize(text, font, fontScale=1, thickness=thickness)
    x = int((image.shape[1] - text_width) / 2)
    y = int((image.shape[0] + text_height) / 2)
    cv2.putText(image, text, (x, y), font, fontScale=1, color=color, thickness=thickness)

    # Show the image
    cv2.imshow("Animal Identification", image)
    cv2.waitKey(0)

def main():
    # Get the path to the image
    image_path = input("Enter the path to the image: ")

    # Identify the animal and get information about it
    animal, confidence, info = identify_animal(image_path)
    print(f"Animal: {animal}")
    print(f"Confidence: {confidence:.2f}")
    print(f"Info: {info}")

    # Draw the animal name and confidence on the image
    draw_text_on_image(image_path, animal, confidence, info)

if __name__ == '__main__':
    main()
