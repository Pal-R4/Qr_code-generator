import pandas as pd
import qrcode
import os

# Load the dataset
df = pd.read_csv('qr_generator/covid.csv')

print(df.columns)

# Create a directory to save QR codes if it doesn't exist
output_dir = 'Qr_codes'
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Generate QR codes for each row in the dataset
for index, row in df.iterrows():
    data_to_encode = str(row['Recovered'])  # Convert to string in case it's not
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
                      )
    qr.add_data(data_to_encode)
    qr.make(fit=True)

    # Create an image from the QR Code instance
    img = qr.make_image(fill='black', back_color='white')

    # Save the image
    img.save(os.path.join(output_dir, f'Qr_code_{index}.png'))
