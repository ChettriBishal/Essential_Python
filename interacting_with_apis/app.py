from libs.openexchange import OpenExchangeClient
import time

APP_ID = "ca77b7c697454803a659ca82bb66404d"   # form of authorization

client = OpenExchangeClient(APP_ID)

usd_amount = 1000

start = time.time()
gbp_amount = client.convert(usd_amount,'USD','GBP')
end = time.time()
print(f"First time the function took {end - start}s")

print(f"USD{usd_amount} is GBP{gbp_amount:.3f}")


start = time.time()
gbp_amount = client.convert(usd_amount,'USD','GBP')
gbp_amount = client.convert(usd_amount,'USD','GBP')
gbp_amount = client.convert(usd_amount,'USD','GBP')
gbp_amount = client.convert(usd_amount,'USD','GBP')
gbp_amount = client.convert(usd_amount,'USD','GBP')
gbp_amount = client.convert(usd_amount,'USD','GBP')
gbp_amount = client.convert(usd_amount,'USD','GBP')
gbp_amount = client.convert(usd_amount,'USD','GBP')
gbp_amount = client.convert(usd_amount,'USD','GBP')

end = time.time()

print(f"Multiple function calls took {end - start}s")






