import argparse
import cv2
import numpy as np
from app.model import TransferLearningModel  # Update with your actual model class

def classify_image(image_path):
    # Load your object detection model (e.g., saved model or TFLite model)
    # Create an instance of the TransferLearningModel class
    model = TransferLearningModel(n_classes=1, input_shape=(640, 640, 3))

    # Build the model
    model = model.build_model()
    # Update with your actual model path
    model_path = r'C:\Users\VIKAS CHEIIURU\OneDrive\Documents\projects_of_vikas_chelluru\Resume_Classification_using_DeepLearning\model_weights\model.h5'


    model.load_weights(model_path)
    target_size = (640, 640)

    class_names = ["Not_Resume", "Resume"]

    # Read the image and convert it to a numpy array
    uploaded_image = cv2.imread(image_path)

    # Resize the image to the target size
    resized_image = cv2.resize(uploaded_image, target_size) 

    image_array = np.array(resized_image) / 255.0  # Normalize pixel values to be in the range [0, 1]

    # Add an extra dimension to match the input shape expected by the model
    image_array = np.expand_dims(image_array, axis=0)

    # Predict using the model
    y_pred = model.predict(image_array)

    # Define the threshold
    threshold = 0.5

    # Convert probabilities to class labels using the threshold
    predicted_class_label = 1 if y_pred[0][0] >= threshold else 0

    # Optionally, you can also get the class name if needed
    predicted_class_name = class_names[predicted_class_label]

    # Draw the predicted class name on top of the image
    font = cv2.FONT_HERSHEY_SIMPLEX
    font_scale = 1
    font_thickness = 2
    text_position = (10, 50)
    text_color = (255, 255, 255)
    
    annotated_image = uploaded_image.copy()
    cv2.putText(annotated_image, f'Predicted Class: {predicted_class_name}', text_position, font, font_scale, text_color, font_thickness)

    # Display the annotated image
    cv2.imshow('Annotated Image', annotated_image)

    # Wait for a key event and close the window when a key is pressed
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Classify an image as 'Resume' or 'Not_Resume'.")
    parser.add_argument("--path", type=str, required=True, help="Path to the image for classification.")
    args = parser.parse_args()

    image_path = args.path
    classify_image(image_path)
