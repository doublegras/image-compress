from PIL import Image
from pathlib import Path
import os
import enquiries
import sys

def yes_no(question):
	options = ['yes', 'no\n']
	confirm = enquiries.choose(question, options)
	return True if confirm == 'yes' else False

images_folder = str(Path().absolute()) + '/images/'

define_original_image_path = yes_no('Is the file in /images folder?')
if define_original_image_path:
	image_name = input('File to compress: ')
	original_path = images_folder + image_name
else:
	ask = input('Enter the absolute path to the image: \n\n/')
	original_path = '/' + ask
	image_name = original_path.split('/')[-1]
	if image_name == '':
		original_path.split('/')[-2]

image = open(original_path)
print('\npath:  ' + original_path)

image = Image.open(original_path)
image_bytes = str(os.path.getsize(original_path))
print(image_name + '  ►  ' + image_bytes + ' bytes\n')

ask_new_image_name = input('Name of the compressed image: ')
new_image_name = ask_new_image_name + '.' + image_name.split('.')[-1]

bytes_target = input('Target size (in bytes): ')
print('\n')


if int(image_bytes) > int(bytes_target):
	for i in range(99, 0, -1):
		image.save('resized_images/' + new_image_name, quality=i)
		new_image = 'resized_images/' + new_image_name
		image_bytes = os.path.getsize(new_image)
		sys.stdout.write(' ►  {bytes}\r'.format(bytes=str(image_bytes)))
		if image_bytes <= int(bytes_target):
			print('\n\nFinal file size: ' + str(image_bytes) + ' bytes\n')
			print('Compressed image save at: ' + '/')
			final_image = Image.open(new_image)
			print(final_image.size)
			break
else:
	print('The size of ' + image_name + ' is already lower than ' + bytes_target + ' bytes')