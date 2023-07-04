# QR Code Generator
The QR Code Generator is a simple Python application that allows users to generate QR codes from text input. It is built using the `qrcode` library and hosted on AWS EC2 using Docker. The application provides a web interface where users can enter the data they want to encode into a QR code. Upon generating the QR code, it is displayed on the web page for easy scanning and sharing.
## Project Setup

To set up and run the QR code generator project locally, follow these steps:

1. Clone the repository:
```
git clone <repository_url>
```
2. Install the required dependencies:
```
pip install -r requirements.txt
```

3. Run the application:
```
streamlit run qr_code_generator.py
```

4. The application will be accessible at `http://localhost:8501` in your web browser.

## Deployed Application

The QR code generator application is currently deployed on `AWS EC2` using `Docker`. You can access the deployed application using the following URL:

[QR Code Generator - Live Preview](http://3.137.184.103:8501/)

## Usage
Enter the URL you want to encode into the QR code in the provided input field.

Click the "Generate QR Code" button.

The generated QR code will be displayed below.

## Features in upcoming releases
* Customization options for the QR code, such as color schemes, logo overlays, and error correction levels.
* Decoding functionality to extract information from existing QR codes.
* Support for various output formats (PNG, SVG, PDF, etc.).
* File upload capability to generate QR codes from uploaded images or files.
* QR code analytics and tracking features.

Feel free to explore and modify the code to incorporate these features or any other enhancements you have in mind.

## Contributing
Contributions are welcome! If you have any improvements or bug fixes, please feel free to submit a pull request.

## License
This project is licensed under the MIT License.


