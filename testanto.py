def travelCost(numberOfNights, city, rentalDays, extraExpense):

  #Custo de Hospedagem
  valuePerNight = 140
  hostingValue = numberOfNights * valuePerNight

  print(f'the total cost of hosting is: R${hostingValue:.2f}')

  #Custo de Passagem
  city = city.lower().strip()
  valueByCity = 0

  if (city == 'são paulo') or (city == 'sao paulo'):
    valueByCity = 312
  elif (city == 'porto alegre'):
    valueByCity = 447
  elif (city == 'recife'):
    valueByCity = 831
  elif (city == 'manaus'):
    valueByCity = 986
  
  print(f'the total cost of ticket is: R${valueByCity:.2f}')

  #Aluguel de Carro
  valuePerDay = 40
  discountSevenDays = 50
  discountThreeDays = 20

  carCost = valuePerDay*rentalDays

  if (rentalDays >= 7):
    carCost -= discountSevenDays
  elif (rentalDays >= 3):
    carCost -= discountThreeDays
  print(f"the car rental is: R${carCost:.2f}")

  # Gasto Extra
  print(f"the additional cost is: R${extraExpense:.2f}")

  #Total da viagem
  totalCost =  (hostingValue + valueByCity + carCost)+ extraExpense
  
  print()
  print(f"the total cost of travel is: R${totalCost:.2f}")


numberOfNights = int(input("how many nights will you be staying?: "))
city = input('what is the destination city?: ')
rentalDays = int(input('how many days do you want to rent?: '))
extraExpense = float(input('how much extra money do you want to take? R$'))

print()

travelCost(numberOfNights, city, rentalDays, extraExpense)