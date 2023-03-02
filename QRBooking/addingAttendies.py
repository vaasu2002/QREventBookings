from QRBooking.database import connectToDatabase
import qrcode

collection = connectToDatabase()

name = "Vaasu Bisht"
email = "vaasu.bisht2021@gmail.com"
regNo = "21MIM10035"
gender = "male"
document = {
    "name": name,
    "email": email,
    "regNo": regNo,
    "gender": gender,
}
try:
    result = collection.insert_one(document)
    doc_id = result.inserted_id
    print(doc_id)
    object_id_str = str(doc_id)
    result = collection.update_one({'_id': doc_id}, {'$set': {'QRCode': object_id_str}})

    qr = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_L, box_size=10, border=4)
    qr.add_data(object_id_str)
    qr.make(fit=True)

    # Save the QR code image to a file
    img = qr.make_image(fill_color="black", back_color="white")
    img.save(f"{regNo}.png")
except:
    print("ALREADY EXISTS")