# Challenges Class:
# -----------------

class SmallChallenges:
    def __init__(self):
        self.room_area()
        print('####################################')
        self.meal_cost()
        print('####################################')
        self.annual_profit()
        print('####################################')
        self.vowels_constant()
        print('####################################')
        self.calls_messages()
        print('####################################')
        self.museum_visitors()
        print('####################################')
        self.find_longest()
        print('####################################')
        self.taxi_fare()
        print('####################################')
        self.delivery_fees()
        print('####################################')

    # Room Area Calculator:
    def room_area(self):
        area_length = int(input(' Please Insert The Length: '))
        area_width = int(input(' Please Insert The Width: '))
        area_all = area_width * area_length
        print(f" Room Area {area_all}. ")

    # Meal Cost With Tax And Tips:
    def meal_cost(self):
        meal_cost = int(input(' Please Enter The Meal Cost: '))
        meal_tax = meal_cost * (10 / 100)
        meal_tip = (meal_cost + meal_tax) * (15 / 100)
        meal_total = meal_cost + meal_tax + meal_tip
        print(
            f"    Meal Cost: {meal_cost:.2f}\n    Meal Tax: {meal_tax:.2f}\n    Meal Tip: {meal_tip:.2f}\n    ------------------\n    Net Total: {meal_total:.2f}")

    # Investment Profits For Annual Savings:
    def annual_profit(self):
        deposit_amount = input(' Please Enter Amount Of Investment: ')
        deposit_amount = float(deposit_amount)
        yearly_interest_rate = 7.5 / 100
        yearly_profits = (deposit_amount * yearly_interest_rate) + deposit_amount
        two_years_profit = yearly_profits * 2
        five_years_profit = yearly_profits * 5
        ten_years_profit = yearly_profits * 10
        print(
            f"  Deposit: {deposit_amount:.2f}\n  Interest Rate: {yearly_interest_rate: .1%}\n  One Year Total Profits: {yearly_profits:.2f}\n  Two Years Profits: {two_years_profit:.2f}\n  Five Years Profits: {five_years_profit:.2f}\n  Ten Years Profits: {ten_years_profit:.2f}")

    # Vowels Or Constants:
    def vowels_constant(self):
        vowels_list = ["A", "E", "I", "O", "U"]
        target_text = input(' Please Insert The Target Text: ')
        vowels_target = []
        constant_target = []

        for target_letter in target_text:
            if target_letter.upper() == "A" or target_letter.upper() == "E" or target_letter.upper() == "I" or target_letter.upper() == "O" or target_letter.upper() == "U":
                vowels_target.append(target_letter)
            else:
                constant_target.append(target_letter)

        print(f" This Is Vowels Target: {vowels_target}, With {len(vowels_target)} Items. ")
        print('.-.-.-.-.-.-.-.-.')
        print(f" This Is Constants Target: {constant_target}, With {len(constant_target)} Items. ")

    # Cost Of Calls - Messages - Internet Usage:
    def calls_messages(self):
        print(' Dear Client Please Provide The Requested Data. ')
        minutes_count = int(input(' Minutes Count: '))
        messages_count = int(input(' Messages Count: '))
        internet_count = int(input(' GB Count: '))
        pay_within = int(input(' Days To Pay: '))

        minutes_price = minutes_count * 1.3
        messages_price = messages_count * 0.3
        internet_price = internet_count * 2
        customer_support = 3
        invoice_before_tax = minutes_price + messages_price + internet_price + customer_support
        invoice_after_tax = (invoice_before_tax * (10/100)) + invoice_before_tax
        if pay_within < 15:
            final_invoice = invoice_after_tax - (invoice_after_tax * (5 / 100))
        else:
            final_invoice = invoice_after_tax
        print(f" Dear Customer The Final Invoice Cost Is: {final_invoice:.2f} ")

    # Cost For Age Of Museum Visitors:
    def museum_visitors(self):
        global ticket_cost
        visitor_age = int(input(' Please Enter Age: '))
        if visitor_age < 10:
            ticket_cost = 17
        elif 10 < visitor_age < 21:
            ticket_cost = 20
        elif 21 < visitor_age:
            ticket_cost = 24
        print(f" Dear Customer The Cost For The Ticket Is : {ticket_cost:0.2f} $.")

    # Find Longest Word In Sentence:
    def find_longest(self):
        words_text = input(' Please Enter The Target Text: ').split()
        longest_word = ''
        for word in words_text:
            while len(word) > len(longest_word):
                longest_word = word
        print(f" The Longest Word Is: {longest_word}, and It Has {len(longest_word)} Alphabet.")

    # Total Taxi Fare:
    def taxi_fare(self):
        trip_distance = int(input(' Enter Distance By Miles: '))
        fixed_trip_fare = 4
        variable_trip_fare = 2.4
        total_trip_fare = (trip_distance * variable_trip_fare) + 4
        print(f" The Total Fare For This Trip Is {total_trip_fare:0.2f} $. ")

    # Delivery Fees:
    def delivery_fees(self):
        order_cost = int(input(' Enter Order Cost: '))
        if order_cost < 100:
            delivery_fee = 5
            total_order_cost = order_cost + (order_cost * (5 / 100))
        elif 100 < order_cost < 500:
            delivery_fee = 10
            total_order_cost = order_cost + (order_cost * (2 / 100))
        else:
            delivery_fee = 15
            total_order_cost = order_cost + (order_cost * (1 / 100))

        final_delivery_fees = total_order_cost + delivery_fee

        print(f"  The Final Total Fees For Delivery Is: {final_delivery_fees:0.2f} $.\n  Delivery Fees: {delivery_fee:0.2f} $.\n  Order Total Cost: {total_order_cost:0.2f} $.")


Small_New = SmallChallenges()
