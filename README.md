# codeGeneratorQR
![image](https://github.com/Anastasios3/codeGeneratorQR/assets/117446378/a561a4c7-6b34-4fab-8da1-9182935f821d)

# QR Code Generator

## Overview

The QR Code Generator is a Python-based application with a graphical user interface (GUI) that allows users to generate QR codes from URLs. This application supports various customization options, real-time preview, and the ability to save QR codes in multiple formats (PNG, SVG, PDF).

## Features

- **Real-time Preview**: The QR code updates in real-time as you type the URL.
- **Error Correction Levels**: Choose from Low (L), Medium (M), Quartile (Q), and High (H) error correction levels to enhance the reliability of the QR code.
- **Customization**: Customize the color and size of the QR code to fit your needs.
- **Save Formats**: Save the generated QR code in PNG, SVG, or PDF format for versatile use.

## Prerequisites

Ensure you have the following software installed on your system:

- Python 3.x
- `pip` (Python package installer)

## Installation

1. **Clone the Repository**

   Clone the repository from GitHub:

   ```sh
   git clone https://github.com/Anastasios3/codeGeneratorQR
   cd codeGeneratorQR
   ```

2. **Install Dependencies**

   Install the required Python packages using `pip`:

   ```sh
   pip install qrcode[pil] pillow reportlab svglib
   ```

## Usage

1. **Run the Application**

   Navigate to the directory containing the script and run it:

   ```sh
   python generatorQR.py
   ```

2. **Generate QR Code**

   - Enter the URL in the input field.
   - Select the desired error correction level from the dropdown menu.
   - Customize the color and size of the QR code.
   - The QR code preview will update in real-time as you type.

3. **Save QR Code**

   - Click the "Save QR Code" button.
   - Choose the desired file format (PNG, SVG, PDF) and location to save the QR code.

## Script Details

### generatorQR.py

The `generatorQR.py` script creates a GUI application using the `tkinter` library. It allows users to input a URL, select error correction levels, customize the QR code's color and size, and save the generated QR code in different formats.

### Key Functionalities:

- **URL Input**: A text entry field for the user to input the URL to be encoded.
- **Error Correction Level**: Dropdown menu to select the error correction level.
- **Color and Size Customization**: Entry fields to specify the QR code color and size.
- **Real-time Preview**: The QR code updates in real-time as the user types.
- **Save Options**: Save the generated QR code as PNG, SVG, or PDF.

## Dependencies

- `tkinter`: Python's standard GUI package.
- `qrcode`: A pure Python QR Code generator.
- `Pillow`: Python Imaging Library (Fork).
- `reportlab`: A library to create PDFs.
- `svglib`: A library to read SVG files.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contributing

Contributions are welcome! Please fork the repository and create a pull request with your changes. For major changes, please open an issue first to discuss what you would like to change.

## Authors

- Anastasios Tatarakis - Larentzos - *Initial work* - [yourusername](https://github.com/Anastasios3)

## Acknowledgments

- Thanks to the developers of the `qrcode`, `Pillow`, `reportlab`, and `svglib` libraries for their excellent tools.
