class Property:
    def __init__(self, square_feet=0, beds=0, baths=0, **kwargs):
        super().__init__(**kwargs)
        self.square_feet = square_feet
        self.beds = beds
        self.baths = baths

    def display(self):
        print("PROPERTY DETAILS:")
        print("=" * 10)
        print("square footage: {}".format(self.square_feet))
        print("bedrooms: {}".format(self.beds))
        print("bathrooms: {}".format(self.baths))
        print()

    @staticmethod
    def prompt_init():
        return dict(square_feet=input("Enter the square feet: "),
                    beds=input("Enter number of bedrooms: "),
                    baths=input("Enter number of bathrooms: "))

    @staticmethod
    def get_valid_input(input_string, valid_options):
        response = ""
        while response.lower() not in valid_options:
            response = input(
                "{} ({})".format(input_string, ", ".join(valid_options)))
        return response

def main():
    property = Property()
    Property.prompt_init()

if __name__ == "__main__":
    main()