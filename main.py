import cv2

# Read the image
imgname = input("Enter the name of the .jpg file: ")
image = cv2.imread(f'{imgname}.jpg')

# Set the new dimensions for resizing
new_width = int(input("Enter the new width: "))
new_height = int(input("Enter the new height: "))

# Resize the image
resized_image = cv2.resize(image, (new_width, new_height))

# Display the original and resized images
cv2.imshow('Original Image', image)
cv2.imshow('Resized Image', resized_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Save the resized image
output_name = input("Enter the name for the resized image: ")
cv2.imwrite(f'{output_name}.jpg', resized_image)
print("Resized image saved successfully!")


