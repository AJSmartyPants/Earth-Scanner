import cv2

# Load the pre-trained model
model = cv2.dnn.readNetFromCaffe('path/to/model.prototxt', 'path/to/weights.caffemodel')

# Load the input image
image = cv2.imread(r"C:\Users\tinao\Downloads\animalimg.jpg")

# Pass the image through the model
(h, w) = image.shape[:2]
blob = cv2.dnn.blobFromImage(cv2.resize(image, (300, 300)), 0.007843, (300, 300), 127.5)
model.setInput(blob)
detections = model.forward()

# Loop over the detections
for i in range(0, detections.shape[2]):
  # Extract the confidence
  confidence = detections[0, 0, i, 2]

  # Filter out weak detections
  if confidence > 0.5:
    # Extract the class label
    class_id = int(detections[0, 0, i, 1])

    # Draw a bounding box around the object
    box = detections[0, 0, i, 3:7] * np.array([w, h, w, h])
    (startX, startY, endX, endY) = box.astype("int")
    cv2.rectangle(image, (startX, startY), (endX, endY), (255, 0, 0), 2)

# Show the output image
cv2.imshow("Output", image)
cv2.waitKey(0)