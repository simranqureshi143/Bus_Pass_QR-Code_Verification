import qrcode

pass_id = "PASS001"

img = qrcode.make(pass_id)
img.save("PASS001_QR.png")

print("✅ QR Code generated: PASS001_QR.png")
