price = int(input("金額を入力してください"))
tax = float(input("税率(%)"))

def calculate_after_tax (price, tax):
  total = price + (price*(tax/100)) 
  return total
print(calculate_after_tax(price, tax))