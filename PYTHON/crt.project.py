companies = ['Tesla', 'Toyota', 'Ford']
print(companies)
a = input("Enter the car company: ").lower()
if a in [a.lower() for a in companies]:
    print("Welcome to the family")
else:
    print("Sorry, the company you entered is not there")

company_models = {
    "tesla": ["Model S", "Model 3", "Model X", "Model Y"],
    "toyota": ["Camry", "Corolla", "Prius", "Rav4"],
    "ford": ["Mustang", "F-150", "Escape", "Explorer"]
}
b = input("Enter the company model: ").lower()
if b in company_models:
    models_list = company_models[b]
    print("Available models for", b.capitalize(), ":", models_list)
else:
    print("Sorry, the model you entered is not present")
    
def get_variant(companies, models):
    print(f"Please choose the variant for {company} {model}:")
    variant = input("Enter 'petrol' or 'diesel': ")
    return variant

