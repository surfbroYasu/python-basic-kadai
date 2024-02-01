def calculate_after_tax (price, tax):
  total = price + (price*(tax/100)) 
  print(f"{total}円です")

calculate_after_tax(int(input("金額を入力してください")), float(input("税率(%)")))
