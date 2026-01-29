Height = float(input('Enter your Height in Cm:'))
Weight = float(input('Enter your Weight in Kg:'))
YourHealth = (Height*Weight)/100
if YourHealth <=12.4:
    print('You are so week.')
elif YourHealth <= 30.5:
    print('You are Healthy.')
elif YourHealth <= 40.5:
    print('You are Energetic.')
elif YourHealth <= 60.5:
    print('You are Over weight.')
elif YourHealth <= 77.5:
    print('You are very Fat person.')