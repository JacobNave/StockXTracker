from twilio.rest import Client

def send_sms(item_price, num_input):
    client = Client("AC6e1b1599828b504afbc918c0dd3bea88", "66d84e8ed4fa45b97fe020963a856d0a")

    client.messages.create(to=num_input,
                        from_="+12059460266",
                        body="Your tracked item is now $" + str(item_price))

if __name__ == "__main__":
    send_sms(200, "+18056125625")
