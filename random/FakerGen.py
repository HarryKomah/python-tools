from faker import Faker

# Create a Faker instance
fake = Faker()

# Example 1: Generating fake text-related data
print("\nExample 1:")
for _ in range(2):
    print("Random Word:", fake.word())
    print("Sentence:", fake.sentence())
    print("Text (100 characters):", fake.text(max_nb_chars=100))
    print("-" * 20)

# Example 2: Generating fake names and addresses
print("Example 2:")
for _ in range(5):
    print("Name:", fake.name())
    print("Address:", fake.address())
    print("-" * 20)

# Example 3: Generating fake email addresses and phone numbers
print("\nExample 3:")
for _ in range(5):
    print("Email:", fake.email())
    print("Phone:", fake.phone_number())
    print("-" * 20)

# Example 4: Generating fake dates
print("\nExample 4:")
for _ in range(5):
    print("Date of Birth:", fake.date_of_birth())
    print("Future Date:", fake.future_date(end_date="+30d"))
    print("-" * 20)

# Example 5: Generating fake lorem ipsum text
print("\nExample 5:")
for _ in range(2):
    print(fake.paragraph())
    print("-" * 20)

# Example 6: Generating fake credit card information
print("\nExample 6:")
for _ in range(2):
    print("Credit Card Number:", fake.credit_card_number())
    print("Credit Card Expiry:", fake.credit_card_expire())
    print("-" * 20)

# Example 7: Generating fake job-related data
print("Example 7:")
for _ in range(5):
    print("Job Title:", fake.job())
    print("Company:", fake.company())
    print("Industry:", fake.industry())
    print("-" * 20)

# Example 8: Generating fake internet-related data
print("\nExample 8:")
for _ in range(5):
    print("Username:", fake.user_name())
    print("Domain Name:", fake.domain_name())
    print("URL:", fake.url())
    print("-" * 20)

# Example 9: Generating fake geographic data
print("\nExample 9:")
for _ in range(5):
    print("City:", fake.city())
    print("Country:", fake.country())
    print("Latitude:", fake.latitude())
    print("Longitude:", fake.longitude())
    print("-" * 20)

# Example 10: Generating fake random data
print("\nExample 10:")
for _ in range(5):
    print("Random Letter:", fake.random_letter())
    print("Random Element from List:", fake.random_element(["apple", "banana", "cherry"]))
    print("Random Digit:", fake.random_digit())
    print("-" * 20)

# Example 11: Generating fake UUIDs and GUIDs
print("\nExample 11:")
for _ in range(5):
    print("UUID4:", fake.uuid4())
    print("GUID:", fake.guid())
    print("-" * 20)

# Example 12: Generating fake file-related data
print("\nExample 12:")
for _ in range(5):
    print("File Name:", fake.file_name(extension="txt"))
    print("File Extension:", fake.file_extension())
    print("File MIME Type:", fake.mime_type())
    print("-" * 20)

# Example 13: Generating fake vehicle-related data
print("\nExample 13:")
for _ in range(5):
    print("Vehicle Make:", fake.vehicle_make())
    print("Vehicle Model:", fake.vehicle_model())
    print("License Plate:", fake.license_plate())
    print("-" * 20)
