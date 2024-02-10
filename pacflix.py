class Pacflix():
    referral_code = []
    user_acc = {}

    def __init__(self, username, current_plan, duration):
        self.username = username
        self.current_plan = current_plan
        self.duration = duration

        username_acc = {self.username: [self.current_plan, self.duration]}
        self.user_acc.update(username_acc)

        Pacflix.referral_code.append(self.username)
        print(f"Your account succesfully created. By sharing this code '{self.username}' to your friends, you can get benefit. Enjoy!")

    def list_plan(self):
        print("List of Pacflix stream plan :")
        print("--------------------------------")
        print("1. Basic Plan")
        print("What you will get :")
        print("Standard Definiton (SD) quality, Download the content, 1 number of device, 3rd party movies")
        print("Price : Rp 120.000")
        print("--------------------------------")
        print("2. Standard Plan")
        print("What you will get :")
        print("High Definiton (HD) quality, Download the content, 2 number of devices, 3rd party movies + Sports (Football, Racing, Basketball)")
        print("Price : Rp 160.000")
        print("--------------------------------")
        print("3. Premium Plan")
        print("What you will get :")
        print("Ultra High Definiton (UHD) quality, Download the content, 4 number of devices, 3rd party movies + Sports (Football, Racing, Basketball) + Pacflix Original")
        print("Price : Rp 200.000")
    
    def check_plan(self):
        for key, value in self.user_acc.items():
            if key == self.username:

                if value[0] in ["Basic Plan", "Standard Plan", "Premium Plan"]:
                    print(f"Your current plan is {value[0]}.")
                    print("Your benefits are :")

                    if value[0] == "Basic Plan":
                        print("Standard Definiton (SD) quality, Download the content, 1 number of device, 3rd party movies") 
                    
                    elif value[0] == "Standard Plan":
                        print("High Definiton (HD) quality, Download the content, 2 number of devices, 3rd party movies + Sports (Football, Racing, Basketball)")
                    
                    elif value[0] == "Premium Plan":
                        print("Ultra High Definiton (UHD) quality, Download the content, 4 number of devices, 3rd party movies + Sports (Football, Racing, Basketball) + Pacflix Original")

                    print(f"You already subscribe this plan for {value[1]} months")
                    return

                elif value[0] == None:
                    print("You don't subscribe any plan yet. Go subscribe!")
                
    def purchase(self, new_plan, duration, ref_code):
        total_price = 0

        if ref_code != None and ref_code in Pacflix.referral_code:
            self.duration = duration

            if new_plan == "Basic Plan":
                self.current_plan = "Basic Plan"
                total_price = (120000 - (0.04 * 120000))
                print(f"You are selecting Basic Plan with referral code from {ref_code}, with total price Rp {total_price} per month for {duration} months.")

            elif new_plan == "Standard Plan":
                self.current_plan = "Standard Plan"
                total_price = (160000 - (0.04 * 160000))
                print(f"You are selecting Standard Plan with referral code from {ref_code}, with total price Rp {total_price} per month for {duration} months.")

            elif new_plan == "Premium Plan":
                self.current_plan = "Premium Plan"
                total_price = (200000 - (0.04 * 200000))
                print(f"You are selecting Premium Plan with referral code from {ref_code}, with total price Rp {total_price} per month for {duration} months.")

            else:
                print("Your selected plan is invalid!")

        elif ref_code != None and ref_code not in Pacflix.referral_code:
            print("Your referral code invalid!")

        elif ref_code == None:
            if new_plan == "Basic Plan":
                self.current_plan = "Basic Plan"
                total_price = 120000
                print(f"You are selecting Basic Plan, with total price Rp {total_price} per month for {duration} months.")

            elif new_plan == "Standard Plan":
                self.current_plan = "Standard Plan"
                total_price = 160000
                print(f"You are selecting Standard Plan, with total price Rp {total_price} per month for {duration} months.")

            elif new_plan == "Premium Plan":
                self.current_plan = "Premium Plan"
                total_price = 200000
                print(f"You are selecting Premium Plan, with total price Rp {total_price} per month for {duration} months.")

            else:
                self.new_plan = 0
                self.duration = 0
                print("Your selected plan is invalid!")

        else:
            print("Something bad happen.")
        
        self.user_acc[self.username] = [self.current_plan, duration]
    
    def upgrade_plan(self, new_plan, duration):
        total_price = 0

        if duration >= 12:
            if self.current_plan == "Basic Plan":
                if new_plan == "Standard Plan":
                    self.current_plan = "Standard Plan"
                    total_price = (160000 - (0.05 * 160000))
                    print(f"You are upgrading to {self.current_plan} with discount, the price you pay Rp {total_price}.")
                
                elif new_plan == "Premium Plan":
                    self.current_plan = "Premium Plan"
                    total_price = (200000 - (0.05 * 200000))
                    print(f"You are upgrading to {self.current_plan} with discount, the price you pay Rp {total_price}.")
                
                else:
                    print("Your new plan is invalid!")
            
            elif self.current_plan == "Standard Plan":
                if new_plan == "Premium Plan":
                    self.current_plan = "Premium Plan"
                    total_price = (200000 - (0.05 * 200000))
                    print(f"You are upgrading to {self.current_plan} with discount, the price you pay Rp {total_price}.")
                
                else:
                    print("Your new plan is invalid!")
            
            else:
                print("You already in the highest plan. You can't upgrade or downgrade to any plan.")

        else:
            if self.current_plan == "Basic Plan":
                if new_plan == "Standard Plan":
                    self.current_plan = "Standard Plan"
                    total_price = 160000
                    print(f"You are upgrading to {self.current_plan}, the price you pay Rp {total_price}.")
                
                elif new_plan == "Premium Plan":
                    self.current_plan = "Premium Plan"
                    total_price = 200000
                    print(f"You are upgrading to {self.current_plan}, the price you pay Rp {total_price}.")
                
                else:
                    print("Your new plan is invalid!")
            
            elif self.current_plan == "Standard Plan":
                if new_plan == "Premium Plan":
                    self.current_plan = "Premium Plan"
                    total_price = 200000
                    print(f"You are upgrading to {self.current_plan}, the price you pay Rp {total_price}.")
                
                else:
                    print("Your new plan is invalid!")
            
            else:
                print("You already in the highest plan. You can't upgrade or downgrade to any plan.")
        
        self.user_acc[self.username] = [self.current_plan, duration]