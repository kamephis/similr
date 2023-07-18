# similr

similr is a Python-based software that allows you to find similar images within a folder based on content matching. It uses advanced image comparison techniques to identify images that contain similar content to a given input image.

## Features

- Find similar images based on content matching
- Supports various image formats (e.g., JPEG, PNG)
- Uses advanced comparison techniques (e.g., Histogram Comparison, SSIM)
- Customizable similarity threshold
- Option to move or copy similar images to a designated results folder

## Installation

1. Clone the repository:
```
git clone https://github.com/your-username/similr.git`
```
2. Update pip
```
pip3 install --upgrade pip
```
3. Install the required dependencies:
```
pip install -r requirements.txt
```


## Usage

1. Place the input image (e.g., `input.jpeg`) that you want to find similar images for in the root folder.

2. Create a folder named `img` in the root directory and add the images you want to compare in this folder.

3. Run the following command to find similar images and move them to the `results` folder:
```
python3 similr.py input.jpeg img results
```
4. By default, the script will move the similar images to the results folder. If you want to copy the images instead, use the `--copy` flag:

5. Adjust the similarity threshold in the code (`similarity > 0.9`) to control the level of similarity required.

6. The results will be stored in the `results` folder, containing the images identified as similar to the input image.

## Contributing

Contributions to similr are welcome! If you have any ideas, bug fixes, or enhancements, feel free to open an issue or submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).

