from twilio.rest import Client

def send_sms(item_price, num_input):
    client = Client("AC6e1b1599828b504afbc918c0dd3bea88", "66d84e8ed4fa45b97fe020963a856d0a")

    client.messages.create(to=num_input,
                        from_="+12059460266",
                        body="Your tracked item is now $" + str(item_price))

def add_item(item_name, item_price, condition):
    file = open("prices.txt", "a")
    file.write(item_name + "," + str(item_price) + "," + str(condition) + "\n")
    file.close()

if __name__ == "__main__":
    #send_sms(200, "+18056125625")
    add_item("Yeezy Boost 350 V2 Zebra", 320, 220)